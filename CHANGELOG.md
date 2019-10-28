# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [2.1.0] - 2019-10-28
### Fixed
- get_repset_name:  Set repset variable to None if no database record is found.

### Changed
- get_repset_name:  Added .connect() call for the connection to the mongo_class.Coll class instance.
- get_repset_name:  Changed a number of arguments from positional to keyword arguments.
- delete_docs:  Changed a number of arguments from positional to keyword arguments.
- truncate_coll:  Changed a number of arguments from positional to keyword arguments.
- run_program:  Changed a number of arguments from positional to keyword arguments.


## [2.0.2] - 2019-10-03
### Fixed
- insert_doc:  Fixed problem with mutable default arguments issue.
- process_args:  Fixed problem with mutable default arguments issue.
- delete_docs:  Fixed problem with mutable default arguments issue.
- truncate_coll:  Fixed problem with mutable default arguments issue.
- run_program:  Fixed problem with mutable default arguments issue.

### Changed
- get_repset_name:  Changed variable to standard naming convention.
- insert_doc:  Removed commented out code.  Not yet implemented.
- insert_doc:  Changed variable to standard naming convention.
- process_args:  Changed variable name to be more descriptive of use.
- delete_docs:  Changed variable name to be more descriptive of use.
- delete_docs:  Changed variables to standard naming convention.
- truncate_coll:  Changed variables to standard naming convention.
- run_program:  Changed variable to standard naming convention.
- main:  Refactored "if" statements.
- Documentation updates.


## [2.0.1] - 2018-11-28
### Changed
- delete_docs:  Removed "gen_libs.rm_newline_list" call.


## [2.0.0] - 2018-04-26
Breaking Change

### Changed
- Changed "mongo_class" calls to new naming schema.
- Changed "mongo_libs" calls to new naming schema.
- Changed "cmds_gen" calls to new naming schema.
- Changed "gen_libs" calls to new naming schema.
- Changed "arg_parser" calls to new naming schema.
- Changed function names from uppercase to lowercase.
- Setup single-source version control.


## [1.2.0] - 2018-04-26
### Added
- Changed "svr_mongo" to "mongo_class" module reference.
- Changed "svr_mongo" to "mongo_class" module reference.
- Added single-source version control.


## [1.1.1] - 2017-08-23
### Fixed
- Error fix for -D option.  Not authenicating database when trying to login.
- Delete_Docs:  Add named argument 'db_auth' to class instance creation.


## [1.1.0] - 2017-08-16
### Changed
- Help_Message:  Replace docstring with printing the programs \_\_doc\_\_.
- Change single quotes to double quotes.
- Convert program to use local libraries from ./lib directory.


## [1.0.0] - 2016-12-06
- Initial creation.

