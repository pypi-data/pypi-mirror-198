#!/usr/bin/env python
"""
Plot the equilibrium quantities come from extract_equilibrium.py

extract_equilibrium.py essentially converts the omas format into a dictionary
so this works mostly on dictionaries along that format, but the equilibrium
class structure itself is a container to manage multiple files and times -- so
we have one method for that structure
"""
import os
import extract_equilibrium as exeq
import plots as eqp
import numpy as np
import h5py
import matplotlib.pyplot as plt


def plot_eq1D(d, fig):
    """
    Plot the 1D profiles in a OMAS-formatted equilibrium dictionary

    This does NOT call plt.show() to allow multiple equilibria to be shown
    That is, one must call plt.show() after this function is called.
    """
    profiles = ["psi", "pressure", "f", "q", "phi", "j_tor", "dvolume_dpsi"]
    profiles += ["volume", "r_outboard", "r_inboard", "triangularity_upper"]
    titles = [None] * len(profiles)
    npsi = d["profiles_1d"]["f"].shape[0]
    p1d = np.zeros((len(profiles), npsi), np.double)
    i = 0
    for pname in profiles:
        p1d[i, :] = d["profiles_1d"][pname]
        titles[i] = pname
        i += 1

    eqp.plot_profiles(p1d, titles, fig)


def plot_eq2D(d, ax1):
    """
    Grab the relevant quantities for a single dict and call the plot
    This does NOT call plt.show() but must be done afterwards
    """
    psia = np.float64(d["global_quantities"]["psi_axis"])
    psib = np.float64(d["global_quantities"]["psi_boundary"])
    rg = d["profiles_2d"]["0"]["grid"]["dim1"]
    zg = d["profiles_2d"]["0"]["grid"]["dim2"]
    psi2d = d["profiles_2d"]["0"]["psi"]
    eqp.plotPsi2D(rg, zg, psi2d, psia, psib, ax1, noShow=True)

    # Plot boundary
    rzbound = []
    rzbound.append(d["boundary"]["outline"]["r"])
    rzbound.append(d["boundary"]["outline"]["z"])
    ax1.plot(rzbound[0], rzbound[1], linestyle="-", color="blue")

    # Plot X-points
    xpts = np.zeros((2, 2), np.double)
    xpts[0, 0] = d["boundary"]["x_point"]["0"]["r"][()]
    xpts[0, 1] = d["boundary"]["x_point"]["0"]["z"][()]
    xpts[1, 0] = d["boundary"]["x_point"]["1"]["r"][()]
    xpts[1, 1] = d["boundary"]["x_point"]["1"]["z"][()]
    ax1.scatter(xpts[0, 0], xpts[0, 1], color="red")
    ax1.scatter(xpts[1, 0], xpts[1, 1], color="red")


def plot_text(d, ax2):
    # Plot text from global_quantiites.  Need to clean
    txtdct = {}
    for i in d["global_quantities"]:
        if isinstance(d["global_quantities"][i], h5py.Group):
            continue
        if isinstance(d["global_quantities"][i], dict):
            continue
        txtdct[i] = np.format_float_positional(
            d["global_quantities"][i][()], precision=2
        )
    eqp.plotAddText(txtdct, ax2)


def plot_all(equilibria, options):
    """
    Use matplotlib to plot equilbria in an entire equilibrium data structure
    from extract_equilibrium.py
    """
    for shotlbl in equilibria:
        for time in equilibria[shotlbl]:
            for eqrun in equilibria[shotlbl][time]:
                d = equilibria[shotlbl][time][eqrun]
                if not options.plot1d:
                    fig, (ax1, ax2) = plt.subplots(1, 2)
                    fig.suptitle(shotlbl + ": " + time + " ms")
                    plot_eq2D(d, ax1)
                    plot_text(d, ax2)
                else:
                    fig = plt.figure()
                    fig.suptitle(shotlbl + ": " + time + " ms")
                    plot_eq1D(d, fig)
    plt.show()

    return


def main():
    """
    Parse arguments and options and act accordingly
    """
    parser = exeq.parse_eqargs()
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

    # Exclude stuff that isn't plotted
    options.excludes = "constraints,code"
    eqs = exeq.Equilibria(options)
    eqs.get_from_file(input_file)
    plot_all(eqs.equilibria, options)


if __name__ == "__main__":
    main()
