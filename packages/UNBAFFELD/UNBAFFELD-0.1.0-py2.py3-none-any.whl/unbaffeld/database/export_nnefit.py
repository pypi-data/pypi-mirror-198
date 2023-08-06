#!/usr/bin/env python
"""
Module for pulling the EFIT data from the OMAS database to
construct the training IO's for EFIT-MOR.
"""

import os
import h5py
import time
import numpy as np
import optparse
import scipy.interpolate as interp
# from matplotlib import rc, pyplot as plt
from matplotlib import pyplot as plt
from numpy.linalg import svd

mu0 = 4 * np.pi * 1.0e-7  # for non-dimensionalizing the inputs


def check_vacuum(input_file):
    """Determine if the discharge is a vacuum shot"""

    h5file = h5py.File(input_file, mode="r")
    vacuum = True
    keey = "equilibrium"
    if keey in h5file.keys():
        h5file[keey]
        vacuum = False

    return vacuum


def get_grid(time_slice):
    """function for producing the 2D rectangular grid of (R,Z)
    Inputs:
    -------
       time_slice: EFIT time slice, h5 object
    Outputs:
    --------
       R,Z meshgrid, each is a 2D array
    """

    grid = time_slice["profiles_2d"]["0"]["grid"]
    x = grid.get("dim1")[()]
    y = grid.get("dim2")[()]
    R, Z = np.meshgrid(x, y)  # generate the RZ mesh

    return R.T, Z.T  # so the first index -> R, 2nd -> Z


def calc_radii(time_slice):
    """
    Function for calculating the major/minor radius of the torus
    We need this for the normalization of fluxes etc
    Inputs:
    -------
       prof1d: h5 object that stores all the profiles_1d quantities
    Outputs:
    --------
       Output: major and minor radii
    """

    prof1d = time_slice["profiles_1d"]
    Rmin = prof1d["r_inboard"][()].min()
    Rmax = prof1d["r_outboard"][()].max()
    return 0.5 * (Rmax + Rmin), 0.5 * (Rmax - Rmin)


def get_mag_data(MagData):
    """
    General-purpose function for importing the multi-sensor mag. data into
    local arrays
    Inputs:
    -------
      MagData: h5 data object
    Outputs:
    --------
       Measured: 1D np array of measured values
       weights: 1D array of all probe weights
       chiSs:    1D array of the ChiSquared values
    NOTES: The function for now does NOT  return the reconstructed signal to
    keep the amount of data returned a bit smaller
    """

    num_sensors = len(MagData)
    measured = np.zeros(num_sensors)
    recons = np.zeros(num_sensors)
    weights = np.zeros(num_sensors)
    chiSq = np.zeros(num_sensors)

    for ip in np.arange(num_sensors):
        measured[ip] = MagData[str(ip)]["measured"][()]
        if "reconstructed" in MagData[str(ip)].keys():
            recons[ip] = MagData[str(ip)]["reconstructed"][()]
        if "weight" in MagData[str(ip)].keys():
            weights[ip] = MagData[str(ip)]["weight"][()]
        if "chi_squared" in MagData[str(ip)].keys():
            chiSq[ip] = MagData[str(ip)]["chi_squared"][()]

    return measured, weights, chiSq


def get_auxQuant1D(time_slice):
    """
    Function for extracting psi and p'(psi) and FF'(psi).
    It also computes GS solver error a la Joey M's script
    Inputs:
    -------
       time_slice : EFIT time slice from OMAS DB
    Outputs:
    --------
       1D normalized psi and p'(psi) and FF'(psi)
    """

    psi = time_slice["profiles_1d/psi"][()]
    ffprime = time_slice["profiles_1d/f_df_dpsi"][()]
    pprime = time_slice["profiles_1d/dpressure_dpsi"][()]
    # Ravg_inv = time_slice["profiles_1d/gm9"][()]
    # R2_inv = time_slice["profiles_1d/gm1"][()]
    # Jt_to_R_fb = -1 * 2 * np.pi * (pprime + ffprime * R2_inv / mu0)
    # Jt_to_R = time_slice["profiles_1d/j_tor"] * Ravg_inv

    # error = abs((Jt_to_R_fb-Jt_to_R)/Jt_to_R)

    return psi, 2 * np.pi * ffprime, 2 * np.pi * pprime


def get_auxQuant2D(time_slice):
    """
    Function for extracting Jtor force-balance on the (R,Z) grid.
    Jtor_fb = R*p' + FF' /mu0*R, as well as p' and FF', both on
    (R, Z) grid and as a function of psi
    Inputs:
    -------
       time_slice : EFIT time slice from OMAS DB
    Outputs:
    --------
       Jtor, FF', p' on the RZ grid
    """

    def ext_arr(inv):
        return np.hstack((inv[0], inv, inv[-1]))

    r = time_slice["profiles_2d/0/grid/dim1"][()]
    z = time_slice["profiles_2d/0/grid/dim2"][()]
    psirz = time_slice["profiles_2d/0/psi"][()].T
    psi, ffprime, pprime = get_auxQuant1D(time_slice)
    # *** ffprime and pprime come with an extra 2*pi x to match COCOS

    # set up the filter for the separatix: psi (1D) is max. at the separatrix
    sep = np.where(psirz > psi.max())
    sep2 = np.where(psirz <= psi.max())

    # set up the 1d psi grid
    dp = psi[1] - psi[0]
    ext_psi_mesh = np.hstack((psi[0] - dp * 1e6, psi, psi[-1] + dp * 1e6))
    interpType = "linear"

    # go from p'(psi) and FF'(psi) to p'(R,Z) and FF'(R,Z)
    pprimerz = interp.interp1d(
        ext_psi_mesh, ext_arr(pprime), kind=interpType, bounds_error=False
    )(psirz)
    ffprimerz = interp.interp1d(
        ext_psi_mesh, ext_arr(ffprime), kind=interpType, bounds_error=False
    )(psirz)

    R, Z = np.meshgrid(r, z)
    Nr, Nz = np.shape(R)

    # normalize psirz
    psirz = (psirz - psi.min()) / (psi.max() - psi.min())

    # (1) get JtorDS from -Del*psi/R
    #  NOTE the transpose as of Oct 5 2021
    # JtorDS = DelStarPsi(psirz.T, r, z).T

    # get the R,Z coords of the last closed flux surface
    LCFSrz = get_boundary(time_slice)

    # R,Z coords of all points within psirz = 1 surface
    Rsep = R[sep2]
    Zsep = Z[sep2]

    # Apply the psirz = 1 filter first
    ffprimerz[sep] = 0.0
    pprimerz[sep] = 0.0
    # JtorDS[sep] = 0.0

    # zero out JtorDS, FF', and p' outside the LCFS
    for i in np.arange(Rsep.size):
        if not isPointInPath(Rsep[i], Zsep[i], LCFSrz):
            ffprimerz[sep2[0][i], sep2[1][i]] = 0.0
            pprimerz[sep2[0][i], sep2[1][i]] = 0.0
            # JtorDS[sep2[0][i], sep2[1][i]] = 0.0

    # (2) JtorFB = p' + FF'
    JtorFB = R * pprimerz + ffprimerz / (mu0 * R)
    # impose the COCOS conventions here, manually
    JtorFB = -JtorFB

    # unit choices below agree with ODS!!
    return JtorFB.T, ffprimerz.T, pprimerz.T


