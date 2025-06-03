# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [5.0.0] - 2025-06-03
- Breaking changes
- Major refactoring of program to handle standalone or replica set Mongo databases.
- Updated to work with pymongo v4.X
- Updated mongo-lib to v4.5.3
- Updated python-lib to v4.0.1

### Fixed
- run_program: Create mongo_class.RepSetColl or mongo_class.Coll depending on settings in configuration file and removed mongo_class.RepSet creation.

### Changed
- insert_doc: Replaced mongo_class.RepSetColl with collection instance passed to function and determine if standalone or replica set is being used.
- delete_docs, truncate_coll: Replaced mongo_class.RepSetColl with collection instance passed to function.
- run_program: Removed check on auth_mech setting and removed calls to get_repset_name and get_repset_hosts.
- Documentation changes.

### Removed
- Removed get_repset_name function.
- Removed get_repset_hosts function.


## [4.0.1] - 2025-03-11
- Updated mongo-libs to v4.5.1

### Fixed
- Fixed pre-header where to determine which python version to use.


## [4.0.0] - 2025-02-28
Breaking changes.

- Add pre-header check on allowable Python versions to run.
- Added pymongo==4.10.1 for Python 3.9 and Python 3.12.
- Added dnspython==2.7.0 for Python 3.9 and Python 3.12.
- Removed support for Python 2.7.
- Updated python-lib v4.0.0
- Updated mongo-lib v4.5.0

### Added
- Support for Mongo 7.0

### Changed
- process_args: Replaced dict() with {}.
- Converted strings to f-strings.
- Documentation changes.

### Removed
- Support for Mongo 3.4


## [3.1.4] - 2024-11-21
- Updated distro==1.9.0 for Python 3
- Updated psutil==5.9.4 for Python 3
- Updated pymongo==4.1.1 for Python 3
- Updated simplejson==3.13.2 for Python 3
- Updated python-lib to v3.0.8
- Updated mongo-lib to v4.3.4

### Deprecated
- Support for Python 2.7


## [3.1.3] - 2024-09-10
- Minor changes.


## [3.1.2] - 2024-04-22
- Updated mongo-lib to v4.3.0
- Added TLS capability
- Set pymongo to 3.12.3 for Python 2 and Python 3.

### Changed
- get_repset_name, delete_docs, truncate_coll, run_program: Added TLS parameters to the database instance calls.
- Set pymongo to 3.12.3 for Python 2 and Python 3.
- config/mongo.py.TEMPLATE: Added TLS entries.
- Documentation updates.


## [3.1.1] - 2024-02-29
- Updated to work in Red Hat 8
- Updated mongo-lib to v4.2.9
- Updated python-lib to v3.0.3

### Changed
- Set simplejson to 3.12.0 for Python 3.
- Set chardet to 3.0.4 for Python 2.
- Documentation updates.


## [3.1.0] - 2023-10-30
- Upgraded python-lib to v2.10.1
- Upgraded mongo-lib to 4.2.7
- Replaced the arg_parser code with gen_class.ArgParser code.

### Fixed
- run_program, delete_docs, truncate_coll: Changed the default value of auth_db to the configuration file auth_db entry.
- process_args: Fixed logic error where key did not have a value assigned to it.

### Changed
- config/mongo.py.TEMPLATE: Added SSL entries.
- Multiple functions: Replaced the arg_parser code with gen_class.ArgParser code.
- Multiple functions: Added SSL entries to the mongo_class instance calls.
- run_program: Removed code to determine if auth_mech was available.
- main, insert_doc: Removed gen_libs.get_inst call.
- Documentation changes.


## [3.0.2] - 2022-12-01
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4
- Upgraded mongo-lib to v4.2.2
 
### Changed
- Converted imports to use Python 2.7 or Python 3.


## [3.0.1] - 2022-06-28
- Upgrade mongo-libs to v4.2.1
- Upgrade python-lib to v2.9.2

### Changed
- config/mongo.py.TEMPLATE: Removed old entries.
- Documentation updates.


## [3.0.0] - 2021-09-15
Breaking Change

### Fixed
- truncate_coll, delete_docs:  Changed keyword argument from db_auth to auth_db.
- main:  Fixed handling command line arguments.

### Changed
- insert_docs:  Replaced cmds_gen.add_cmd with gen_libs.add_cmd.
- run_program:  Added auth_db keyword argument to mongo_class.RepSet instance call.
- truncate_coll, delete_docs:  Changed default authentication database from none to -b option value.
- run_program, delete_docs, truncate_coll, get_repset_name:  Added check on connection status.
- insert_doc:  Replaced cmds_gen.run_prog with the subprocess execution code.
- truncate_coll, delete_docs:  Added auth_mech to mongo_class instance call.
- get_repset_name, run_program:  Processed and added auth_mech to the mongo_class instance call.
- Removed unneccessary \*\*kwargs from arguments lists.
- truncate_coll, delete_docs, get_repset_name:  Replaced cmds_gen.disconnect call with mongo_libs.disconnect.
- run_program, truncate_coll, delete_docs, get_repset_name:  Update configuration entries to match new config file and addeduse_arg and use_uri to mongo_class instance call.
- config/mongo.py.TEMPLATE:  Added SSL entries and auth_db entry.
- Documentation updates.

### Removed
- cmds_gen module


## [2.1.0] - 2019-10-28
### Fixed
- get_repset_name:  Set repset variable to None if no database record is found.

### Changed
- get_repset_name:  Added .connect() call for the connection to the mongo_class.Coll class instance.
- get_repset_name, delete_docs, truncate_coll, run_program:  Changed a number of arguments from positional to keyword arguments.


## [2.0.2] - 2019-10-03
### Fixed
- insert_doc, process_args, delete_docs, truncate_coll, run_program:  Fixed problem with mutable default arguments issue.

### Changed
- get_repset_name, insert_doc, delete_docs, truncate_coll, run_program:  Changed variable to standard naming convention.
- insert_doc:  Removed commented out code.  Not yet implemented.
- process_args, delete_docs:  Changed variable name to be more descriptive of use.
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
- Added single-source version control.


## [1.1.1] - 2017-08-23
### Fixed
- Error fix for -D option.  Not authenicating database when trying to login.
- Delete_Docs:  Add named argument 'db_auth' to class instance creation.


## [1.1.0] - 2017-08-16
### Changed
- Help\_Message:  Replace docstring with printing the programs \_\_doc\_\_.
- Change single quotes to double quotes.
- Convert program to use local libraries from ./lib directory.


## [1.0.0] - 2016-12-06
- Initial creation.

