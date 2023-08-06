"""
Plot different quantities of interest.py

Sometimes matplotlib can be difficult to install or cause problems, so this
helps isolate the matplotlib code (somewhat)
isolates those imports.
"""

import matplotlib.pyplot as plt
import numpy as np


def plotPsi2D(rg, zg, psi2d, psia, psib, ax, noShow=False):
    """
    Plot the equilibrium flux surfaces
    Options:
        rz,zg,psi2d:  The flux functiona and grid
        psia, psib:  psi values on axis and boundary respectivly
        ax:   Pass in a matplotlib ax object
        noShow:  Do not invoke show (so that other plots can be added)
    """
    # Fine-tune contours by controlling those in and out of separatrix separately
    minlevels = np.linspace(np.min(psi2d), psib, 25, endpoint=False)
    maxlevels = np.linspace(psib, np.max(psi2d), 20)
    levels = np.concatenate((minlevels, maxlevels), axis=0)
    ax.contour(rg, zg, np.transpose(psi2d), levels=levels)
    # Plot the boundary separately
    ax.contour(rg, zg, np.transpose(psi2d), levels=[psib], colors="black")
    ax.set_aspect("equal")
    ax.set_xlabel("R [m]")
    ax.set_ylabel("Z [m]")
    if not noShow:
        plt.legend()
        plt.show()
    return


def plotAddText(indict, ax):
    """
    Add text from a dictionary to subplot
    """
    ax.axis("off")
    alignment = {}
    # alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
    xoff = 0.0
    yoff = 0.0
    yspace = 0.08
    for var in indict:
        yoff += yspace
        txt = var + " = " + str(indict[var])
        ax.text(xoff, yoff, txt, **alignment, fontsize=11)
    return


def plot_profiles(profiles, titles, fig, noShow=False):
    """
    Plot the profiles
    Assumes 9 profiles + dependent variable in 0
    """
    axs = fig.subplots(3, 3, sharex=True)
    for k in range(1, profiles.shape[0] - 1):
        i = int((k - 1) / 3)
        j = k - 1 - i * 3
        axs[i, j].plot(profiles[0, :], profiles[k])
        axs[i, j].set_title(titles[k])

    for ax in axs.flat:
        # ax.set(xlabel=titles[0], ylabel=titles[k])
        ax.set(xlabel=titles[0])
        ax.label_outer()

    return