def DelStarPsi(psirz, r, z):
    """
    Stand-alone Jtor function from -Del*psi/R to be able to get
    Jtor given psi, in anticipation of the taking psiNN as input
     Inputs:
     -------
       psirz: 2D array of normalized psi on the R,Z grid
       r, z : 1D R and Z coords of the rectangular EFIT grida
     Outputs:
     --------
       JtorDS on the R,Z grid
       divB on the R, Z grid: OPTIONAL currently
    """

    # nr = len(r)
    # nz = len(z)
    R, Z = np.meshgrid(r, z)
    R = R.T
    Z = Z.T
    dr = r[1] - r[0]
    dz = z[1] - z[0]

    # choose the last flux surface, 1.0 is the separatrix
    # sep = np.where(psirz > 0.9)

    # Carry out Del*psi with the COCOS conventions appearing explicity in here
    [dPsidR, dPsidZ] = np.gradient(psirz, dr, dz, edge_order=1)
    Br = (dPsidZ / R) / (2 * np.pi)
    Bz = -(dPsidR / R) / (2 * np.pi)
    dBrdZ = np.gradient(Br, dz, edge_order=1)[1]
    dBzdR = np.gradient(Bz, dr, edge_order=1)[0]
    # calculate d/dR Br + d/dZ Bz for div(B) = 0 check
    # dBrdR = np.gradient(Br, dr, edge_order=1)[0]
    # dBzdZ = np.gradient(Bz, dz, edge_order=1)[1]

    Jtor = dBrdZ - dBzdR  # / mu0
    # divB = dBrdR + dBzdZ

    # zero out Jtor outside the separatrix
    # Jtor[sep] = 0.0
    # divB[sep] = 0.0  # output this in the future!

    # Jtor = SVDfilter_sigs(Jtor)

    return Jtor


def SVDfilter_sigs(data, n_cutoff):
    """
    Reconstruct a signal after truncating them
    based on their SVD
     Inputs:
     -------
       data: 1D array of dianostic measurements at a time slice
       n_cutoff: Eigenmode number for truncating the SVD reconstruction
     Outputs:
     --------
       recons_sig: 2D array of reconstructred constraints
    """
    from scipy.sparse import spdiags

    # SVD the probe data
    U, S, Vt = svd(data)

    # truncate signals based on SVD, threshold set to the middle of
    # the range of the singular values
    # midp = np.average([np.log(S.max()), np.log(S.min())])
    thres = S[n_cutoff]  # np.exp(midp)
    it = np.where(S > thres)

    # make a diagonal array out of the eigenvalues
    diags = np.array([0])
    sigmas = S[it]
    SS = spdiags(sigmas, diags, len(it[0]), len(it[0])).toarray()

    # reconstruct
    recons_data = np.matmul(U[:, it], np.matmul(SS, Vt[it, :]))
    recons_data = recons_data.squeeze()

    return recons_data


def get_XpointRZ(time_slice):
    """
    Function that outputs R, Z coords of the X-points at each time slice

    Inputs:
    -------
       time_slice : EFIT time slice from OMAS DB
    Outputs:
    --------
       R and Z coords of the X-points

    """
    xp = time_slice["boundary"]["x_point"]
    for xx in xp.keys():
        Rx = xp[str(xx)].get("r")[()]
        Zx = xp[str(xx)].get("z")[()]

    return Rx, Zx


def get_boundary(time_slice, interpFlag=False, interpType="linear"):
    """
    Function that outputs R, Z coords of the last closed flux surface
    for each time slice

    Inputs:
    -------
       time_slice : EFIT time slice from OMAS DB
    Outputs:
    --------
       R and Z coords of the boundary as a Np x 2 Numpy array

    """

    outline = time_slice["boundary"]["outline"]
    Rb = outline.get("r")[()]
    Zb = outline.get("z")[()]
    boundary = np.vstack((Rb, Zb))

    # parameterize the boundary in terms of a polar angle to output LCFS
    # of a fixed size for NN training target
    if interpFlag:
        R0 = 0.5 * (Rb.min() + Rb.max())
        Z0 = 0.5 * (Zb.min() + Zb.max())
        tht = np.arctan2(Zb - Z0, Rb - R0)
        tht = np.unique(tht)
        tht_sort = np.sort(tht)
        # define the uniform theta coord
        tht2 = np.linspace(tht_sort[0], tht_sort[-1], 100)
        ff = interp.interp1d(tht_sort, Rb[np.argsort(tht)], kind=interpType)
        Rbnew = ff(tht2)
        ff = interp.interp1d(tht_sort, Zb[np.argsort(tht)], kind=interpType)
        Zbnew = ff(tht2)
        # close the boundary shape by repeating the first element
        Rbnew = np.append(Rbnew, Rbnew[0])
        Zbnew = np.append(Zbnew, Zbnew[0])
        boundary = np.vstack((Rbnew, Zbnew))

    return boundary.T


def isPointInPath(x, y, poly):
    """
    Function for deteriming if given x,y coord is inside a boundary defined
    by the polynomial poly

    Inputs:
    -------
      x, y : scalar variable, RZ coord. of the point of interest
      poly : boundary shape
    """
    num = len(poly)
    i = 0
    j = num - 1
    c = False

    for i in range(num):
        if ((poly[i][1] > y) != (poly[j][1] > y)) and (
            x
            < (poly[j][0] - poly[i][0]) * (y - poly[i][1]) / (poly[j][1] - poly[i][1])
            + poly[i][0]
        ):
            c = not c
        j = i

    return c


def get_global_quant(time_slice):
    """
    Function for pulling the following items from the ODS data
    ['beta_normal', 'beta_tor', 'ip', 'li_3', 'magnetic_axis',
      'psi_axis', 'psi_boundary', 'q_95', 'q_axis', 'q_min']
    """
    R0 = time_slice["global_quantities"]["magnetic_axis"]["r"][()]
    Z0 = time_slice["global_quantities"]["magnetic_axis"]["z"][()]
    BetaN = time_slice["global_quantities"]["beta_normal"][()]
    li = time_slice["global_quantities"]["li_3"][()]
    Ip = time_slice["global_quantities"]["ip"][()]
    q_axis = time_slice["global_quantities"]["q_axis"][()]
    q95 = time_slice["global_quantities"]["q_95"][()]
    q_min = time_slice["global_quantities"]["q_min"]["value"][()]
    # qvals = [q_axis, q_min, q_95]

    return R0, Z0, BetaN, li, abs(q95), abs(q_axis), abs(q_min), Ip


def load_time_slice(input_file):
    """
    Just a really tiny function for loading a desired time slice into
    the working space
    """

    # read in the input file
    hin = h5py.File(input_file, mode="r")

    # Equilibrium group contains a mixture of inputs and outputs
    eqgrp = hin.get("equilibrium")

    # Time slices
    time = eqgrp.get("time")[()]
    time_slices = np.arange(time.size)
    Nt = len(time_slices)

    Slice = input("Choose of the " + str(Nt) + "--many time slices: ")

    return eqgrp.get(f"time_slice/{Slice}")


