#!/usr/bin/env python
"""
Extract the equilibrium from an OMAS-formatted file
"""
import os
import h5py
import numpy as np
import utils
import zlib
from extract import ExtractData, parse_extract_args


class Equilibria(ExtractData):
    def __init__(self, options=None):
        super().__init__(options=options)

        self.time_in = None
        self.slice_in = None
        self.excludes = []
        self.n_eq = 0

        if options:
            if options.time:
                self.time_in = options.time
            if options.slice:
                self.slice_in = options.slice
            if options.excludes:
                self.excludes = options.excludes.split(",")

        # For convenience, make this the same as the key name in the
        # @property function below
        self.root_name = "equilibria"
        self._data[self.root_name] = {}

    # Useful extract function/decorator:
    # Allows the referral to self.equilibria as a member
    @property
    def equilibria(self):
        return self._data["equilibria"]

    def get_from_file(self, input_file, h5in=None):
        """
        Get the data from a singl OMAS file, but store into
        a modified dictionary of that file to enable multiple
        equilibria
        """
        # Get handles
        if not h5in:
            h5in = h5py.File(input_file, mode="r")

        shotlbl = self._get_shotlabel(h5in)
        if not shotlbl:
            print("File invalid because cannot find machine or shot number.")
            return

        # Open the groups of interest
        # TODO:  Need to get the vacuum toroidal fields
        eqgrp = h5in.get("equilibrium")
        time = eqgrp.get("time")[()]

        slice_select = self._get_slices(time)

        eqdct = {}
        for nts in slice_select:
            nts = int(nts)
            timegrp = eqgrp.get("time_slice/" + str(nts))
            timenm = str(time[nts])
            eqdct[timenm] = {}
            if self.verbose:
                print(timenm)
            eqlbl = self._get_eqlabel(timegrp)
            utils.datalist = []
            if self.verbose:
                print("    ", eqlbl)
            eqdct[timenm][eqlbl] = utils.getdbvals(timegrp, self.excludes, self.verbose)
            self.n_eq += 1

        if shotlbl not in self.equilibria:
            self.equilibria[shotlbl] = {}

        # time slice could already exist from combining multiple files
        for timenm in eqdct:
            if timenm not in self.equilibria[shotlbl]:
                self.equilibria[shotlbl][timenm] = eqdct[timenm]
            else:
                # Assume one eqlbl per timenm
                eqlbl = eqdct[timenm].keys()[0]
                self.equilibria[shotlbl][timenm][eqlbl] = eqdct[timenm][eqlbl]
        return

    def _get_eqlabel(self, tgrp):
        """
        The efitai "database" can/should have multiple equilibria for a single
        discharge/time slice.   This requires some type of labeling for each
        equilibria.  Rather than try to come up with some type of complicated
        naming scheme (from files which are usually incomplete in their
        provenance, we use a reproducible hash of the flux function to label
        """
        psi2d = tgrp.get("profiles_2d/0/psi")  # Why the 0?
        # Use adler32 because that is sufficient for our purposes and gives
        # short hashes
        return "eq" + str(zlib.adler32(psi2d[()].data.tobytes()))

    def _get_slices(self, time):
        """
        Choose the slices to pull based on either the time or slice inputs
        """
        t_str = ",".join(str(x) for x in time)
        timestr = t_str.split(",")
        slice_select = None
        if self.time_in:
            # Select times from input
            time_select = self.time_in.split(",")
            slice_select = []
            for ts in time_select:
                if ts in timestr:
                    slice_select.append(timestr.index(ts))
                else:
                    print("Time ", ts, " not found.")

        if self.slice_in:
            slice_select = self.slice_in.split(",")

        if not slice_select:
            slice_select = np.arange(time.size)

        return slice_select

    def list_times_in_file(self, input_file):
        """
        Print the time slices and their associated times
        """
        h5in = h5py.File(input_file, mode="r")
        # Can contain multiple equilibria
        eqgrp = h5in.get("equilibrium")

        # Time slices
        time = eqgrp.get("time")[()]
        time_slices = np.arange(time.size)

        print("Slice", "\t", "time [s]")
        for ts in time_slices:
            print(ts, "\t", time[ts])


def parse_eqargs():
    """
    Routine for getting the options and arguments for extracting equilibrium.py
    It is it's own routine to allow other scripts (like plot_equilibrium.py)
    to use it.
    """
    parser = parse_extract_args()
    parser.add_option(
        "-s",
        "--slice",
        help="Comma delimited list of time slices (integers) select",
        default=None,
    )
    parser.add_option(
        "-t", "--time", help="Comma delimited list of times select", default=None
    )
    parser.add_option(
        "-l",
        "--list",
        help="List all of the times that have equilibria",
        dest="list",
        action="store_true",
    )
    return parser


def main():
    """
    Parse arguments and options and act accordingly
    """
    parser = parse_eqargs()
    options, args = parser.parse_args()

    # Sanity checks
    if len(args) < 1:
        parser.print_usage()
        return

    input_file = args[0]

    if not os.path.exists(input_file):
        print("Input file ", input_file, " must exist.")
        return
    if os.path.splitext(input_file)[1] not in [".h5"]:
        print("Input file ", input_file, " must be an h5 file.")
        return

    # Show how it's used
    if options.verbose:
        print("INSTANTIATING CLASS")
    eqs = Equilibria(options)

    # Sometimes it's useful just to see the times
    if options.list:
        if options.verbose:
            print("LISTING FILE")
        eqs.list_times_in_file(input_file)
        return

    if options.restore_file:
        eqs.restore(options.restore_file)

    eqs.get_from_file(input_file)

    if options.output_file:
        eqs.dump(options.output_file)


if __name__ == "__main__":
    main()
