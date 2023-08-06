
Naming conventions
===================

`extract_` => extract (get) data from the database
`fetch_`   => fetch (get) data from external sources (like MDS+) to put into database or auxilary files
`plot_`    => plot data that has been extracted
`export_`  => export data into another format

General rules of thumb for developing
=======================================

`extract_` and `export_` files:
  o Classes to enable composition of workflow scripts more easily
  o No import of matplotlib or other plotting libraries to reduce dependencies
  o Extract methods should always take h5in as an optional parameter for performance reasons (opening and closing a file is time consuming)
  o Related:  Do not close h5 files -- allow workflow scripts to do it

`plot_` files:
  o Use methods but not classes:  want reuse but more flexible api

`fetch_` files:
  o Generally these are workflow scripts to not too much emphasis on form