def extract_inputs(input_file, efit_type="01"):
    """
    Construct the input vector for the NN
    Inputs:
    -------
      input_file: h5 data object from the OMAS DB
      efit_type : optional flag to switch between EFIT types
    Outputs:
    --------
      contraints : 2D array of mag. and MSE constraints for all time slces
      times:  1D array containing the physical time of all the time slices
      shotWeights: 1D array that is a product of all MP and FL weights
                   for all the time slices.
    """

    # standard checks
    if not os.path.exists(input_file):
        print("Input file ", input_file, " must exist.")
        return
    if os.path.splitext(input_file)[1] not in [".h5"]:
        print("Input file ", input_file, " must be an h5 file.")
        return

    # read in the input file
    hin = h5py.File(input_file, mode="r")

    # Equilibrium group contains a mixture of inputs and outputs
    eqgrp = hin.get("equilibrium")
    ts0 = eqgrp.get("time_slice/0")

    # Time slices
    time = eqgrp.get("time")[()]
    time_slices = np.arange(time.size)
    # Nt = len(time_slices)

    # Define normalization constants, all 1D arrays
    # First, get the vacuum toroidal field to non-dimensionalize inputs
    # this is a 1D array of length time_slices
    B0 = abs(eqgrp["vacuum_toroidal_field"]["b0"][:])
    R0, r0 = calc_radii(ts0)
    psiV = B0 * r0 * R0  # for fluxes
    I0 = B0 * r0 / mu0

    # determine the number of Bpol_probes and flux loops
    probe_array = ts0["constraints"]["bpol_probe"]
    flux_loops = ts0["constraints"]["flux_loop"]
    num_probes = len(probe_array)
    num_floops = len(flux_loops)

    # COMMENTS TODO
    # There is a bug in omas2efitaidb.py where the pressure is put into /inputs
    # which it should not.  It should be put into the equilibrium somewhere
    # since it depends on the reconstruction method (magnetics versus kinetic)
    #
    # mse_angles = ts0["constraints"]["mse_polarisation_angle"]
    # pf_current = ts0["constraints"]["pf_current"]  # CA-- what to do with this
    num_MSE = 14  # only channels 1-11 and 41-44 are in use len(mse_angles)
    # num_pfc = len(pf_current)

    # Number of constraints: num_probes + num_floops + 2, for MAGNETICS ONLY
    # (one for Ip and another for the diamagnetic flux)
    Nd = num_floops + num_probes + 2

    # Adjust the number of constraints for other types of EFIT
    if efit_type == "02":  # cases for EFIT02 and on
        Nd = Nd + num_MSE
        print("You are pulling data from EFIT02")
    elif efit_type == "kin":
        # Note: Npp is undefined!
        Nd = Nd + num_MSE + Npp  # add the pressure constraint
        print("You are pulling data from kinEFIT's")

    # pull the file label , i.e. efitversion
    eqgrp["code"]["parameters"]["time_slice"]["0"]["in1"]["efitversion"][()]

    # get the shot number
    metagrp = hin.get("dataset_description/data_entry")
    shotnum = str(metagrp.get("pulse")[()])
    print("Processing shot " + str(shotnum))

    # Apply the filter here to reduce cost of processing
    global_quant = np.zeros((8, len(time_slices)))
    for i in time_slices:
        tgrp = eqgrp.get("time_slice/" + str(i))
        global_quant[:, i] = get_global_quant(tgrp)

    # discard any time slice with BetaN > 10., li > 15, q95 > 15 and q0>15,
    goodSlices = filter_time_slices(global_quant)
    Nt = sum(goodSlices)  # number of True's from goodSLices

    # initialize arrays
    constraints = np.zeros((Nd, Nt))
    # Ip = np.zeros(Nd)
    chi2all = np.zeros((Nd, Nt))
    all_weights = np.ones(Nd)  # initial weight vector for the constraints
    checkWeights = all_weights
    # MAIN LOOP over all the time slices contained within the shot data
    it = 0
    for i in time_slices[goodSlices]:
        tgrp = eqgrp.get("time_slice/" + str(i))

        # diagnotic weights
        # mp_weights = eqgrp.get(f"code/parameters/time_slice/{i}/in1/fwtmp2")[()]
        mp_weights = eqgrp.get("code/parameters/time_slice/" + str(i) + "/in1/fwtmp2")[
            ()
        ]
        fl_weights = eqgrp.get("code/parameters/time_slice/" + str(i) + "/in1/fwtsi")[
            ()
        ]
        # mse_weights =
        #       eqgrp.get('code/parameters/time_slice/' + str(i) + '/in1/fwtgam')[()]

        all_weights[:num_probes] = mp_weights
        all_weights[num_probes + 1: num_probes + 1 + num_floops] = fl_weights
        # all_weights = np.stack((mp_weights, 1, fl_weights, 1))
        checkWeights = checkWeights * all_weights

        # loop over all of the constraints in the time slice h5
        # These are:'bpol_probe', 'diamagnetic_flux', 'flux_loop', 'ip',
        #           'mse_polarisation_angle', 'pf_current', 'pressure
        all_signals = np.array([])
        all_chi2 = np.array([])
        for key in tgrp["constraints"]:
            if "0" in tgrp["constraints"][key].keys():
                diag_data = tgrp["constraints"][key]
                diagnostic, weights, chi2 = get_mag_data(diag_data)
            else:
                diagnostic = tgrp["constraints"][key]["measured"][()]

            all_signals = np.append(all_signals, diagnostic)
            all_chi2 = np.append(all_chi2, chi2)

        constraints[:, it] = all_weights * all_signals[:Nd]
        chi2all[:, it] = all_weights * all_chi2[:Nd]
        # Wzeros = np.where(all_weights <= 1.0e-10)[0]

        # **** This logic FAILS because the MSE diagnostic comes on later
        # than the other diagnostics, so it reads 0's for a series of time
        # slices in the beginning   *****
        # check MSE ch1 to see if MSE signals are non-zero
        # num_nonzeroMSE = len(np.nonzero(all_signals[Nd + 1])[0])
        # if num_nonzeroMSE > 2:
        #    print('You are pulling data from EFIT02')
        #    constraints[:, it] =
        #       np.concatanate((constraints[:,i], all_signals[Nd: Nd + 11] ))
        #    Nd = Nd + num_MSE

        # non-dimensionalize the inputs
        constraints[:num_probes, it] = constraints[:num_probes, it] / (
            r0 * B0[i] / R0
        )  # Bpol_probes
        constraints[num_probes, it] = (
            constraints[num_probes, it] / psiV[i]
        )  # Diamag. flux
        constraints[num_probes + 1: num_probes + 1 + num_floops, it] = constraints[
            num_probes + 1: num_probes + 1 + num_floops, it
        ] / (
            psiV[i] / (2 * np.pi)
        )  # Flux loops
        constraints[num_probes + 1 + num_floops, it] = (
            constraints[num_probes + 1 + num_floops, it] / I0[i]
        )  # Ip

        it += 1

    # discard any time slice with mag Chi2 > 30.
    TotalChi2 = np.sum(chi2all, axis=0)

    return constraints, time[goodSlices], TotalChi2
    # return constraints[:, goodSlices], time[goodSlices], TotalChi2[goodSlices]


