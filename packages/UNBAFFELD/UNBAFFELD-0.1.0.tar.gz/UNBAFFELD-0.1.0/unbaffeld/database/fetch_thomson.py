#!/usr/bin/python
#
import getopt
import numpy as np
import os

# from omas import *
import matplotlib.pyplot as plt
from scipy import interpolate

SMALL_SIZE = 12
MEDIUM_SIZE = 20

def main(argv):
    shot = ""
    time = ""
    machine = "d3d"
    allShots = False
    folderM = "/fusion/projects/efitai/database/magnetic"
    folderS = "/fusion/projects/efitai/database/mse"
    folderK = "/fusion/projects/efitai/database/kinetic"
    folder = folderM
    try:
        opts, args = getopt.getopt(argv, "hs:t:d:m:e:a")
    except getopt.GetoptError:
        print("getTS.py -s <shotNumber> -t <time_in_sec> -e <magnetic/mse/kinetic> -all")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("getTS.py -s <shotNumber> -t <time_in_sec>")
            sys.exit()
        elif opt in ("-e", "--equilibrium"):
            if arg == "kinetic" :
               folder = folderK
            elif arg == "mse" :
               folder == folderS
            elif arg == "magnetic" :
               folder = folderM
            else :
               print("Invalid selection for option --eqilibrium. Default magnetic is used")
               folder = folderM
        elif opt in ("-a", "--all"):
            allShots = True
        elif opt in ("-s", "--shot"):
            shot = int(arg)
        elif opt in ("-m", "--machine"):
            machine = arg
        elif opt in ("-t", "--time"):
            time = float(arg)
        elif opt in ("-d", "--directory"):
            folder = arg
    if not allShots : 
        if shot == "":
           print("Shot number is undefined\ngetTS.py -s <shotNumber> -t <time_in_sec>")
           sys.exit(1)
        if time == "":
           print("Time is undefined\ngetTS.py -s <shotNumber> -t <time_in_sec>")
           sys.exit(1)
    return shot, time, machine, folder, allShots


