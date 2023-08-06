#!/usr/bin/env python
"""
Module for converting omas format files to efitaidb files
"""
import os
import datetime
import optparse
import h5py
import numpy as np
import pandas as pd


class ThomsonChannels:
    def __init__(self, input_file):
        """
        method for converting from an H5 file that is a discharge-oriented OMAS
        format to one that is EFIT-AI based:  Allow multiple equilibria at a given
        time slice, enable addition of new time slices, etc.
        """
        # Get handles
        hin = h5py.File(input_file, mode="r")

        thomson = hin.get("/inputs/thomson_scattering/channel")
        cd = hin.get("inputs/thomson_scattering/ids_properties/creation_date")
        creation_time = pd.to_datetime(str(cd[()]).strip("b").strip("'"))
        # Creation time can include minutes and seconds which makes it difficult
        # to work with the times as you *must* have this reference time.  To
        # simplify, we strip off H:M:S
        creation_time = pd.to_datetime(creation_time.date())
        rlist = []
        zlist = []
        ne = {}
        neerr = {}
        te = {}
        teerr = {}

        # Loop through channels numerically
        clist = [int(c) for c in thomson.keys()]
        clist.sort()
        channels = np.array(clist, dtype=np.str)

        for channel in channels:
            chgrp = thomson.get(channel)
            posgrp = chgrp.get("position")
            rlist.append(posgrp.get("r")[()])
            zlist.append(posgrp.get("z")[()])
            negrp = chgrp.get("n_e")
            time = negrp.get("time")[()]
            time_dt = creation_time + pd.to_timedelta(time, unit="s")
            # Keep track of channel with most time slices
            ne[channel] = pd.Series(negrp.get("data")[()], index=time, name=channel)
            ne[channel] = pd.Series(negrp.get("data")[()], index=time_dt, name=channel)
            neerr[channel] = pd.Series(
                negrp.get("data_error_upper")[()], index=time_dt, name=channel
            )
            tegrp = chgrp.get("t_e")
            te[channel] = pd.Series(tegrp.get("data")[()], index=time_dt, name=channel)
            teerr[channel] = pd.Series(
                tegrp.get("data_error_upper")[()], index=time_dt, name=channel
            )

        self.n_e = pd.DataFrame(ne)
        self.t_e = pd.DataFrame(te)
        self.n_e_err = pd.DataFrame(neerr)
        self.t_e_err = pd.DataFrame(teerr)
        self.r = np.array(rlist)
        self.z = np.array(zlist)
        self.channels = channels
        self.time_ref = creation_time

    def time_ave(self, time, window):
        """
        Average density and temperature each channel at the time given by the
        time array over the window specified.  The time array and window are
        assumed to be given in msec.
        """
        # between_time is difficult to work with but handles the Nan's well.
        # Adding time_ref converts from timedelta to datetime
        # and then .time() converts to the datetime.time format that
        # between_time needs.

        n_ave = {}
        t_ave = {}
        nchannels = self.n_e.shape[1]
        ntime = len(time)
        tdt = np.zeros(ntime, dtype=datetime.datetime)
        for channel in range(nchannels):
            n_ave[str(channel)] = np.zeros(ntime)
            t_ave[str(channel)] = np.zeros(ntime)
        i = 0
        for t in time:
            strt = self.time_ref + pd.to_timedelta(t - 0.5 * window, unit="ms")
            stop = self.time_ref + pd.to_timedelta(t + 0.5 * window, unit="ms")
            for channel in range(nchannels):
                n_ave[str(channel)][i] = self.n_e.between_time(
                    strt.time(), stop.time()
                ).mean()[channel]
                t_ave[str(channel)][i] = self.t_e.between_time(
                    strt.time(), stop.time()
                ).mean()[channel]
            # tdt[i]=ts.time_ref+pd.to_timedelta(t, unit='ms')
            tdt[i] = pd.to_timedelta(t, unit="ms")
            i += 1

        for channel in range(nchannels):
            n_ave[str(channel)] = pd.Series(n_ave[str(channel)], index=tdt)
            t_ave[str(channel)] = pd.Series(t_ave[str(channel)], index=tdt)

        return pd.DataFrame(n_ave), pd.DataFrame(t_ave)


def main():
    """
    Convert
    """
    parser = optparse.OptionParser(usage="%prog [options] inputFileName")
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

    # tc = ThomsonChannels(input_file)
    # time_get = 4.06115405


if __name__ == "__main__":
    main()