def extract_outputs(input_file, jtorOn=True):
    """
    Extract the data from h5 OMAS file to construct the output
    vector
    Inputs:
    -------
      input_file: h5 data object from the OMAS DB
      Jtor      : flag for extracting FF' + p' from the geqdsk files
                  on the go to reconstruct Jtor
    Outputs:
    --------
      psi2d : the flux function on the 2D grid
    NOTES: The calculated Ip and Btor are also extracted in this routine but
      currently NOT returned
    """
    # read in the input file
    hin = h5py.File(input_file, mode="r")

    # Equilibrium group contains a mixture of inputs and outputs
    eqgrp = hin.get("equilibrium")
    ts0 = eqgrp.get("time_slice/0")

    # Get the vacuum toroidal field to non-dimensionalize inputs
    # this is a 1D array of length time_slices
    B0 = abs(eqgrp["vacuum_toroidal_field"]["b0"][:])

    # define mormalization constants, all 1D arrays
    R0, r0 = calc_radii(ts0)
    # psiV = B0 * r0 * R0  # vaccuum flux
    # I0 = B0 * r0 / mu0

    # Get the grid
    R, Z = get_grid(ts0)
    Nr = len(R[0])
    Nz = len(Z[1])  # CHECK the meshgrid indexing for NON-square grids

    # Time slices
    time = eqgrp.get("time")[()]
    time_slices = np.arange(time.size)

    # Apply the filter here to reduce cost of processing
    global_quant = np.zeros((8, len(time_slices)))
    for i in time_slices:
        tgrp = eqgrp.get("time_slice/" + str(i))
        global_quant[:, i] = get_global_quant(tgrp)

    # discard any time slice with BetaN > 10., li > 15, q95 > 15 and q0>15,
    goodSlices = filter_time_slices(global_quant)
    Nt = sum(goodSlices)  # number of True's from goodSLices

    # initialize array for storing the solution vector
    psirz = np.zeros((Nr, Nz, Nt))
    Btor = np.zeros((Nr, Nz, Nt))
    JtorFB = np.zeros((Nr, Nz, Nt))
    FFprimerz = np.zeros((Nr, Nz, Nt))
    Pprimerz = np.zeros((Nr, Nz, Nt))

    # MAIN LOOP over all the time slices contained within the shot data
    it = 0
    for i in time_slices[goodSlices]:
        # Inputs.  Base output label on 2D psi
        tgrp = eqgrp.get("time_slice/" + str(i))
        psi = tgrp.get("profiles_2d/0/psi")[()]
        psiSep = tgrp.get("profiles_1d/psi")[()].max()
        psiAxis = tgrp.get("profiles_1d/psi")[()].min()
        # psirz[..., it] = psi/psiV[i, np.newaxis] #old way to normalize
        psirz[..., it] = (psi - psiAxis) / (psiSep - psiAxis)
        Btor[..., it] = tgrp.get("profiles_2d/0/b_field_tor")[()] / B0[i, np.newaxis]
        # Get the calculated Ip
        # Ip[i] = eqgrp['time_slice'][str(i)]['global_quantities']['ip'][()] / I0[i]

        if jtorOn:
            # minor radius r0 and vacuum field B0 are used to normalize JtorFB
            JtFBrz, FFpRZ, PpRZ = get_auxQuant2D(tgrp)
            JtorFB[..., it] = JtFBrz * mu0 * r0 / (2 * np.pi * abs(B0[i, np.newaxis]))
            FFprimerz[..., it] = FFpRZ * r0 / (2 * np.pi * abs(B0[i, np.newaxis]))
            Pprimerz[..., it] = (
                PpRZ * mu0 * r0**2 / (2 * np.pi * abs(B0[i, np.newaxis]))
            )

        it += 1

    return psirz, Btor, JtorFB, FFprimerz, Pprimerz


def extract_outputs_NN(input_file, jtorOn=True):
    """
    Extract the data from h5 OMAS file to construct the output
    vector
    Inputs:
    -------
      input_file: h5 data object from the OMAS DB
      Jtor      : flag for extracting FF' + p' from the geqdsk files
                  on the go to reconstruct Jtor
    Outputs:
    --------
      psi2d : the flux function on the 2D grid
    NOTES: The calculated Ip and Btor are also extracted in this routine but
      currently NOT returned
    """
    # read in the input file
    hin = h5py.File(input_file, mode="r")

    # Equilibrium group contains a mixture of inputs and outputs
    eqgrp = hin.get("equilibrium")
    ts0 = eqgrp.get("time_slice/0")

    # Get the vacuum toroidal field to non-dimensionalize inputs
    # this is a 1D array of length time_slices
    B0 = abs(eqgrp["vacuum_toroidal_field"]["b0"][:])

    # define mormalization constants, all 1D arrays
    R0, r0 = calc_radii(ts0)
    # psiV = B0 * r0 * R0  # vaccuum flux
    # I0 = B0 * r0 / mu0

    # Get the grid
    R, Z = get_grid(ts0)
    Nr = len(R[0])
    Nz = len(Z[1])  # CHECK the meshgrid indexing for NON-square grids

    # Time slices
    time = eqgrp.get("time")[()]
    time_slices = np.arange(time.size)

    # Apply the filter here to reduce cost of processing
    global_quant = np.zeros((8, len(time_slices)))
    for i in time_slices:
        tgrp = eqgrp.get("time_slice/" + str(i))
        global_quant[:, i] = get_global_quant(tgrp)

    # discard any time slice with BetaN > 10., li > 15, q95 > 15 and q0>15,
    goodSlices = filter_time_slices(global_quant)
    Nt = sum(goodSlices)  # number of True's from goodSLices

    # initialize array for storing the solution vector
    psirz = np.zeros((Nr, Nz, Nt))
    Btor = np.zeros((Nr, Nz, Nt))
    JtorFB = np.zeros((Nr, Nz, Nt))
    FFprimerz = np.zeros((Nr, Nz, Nt))
    Pprimerz = np.zeros((Nr, Nz, Nt))

    # MAIN LOOP over all the time slices contained within the shot data
    it = 0
    for i in time_slices[goodSlices]:
        # Inputs.  Base output label on 2D psi
        tgrp = eqgrp.get("time_slice/" + str(i))
        psi = tgrp.get("profiles_2d/0/psi")[()]
        psiSep = tgrp.get("profiles_1d/psi")[()].max()
        psiAxis = tgrp.get("profiles_1d/psi")[()].min()
        # psirz[..., it] = psi/psiV[i, np.newaxis] #old way to normalize
        psirz[..., it] = (psi - psiAxis) / (psiSep - psiAxis)
        Btor[..., it] = tgrp.get("profiles_2d/0/b_field_tor")[()] / B0[i, np.newaxis]
        # Get the calculated Ip
        # Ip[i] = eqgrp['time_slice'][str(i)]['global_quantities']['ip'][()] / I0[i]

        if jtorOn:
            # minor radius r0 and vacuum field B0 are used to normalize JtorFB
            JtFBrz, FFpRZ, PpRZ = get_auxQuant2D(tgrp)
            JtorFB[..., it] = JtFBrz * mu0 * r0 / (2 * np.pi * abs(B0[i, np.newaxis]))
            FFprimerz[..., it] = FFpRZ * r0 / (2 * np.pi * abs(B0[i, np.newaxis]))
            Pprimerz[..., it] = (
                PpRZ * mu0 * r0**2 / (2 * np.pi * abs(B0[i, np.newaxis]))
            )

        it += 1

    return (
        psirz,
        Btor,
        JtorFB,
        FFprimerz,
        Pprimerz,
        B0[goodSlices],
        np.ones((len(goodSlices))) * r0,
    )


