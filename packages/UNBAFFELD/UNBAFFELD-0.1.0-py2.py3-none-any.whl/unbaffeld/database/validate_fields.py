# Name of sets currently required in what is considered base files
base = ["required", "equilibria_required", "magnetics_required", "kinetics_required"]

# Additional files beyond base must still meet certain requirements
additional = ["diagnostics_required"]

small = ["required"]

# set of sets
allsets = ["base", "additional", "small"]
# TODO: for loop with uniquify
sumsets = base + additional

# ------------------------------------------------------------
# Dataset/group sets
# The required data is that used for the indexing of the metadata
# See export_pandas.py for the fields used
#
required = []
required += ["/dataset_description/data_entry/machine"]
required += [
    "/dataset_description/data_entry/pulse"
]  # TODO:  What to do about ITER or purely theoretical runs?
required += ["/equilibrium/time_slice/0/boundary"]
required += ["/equilibrium/time_slice/0/boundary/x_point/0/r"]
required += ["/equilibrium/time_slice/0/boundary/x_point/0/z"]
required += ["/equilibrium/time_slice/0/boundary/x_point/1/r"]
required += ["/equilibrium/time_slice/0/boundary/x_point/1/z"]
required += ["/equilibrium/time_slice/0/global_quantities"]
required += ["/equilibrium/time_slice/0/global_quantities/beta_normal"]
required += ["/equilibrium/time_slice/0/global_quantities/beta_normal"]
required += ["/equilibrium/time_slice/0/global_quantities/ip"]
required += ["/equilibrium/time_slice/0/global_quantities/li_3"]
required += ["/equilibrium/time_slice/0/global_quantities/magnetic_axis"]
required += ["/equilibrium/time_slice/0/global_quantities/psi_axis"]
required += ["/equilibrium/time_slice/0/global_quantities/psi_boundary"]
required += ["/equilibrium/time_slice/0/global_quantities/q_axis"]
required += ["/equilibrium/time_slice/0/global_quantities/q_95"]
required += ["/equilibrium/time_slice/0/global_quantities/q_min"]
required += ["/equilibrium/time_slice/0/profiles_1d"]
required += ["/equilibrium/time_slice/0/profiles_1d/elongation"]
required += ["/equilibrium/time_slice/0/profiles_1d/triangularity_upper"]
required += ["/equilibrium/time_slice/0/profiles_1d/triangularity_lower"]
required += ["/equilibrium/time_slice/0/profiles_1d/volume"]
required += ["/equilibrium/time_slice/0/profiles_1d/area"]
required += ["/equilibrium/time_slice/0/profiles_1d/surface"]

equilibria_required = []
equilibria_required += ["/equilibrium/code/parameters"]
equilibria_required += ["/equilibrium/time"]
equilibria_required += ["/equilibrium/time_slice"]
equilibria_required += ["/equilibrium/vacuum_toroidal_field"]

magnetics_required = []
magnetics_required += ["/equilibrium/time_slice/0/constraints/bpol_probe"]
magnetics_required += ["/equilibrium/time_slice/0/constraints/flux_loop"]
magnetics_required += ["/equilibrium/time_slice/0/constraints/ip"]
magnetics_required += ["/equilibrium/time_slice/0/constraints/diamagnetic_flux"]
magnetics_required += ["/equilibrium/time_slice/0/constraints/pf_current"]

kinetics_required = []
kinetics_required += ["/wall"]
kinetics_required += ["/core_profiles", "/core_sources", "edge_profiles"]

diagnostics_required = ["/charge_exchange", "/interferometer", "/thomson_scattering"]
