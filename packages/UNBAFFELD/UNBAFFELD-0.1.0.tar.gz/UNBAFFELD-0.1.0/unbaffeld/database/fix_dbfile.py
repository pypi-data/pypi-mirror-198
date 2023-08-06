#!/usr/bin/env python
"""
File to validate h5 files to see if the conform to various EFIT-AI standards
"""
import os
import optparse
import h5py
import validate_fields as vf  # noqa


class FixUp:
    def __init__(self, files, options=None):
        # --fix isn't really optional so misnamed, but any other method is just
        # as ugly
        if options:
            self.verbose = options.verbose
            if not options.fix:
                raise Exception("Nothing to fix.  Use --fix")
            self.fix_items = {}
            for items in options.fix.split():
                key, val = items.split(",")
                print(key, val)
                self.fix_items[key] = val
        else:
            raise Exception("Nothing to fix.  Use --fix")
        self.files = files
        self.require = ["sumsets"]

    def fix(self):
        """
        Do the actual validation
        """
        ind = "  "
        for file in self.files:
            if not os.path.exists(file):
                print("File does not exist", file)
                continue
            h5io = h5py.File(file, mode="r+")

            if self.verbose:
                print("Processing ", file)
            # This set is a python list
            for vsetname in self.require:
                vsetname = vsetname.strip()
                vset = eval("vf." + vsetname)
                for vlistname in vset:
                    vlist = eval("vf." + vlistname)
                    if self.verbose:
                        print(ind, vlistname)
                    for member in vlist:
                        if self.verbose:
                            print(2 * ind, member)
                        for fitem in self.fix_items:
                            # This whole nested loop complication is just to
                            # enable check and make sure we can use short names
                            if fitem in member:
                                val = self.fix_items[fitem]
                                print("Fixing: ", fitem, "with", val)
                                h5io.create_dataset(member, data=val)

            h5io.close()

        return


def parse_fixargs():
    """
    Routine for parsing arguments
    """
    parser = optparse.OptionParser(usage="%prog [options] file(s)")

    rh = "Things to fix:  machine,DIII-D pulse,177452"
    parser.add_option("-f", "--fix", help=rh, default=None)

    parser.add_option(
        "-v", "--verbose", help="Verbose output", dest="verbose", action="store_true"
    )
    return parser


def main():
    """
    Parse arguments and options and act accordingly
    """
    parser = parse_fixargs()
    options, args = parser.parse_args()

    # Sanity checks
    if len(args) < 1:
        parser.print_usage()
        return

    # Show how it's used
    if options.verbose:
        print("INSTANTIATING CLASS")
    fx = FixUp(args[:], options)
    fx.fix()


if __name__ == "__main__":
    main()