from omfit_classes.omfit_thomson import *
class thomsonScattering:
    def __init__(self, machine, shot):
        tokamaks = {"d3d": "DIII-D"}
        self.machine = machine
        self.shot = shot
        # ods = ODS()
        # with ods.open(self.machine, self.shot) :
        # self.R = ods['thomson_scattering.channel[:].position.r']
        # self.ne = ods['thomson_scattering.channel[:].n_e.data']
        # self.neTime = ods['thomson_scattering.channel[:].n_e.time']
        # self.te = ods['thomson_scattering.channel[:].t_e.data']
        # self.teTime = ods['thomson_scattering.channel[:].t_e.time']
        for r in [-1, 1, 0] :
            ts = OMFITthomson(tokamaks[self.machine], self.shot, revision_num=r)
            ts.gather()
            if not(isinstance((ts["raw"]["core"]["r"]), type(None))):
               break
        self.R = list(ts["raw"]["core"]["r"]) + list(ts["raw"]["tangential"]["r"])
        self.Z = list(ts["raw"]["core"]["z"]) + list(ts["raw"]["tangential"]["z"])
        self.PHI = list(np.zeros(len(self.R)))
        # remove times with empty measurements
        timeNeC = []
        timeTeC = []
        neCC = []
        nerrCC = []
        teCC = []
        terrCC = []
        for (ne, te, nerr, terr) in zip(
            ts["raw"]["core"]["density"],
            ts["raw"]["core"]["temp"],
            ts["raw"]["core"]["density_e"],
            ts["raw"]["core"]["temp_e"],
        ):
            timeNeC.append(ts["raw"]["core"]["time"][:])
            timeTeC.append(ts["raw"]["core"]["time"][:])
            neCC.append(ne[:])
            teCC.append(te[:])
            nerrCC.append(nerr[:])
            terrCC.append(terr[:])
        timeNeT = []
        timeTeT = []
        neTC = []
        nerrTC = []
        teTC = []
        terrTC = []
        for (ne, te, nerr, terr) in zip(
            ts["raw"]["tangential"]["density"],
            ts["raw"]["tangential"]["temp"],
            ts["raw"]["tangential"]["density_e"],
            ts["raw"]["tangential"]["temp_e"],
        ):
            timeNeT.append(ts["raw"]["tangential"]["time"][:])
            timeTeT.append(ts["raw"]["tangential"]["time"][:])
            neTC.append(ne[:])
            teTC.append(te[:])
            nerrTC.append(nerr[:])
            terrTC.append(terr[:])
        self.nchannels = len(self.R)
        self.fneC = [
            interpolate.interp1d(t, ne, kind="linear") for (t, ne) in zip(timeNeC, neCC)
        ]
        self.fteC = [
            interpolate.interp1d(t, te, kind="linear") for (t, te) in zip(timeTeC, teCC)
        ]
        self.fneT = [
            interpolate.interp1d(t, ne, kind="linear") for (t, ne) in zip(timeNeT, neTC)
        ]
        self.fteT = [
            interpolate.interp1d(t, te, kind="linear") for (t, te) in zip(timeTeT, teTC)
        ]
        self.fnerrC = [
            interpolate.interp1d(t, nerr, kind="linear")
            for (t, nerr) in zip(timeNeC, nerrCC)
        ]
        self.fterrC = [
            interpolate.interp1d(t, terr, kind="linear")
            for (t, terr) in zip(timeTeC, terrCC)
        ]
        self.fnerrT = [
            interpolate.interp1d(t, nerr, kind="linear")
            for (t, nerr) in zip(timeNeT, nerrTC)
        ]
        self.fterrT = [
            interpolate.interp1d(t, terr, kind="linear")
            for (t, terr) in zip(timeTeT, terrTC)
        ]
        return

    def getNe(self, time):
        return np.transpose(
            [fc(time)[()] for fc in self.fneC] + [fc(time)[()] for fc in self.fneT]
        )

    def getTe(self, time):
        return np.transpose(
            [fc(time)[()] for fc in self.fteC] + [fc(time)[()] for fc in self.fteT]
        )

    def getNerr(self, time):
        return np.transpose(
            [fc(time)[()] for fc in self.fnerrC] + [fc(time)[()] for fc in self.fnerrT]
        )

    def getTerr(self, time):
        return np.transpose(
            [fc(time)[()] for fc in self.fterrC] + [fc(time)[()] for fc in self.fterrT]
        )

    def getR(self):
        return np.transpose(
            [self.R]
        )

    def getZ(self):
        return np.transpose(
            [self.Z]
        )

    def getnChannels(self):
        return self.nchannels

    def getPsi(self, eq, r, z):
        from scipy import interpolate

        self.r0 = eq["global_quantities"]["magnetic_axis"]["r"][()]
        self.z0 = eq["global_quantities"]["magnetic_axis"]["z"][()]
        self.psi_axis = eq["global_quantities"]["psi_axis"][()]
        self.psi_boundary = eq["global_quantities"]["psi_boundary"][()]
        psi = interpolate.interp2d(
            eq["profiles_2d"]["0"]["grid"]["dim1"],
            eq["profiles_2d"]["0"]["grid"]["dim2"],
            eq["profiles_2d"]["0"]["psi"],
            kind="linear",
        )(r, z)[0]
        psi_norm = (psi - self.psi_axis) / (self.psi_boundary - self.psi_axis)
        return psi_norm, psi

    def gather(self, eq, time):
        ne = self.getNe(time)
        nerr = self.getNerr(time)
        te = self.getTe(time)
        terr = self.getTerr(time)
        psi_norm = [self.getPsi(eq, r, z)[0] for (r, z) in zip(self.R, self.Z)]
        psi = [self.getPsi(eq, r, z)[1] for (r, z) in zip(self.R, self.Z)]
        self.ne = [x for _, x in sorted(zip(psi_norm, ne))]
        self.te = [x for _, x in sorted(zip(psi_norm, te))]
        self.nerr = [x for _, x in sorted(zip(psi_norm, nerr))]
        self.terr = [x for _, x in sorted(zip(psi_norm, terr))]
        self.psi = [x for _, x in sorted(zip(psi_norm, psi))]
        self.psi_norm = sorted(psi_norm)

    def plotNe(self):
        fig, ax = plt.subplots()
        plt.rc("font", size=SMALL_SIZE)  # controls default text sizes
        plt.rc("xtick", labelsize=SMALL_SIZE)  # fontsize of the tick labels
        plt.rc("ytick", labelsize=SMALL_SIZE)  # fontsize of the tick labels
        plt.rc("axes", titlesize=MEDIUM_SIZE)  # fontsize of the axes title
        plt.rc("axes", labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
        plt.rc("legend", fontsize=SMALL_SIZE)  # legend fontsizefrom omas import *
        ax.errorbar(
            self.psi_norm,
            np.array(self.ne) / 1e19,
            yerr=np.array(self.nerr) / 1e19,
            fmt="bo",
            label=None,
        )
        ax.set(xlabel=r"$\psi_n$", ylabel=r"$n_e$ (10$^{19}$ m$^{-3}$)")
        ax.grid()
        ax.relim()
        ax.legend()
        plt.show()

    def plotTe(self):
        fig, ax = plt.subplots()
        plt.rc("font", size=SMALL_SIZE)  # controls default text sizes
        plt.rc("xtick", labelsize=SMALL_SIZE)  # fontsize of the tick labels
        plt.rc("ytick", labelsize=SMALL_SIZE)  # fontsize of the tick labels
        plt.rc("axes", titlesize=MEDIUM_SIZE)  # fontsize of the axes title
        plt.rc("axes", labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
        plt.rc("legend", fontsize=SMALL_SIZE)  # legend fontsizefrom omas import *
        ax.errorbar(
            self.psi_norm,
            np.array(self.te) / 1e3,
            yerr=np.array(self.terr) / 1e3,
            fmt="bo",
            label=None,
        )
        ax.set(xlabel=r"$\psi_n$", ylabel=r"$T_e$ (keV)")
        ax.grid()
        ax.relim()
        ax.legend()
        plt.show()

    def plotRZ(self, eq, limiter):
        fig, ax = plt.subplots()
        plt.rc("font", size=SMALL_SIZE)  # controls default text sizes
        plt.rc("xtick", labelsize=SMALL_SIZE)  # fontsize of the tick labels
        plt.rc("ytick", labelsize=SMALL_SIZE)  # fontsize of the tick labels
        plt.rc("axes", titlesize=MEDIUM_SIZE)  # fontsize of the axes title
        plt.rc("axes", labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
        plt.rc("legend", fontsize=SMALL_SIZE)  # legend fontsizefrom omas import *
        eq_bound = eq["boundary"]["outline"]
        ax.plot(eq_bound["r"][:], eq_bound["z"][:], label=None)
        ax.plot(limiter["r"][:], limiter["z"][:], label=None)
        for i in range(self.nchannels):
            ax.plot(self.R[i], self.Z[i], "o", label=None)
        ax.set(xlabel=r"$r$ (m)", ylabel=r"$z$ (m)")
        ax.set_aspect("equal")
        ax.grid()
        ax.relim()
        ax.legend()
        # fig.savefig(fileName + ".png", transparent=True, bbox_inches='tight')
        plt.show()


if __name__ == "__main__":
    import sys
    import h5py
    import glob

    shots = []
    shot, time, machine, folder, allshots = main(sys.argv[1:])
    if allshots :
       for f in glob.glob(folder+"/*.h5") :
           shots.append(int(f.split('.')[-2].split('/')[-1]))
    else :
       shots = [shot]
       times = [time]
    fLog = open('failed.txt', 'w')
    for ii,s in enumerate(shots) :
       print("Processing ", ii, " out of ", len(shots), " discharges: ", s)
       fName = str(s) + ".h5"
       try :
         ts = thomsonScattering(machine, s)
       except :
         fLog.write(fName + "\n")
         continue
       ierr = os.system('cp ' + folder + "/" + fName + " " + fName)
       ierr = os.system('chmod u+w ' + fName)
       fh5 = h5py.File(fName, "a")
       if allshots :
          times = fh5["equilibrium"]["time"][:]
       gTS = fh5.create_group("thomson_scattering")
       gTS.create_group("ids_properties").create_dataset("homogeneous_time", data=1, dtype='i') 
       gS = gTS.create_group("channel")
       nchannels = ts.getnChannels()
       gChannels = []
       for i in range(nchannels) :
           gChannels.append(gS.create_group(str(i)))
       ne = []
       te = []
       neErr = []
       teErr = []
       badTimes = []
       for t in times :
           try :
              ne.append(ts.getNe(1e3*t))
              te.append(ts.getTe(1e3*t))
              neErr.append(ts.getNerr(1e3*t))
              teErr.append(ts.getTerr(1e3*t))
           except :
              ne.append(np.zeros(len(ne[-1])))
              te.append(np.zeros(len(ne[-1])))
              neErr.append(np.zeros(len(ne[-1])))
              teErr.append(np.zeros(len(ne[-1])))
              badTimes.append(t)
       if len(badTimes)>0 :
           fLog.write(fName + " at times ")
           for t in badTimes :
               fLog.write(str(t) + " ")
           fLog.write("\n")  
       ne = np.transpose(ne)
       te = np.transpose(te)
       neErr = np.transpose(neErr)
       teErr = np.transpose(teErr)
       for ig, gC in enumerate(gChannels) :
           gP = gC.create_group("position")
           gP.create_dataset("r", data=ts.getR()[ig], dtype='float64')
           gP.create_dataset("z", data=ts.getZ()[ig], dtype='float64')
           gP.create_dataset("phi", data=0.0, dtype='float64')
           gTe = gC.create_group("n_e")
           gTe.create_dataset("data", data=ne[ig], dtype='float64')
           gTe.create_dataset("time", data=times, dtype='float64')
           gTe.create_dataset("error", data=neErr[ig], dtype='float64')
           gNe = gC.create_group("t_e")
           gNe.create_dataset("data", data=te[ig], dtype='float64')
           gNe.create_dataset("time", data=times, dtype='float64')
           gNe.create_dataset("error", data=teErr[ig], dtype='float64')
       gTS.create_dataset('time', data=times, dtype='float64')
       if not allshots :
          t_index = str(
            np.argmin(abs(fh5["equilibrium"]["time"][:] - time / 1e3))
            )  # find min index for particular time
          limiter = fh5["wall"]["description_2d"]["0"]["limiter"]["unit"]["0"]["outline"]
          eq = fh5["equilibrium"]["time_slice"][t_index]
          ts.gather(eq, 1e3*time)
          ts.plotRZ(eq, limiter)
          ts.plotNe()
          ts.plotTe()
       fh5.close()
    fLog.close()
