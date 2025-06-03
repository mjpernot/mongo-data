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
            {-I -b db_name -t coll_name -a name -f {path/file | path/file*} |
             -D -b db_name -t coll_name
                {-k1 "key" -l1 "value1" ["value2" "value3" ...]
                 [-k[2-5] "key" -l[2-5] "value1" ["value2" "value3" ...]] |
                 [-f {path/file | path/file*}] [-a name]} |
             -T -b db_name -t coll_name [-a name]}
             [-p path}
            [-v | -h]

    Arguments:
        -c cfg_file => Mongo configuration file.  Required arg.
        -d dir path => Config directory path.  Required arg.

        -I => Insert JSON document into database.
            -b db_name => Database Name.
            -t coll_name => Collection Name.
            -f file(s) => JSON document to be inserted.  Requires absolute
                path.
            -a name => Authentication Database Name.  Required for accounts
                not in database (-b option).

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
        NOTE 2:  -I and -D are XOR options.
        NOTE 3:  -k1 and -l1 are required to be paried for -D option.
            -k[2-5] and -l[2-5] are optional, but are required to be paired.

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
import subprocess

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


#def get_repset_name(svr_cfg):

#    """Function:  get_repset_name

#    Description:  Fetch the Replication Set Name from the condfiguration file
#        or from the Mongo database.

#    Arguments:
#        (input) svr_cfg -> Server configuration module
#        (output) rep_set -> Replication set name

#    """

    # Only pass authorization mechanism if present.
#    auth_mech = {"auth_mech": svr_cfg.auth_mech} if hasattr(
#        svr_cfg, "auth_mech") else {}

#    try:
#        rep_set = svr_cfg.repset

#    except AttributeError:
#        coll = mongo_class.Coll(
#            svr_cfg.name, svr_cfg.user, svr_cfg.japd, host=svr_cfg.host,
#            port=svr_cfg.port, db="local", coll="system.replset",
#            auth=svr_cfg.auth, conf_file=svr_cfg.conf_file,
#            ssl_client_ca=svr_cfg.ssl_client_ca,
#            ssl_client_cert=svr_cfg.ssl_client_cert,
#            ssl_client_key=svr_cfg.ssl_client_key,
#            ssl_client_phrase=svr_cfg.ssl_client_phrase,
#            auth_type=svr_cfg.auth_type, tls_ca_certs=svr_cfg.tls_ca_certs,
#            tls_certkey=svr_cfg.tls_certkey,
#            tls_certkey_phrase=svr_cfg.tls_certkey_phrase, **auth_mech)
#        status = coll.connect()
#        rep_set = None

#        if status[0]:
#            if coll.coll_cnt() != 0:
#                rep_set = coll.coll_find1().get("_id")

#            mongo_libs.disconnect([coll])

#        else:
#            print(f"get_repset_name: Connection failure:  {status[1]}")

#    return rep_set


#def get_repset_hosts(svr_cfg):

#    """Function:  get_repset_hosts

#    Description:  See if the Rep Set hosts is in the config file, otherwise set
#        to None.

#    Arguments:
#        (input) svr_cfg -> Server Configuration module
#        (output) repset_hosts -> Contain string of rep set hosts

#    """

#    try:
#        repset_hosts = svr_cfg.repset_hosts

#    except AttributeError:
#        repset_hosts = None

#    return repset_hosts


def insert_doc(coll, args, **kwargs):

    """Function:  insert_doc

    Description:  Insertion of document(s) into a Mongo database.  The document
        can either be an external JSON document(s) or created internally
        and then inserted into the database.  Have the ability to
        insert multiple external JSON document files into the database.

    Arguments:
        (input) coll -> Mongo collection instance
        (input) args -> ArgParser class instance
        (input) kwargs:
            opt_arg -> Contains list of optional arguments for command line
            opt_rep -> Contains list of replaceable arguments for command line

    """

    use_repset=False

    if isinstance(coll, mongo_class.RepSetColl):
        use_repset=True

    if args.arg_exist("-f"):
        cmd = mongo_libs.create_cmd(
            coll, args, "mongoimport", "-p", use_repset=use_repset, **kwargs)
