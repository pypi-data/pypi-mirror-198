

EFIT-AI Database utilities quickstart
======================================

validating file
~~~~~~~~~~~~~~~~~~~~~~

Many OMAS files do not have all of the data needed for various EFIT-AI
workflows.  To help understand what files conform to various standards, we have
`validator.py`.

Show the usage and options::

    validator.py -h

Validate all of the h5 files in `data/diii-d` directory::

    validator.py ../data/diii-d/*.h5

To validate on smaller set of validation parameters (see `validate_fields.py`)::

    validator.py -r small ../data/diii-d/*.h5

fixing an unvalidated file
~~~~~~~~~~~~~~~~~~~~~~~~~~

For simple fixes, `fix_dbfile.py` is available.  Bigger fixes typically involve
a type of fetch to get the additional data and then adding it.  Here, we show
the most common fix:  adding the machine data::

    fix_dbfile.py -r 'machine,DIII-D' ../data/diii-d/omas_182086.h5




extracting equilibrium
~~~~~~~~~~~~~~~~~~~~~~

From the source directory (can translate as needed from installs).

Show the usage and options::

    extract_equilibrium.py -h

Show the time slices and times that are listed in a file::

    extract_equilibrium.py --list ../data/diii-d/165908_pankin_165908_test.h5


Extract the first time slice from the file::

    extract_equilibrium.py -s 0 ../data/diii-d/165908_pankin_165908_test.h5

This doesn't actually do anything -- the data is loaded into memory and then
nothing is put into the file.  Let's cache that data and show what's going on
while we are running (verbose setting)::

    extract_equilibrium.py -v -s 0 -o eqs.h5 ../data/diii-d/165908_pankin_165908_test.h5

Let's see how the caching stores the data::

     ➜ h5lr eqs.h5  | head -5
     /                                              Group
     /DIII-D_165908                                 Group
     /DIII-D_165908/3.1                             Group
     /DIII-D_165908/3.1/eq2000380601                Group
     /DIII-D_165908/3.1/eq2000380601/boundary       Group


The `3.1` here refers the time of 3.1 seconds of shot `165908` on the `DIII-D`
experimental machine.  The `eq2000380601` is a label for that specific
equilibrium because any given time slice can have multiple equilibria (magnetic
EFIT, kinetic EFIT, ...).

plotting equilibrium
~~~~~~~~~~~~~~~~~~~~~~

Let's plot the equilibria in a file (this uses the extraction code above)::

   plot_equilibrium.py ../data/diii-d/165908_pankin_165908_test.h5

That should have two figures because that file has two equilibria.   Let's plot
just the first one.  This uses the same options as above::

   plot_equilibrium.py -s 0 -v ../data/diii-d/165908_pankin_165908_test.h5

To show the 1D profiles::

   plot_equilibrium.py -s 0 -v --1d ../data/diii-d/165908_pankin_165908_test.h5


