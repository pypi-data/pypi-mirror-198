#!/usr/bin/env python
"""
Module for converting omas format files to efitaidb files
"""
import os
import pandas as pd
import extract_equilibrium as exeq


class EaPandas(exeq.Equilibria):
    def __init__(self, options=None):
        super().__init__(options=options)

        self.eqdf = pd.DataFrame()  # Equilibrium dataframe

        # We are ignore most stuff in the OMAS tree
        self.excludes = "constraints code profiles_2d".split()

    def get_dataframe(self, input_file):
        """
        The dictionary the comes from extract_equilibrium has too many nestings
        when what we want are uniq names for columns so we have to reformat that
        OMAS-oriented nested dictionary with a new one.  This does that

        General order of dict to be converted to dataframe is:
        machine - pulse - time - eq_label - qty_name
        """

        self.get_from_file(input_file)

        for shotlbl in self.equilibria:
            machine, shot = shotlbl.split("_")
            machine = str(machine)
            shot = int(shot)
            for time in self.equilibria[shotlbl]:
                for eqrun in self.equilibria[shotlbl][time]:
                    d = self.equilibria[shotlbl][time][eqrun]
                    e = self._fill_dict(d)

                    # Basic metadata
                    # TODO:  Need eqtype
                    # e["eqlabel"] = eqrun  # Use as index
                    e["filename"] = input_file
                    e["machine"] = machine
                    e["pulse"] = int(shot)
                    e["time"] = float(time)

                    # TODO:  It would be more performant to make a column of
                    # series per file
                    if self.eqdf.empty:
                        self.eqdf = pd.DataFrame(e, index=[eqrun])
                    else:
                        self.eqdf = pd.concat(
                            [self.eqdf, pd.DataFrame(e, index=[eqrun])]
                        )
        #
        # Returning the df itself is useful for interactive work
        return self.eqdf

    def _fill_dict(self, d):
        """
        Fill the pandas-style dictionary (e)  based on the input dictionary (d)
        """
        e = {}

        e["xpt0_r"] = d["boundary"]["x_point"]["0"]["r"][()]
        e["xpt0_z"] = d["boundary"]["x_point"]["0"]["z"][()]
        e["xpt1_r"] = d["boundary"]["x_point"]["1"]["r"][()]
        e["xpt1_z"] = d["boundary"]["x_point"]["1"]["z"][()]

        g = d["global_quantities"]
        e["beta_normal"] = g["beta_normal"][()]
        e["beta_tor"] = g["beta_tor"][()]
        e["ip"] = g["ip"][()]
        e["li_3"] = g["li_3"][()]
        e["magnetic_axis.b_field_tor"] = g["magnetic_axis"]["b_field_tor"][()]
        e["magnetic_axis.r"] = g["magnetic_axis"]["r"][()]
        e["magnetic_axis.z"] = g["magnetic_axis"]["z"][()]
        e["psi_axis"] = g["psi_axis"][()]
        e["psi_boundary"] = g["psi_boundary"][()]
        e["q_axis"] = g["q_axis"][()]
        e["q_95"] = g["q_95"][()]
        e["q_min"] = g["q_min"]["value"][()]
        e["q_min.rho_tor_norm"] = g["q_min"]["rho_tor_norm"][()]

        p = d["profiles_1d"]
        e["elongation"] = p["elongation"][()][-1]
        e["triangularity_upper"] = p["triangularity_upper"][()][-1]
        e["triangularity_lower"] = p["triangularity_lower"][()][-1]
        e["volume"] = p["volume"][()][-1]
        e["area"] = p["area"][()][-1]
        e["surface"] = p["surface"][()][-1]

        # Floats are sufficient for metadata and take up less space
        for qty in e:
            e[qty] = float(e[qty])

        return e

    def restore(self, input_file):
        """
        Restore a previously save eq dataframe
        """
        with pd.HDFStore(input_file) as store:
            if self.eqdf:
                self.eqdf = pd.concat(self.eqdf, store["efitai"])
            else:
                self.eqdf = store["efitai"]

    def dump(self, output_file):
        """
        Write the data -- no sanity checks.
        This overwrites the normal h5py dump in extract.py because we just use
        pandas natural functionality

        TODO:  Add metadata about the metadata (clunky in h5py)
        In particular, we want something about the directory structure, date
        created, etc.
        """
        store = pd.HDFStore(output_file)
        store.put("efitai", self.eqdf)
        store.close()


def main():
    """
    Convert
    """
    parser = exeq.parse_eqargs()
    parser.add_option(
        "-i",
        "--input",
        help="Add dataframe in stored HDF5 file to dataframe",
        dest="input_file",
        default=None,
    )
    options, args = parser.parse_args()

    # Sanity checks
    if len(args) < 1:
        parser.print_usage()
        return

    directory = args[0]

    if not os.path.exists(directory):
        print("Input file ", directory, " must exist.")
        return

    # Show how it's used
    eadf = EaPandas(options)

    # Add saved file to dataframe (if just a restore, one must give a directory
    # with no output files
    if options.input_file:
        eadf.restore(options.input_file)

    for file in args:
        if not os.path.exists(file):
            print("Input file ", file, " must exist.")
            continue
        # TODO:  Check to see if file is already been in dataframe
        eadf.get_dataframe(file)

    if options.output_file:
        eadf.dump(options.output_file)


if __name__ == "__main__":
    main()