#        cmd = mongo_libs.create_cmd(
#            repclu, args, "mongoimport", "-p", use_repset=True, **kwargs)
        orig_cmd = list(cmd)

        # Process files and add --file option
        for fname in args.get_val("-f"):
            upd_cmd = gen_libs.add_cmd(
                cmd, arg=kwargs.get("opt_rep")["-f"], val=fname)
            proc1 = subprocess.Popen(upd_cmd)           # pylint:disable=R1732
            proc1.wait()
            cmd = list(orig_cmd)


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
            opt_arg -> Contains list of optional arguments for command line
            opt_rep -> Contains list of replaceable arguments for command line

    """

#    coll = mongo_class.RepSetColl(
#        repclu.name, repclu.user, repclu.japd, host=repclu.host,
#        port=repclu.port, auth=repclu.auth, repset=repclu.repset,
#        repset_hosts=repclu.repset_hosts, db=args.get_val("-b"),
#        auth_db=args.get_val("-a", def_val=repclu.auth_db),
#        coll=args.get_val("-t"), auth_mech=repclu.auth_mech,
#        ssl_client_ca=repclu.ssl_client_ca,
#        ssl_client_cert=repclu.ssl_client_cert,
#        ssl_client_key=repclu.ssl_client_key,
#        ssl_client_phrase=repclu.ssl_client_phrase,
#        auth_type=repclu.auth_type, tls_ca_certs=repclu.tls_ca_certs,
#        tls_certkey=repclu.tls_certkey,
#        tls_certkey_phrase=repclu.tls_certkey_phrase)
#    status = coll.connect()

#    if status[0]:
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

#        mongo_libs.disconnect([coll])

#    else:
#        print(f"delete_docs: Connection failure:  {status[1]}")


def truncate_coll(coll, args, **kwargs):

    """Function:  truncate_coll

    Description:  Truncate a collection in a Mongo database.

    Arguments:
        (input) coll -> Mongo collection instance
        (input) args -> ArgParser class instance
        (input) kwargs:
            opt_arg -> Contains list of optional arguments for command line
            opt_rep -> Contains list of replaceable arguments for command line

    """

    coll.coll_del_many({}, True)

#    coll = mongo_class.RepSetColl(
#        repclu.name, repclu.user, repclu.japd, host=repclu.host,
#        port=repclu.port, auth=repclu.auth, repset=repclu.repset,
#        repset_hosts=repclu.repset_hosts, db=args.get_val("-b"),
#        coll=args.get_val("-t"), auth_mech=repclu.auth_mech,
#        auth_db=args.get_val("-a", def_val=repclu.auth_db),
#        ssl_client_ca=repclu.ssl_client_ca,
#        ssl_client_cert=repclu.ssl_client_cert,
#        ssl_client_key=repclu.ssl_client_key,
#        ssl_client_phrase=repclu.ssl_client_phrase,
#        auth_type=repclu.auth_type, tls_ca_certs=repclu.tls_ca_certs,
#        tls_certkey=repclu.tls_certkey,
#        tls_certkey_phrase=repclu.tls_certkey_phrase)
#    status = coll.connect()

#    if status[0]:
#        # Require override option
#        coll.coll_del_many({}, True)
#        mongo_libs.disconnect([coll])

#    else:
#        print(f"truncate_coll: Connection failure:  {status[1]}")


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

#    svr_cfg = gen_libs.load_module(args.get_val("-c"), args.get_val("-d"))
#    rep_set = get_repset_name(svr_cfg)
#    repset_hosts = get_repset_hosts(svr_cfg)

    # Only pass authorization mechanism if present
#    auth_mech = {"auth_mech": svr_cfg.auth_mech} if hasattr(
#        svr_cfg, "auth_mech") else {}

#    repclu = mongo_class.RepSet(
#        svr_cfg.name, svr_cfg.user, svr_cfg.japd, host=svr_cfg.host,
#        port=svr_cfg.port, auth=svr_cfg.auth, repset=rep_set,
#        repset_hosts=repset_hosts,
#        auth_db=args.get_val("-a", def_val=svr_cfg.auth_db),
#        ssl_client_ca=svr_cfg.ssl_client_ca,
#        ssl_client_cert=svr_cfg.ssl_client_cert,
#        ssl_client_key=svr_cfg.ssl_client_key,
#        ssl_client_phrase=svr_cfg.ssl_client_phrase,
#        auth_type=svr_cfg.auth_type, tls_ca_certs=svr_cfg.tls_ca_certs,
#        tls_certkey=svr_cfg.tls_certkey,
#        tls_certkey_phrase=svr_cfg.tls_certkey_phrase, **auth_mech)
#    status = repclu.connect()

    if status[0]:
        # Intersect args_array & func_dict to determine which functions to call
        for func in set(args.get_args_keys()) & set(func_dict.keys()):
            func_dict[func](coll, args, **kwargs)
#            func_dict[func](repclu, args, **kwargs)

        mongo_libs.disconnect([coll])
#        mongo_libs.disconnect([repclu])

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
    func_dict = {"-I": insert_doc, "-D": delete_docs, "-T": truncate_coll}
    opt_arg_list = {
        "-a": "--authenticationDatabase=", "-b": "--db=",
        "-t": "--collection="}
    opt_arg_rep = {"-f": "--file="}
    opt_con_req_list = {"-k1": ["-l1"]}
    opt_multi_list = ["-f", "-l1", "-l2", "-l3", "-l4", "-l5"]
    opt_req_list = ["-b", "-c", "-d", "-t"]
    opt_val_list = [
        "-a", "-b", "-c", "-d", "-f", "-k1", "-l1", "-p", "-t", "-k2", "-l2",
        "-k3", "-l3", "-k4", "-l4", "-k5", "-l5"]
    opt_xor_dict = {"-D": ["-I", "-T"], "-I": ["-D", "-T"], "-T": ["-D", "-I"]}
    xor_noreq_list = {"-k1": "-f"}

    # Process argument list from command line
    args = gen_class.ArgParser(
        sys.argv, opt_val=opt_val_list, multi_val=opt_multi_list,
        do_parse=True)

    # Remove dupe files
    if args.arg_exist("-f"):
        args.update_arg("-f", gen_libs.rm_dup_list(args.get_val("-f")))

    if not gen_libs.help_func(args, __version__, help_message)  \
       and args.arg_require(opt_req=opt_req_list)               \
       and args.arg_dir_chk(dir_perms_chk=dir_perms_chk)        \
       and args.arg_xor_dict(opt_xor_val=opt_xor_dict)          \
       and args.arg_cond_req(opt_con_req=opt_con_req_list)      \
       and args.arg_noreq_xor(xor_noreq=xor_noreq_list)         \
       and args.arg_file_chk(file_perm_chk=file_perm_chk):
        run_program(
            args, func_dict, opt_arg=opt_arg_list, opt_rep=opt_arg_rep)


if __name__ == "__main__":
    sys.exit(main())