def extract_other_outputs(input_file):
    """
    Extract R,Z of mag. axis, BetaN, li, q95 from the OMAS data
    RZ coords of the LCFS

    Inputs:
    -------
      input_file: h5 data object from the OMAS DB
    Outputs:
    --------
      global_quant = R0, Z0, BetaN, li, q95 for all time slices
    """

    hin = h5py.File(input_file, mode="r")
    eqgrp = hin.get("equilibrium")

    # Time slices
    time = eqgrp.get("time")[()]
    time_slices = np.arange(time.size)
    Nt = len(time_slices)

    # get the number of points along the last closed flux surface
    # nb = np.shape(get_boundary(eqgrp.get("time_slice/0")))[0]

    global_quant = np.zeros((8, Nt))
    # LCFSrz = np.zeros((2 * nb, Nt))  # stacking R and Z coords on top of each other

    # MAIN LOOP over all the time slices contained within the shot data
    for i in time_slices:
        tgrp = eqgrp.get("time_slice/" + str(i))
        global_quant[:, i] = get_global_quant(tgrp)
        # RZplasmaBnd = get_boundary(tgrp)
        # LCFSrz[..., i] = np.hstack((RZplasmaBnd[:,0], RZplasmaBnd[:,1])).T

    goodSlices = filter_time_slices(global_quant)

    return global_quant[:, goodSlices]


def filter_time_slices(EFITglobal_scalars):
    """
    Function for keeping only the time slices with reasonable values
    of BetaN, L_i, q95, q0 etc
    """

    # define the hard limits for filtering data
    BetaNlim = 10.0
    lilim = 10.0
    q95lim = 15.0
    q0lim = 10.0

    # add the Flat top filter
    Ip = EFITglobal_scalars[-1, :]
    IpFT = 0.95 * Ip.max()

    goodSlices = (
        (EFITglobal_scalars[2, :] <= BetaNlim)
        & (EFITglobal_scalars[3, :] <= lilim)
        & (EFITglobal_scalars[4, :] <= q95lim)
        & (EFITglobal_scalars[5, :] <= q0lim)
        & (Ip >= IpFT)
    )

    return goodSlices


def plot_data(inputs, outputs, time, R, Z, shotnum):
    """
    Plot a subset of the time-dependent (magnetic) constraints as well as
    as the flux surfaces from a particular time slice
    Inputs:
    -------
      inputs: 2D array of dimensions (number of constraints) x (number of EFIT's)
      outputs: Tuple of 4 elements, each containing a 3D array of psi, Btor,
              Jtor, and JtorDS on the RZ grid for all times slices within a shot
      time: 1D array of time slices
    """

    from numpy import random as rd

    plt.close("all")
    # plt.rc('text',usetex=True)
    # plt.rc('font',family='serif')
    lblsz = 15
    field_title = [
        r"$\psi(R,Z)$",
        r"$B_{\phi}(R,Z)$",
        r"$J_{\phi}^{FB}(R,Z)$",
        r"$FF'(R,Z)$",
        r"$p'(R,Z)$",
        r"$J_{\phi}^{DS}(R,Z)$",
    ]

    # n_inputs = len(inputs)
    npr = 76
    nfl = 44
    prb_indx = rd.randint(0, npr, 3)  # HARD-CODED!
    fl_indx = rd.randint(0, nfl, 3)  # HARD-CODED!

    # choose a time index at random over time slices
    nts = len(time)
    time_indx = rd.randint(nts)
    prtimes = np.sort(rd.randint(0, nts, 3))

    #   #############################################################################
    #   ##           plot probe measurements vs poloidal angle theta               ##
    #   #############################################################################
    probesRZ = np.loadtxt("probesRZ.txt")
    Rp, Zp = probesRZ[:, 0], probesRZ[:, 1]
    # R0 = np.average([R.min(), R.max()])
    # tht = np.arctan2(Zp, Rp - R0) # using the polar angle as the arc length parameter

    # load probe uncertainty next
    bitmpi = np.loadtxt("sigmaProbes.txt")

    # load probe weights
    weights = np.loadtxt("probeWeights.txt")
    nonz = np.nonzero(weights)[0]
    zw = np.argwhere(weights == 0)[0]

    probes = inputs[:npr, prtimes]
    # sort according to polar angle
    # probes = probes[np.argsort(tht), :]
    # tht2 = tht[np.argsort(tht)]

    _ = plt.figure(0, [21, 6.5])
    plt.subplots_adjust(left=0.05, right=0.99, top=0.98, bottom=0.12, wspace=0.2)
    ax = plt.subplot(131)
    ax.tick_params(labelsize=lblsz)
    plt.plot(Rp[nonz], Zp[nonz], "bo")
    plt.plot(Rp[zw], Zp[zw], "rx")
    # number each location
    ip = 1
    for x, y in zip(Rp, Zp):
        plt.text(x, y, str(ip), color="r", fontsize=12)
        ip += 1
    plt.grid(True)
    ax.set_xlabel(r"$R$", fontsize=lblsz)
    ax.set_ylabel(r"$Z$", fontsize=lblsz)

    ax = plt.subplot(132)
    ax.yaxis.set_label_coords(-0.1, 0.47)
    # loop over the selected time slices to plot the sigmas
    for jj in np.arange(len(prtimes)):
        sigmaProbes = np.maximum(0.03 * probes[:, jj], bitmpi * 10.0)
        # sigmaProbes = sigmaProbes[np.argsort(tht)]
        # plt.plot(180*tht2[nonz]/np.pi, probes[nonz, jj], \
        #         label = str(time[prtimes[jj]]) + ' s' )
        plt.plot(nonz, probes[nonz, jj], label=str(time[prtimes[jj]]) + " s")
        plt.fill_between(
            nonz,
            probes[nonz, jj] - sigmaProbes[nonz],
            probes[nonz, jj] + sigmaProbes[nonz],
            alpha=0.6,
        )
    ax.tick_params(labelsize=lblsz)
    # ax.set_xlabel(r'$\theta$', fontsize = lblsz )
    ax.set_xlabel(r"probe", fontsize=lblsz)
    ax.set_ylabel(r"$B_p$ signal", fontsize=lblsz)
    ax.legend(frameon=True, loc=[0.03, 0.03], ncol=1, prop={"size": lblsz})
    plt.grid(True)

    ax = plt.subplot(133)
    ax.yaxis.set_label_coords(-0.03, 0.53)
    # loop over the selected time slices to plot the sigmas
    for jj in np.arange(len(prtimes)):
        sigmaProbes = np.maximum(0.03 * probes[:, jj], bitmpi * 10.0)
        # sigmaProbes = sigmaProbes[np.argsort(tht)]
        nonz = np.nonzero(weights)[0]
        # nonz = np.nonzero(probes[:, jj])[0]
        # plt.semilogy(180*tht2[nonz]/np.pi, sigmaProbes[nonz]/abs(probes[nonz, jj]), \
        #         label = str(time[prtimes[jj]]) + ' s' )
        # plt.semilogy(180*tht2[nonz]/np.pi, 0.03*np.ones(len(nonz)),'k--')
        plt.semilogy(
            nonz,
            sigmaProbes[nonz] / abs(probes[nonz, jj]),
            label=str(time[prtimes[jj]]) + " s",
        )
        plt.semilogy(nonz, 0.03 * np.ones(len(nonz)), "k--")
    ax.tick_params(labelsize=lblsz)
    ax.set_xlabel(r"probe", fontsize=lblsz)
    # ax.set_xlabel(r'$\theta$', fontsize = lblsz )
    ax.set_ylabel(r"$\sigma/B_p$", fontsize=lblsz)
    # ax.legend(frameon = True, loc = [.03,.65], ncol = 1, prop={'size': lblsz} )
    plt.grid(True)
    plt.show()
    plt.savefig("Probes_vs_theta" + str(shotnum) + ".png")

    #   #############################################################################
    #   # plot psi, Btor, JtorFB, and JtorDS on the (R,Z) grid
    #   #############################################################################
    _ = plt.figure(1, [15, 10])
    plt.subplots_adjust(
        left=0.07, right=0.99, top=0.96, bottom=0.08, wspace=0.0, hspace=0.11
    )
    for ii in np.arange(4):
        field2D = outputs[ii][..., time_indx].T
        ax = plt.subplot(2, 2, ii + 1)
        ax.tick_params(labelsize=lblsz)
        plt.title(field_title[ii], fontsize=lblsz)
        plt.pcolor(R, Z, field2D)
        plt.colorbar()
        plt.contour(R, Z, field2D, 20, colors="k")
        if ii > 1:
            ax.set_xlabel(r"$R$", fontsize=lblsz)
        else:
            ax.set_xticks([])
        if np.mod(ii, 2) == 0:
            ax.set_ylabel(r"$Z$", fontsize=lblsz)
        else:
            ax.set_yticks([])
        ax.text(
            0.7,
            0.05,
            "time = " + str(time[time_indx]),
            transform=ax.transAxes,
            size=18,
            color="w",
        )
    plt.show()
    plt.savefig("EFITsolutions" + str(shotnum) + ".png")

    #   #############################################################################
    #   ##           plot select constraints vs time                               ##
    #   #############################################################################
    _ = plt.figure(2)
    plt.subplots_adjust(left=0.11, right=0.99, top=0.92, bottom=0.14)
    ax = plt.subplot(111)
    ax.tick_params(labelsize=lblsz)
    plt.title("Constraints", fontsize=lblsz)
    plt.plot(time, inputs[prb_indx[0], :], lw=2, label="probe " + str(prb_indx[0]))
    plt.plot(
        time, inputs[prb_indx[0] + 1, :], lw=2, label="probe " + str(prb_indx[0] + 1)
    )
    plt.plot(time, inputs[121, :], "--", lw=2, label=r"$I_p(MA)$")
    plt.plot(
        time, inputs[76 + fl_indx[0], :], "-.", lw=2, label="Fl loop " + str(fl_indx[0])
    )
    if len(inputs[:, 1]) > 122:  # figure out nonzero MSE cords and plot a couple
        mse_indx = np.arange(3)  # rd.randint(0, 11, 3) # pick 3 at random
        # plt.plot(time, inputs[122 + mse_indx[0], :], '.', lw=2, \
        #         label = 'MSE ch '+ str(mse_indx[0]) )
        plt.plot(
            time,
            5 * inputs[122 + mse_indx[1], :],
            ".",
            lw=2,
            label=r"5 $\times$MSE ch " + str(mse_indx[1]),
        )
        plt.plot(
            time,
            5 * inputs[122 + mse_indx[2], :],
            ".",
            lw=2,
            label=r"5 $\times$MSE ch " + str(mse_indx[2]),
        )
    plt.grid(True)
    plt.xlabel(r"time (s)", fontsize=lblsz)
    ax.legend(frameon=False, loc=[0.25, 0.63], ncol=2, prop={"size": 14})
    plt.show()
    plt.savefig("constraints_vs_time" + str(shotnum) + ".png")


