#!/usr/bin/env python
"""
File to validate h5 files to see if the conform to various EFIT-AI standards
"""
import os
import optparse
import h5py
import validate_fields as vf


class Validate:
    def __init__(self, files, options=None):
        if options:
            self.verbose = options.verbose
            self.require = options.require.split(",")
        else:
            self.verbose = False
            self.require = ["base"]
        self.files = files

    def validate(self):
        """
        Do the actual validation
        """
        ind = "  "
        for file in self.files:
            if not os.path.exists(file):
                print("File does not exist", file)
                continue
            h5in = h5py.File(file, mode="r")
            failures = []

            if self.verbose:
                print("Processing ", file)
            # This set is a python list
            for vsetname in self.require:
                if vsetname not in vf.allsets:
                    print(vsetname, "is not a valid set for validation")
                vsetname = vsetname.strip()
                vset = eval("vf." + vsetname)
                if self.verbose:
                    print(ind, vsetname)
                for vlistname in vset:
                    vlist = eval("vf." + vlistname)
                    if self.verbose:
                        print(2 * ind, vlistname)
                    for member in vlist:
                        if member not in h5in:
                            if self.verbose:
                                print(3 * ind, "Member not found ", member)
                            failures.append(member)
                        else:
                            if self.verbose:
                                print(3 * ind, "Member found ", member)
            if failures:
                print("\nFile not valid (for set " + vsetname + "): ", file)
                print("failures are: ", " ".join(failures), "\n")
            else:
                print("\nFile valid (for set " + vsetname + "): ", file)

        return


def parse_valargs():
    """
    Routine for parsing arguments
    """
    parser = optparse.OptionParser(usage="%prog [options] file(s)")

    rh = "Commit delimited list of set to require from " + str(vf.allsets)
    parser.add_option("-r", "--require", help=rh, default="base")

    parser.add_option(
        "-v", "--verbose", help="Verbose output", dest="verbose", action="store_true"
    )
    return parser


def main():
    """
    Parse arguments and options and act accordingly
    """
    parser = parse_valargs()
    options, args = parser.parse_args()

    # Sanity checks
    if len(args) < 1:
        parser.print_usage()
        return

    # Show how it's used
    if options.verbose:
        print("INSTANTIATING CLASS")
    val = Validate(args[:], options)
    val.validate()


if __name__ == "__main__":
    main()
