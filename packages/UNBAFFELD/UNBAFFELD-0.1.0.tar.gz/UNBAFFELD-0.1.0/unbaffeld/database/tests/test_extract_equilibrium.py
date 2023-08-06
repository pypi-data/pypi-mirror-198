import os
import sys

curdir = os.path.dirname(os.path.abspath(__file__))
pardir = os.path.abspath(os.path.join(curdir, ".."))
sys.path.append(pardir)

try:
    import extract_equilibrium
except ModuleNotFoundError:
    print("Can not import 'extract_equilibrium'. Path is:", end="\n")
    print(f"{sys.path}")
    raise


def test_extract_equilibria():
    """
    Fixtures are callables decorated with @fixture
    """
    curdir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.abspath(os.path.join(curdir, "..", "..", "data", "diii-d"))
    file_name = os.path.join(data_dir, "165908_pankin_165908_test.h5")

    print("Test the parse_eqargs method")
    parser = extract_equilibrium.parse_eqargs()
    options, args = parser.parse_args()
    assert options.verbose is None  # store_false gives None

    # File has two time slices - only load one
    options.time = "3.1"

    # Test the init
    eqs = extract_equilibrium.Equilibria(options)
    assert eqs.root_name == "equilibria"

    # Test the data read
    eqs.get_from_file(file_name)
    assert "3.1" in eqs.equilibria["DIII-D_165908"]  # Check time

    # Test the dump method
    eqs.dump("dump_165908.h5")
    assert os.path.exists("dump_165908.h5")

    # Test the restore  method
    eqrestore = extract_equilibrium.Equilibria(options)
    eqrestore.restore("dump_165908.h5")
    # assert '3.1' in eqrestore.equilibria['DIII-D_165908']  # Check time