def plot_data_NN(inputs, outputs, time, R, Z):
    """
    Plot a subset of the time-dependent (magnetic) constraints as well as
    as the flux surfaces from a particular time slice
    Inputs:
    -------
      inputs: 2D array of dimensions (number of constraints) x (number of EFIT's)
      outputs: Tuple of 4 elements, each containing a 3D array of psi, Btor,
              Jtor, and JtorDS on the RZ grid for all times slices within a shot
      time: 1D array of time slices
    """

    from numpy import random as rd

    plt.close("all")
    # plt.rc('text',usetex=True)
    # plt.rc('font',family='serif')
    lblsz = 15
    field_title = [
        r"$\psi(R,Z)$",
        r"$NN: \psi(R,Z)$",
        r"$J_{\phi}^{FB}(R,Z)$",
        r"$NN: J_{\phi}^{FB}(R,Z)$",
    ]

    # n_inputs = len(inputs)
    # npr = 76
    # nfl = 44
    # prb_indx = rd.randint(0, npr, 3)  # HARD-CODED!
    # fl_indx = rd.randint(0, nfl, 3)  # HARD-CODED!

    # choose a time index at random over time slices
    nts = len(time)
    time_indx = rd.randint(nts)
    # prtimes = np.sort(rd.randint(0, nts, 3))

    #   #############################################################################
    #   ##           plot probe measurements vs poloidal angle theta               ##
    #   #############################################################################
    #     probesRZ = np.loadtxt('probesRZ.txt')
    #     Rp, Zp = probesRZ[:, 0], probesRZ[:,1]
    #     R0 = np.average([R.min(),R.max()])
    #     tht = np.arctan2(Zp, Rp - R0) # using the polar angle as
    #                                   # the arc length parameter

    #     # load probe uncertainty next
    #     bitmpi = np.loadtxt('sigmaProbes.txt')

    #     # load probe weights
    #     weights = np.loadtxt('probeWeights.txt')
    #     nonz = np.nonzero(weights)[0]
    #     zw = np.argwhere(weights==0)[0]

    #     probes = inputs[:npr, prtimes]
    #     # sort according to polar angle
    #     #probes = probes[np.argsort(tht), :]
    #     #tht2 = tht[np.argsort(tht)]

    #     fig = plt.figure(0, [21,6.5])
    #     plt.subplots_adjust(left=0.05, right=0.99, top=0.98, bottom=0.12, wspace=0.2)
    #     ax = plt.subplot(131)
    #     ax.tick_params(labelsize = lblsz)
    #     plt.plot(Rp[nonz], Zp[nonz], 'bo')
    #     plt.plot(Rp[zw], Zp[zw], 'rx')
    #     # number each location
    #     ip = 1
    #     for x, y in zip(Rp, Zp):
    #         plt.text(x, y, str(ip), color='r', fontsize=12)
    #         ip += 1
    #     plt.grid(True)
    #     ax.set_xlabel(r'$R$', fontsize = lblsz )
    #     ax.set_ylabel(r'$Z$', fontsize = lblsz )

    #     ax = plt.subplot(132)
    #     ax.yaxis.set_label_coords(-0.1, 0.47)
    #     # loop over the selected time slices to plot the sigmas
    #     for jj in np.arange(len(prtimes)):
    #         sigmaProbes = np.maximum(0.03*probes[:, jj], bitmpi*10.)
    #         #sigmaProbes = sigmaProbes[np.argsort(tht)]
    #         #plt.plot(180*tht2[nonz]/np.pi, probes[nonz, jj], \
    #         #         label = str(time[prtimes[jj]]) + ' s' )
    #         plt.plot(nonz, probes[nonz, jj], \
    #                  label = str(time[prtimes[jj]]) + ' s' )
    #         plt.fill_between(nonz, \
    #                          probes[nonz, jj] - sigmaProbes[nonz], \
    #                          probes[nonz, jj] + sigmaProbes[nonz], alpha=0.6)
    #     ax.tick_params(labelsize = lblsz)
    #     #ax.set_xlabel(r'$\theta$', fontsize = lblsz )
    #     ax.set_xlabel(r'probe', fontsize = lblsz )
    #     ax.set_ylabel(r'$B_p$ signal', fontsize = lblsz )
    #     ax.legend(frameon = True, loc = [.03,.03], ncol = 1, prop={'size': lblsz} )
    #     plt.grid(True)

    #     ax = plt.subplot(133)
    #     ax.yaxis.set_label_coords(-0.03, 0.53)
    #     # loop over the selected time slices to plot the sigmas
    #     for jj in np.arange(len(prtimes)):
    #         sigmaProbes = np.maximum(0.03*probes[:, jj], bitmpi*10.)
    #         #sigmaProbes = sigmaProbes[np.argsort(tht)]
    #         nonz = np.nonzero(weights)[0]
    #         #nonz = np.nonzero(probes[:, jj])[0]
    #         #plt.semilogy(180*tht2[nonz]/np.pi, \
    #         #         sigmaProbes[nonz]/abs(probes[nonz, jj]), \
    #         #         label = str(time[prtimes[jj]]) + ' s' )
    #         #plt.semilogy(180*tht2[nonz]/np.pi, 0.03*np.ones(len(nonz)),'k--')
    #         plt.semilogy(nonz, sigmaProbes[nonz]/abs(probes[nonz, jj]), \
    #                  label = str(time[prtimes[jj]]) + ' s' )
    #         plt.semilogy(nonz, 0.03*np.ones(len(nonz)),'k--')
    #     ax.tick_params(labelsize = lblsz)
    #     ax.set_xlabel(r'probe', fontsize = lblsz )
    #     #ax.set_xlabel(r'$\theta$', fontsize = lblsz )
    #     ax.set_ylabel(r'$\sigma/B_p$', fontsize = lblsz )
    #     #ax.legend(frameon = True, loc = [.03,.65], ncol = 1, prop={'size': lblsz} )
    #     plt.grid(True)
    #     plt.show()
    # #     plt.savefig('Probes_vs_theta' + str(shotnum) + '.png')

    #   #############################################################################
    #   # plot psi, Btor, JtorFB, and JtorDS on the (R,Z) grid
    #   #############################################################################
    #     fig = plt.figure(1, [15,10])
    #     plt.subplots_adjust(left=0.07, right=0.99, top=0.96, bottom=0.08,\
    #                         wspace =0.0, hspace = 0.11)
    #     for ii in np.arange(4):
    #         field2D = outputs[ii][..., time_indx].T
    #         ax = plt.subplot(2, 2, ii+1)
    #         ax.tick_params(labelsize = lblsz)
    #         plt.title(field_title[ii], fontsize = lblsz)
    # #         plt.pcolor(R, Z, field2D)
    # #         plt.colorbar()
    # #         plt.contour(R, Z, field2D, 20, colors='k')
    #         if ii % 2 == 0:
    #             lmin, lmax = field2D.min(), field2D.max()
    #         plt.pcolor(R, Z, field2D, vmin=lmin, vmax=lmax)
    #         plt.colorbar()
    #         if ii < 3:
    #             n_lines = 20
    #         else:
    #             n_lines = 10
    #         plt.contour(R, Z, field2D, n_lines, colors='k')

    #         if ii > 1:
    #             ax.set_xlabel(r'$R$', fontsize = lblsz )
    #         else:
    #             ax.set_xticks([])
    #         if np.mod(ii, 2)==0:
    #             ax.set_ylabel(r'$Z$', fontsize = lblsz )
    #         else:
    #             ax.set_yticks([])
    #         ax.text(.7, 0.05,'time = '+ str(time[time_indx]), \
    #              transform=ax.transAxes, size=18, color='w')
    #     plt.show()
    #     plt.close("all")
    #     field_title =[r'$\psi(R,Z) & NN: \psi(R,Z)$', r'$NN: \psi(R,Z)$',\
    #                   r'$J_{\phi}^{FB}(R,Z)& NN: J_{\phi}^{FB}(R,Z)$',
    #                   r'$NN: J_{\phi}^{FB}(R,Z)$']
    #     fig = plt.figure(1, [15,10])
    #     plt.subplots_adjust(left=0.07, right=0.99, top=0.96, bottom=0.08,\
    #                         wspace =0.0, hspace = 0.11)
    #     for ii in [0,2]:
    # #     for ii in np.arange(4):
    #         field2D = outputs[ii][..., time_indx].T
    #         field2D_nn = outputs[ii+1][..., time_indx].T
    #         ax = plt.subplot(2, 2, ii+1)
    #         ax.tick_params(labelsize = lblsz)
    #         plt.title(field_title[ii], fontsize = lblsz)
    #         if ii % 2 == 0:
    #             lmin, lmax = field2D.min(), field2D.max()
    # #             n_lines =
    # #         plt.pcolor(R, Z, field2D, vmin=lmin, vmax=lmax)
    # #         plt.colorbar()
    #         if ii < 3 :
    #             n_lines =20
    #         else:
    #             n_lines =10
    #         plt.contour(R, Z, field2D, levels=np.linspace(lmin, lmax, n_lines),\
    #                         linestyles='solid', colors='k')

    #         plt.contour(R, Z, field2D_nn, levels=np.linspace(lmin, lmax, n_lines),\
    #                         linestyles='dashed', colors='r')
    #         if ii > 1:
    #             ax.set_xlabel(r'$R$', fontsize = lblsz )
    #         else:
    #             ax.set_xticks([])
    #         if np.mod(ii, 2)==0:
    #             ax.set_ylabel(r'$Z$', fontsize = lblsz )
    #         else:
    #             ax.set_yticks([])
    #         ax.text(.7, 0.05,'time = '+ str(time[time_indx]), \
    #              transform=ax.transAxes, size=18, color='w')
    #     plt.show()
    plt.close("all")
    # plt.rc('text',usetex=True)
    # plt.rc('font',family='serif')
    lblsz = 16
    #     field_title =[r'$\psi(R,Z)$', r'$B_{\phi}(R,Z)$',\
    #                   r'$J_{\phi}^{FB}(R,Z)$',r'$J_{\phi}^{DS}(R,Z)$']

    field_title = [
        r"$\psi(R,Z)$",
        r"NN: $\psi(R,Z)$",
        r"$J_{\phi}^{FB}(R,Z)$",
        r"NN: $J_{\phi}^{FB}(R,Z)$",
    ]

    # choose a time index at random over time slices
    time_indx = rd.randint(len(time))
    print("............time_indx", time_indx)
    # plot psi, Btor, JtorFB, and JtorDS on the (R,Z) grid
    _ = plt.figure(1, [15, 10])
    plt.subplots_adjust(
        left=0.07, right=0.99, top=0.96, bottom=0.08, wspace=0.0, hspace=0.11
    )
    for ii in np.arange(4):
        field2D = outputs[ii][..., time_indx].T
        ax = plt.subplot(2, 2, ii + 1)
        ax.tick_params(labelsize=lblsz)
        plt.title(field_title[ii], fontsize=lblsz)
        if ii % 2 == 0:
            lmin, lmax = field2D.min(), field2D.max()
        plt.pcolor(R, Z, field2D, vmin=lmin, vmax=lmax)
        plt.colorbar()
        if ii % 2 == 0:
            plt.contour(
                R,
                Z,
                field2D,
                levels=np.linspace(lmin, lmax, 10),
                linestyles="solid",
                colors="k",
            )
        else:
            plt.contour(
                R,
                Z,
                field2D,
                levels=np.linspace(lmin, lmax, 10),
                linestyles="dashed",
                colors="r",
            )

        if ii > 1:
            ax.set_xlabel(r"$R$", fontsize=lblsz)
        else:
            ax.set_xticks([])
        if np.mod(ii, 2) == 0:
            ax.set_ylabel(r"$Z$", fontsize=lblsz)
        else:
            ax.set_yticks([])
        ax.text(
            0.7,
            0.05,
            "time = " + str(time[time_indx]),
            transform=ax.transAxes,
            size=18,
            color="w",
        )
    plt.show()

    plt.close("all")
    # plt.rc('text',usetex=True)
    # plt.rc('font',family='serif')
    lblsz = 16
    #     field_title =[r'$\psi(R,Z)$', r'$B_{\phi}(R,Z)$',\
    #                   r'$J_{\phi}^{FB}(R,Z)$',r'$J_{\phi}^{DS}(R,Z)$']

    field_title = [
        r"$\psi(R,Z) & NN: $\psi(R,Z)$",
        r"$J_{\phi}^{FB}(R,Z) & NN:  J_{\phi}^{FB}(R,Z)$",
    ]

    # choose a time index at random over time slices
    #     time_indx = rd.randint(len(time))

    # plot psi, Btor, JtorFB, and JtorDS on the (R,Z) grid
    _ = plt.figure(1, [15, 10])
    plt.subplots_adjust(
        left=0.07, right=0.99, top=0.96, bottom=0.08, wspace=0.0, hspace=0.11
    )
    for ii in [0, 2]:
        field2D = outputs[ii][..., time_indx].T
        field2D_nn = outputs[ii + 1][..., time_indx].T
        ax = plt.subplot(2, 2, ii + 1)
        ax.tick_params(labelsize=lblsz)
        #         plt.title(field_title[ii], fontsize = lblsz)
        if ii % 2 == 0:
            lmin, lmax = field2D.min(), field2D.max()
        #         plt.pcolor(R, Z, field2D, vmin=lmin, vmax=lmax)
        #         plt.colorbar()

        plt.contour(
            R,
            Z,
            field2D,
            levels=np.linspace(lmin, lmax, 10),
            linestyles="solid",
            colors="k",
        )

        plt.contour(
            R,
            Z,
            field2D_nn,
            levels=np.linspace(lmin, lmax, 10),
            linestyles="dashed",
            colors="r",
        )
        if ii > 1:
            ax.set_xlabel(r"$R$", fontsize=lblsz)
        else:
            ax.set_xticks([])
        if np.mod(ii, 2) == 0:
            ax.set_ylabel(r"$Z$", fontsize=lblsz)
        else:
            ax.set_yticks([])
        ax.text(
            0.7,
            0.05,
            "time = " + str(time[time_indx]),
            transform=ax.transAxes,
            size=18,
            color="w",
        )
    plt.show()


