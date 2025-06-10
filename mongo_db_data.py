#!/bin/sh
# Classification (U)

# Shell commands follow
# Next line is bilingual: it starts a comment in Python & is a no-op in shell
""":"

# Find a suitable python interpreter (can adapt for specific needs)
# NOTE: Ignore this section if passing the -h option to the program.
#   This code must be included in the program's initial docstring.
for cmd in python3.12 python3.9 ; do
   command -v > /dev/null $cmd && exec $cmd $0 "$@"
done

echo "OMG Python not found, exiting...."

exit 2

# Previous line is bilingual: it ends a comment in Python & is a no-op in shell
# Shell commands end here

   Program:  mongo_db_data.py

    Description:  Program to either take a external JSON document and insert
        into a Mongo database, delete a document from a Mongo database
        collection based on passed key(s) and value(s), or truncate a
        collection within a Mongo database.

    Usage:
        mongo_db_data.py -c cfg_file -d path
            {-I -b db_name -t coll_name -f {path/file | path/file*} [-a name]
                [-m path] [-r] |
            {-K -b db_name -t coll_name -f {path/file | path/file*} [-a name]
                [-m path] [-r] |
             -D -b db_name -t coll_name
                {-k1 "key" -l1 "value1" ["value2" "value3" ...]
                 [-k[2-5] "key" -l[2-5] "value1" ["value2" "value3" ...]] |
                 [-f {path/file | path/file*}] [-a name]} |
             -T -b db_name -t coll_name [-a name]}
            [-p path]
            [-v | -h]

    Arguments:
        -c cfg_file => Mongo configuration file.
        -d dir path => Config directory path.

        -I => Import JSON document into database.
            -b db_name => Database Name.
            -t coll_name => Collection Name.
            -f file(s) => JSON document to be imported.  Requires absolute
                path.
            -a name => Authentication Database Name.  Required for accounts
                not in database (-b option).
            -m path => Archive the file(s) to the directory.
            -r => Remove the files once the insertion is completed.

        -K => Insert JSON document entries into database.
            -b db_name => Database Name.
            -t coll_name => Collection Name.
            -f file(s) => JSON document to be inserted.  Requires absolute
                path.
            -a name => Authentication Database Name.  Required for accounts
                not in database (-b option).
            -m path => Archive the file(s) to the directory.
            -r => Remove the files once the insertion is completed.

        -D => Delete JSON document from database.
            -b db_name => Database Name.
            -t coll_name => Collection Name.
            -k[1-5] key => Name of key in document to delete on.
            -l[1-5] value(s) => One or more values for associated key.
                Values are enclosed in quotes (") and space-delimited ( ).
            -f file(s) => JSON Document for delete search criteria.  Requires
                 absolute path.
            -a name => Authentication Database Name.  Required for accounts
                not in database (-b option).

        -T => Truncate collection in database.
            -b db_name => Database Name.
            -t coll_name => Collection Name.
            -a name => Authentication Database Name.  Required for accounts
                not in database (-b option).

        -p => Path to Mongo binaries.  Only required if the user
            running the program does not have the Mongo binaries in their path.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v and/or -h overrides all other options.
        NOTE 2:  -I, -K, -T and -D are XOR options.
        NOTE 3:  -k1 and -l1 are required to be paried for -D option.
            -k[2-5] and -l[2-5] are optional, but are required to be paired.
        NOTE 4:  The difference between -I and -K options are: -I uses the
            mongoimport command to insert in bulk all entries into a
            collection, whereas the -K option uses the insert command to insert
            one entry at a time into the collection.

    Notes:
        Mongo configuration file format (config/mongo.py.TEMPLATE).  The
            configuration file format is for connecting to a Mongo database or
            replica set for monitoring.  A second configuration file can also
            be used to connect to a Mongo database or replica set to insert the
            results of the performance monitoring into.

            There are two ways to connect methods:  single Mongo database or a
            Mongo replica set.

            Single database connection:

            # Single Configuration file for Mongo Database Server.
            user = "USER"
            japd = "PSWORD"
            host = "IP_ADDRESS"
            name = "HOSTNAME"
            port = 27017
            conf_file = None
            auth = True
            auth_db = "admin"
            auth_mech = "SCRAM-SHA-1"

            Replica Set connection:  Same format as above, but with these
                additional entries at the end of the configuration file.  By
                default all these entries are set to None to represent not
                connecting to a replica set.

            repset = "REPLICA_SET_NAME"
            repset_hosts = "HOST1:PORT, HOST2:PORT, HOST3:PORT, [...]"
            db_auth = "AUTHENTICATION_DATABASE"

            If Mongo is set to use TLS or SSL connections, then one or more of
                the following entries will need to be completed to connect
                using TLS or SSL protocols.
                Note:  Read the configuration file to determine which entries
                    will need to be set.

                SSL:
                    auth_type = None
                    ssl_client_ca = None
                    ssl_client_key = None
                    ssl_client_cert = None
                    ssl_client_phrase = None
                TLS:
                    auth_type = None
                    tls_ca_certs = None
                    tls_certkey = None
                    tls_certkey_phrase = None

            Note:  Secure Environment for Mongo.
              If operating in a secure environment, this package will
              require at least a minimum of pymongo==3.8.0 or better.  It will
              also require a manual change to the auth.py module in the pymongo
              package.  See below for changes to auth.py.

            - Locate the auth.py file python installed packages on the system
                in the pymongo package directory.
            - Edit the file and locate the "_password_digest" function.
            - In the "_password_digest" function there is an line that should
                match: "md5hash = hashlib.md5()".  Change it to
                "md5hash = hashlib.md5(usedforsecurity=False)".
            - Lastly, it will require the Mongo configuration file entry
                auth_mech to be set to: SCRAM-SHA-1 or SCRAM-SHA-256.

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Example:
        mongo_db_data.py -c mongo -d config -b GMI -t FAC -f ins_doc -I

":"""
# Python program follows


