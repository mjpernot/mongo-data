# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in mongo_db_data.py.

    Usage:
        test/unit/mongo_db_data/run_program.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_db_data                            # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


def insert_doc(repset, args_array):

    """Function:  insert_doc

    Description:  Stub holder for mongo_db_data.insert_doc function.

    Arguments:
        (input) repset -> Replication set instance.
        (input) args_array -> Array of command line options and values.

    """

    status = True

    if repset and args_array:
        status = True

    return status


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val
        get_args_keys

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "mysql_cfg", "-d": "config"}

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)

    def get_args_keys(self):

        """Method:  get_args_keys

        Description:  Method stub holder for gen_class.ArgParser.get_args_keys.

        Arguments:

        """

        return list(self.args_array.keys())


class RepSetColl():                                     # pylint:disable=R0903

    """Class:  RepSetColl

    Description:  Class stub holder for mongo_class.RepSetColl class.

    Methods:
        __init__
        connect

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.status = True
        self.err_msg = None
        self.db_name = None
        self.coll = None

    def connect(self):

        """Method:  connect

        Description:  Stub method holder for mongo_class.Server.connect.

        Arguments:

        """

        return self.status, self.err_msg


class Coll():                                            # pylint:disable=R0903

    """Class:  Coll

    Description:  Class stub holder for mongo_class.Coll class.

    Methods:
        __init__
        connect

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.status = True
        self.err_msg = None
        self.coll_db = None
        self.coll_coll = None

    def connect(self):

        """Method:  connect

        Description:  Stub method holder for mongo_class.Server.connect.

        Arguments:

        """

        return self.status, self.err_msg


class Cfg():                                            # pylint:disable=R0903

    """Class:  Cfg

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the Cfg class.

        Arguments:

        """

        self.name = "MongoName"
        self.user = "root"
        self.japd = None
        self.host = "HostName"
        self.port = 27017
        self.auth = True
        self.conf_file = "ConFile"
        self.repset = "RepSetName"
        self.repset_hosts = "localhost:27017,localhost:27016"
        self.auth_db = "admin"
        self.ssl_client_ca = None
        self.ssl_client_cert = None
        self.ssl_client_key = None
        self.ssl_client_phrase = None
        self.auth_type = None
        self.tls_ca_certs = None
        self.tls_certkey = None
        self.tls_certkey_phrase = None


class Cfg2():                                          # pylint:disable=R0903

    """Class:  Cfg2

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the Cfg2 class.

        Arguments:

        """

        self.name = "MongoName"
        self.user = "root"
        self.japd = None
        self.host = "HostName"
        self.port = 27017
        self.auth = True
        self.conf_file = "ConFile"
        self.repset = None
        self.auth_db = "admin"
        self.auth_mech = "SCRAM-SHA-1"
        self.ssl_client_ca = None
        self.ssl_client_cert = None
        self.ssl_client_key = None
        self.ssl_client_phrase = None
        self.auth_type = None
        self.tls_ca_certs = None
        self.tls_certkey = None
        self.tls_certkey_phrase = None


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.


    Methods:
        setUp
        test_connection_fail_rep
        test_connection_fail_nonrep
        test_connection_success_rep
        test_connection_success_nonrep

        test_without_a_option
        test_with_a_option
        test_run_program

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = Cfg()
        self.cfg2 = Cfg2()
        self.mongorep = RepSetColl()
        self.mongo = Coll()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args.args_array = {"-I": True, "-c": "config", "-d": "dir/path"}
        self.args2.args_array = {
            "-I": True, "-c": "config", "-d": "dir/path", "-a": "auth_db"}
        self.func_names = {"-I": insert_doc}

    @mock.patch("mongo_db_data.gen_libs.load_module")
    @mock.patch("mongo_db_data.mongo_libs.create_instance")
    def test_connection_fail_rep(self, mock_coll, mock_load):

        """Function:  test_connection_fail_rep

        Description:  Test with failed connection in replica set.

        Arguments:

        """

        self.mongorep.status = False
        self.mongorep.err_msg = "Error Connection Message"

        mock_coll.return_value = self.mongorep
        mock_load.return_value = self.cfg

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_db_data.run_program(self.args, self.func_names))

    @mock.patch("mongo_db_data.gen_libs.load_module")
    @mock.patch("mongo_db_data.mongo_libs.create_instance")
    def test_connection_fail_nonrep(self, mock_coll, mock_load):

        """Function:  test_connection_fail_nonrep

        Description:  Test with failed connection in standalone node.

        Arguments:

        """

        self.mongo.status = False
        self.mongo.err_msg = "Error Connection Message"

        mock_coll.return_value = self.mongo
        mock_load.return_value = self.cfg2

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_db_data.run_program(self.args, self.func_names))

    @mock.patch("mongo_db_data.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.gen_libs.load_module")
    @mock.patch("mongo_db_data.mongo_libs.create_instance")
    def test_connection_success_rep(self, mock_coll, mock_load):

        """Function:  test_connection_success_rep

        Description:  Test with successful connection in replica set.

        Arguments:

        """

        mock_coll.return_value = self.mongorep
        mock_load.return_value = self.cfg

        self.assertFalse(mongo_db_data.run_program(self.args, self.func_names))

    @mock.patch("mongo_db_data.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.gen_libs.load_module")
    @mock.patch("mongo_db_data.mongo_libs.create_instance")
    def test_connection_success_nonrep(self, mock_coll, mock_load):

        """Function:  test_connection_success_nonrep

        Description:  Test with successful connection in standalone node.

        Arguments:

        """

        mock_coll.return_value = self.mongo
        mock_load.return_value = self.cfg2

        self.assertFalse(mongo_db_data.run_program(self.args, self.func_names))


if __name__ == "__main__":
    unittest.main()