# #     plt.savefig('EFITsolutions' + str(shotnum) + '.png')

#     #############################################################################
#     ##           plot select constraints vs time                               ##
#     #############################################################################
#     fig = plt.figure(2)
#     plt.subplots_adjust(left=0.11, right=0.99, top=0.92, bottom=0.14)
#     ax = plt.subplot(111)
#     ax.tick_params(labelsize = lblsz)
#     plt.title('Constraints', fontsize = lblsz)
#     plt.plot(time, inputs[prb_indx[0],:], lw=2, label = 'probe '+ str(prb_indx[0]))
#     plt.plot(time, inputs[prb_indx[0]+1,:], lw=2,
#              label = 'probe '+ str(prb_indx[0]+1) )
#     plt.plot(time, inputs[121, :],'--', lw=2, label=r'$I_p(MA)$')
#     plt.plot(time, inputs[76  + fl_indx[0], :], '-.', lw=2, \
#              label = 'Fl loop '+ str(fl_indx[0]) )
#     if len(inputs[:,1]) > 122: # figure out nonzero MSE cords and plot a couple
#         mse_indx = np.arange(3)#rd.randint(0, 11, 3) # pick 3 at random
#         #plt.plot(time, inputs[122 + mse_indx[0], :], '.', lw=2, \
#         #         label = 'MSE ch '+ str(mse_indx[0]) )
#         plt.plot(time, 5*inputs[122 + mse_indx[1], :], '.', lw=2, \
#                  label = r'5 $\times$MSE ch '+ str(mse_indx[1]) )
#         plt.plot(time, 5*inputs[122 + mse_indx[2], :], '.', lw=2, \
#                  label = r'5 $\times$MSE ch '+ str(mse_indx[2]) )
#     plt.grid(True)
#     plt.xlabel(r'time (s)', fontsize = lblsz )
#     ax.legend( frameon=False, loc = [.25,.63], ncol =2 ,prop={'size': 14} )
#     plt.show()
# # #     plt.savefig('constraints_vs_time' + str(shotnum) + '.png')


