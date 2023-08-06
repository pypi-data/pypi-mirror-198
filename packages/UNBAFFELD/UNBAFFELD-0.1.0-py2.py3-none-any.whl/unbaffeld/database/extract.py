#!/usr/bin/env python
"""
Base class for all extract_ classes
"""
import os
import glob
import optparse
import h5py
import utils


class ExtractData:
    def __init__(self, options=None):
        if options:
            self.verbose = options.verbose
        else:
            self.verbose = False
        self._data = {}
        # This should be defined for each derived class
        # See extract_equilibrium for an example of
        # implementation expectations.
        self.root_name = None
        # TODO:  Show the property trick here

    def _get_shotlabel(self, h5in):
        """
        Find the machine and shot to label the root directory
        """
        metagrp = h5in.get("dataset_description/data_entry")
        if "machine" in metagrp.keys():
            try:
                machine = str(metagrp.get("machine")[()].decode("utf-8"))
            except Exception:
                machine = str(metagrp.get("machine")[()])
        else:
            return None
        return machine + "_" + str(metagrp.get("pulse")[()])

    def get_from_file(self, input_file, h5in=None):
        """
        This method should be defined for each derived class
        #TODO:   Make this a generic get everything
        """
        print("Method not defined")
        return

    # TODO:  Add getting the wall here
    def get_from_directory(self, directory):
        """
        Give a directory and loop over all of the files in it
        """
        for file in glob.glob("*.h5"):
            self.get_from_file(file)
        return

    def dump(self, outfile):
        """
        Save the nested dictionary  into an h5file
        """
        file_exists = os.path.exists(outfile)
        if file_exists:
            print("Adding to file: ", outfile)
            hout = h5py.File(outfile, mode="r+")
        else:
            print("Creating new file: ", outfile)
            hout = h5py.File(outfile, mode="w")

        # Now write out the nested dictionary
        for key, value, h5node in utils.write_dict(self._data[self.root_name], hout):
            # print(key)
            if key not in h5node:
                h5node.create_dataset(key, data=value)

        return

    def restore(self, restore_file):
        """
        Save the data dictionary into an h5file
        """
        file_exists = os.path.exists(restore_file)
        if file_exists:
            print("Restoring from file: ", restore_file)
            h5in = h5py.File(restore_file, mode="r")
        else:
            print("Cannot fine restore file: ", restore_file)
            return

        #  Get the route
        utils.datalist = []
        self._data[self.root_name] = utils.getdbvals(h5in)

        return


def parse_extract_args():
    """
    General arguments that control the extraction
    """
    parser = optparse.OptionParser(usage="%prog [options] omas_datafile(s)")
    parser.add_option(
        "-r",
        "--restore",
        help="Restore data from a previous write(dump) iile",
        dest="restore_file",
        default=None,
    )
    parser.add_option(
        "-e",
        "--excludes",
        help="Comma-delimited list of strings to exclude in ",
        dest="excludes",
        default=None,
    )
    parser.add_option(
        "-o",
        "--output",
        help="Write data to output file",
        dest="output_file",
        default=None,
    )
    parser.add_option(
        "-v", "--verbose", help="Verbose output", dest="verbose", action="store_true"
    )
    return parser