# Libraries and Global Variables

# Standard
import sys
import os
import subprocess
import json

# Local
try:
    from .lib import gen_libs
    from .lib import gen_class
    from .mongo_lib import mongo_libs
    from .mongo_lib import mongo_class
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs                     # pylint:disable=R0402
    import lib.gen_class as gen_class                   # pylint:disable=R0402
    import mongo_lib.mongo_libs as mongo_libs           # pylint:disable=R0402
    import mongo_lib.mongo_class as mongo_class         # pylint:disable=R0402
    import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def is_file_deletable(fname):

    """Function:  is_file_deletable

    Description:  Determine if a file can be removed.

    Arguments:
        (input) fname -> Filename and full path
        (output) status -> True|False - File can be removed

    """

    status = False
    f_dirname = os.path.dirname(fname)

    # Ensure object is a file and writable and the directory has correct perms
    if os.path.isfile(fname):
        if os.access(fname, os.W_OK):
            if os.access(f_dirname, os.W_OK | os.X_OK):
                status = True

    return status


def post_process(args):

    """Function:  post_process

    Description:  Post processing of files.

    Arguments:
        (input) args -> ArgParser class instance

    """

    if args.arg_exist("-m"):

        for fname in args.get_val("-f"):

            # Check if file is removable and archive directory writable
            if args.arg_dir_chk(dir_perms_chk={"-m": 7}) \
               and is_file_deletable(fname):
                gen_libs.mv_file2(fname, args.get_val("-m"))

            else:
                print("post_process: Incorrect perms for file or directory")
                print(f'\tDirectory: {args.get_val("-m")}')
                print(f"\tFile: {fname}")
                

    elif args.arg_exist("-r"):
        for fname in args.get_val("-f"):
            status = gen_libs.rm_file(fname)

            if not status[0]:
                print("post_process: Error encountered during file removal")
                print(f"Error Message: {status[1]}")


def insert_doc2(coll, args, **kwargs):

    """Function:  insert_doc2

    Description:  Insert of document(s) into a Mongo database.  Have the
        ability to insert multiple external JSON document files into the
        database.

    Arguments:
        (input) coll -> Mongo collection instance
        (input) args -> ArgParser class instance
        (input) kwargs:
            cfg -> Configuration setup
            opt_arg -> Contains list of optional arguments for command line
            opt_rep -> Contains list of replaceable arguments for command line

    """

    for fname in args.get_val("-f"):
        with open(fname, mode="r", encoding="UTF-8") as fhdr:

            for data in fhdr:
                status = mongo_libs.ins_doc(
                    kwargs.get("cfg"), args.get_val("-b"), args.get_val("-t"),
                    json.loads(data))

                if not status[0]:
                    print("insert_doc2: Insertion into Mongo failed.")
                    print(f"Mongo error message:  {status[1]}")
                    print(f"Data: {data}")

    if args.arg_exist("-m") or args.arg_exist("-r"):
        post_process(args)


