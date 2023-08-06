#!/usr/bin/env python
"""
Extract the magnetics data from an OMAS formatted file and put into
a format useful for further analysis.  Because the magnetics data in OMAS is a
subset of equilibrium, the Magnetics class inherits from Equilibria and is
tailored to just those issues.
"""
import os
import h5py
import numpy as np
import utils
from extract_equilibrium import Equilibria, parse_eqargs


file_dir = os.path.dirname(os.path.abspath(__file__))


class Magnetics(Equilibria):
    def __init__(self, options=None):
        super().__init__(options=options)

        # Default skips equilibrium quantities to minimize data
        if options.keep_equilibrium is not True:
            self.excludes = ["profiles_1d", "profiles_2d"]

        # For convenience, make this the same as the key name in the
        # @property function below
        self.root_name = "magnetics"
        self._data[self.root_name] = {}

    # Useful extract function/decorator:
    # Allows the referral to self.equilibria as a member
    @property
    def magnetics(self):
        return self._data["magnetics"]

    def get_from_file(self, input_file, h5in=None):
        """
        Because the inputs relevant to magnetics are invariant for different
        equilibria, it is stored very differently than the default
        extract_equilibrium method
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
            utils.datalist = []
            eqdct[timenm] = utils.getdbvals(timegrp, self.excludes, self.verbose)
            self.n_eq += 1

        if shotlbl not in self.magnetics:
            self.magnetics[shotlbl] = {}

        # This could possibly be in constructor, but it might be machine
        # specific
        self.magglobal = ["diamagnetic_flux", "ip"]
        self.magprobes = ["bpol_probe", "flux_loop", "pf_current"]

        self.mp_fields = {}
        for probe in self.magprobes:
            self.mp_fields[probe] = ["measured", "weight", "reconstructed"]
        self.mp_fields["bpol_probe"] += ["exact", "chi_squared"]
        self.mp_fields["flux_loop"] += ["exact", "chi_squared"]
        for diag in self.magglobal:
            self.mp_fields[diag] = ["exact", "measured"]

        nprobes = []
        # Nested dictionary is verbose and not useful for analysis
        magdct = {}
        if self.verbose:
            print("\n --------------- \n")

        for time in eqdct:
            magdct[time] = {}

            # Note: not using the equilibria datastructure from
            # extract_equilibrium.py for convenience
            eqkeys = list(eqdct[time].keys())
            eqkeys.remove("constraints")  # This is what we alter
            for qty in eqkeys:
                if qty in eqdct[time]:
                    magdct[time][qty] = eqdct[time][qty]

            # Count probes
            for ptype in self.magprobes:
                pdct = eqdct[time]["constraints"][ptype]
                n = 0
                for probe in pdct:
                    n += 1
                nprobes.append(n)
                # Initialize numpy arrays
                nfield = len(self.mp_fields[ptype])
                magdct[time][ptype] = np.zeros((nfield, n), np.double)
                # No redo loop while filling these arrays
                for probe in pdct:
                    j = int(probe)
                    i = 0
                    for fields in self.mp_fields[ptype]:
                        if self.verbose:
                            print(ptype, probe, fields)
                        magdct[time][ptype][i, j] = pdct[probe][fields][()]
                        i += 1
            for ptype in self.magglobal:
                nfield = len(self.mp_fields[ptype])
                magdct[time][ptype] = np.zeros((nfield, 1), np.double)
                i = 0
                pdct = eqdct[time]["constraints"][ptype]
                for fields in self.mp_fields[ptype]:
                    magdct[time][ptype][i, 0] = pdct[fields][()]
                    i += 1
                    if self.verbose:
                        print(ptype, fields)

        self.magnetics[shotlbl] = magdct
        self.magnetics[shotlbl].update(self.get_machine_data(shotlbl))

        return h5in

    def get_machine_data(self, shotlbl):
        """
        See if machine data can be found and read it in
        """
        machine, shot = shotlbl.split("_")
        shot = int(shot)
        data_filename = machine + "_machine.h5"
        mfile = os.path.join(os.path.dirname(file_dir), "data", data_filename)
        h5in = h5py.File(mfile, mode="r")

        for setnm in h5in:
            if not setnm.startswith("efit_set"):
                continue
            h5set = h5in.get(setnm)
            min_pulse_num = int(h5set.get("min_pulse_num")[()])
            max_pulse_num = int(h5set.get("max_pulse_num")[()])

            if min_pulse_num <= shot < max_pulse_num:
                magnetics = utils.getdbvals(h5set, verbose=self.verbose)

                return magnetics

        # If this is returned, then correct range was not found
        return None


def parse_magargs():
    """
    Routine for getting the options and arguments for extracting equilibrium.py
    It is it's own routine to allow other scripts (like plot_equilibrium.py)
    to use it.
    """
    parser = parse_eqargs()
    parser.add_option(
        "-k",
        "--keep_equilibrium",
        help="Keep equilibrium data with the magnetics data",
        dest="keep_equilibrium",
        action="store_true",
    )
    return parser


def main():
    """
    Parse arguments and options and act accordingly
    """
    parser = parse_magargs()
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
    mags = Magnetics(options)

    # Sometimes it's useful just to see the times
    if options.list:
        if options.verbose:
            print("LISTING FILE")
        mags.list_times_in_file(input_file)
        return

    if options.restore_file:
        mags.restore(options.restore_file)

    mags.get_from_file(input_file)

    if options.output_file:
        mags.dump(options.output_file)


if __name__ == "__main__":
    main()
