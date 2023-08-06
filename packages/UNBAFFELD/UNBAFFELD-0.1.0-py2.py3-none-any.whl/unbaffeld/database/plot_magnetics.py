#!/usr/bin/env python
"""
Plot the magnetics possibly, along with the equilibrium

extract_magnetics.py essentially converts the omas format into a dictionary
that is more useful to work with.  This takes that format, and then sets that
"""
import os
import extract_magnetics as exmags
import plot_equilibrium as pleq
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def plot_probe_locs(magdict, ax1):
    """
    Plot the probes on the equilibrium plot in the same way that OMFIT does it.
    Key plotting info is from magneticConstraints.py in OMFIT by Orso Meneghini
    """
    fontsize = 10
    # scaleSizes = 50.0
    # cm = get_cmap('RdYlGn')

    # FLUX LOOPS
    x0 = magdict["flux_loop"]["R"]
    y0 = magdict["flux_loop"]["Z"]
    # TODO:  Have the interface include the time dependent data and have the
    #  size and color use that like EFIT
    # COILS is the actual signal -- so scale the size according to signal
    # s0 = squeeze((kEQDSK['IN1']['COILS'] != 0) * scaleSizes)[: len(x0)]
    # FWTSI is the fit weights.  So this colors according to that
    # c0 = squeeze(kEQDSK['IN1']['FWTSI'])[: len(x0)]
    _ = ax1.scatter(x0, y0, vmin=0, marker="o", alpha=0.75)
    #                s=s0, c=c0,  cmap=cm,

    for k in range(len(x0)):
        ax1.text(
            x0[k],
            y0[k],
            "\n " + str(k + 1),
            horizontalalignment="left",
            verticalalignment="top",
            fontsize=fontsize,
            color="w",
            zorder=1000,
            weight="bold",
        )
        ax1.text(
            x0[k],
            y0[k],
            "\n " + str(k + 1),
            horizontalalignment="left",
            verticalalignment="top",
            fontsize=fontsize,
            color="k",
            zorder=1001,
        )

    # Magnetic Probes
    x0 = magdict["magnetic_probes"]["r_center"]
    y0 = magdict["magnetic_probes"]["z_center"]
    l0 = magdict["magnetic_probes"]["length"]
    a0 = magdict["magnetic_probes"]["angle"]
    # EXPMT:  Experimental probe signals
    # s0 = squeeze((kEQDSK['IN1']['EXPMP2'] != 0) * scaleSizes)[: len(x0)]
    # c0 = squeeze(fwtmp2)[: len(x0)]

    # second, detect the negative-length probes and compute the
    # 90 deg = pi/2 [rad] angle to be exploited as a correction
    sgn = np.abs(l0) / l0
    boo = (1 - sgn) / 2.0
    cor = boo * np.pi / 2.0

    # then, compute the two-point arrays to build the partial rogowskis
    # as segments rather than single points, applying the correction
    px = x0 - l0 / 2.0 * np.cos(a0 * np.pi / 180.0 + cor)
    py = y0 - l0 / 2.0 * np.sin(a0 * np.pi / 180.0 + cor)
    qx = x0 + l0 / 2.0 * np.cos(a0 * np.pi / 180.0 + cor)
    qy = y0 + l0 / 2.0 * np.sin(a0 * np.pi / 180.0 + cor)

    # finally, plot
    for k in range(len(x0)):
        segx = [px[k], qx[k]]
        segy = [py[k], qy[k]]
        # col = cm(c0[k])   # Should figure out how it is colored
        if l0[k] > 0:
            ax1.plot(segx, segy, "-", lw=2, alpha=0.75)
            ax1.plot(x0[k], y0[k], "s", color="b", alpha=0.75)
        else:
            ax1.plot(segx, segy, "s-", lw=2, color="b", alpha=0.75)

    for k in range(len(x0)):
        ax1.text(
            x0[k],
            y0[k],
            "\n " + str(k + 1),
            horizontalalignment="left",
            verticalalignment="top",
            fontsize=fontsize,
            color="w",
            zorder=1000,
            weight="bold",
        )

        ax1.text(
            x0[k],
            y0[k],
            "\n " + str(k + 1),
            horizontalalignment="left",
            verticalalignment="top",
            fontsize=fontsize,
            color="k",
            zorder=1001,
        )

    return


def plot_mag1D(d, axu, axl):
    """
    Plot the magnetic signals and flux loops as 1D signals

    This does NOT call plt.show() to allow multiple equilibria to be shown
    That is, one must call plt.show() after this function is called.

    See extract_magnetics.py for the layout of data
    """
    # Flux loops
    measured = d["flux_loop"][0, :]
    weight = d["flux_loop"][1, :]
    reconstructed = d["flux_loop"][2, :]
    n = len(measured)
    axu.plot(range(n), measured, label="measured")
    axu.plot(range(n), weight, label="weight")
    axu.plot(range(n), reconstructed, label="reconstructed")
    axu.set_title("Flux loops")
    axu.label_outer()

    # Magnetic probes
    measured = d["bpol_probe"][0, :]
    weight = d["bpol_probe"][1, :]
    reconstructed = d["bpol_probe"][2, :]
    n = len(measured)
    axl.plot(range(n), measured, label="measured")
    axl.plot(range(n), weight, label="weight")
    axl.plot(range(n), reconstructed, label="reconstructed")
    axl.set_title("Magnetic Probe (B_pol)")
    axl.label_outer()


def plot_all(magnetics, options, maginfo):
    """
    Use matplotlib to plot equilbria in an entire equilibrium data structure
    """
    for shotlbl in magnetics:
        for time in magnetics[shotlbl]:
            if not time.split(".")[0].isnumeric():
                continue
            d = magnetics[shotlbl][time]
            fig = plt.figure(tight_layout=True)
            gs = gridspec.GridSpec(2, 2)

            ax1 = fig.add_subplot(gs[:, 0])
            fig.suptitle(shotlbl + ": " + time + " ms")
            pleq.plot_eq2D(d, ax1)
            plot_probe_locs(magnetics[shotlbl], ax1)

            ax2 = fig.add_subplot(gs[0, 1])
            ax3 = fig.add_subplot(gs[1, 1])
            plot_mag1D(d, ax2, ax3)
    plt.show()

    return


def main():
    """
    Parse arguments and options and act accordingly
    """
    parser = exmags.parse_magargs()
    parser.add_option(
        "-1", "--1d_plot", help="Make plots 1D", dest="plot1d", action="store_true"
    )

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

    # Keep the equilibrium in the plots
    options.keep_equilibrium = True
    mags = exmags.Magnetics(options)
    mags.get_from_file(input_file)
    maginfo = {}
    maginfo["magglobal"] = mags.magglobal
    maginfo["magprobes"] = mags.magprobes
    maginfo["mp_fields"] = mags.mp_fields
    plot_all(mags.magnetics, options, maginfo)


if __name__ == "__main__":
    main()