def insert_doc(coll, args, **kwargs):

    """Function:  insert_doc

    Description:  Import of document(s) into a Mongo database.  Have the
        ability to import multiple external JSON document files into the
        database.

    Arguments:
        (input) coll -> Mongo collection instance
        (input) args -> ArgParser class instance
        (input) kwargs:
            cfg -> Configuration setup
            opt_arg -> Contains list of optional arguments for command line
            opt_rep -> Contains list of replaceable arguments for command line

    """

    use_repset=False

    if isinstance(coll, mongo_class.RepSetColl):
        use_repset=True

    if args.arg_exist("-f"):
        cmd = mongo_libs.create_cmd(
            coll, args, "mongoimport", "-p", use_repset=use_repset, **kwargs)
        orig_cmd = list(cmd)

        # Process files and add --file option
        for fname in args.get_val("-f"):
            upd_cmd = gen_libs.add_cmd(
                cmd, arg=kwargs.get("opt_rep")["-f"], val=fname)
            proc1 = subprocess.Popen(upd_cmd)           # pylint:disable=R1732
            proc1.wait()
            cmd = list(orig_cmd)

    if args.arg_exist("-m") or args.arg_exist("-r"):
        post_process(args)


def process_args(args):

    """Function:  process_args

    Description:  Will process each of the -kN and -lN pairs and parse them
        into search criteria string.

    Arguments:
        (input) args -> ArgParser class instance
        (output) status -> True|False - If an error has occurred
        (output) qry -> Mongo search query criteria

    """

    status = False
    qry = {}

    # Process key|value pairs
    for item in range(1, 6):
        key = "-k" + str(item)
        val = "-l" + str(item)
        sub_qry = {}

        # Only create if have key and value associated
        if args.arg_exist(key) and args.arg_exist(val):
            sub_qry["$in"] = args.get_val(val)
            qry[args.get_val(key)] = sub_qry
            status = False

        # Missing key, but have value
        elif not args.arg_exist(key) and args.arg_exist(val):
            print(f"WARNING: Missing key for value: {val} ="
                  f" {args.get_val(val)}")
            status = True

        # Have key, but missing value
        elif args.arg_exist(key) and not args.arg_exist(val):
            print(f"WARNING: Missing value for key: {val} ="
                  f" {args.get_val(val)}")
            status = True

    return status, qry


def delete_docs(coll, args, **kwargs):                # pylint:disable=W0613

    """Function:  delete_docs

    Description:  Deletion of a document in a Mongo database.  Allows for one
        or more key|value(s) pairs to be used as the search criteria for
        the deletion command.  For each key, must have a corresponding
        set of value(s).

    Arguments:
        (input) coll -> Mongo collection instance
        (input) args -> ArgParser class instance
        (input) kwargs:
            cfg -> Configuration setup
            opt_arg -> Contains list of optional arguments for command line
            opt_rep -> Contains list of replaceable arguments for command line

    """

    if args.arg_exist("-f"):

        for fname in args.get_val("-f"):
            lines = gen_libs.file_2_list(fname)

            # Process each line as a delete
            for qry in lines:
                coll.coll_del_many(gen_libs.str_2_type(qry))

    # Assume -kN and -lN options
    else:
        status, qry = process_args(args)

        if not status:
            coll.coll_del_many(qry)


def truncate_coll(coll, args, **kwargs):

    """Function:  truncate_coll

    Description:  Truncate a collection in a Mongo database.

    Arguments:
        (input) coll -> Mongo collection instance
        (input) args -> ArgParser class instance
        (input) kwargs:
            cfg -> Configuration setup
            opt_arg -> Contains list of optional arguments for command line
            opt_rep -> Contains list of replaceable arguments for command line

    """

    coll.coll_del_many({}, True)