#     #############################################################################
#     ##           plot the first 4 SVD eigenmodes                               ##
#     #############################################################################
#     svd_title = ['mode 0', 'modes 0--1', 'modes 0--2', 'modes 0--3']
#     JtorDS = outputs[3][..., time_indx].T
#     U, S, Vt = svd(JtorDS)
#     fig = plt.figure(3, [15,10])
#     plt.subplots_adjust(left=0.07, right=0.99, top=0.96, bottom=0.08,\
#                         wspace =0.0, hspace = 0.11)
#     for ii in np.arange(4):
#         field2D = SVDfilter_sigs(JtorDS, ii+1)
#         ## if you want to look at each mode separately uncomment the following:
#         #field2D = S[ii]*np.outer(U[:,ii], Vt[ii,:])
#         ax = plt.subplot(2, 2, ii+1)
#         ax.tick_params(labelsize = lblsz)
#         plt.title(svd_title[ii], fontsize = lblsz)
#         plt.pcolor(R, Z, field2D)
#         plt.colorbar()
#         plt.contour(R, Z, field2D, 20, colors='k')
#         if ii > 1:
#             ax.set_xlabel(r'$R$', fontsize = lblsz )
#         else:
#             ax.set_xticks([])
#         if np.mod(ii, 2)==0:
#             ax.set_ylabel(r'$Z$', fontsize = lblsz )
#         else:
#             ax.set_yticks([])
#         ax.text(.65, 0.05,'time = '+ str(time[time_indx]), \
#              transform=ax.transAxes, size=18, color='w')
#         ax.text(.65, 0.85,r'$\lambda = $'+ str(round(S[ii],1)), \
#              transform=ax.transAxes, size=18, color='w')
#     #plt.show()
# #     plt.savefig('JtorDS_SVD_4eigenmodes' + str(shotnum) + '.png')


def main():
    """
    Extract the features and targets; and make plots
    """
    parser = optparse.OptionParser(usage="%prog [options] OMAS_file_name")
    parser.add_option("-m", "--machine", help="Set the machine name ", default="DIII-D")
    options, args = parser.parse_args()

    # Sanity checks
    if not len(args) == 1:
        parser.print_usage()
        return

    input_file = args[0]

    if not os.path.exists(input_file):
        print("Input file ", input_file, " must exist.")
        return
    if os.path.splitext(input_file)[1] not in [".h5"]:
        print("Input file ", input_file, " must be an h5 file.")
        return

    if check_vacuum(input_file):
        print("This is a vacuum shot. Skip it!")
    else:
        hin = h5py.File(input_file, mode="r")
        metagrp = hin.get("dataset_description/data_entry")
        shotnum = str(metagrp.get("pulse")[()])
        R, Z = get_grid(hin.get("equilibrium/time_slice/0"))
        inputs, times, TotalChi2 = extract_inputs(input_file, "01")
        EFIToutputs = extract_outputs(input_file)
        _ = extract_other_outputs(input_file)
        # plot constraints and psi or Jtor
        plot_data(inputs, EFIToutputs, times, R.T, Z.T, shotnum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print((end - start) / 60.0, " mins")