def run_program(args, func_dict, **kwargs):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args -> ArgParser class instance
        (input) func_dict -> Dictionary list of functions and options
        (input) kwargs:
            opt_arg -> Contains list of optional arguments for command line
            opt_rep -> Contains list of replaceable arguments for command line

    """

    func_dict = dict(func_dict)
    cfg = gen_libs.load_module(args.get_val("-c"), args.get_val("-d"))

    if cfg.repset:
        coll = mongo_libs.create_instance(
            args.get_val("-c"), args.get_val("-d"), mongo_class.RepSetColl)
        coll.db_name = args.get_val("-b")
        coll.coll = args.get_val("-t")

    else:
        coll = mongo_libs.create_instance(
            args.get_val("-c"), args.get_val("-d"), mongo_class.Coll)
        coll.coll_db = args.get_val("-b")
        coll.coll_coll = args.get_val("-t")

    status = coll.connect()

    if status[0]:
        # Intersect args_array & func_dict to determine which functions to call
        for func in set(args.get_args_keys()) & set(func_dict.keys()):
            func_dict[func](coll, args, cfg=cfg, **kwargs)

        mongo_libs.disconnect([coll])

    else:
        print(f"run_program: Connection failure:  {status[1]}")


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_perms_chk -> contains directories and their octal permissions
        file_perm_chk -> file check options with their perms in octal
        func_dict -> dictionary list for the function calls or other options
        opt_arg_list-> contains list of optional arguments for command line
        opt_arg_rep -> contains list of replaceable arguments for command line
        opt_con_req_list -> contains the options that require other options
        opt_multi_list -> contains the options that will have multiple values
        opt_req_list -> contains the options that are required for the program
        opt_val_list -> contains options which require values
        opt_xor_dict -> contains options which are XOR with its values
        xor_noreq_list -> contains options that are XOR, but are not required

    Arguments:
        (input) argv -> Arguments from the command line

    """

    dir_perms_chk = {"-d": 5, "-p": 5}
    file_perm_chk = {"-f": 6}
    func_dict = {
        "-I": insert_doc, "-D": delete_docs, "-T": truncate_coll,
        "-K": insert_doc2}
    opt_arg_list = {
        "-a": "--authenticationDatabase=", "-b": "--db=",
        "-t": "--collection="}
    opt_arg_rep = {"-f": "--file="}
    opt_con_req_list = {
        "-k1": ["-l1"], "-k2": ["-l2"], "-k3": ["-l3"], "-k4": ["-l4"],
        "-k5": ["-l5"], "-I": ["-b", "-t", "-f"], "-K": ["-b", "-t", "-f"],
        "-D": ["-b", "-t"], "-T": ["-b", "-t"]}
    opt_multi_list = ["-f", "-l1", "-l2", "-l3", "-l4", "-l5"]
    opt_req_list = ["-b", "-c", "-d", "-t"]
    opt_val_list = [
        "-a", "-b", "-c", "-d", "-f", "-k1", "-l1", "-p", "-t", "-k2", "-l2",
        "-k3", "-l3", "-k4", "-l4", "-k5", "-l5", "-m"]
    opt_xor_dict = {
        "-D": ["-I", "-T", "-K"], "-I": ["-D", "-T", "-K"],
        "-T": ["-D", "-I", "-K"], "-K": ["-D", "-T", "-I"]}
    xor_noreq_list = {"-k1": "-f"}

    # Process argument list from command line
    args = gen_class.ArgParser(
        sys.argv, opt_val=opt_val_list, multi_val=opt_multi_list)

    if args.arg_parse2()                                            \
       and not gen_libs.help_func(args, __version__, help_message)  \
       and args.arg_require(opt_req=opt_req_list)                   \
       and args.arg_dir_chk(dir_perms_chk=dir_perms_chk)            \
       and args.arg_xor_dict(opt_xor_val=opt_xor_dict)              \
       and args.arg_cond_req(opt_con_req=opt_con_req_list)          \
       and args.arg_noreq_xor(xor_noreq=xor_noreq_list)             \
       and args.arg_file_chk(file_perm_chk=file_perm_chk):
        run_program(
            args, func_dict, opt_arg=opt_arg_list, opt_rep=opt_arg_rep)


if __name__ == "__main__":
    sys.exit(main())
