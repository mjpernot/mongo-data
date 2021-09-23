#!/usr/bin/python
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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import mongo_db_data
import lib.gen_libs as gen_libs
import version

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


class RepSet(object):

    """Class:  RepSet

    Description:  Class stub holder for mongo_class.RepSet class.

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

    def connect(self):

        """Method:  connect

        Description:  Stub method holder for mongo_class.Server.connect.

        Arguments:

        """

        return self.status, self.err_msg


class CfgTest(object):

    """Class:  CfgTest

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

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
        self.use_arg = True
        self.use_uri = False


class CfgTest2(object):

    """Class:  CfgTest2

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

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
        self.auth_mech = "SCRAM-SHA-1"
        self.use_arg = True
        self.use_uri = False


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.


    Methods:
        setUp
        test_connection_fail
        test_connection_success
        test_auth_mech
        test_no_auth_mech
        test_run_program

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = CfgTest()
        self.cfg2 = CfgTest2()
        self.repset = RepSet()
        self.args_array = {"-I": True, "-c": "config", "-d": "dir/path"}
        self.func_dict = {"-I": insert_doc}

    @mock.patch("mongo_db_data.gen_libs.load_module")
    @mock.patch("mongo_db_data.get_repset_hosts")
    @mock.patch("mongo_db_data.get_repset_name")
    @mock.patch("mongo_db_data.mongo_class.RepSet")
    def test_connection_fail(self, mock_repset, mock_name, mock_hosts,
                             mock_load):

        """Function:  test_connection_fail

        Description:  Test with failed connection.

        Arguments:

        """

        self.repset.status = False
        self.repset.err_msg = "Error Connection Message"

        mock_repset.return_value = self.repset
        mock_hosts.return_value = "RepSetHosts"
        mock_name.return_value = "RepSetName"
        mock_load.return_value = self.cfg

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_data.run_program(self.args_array,
                                                       self.func_dict))

    @mock.patch("mongo_db_data.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.gen_libs.load_module")
    @mock.patch("mongo_db_data.get_repset_hosts")
    @mock.patch("mongo_db_data.get_repset_name")
    @mock.patch("mongo_db_data.mongo_class.RepSet")
    def test_connection_success(self, mock_repset, mock_name, mock_hosts,
                                mock_load):

        """Function:  test_connection_success

        Description:  Test with successful connection.

        Arguments:

        """

        mock_repset.return_value = self.repset
        mock_hosts.return_value = "RepSetHosts"
        mock_name.return_value = "RepSetName"
        mock_load.return_value = self.cfg

        self.assertFalse(mongo_db_data.run_program(self.args_array,
                                                   self.func_dict))

    @mock.patch("mongo_db_data.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.gen_libs.load_module")
    @mock.patch("mongo_db_data.get_repset_hosts")
    @mock.patch("mongo_db_data.get_repset_name")
    @mock.patch("mongo_db_data.mongo_class.RepSet")
    def test_auth_mech(self, mock_repset, mock_name, mock_hosts, mock_load):

        """Function:  test_auth_mech

        Description:  Test with auth_mech passed.

        Arguments:

        """

        mock_repset.return_value = self.repset
        mock_hosts.return_value = "RepSetHosts"
        mock_name.return_value = "RepSetName"
        mock_load.return_value = self.cfg2

        self.assertFalse(mongo_db_data.run_program(self.args_array,
                                                   self.func_dict))

    @mock.patch("mongo_db_data.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.gen_libs.load_module")
    @mock.patch("mongo_db_data.get_repset_hosts")
    @mock.patch("mongo_db_data.get_repset_name")
    @mock.patch("mongo_db_data.mongo_class.RepSet")
    def test_no_auth_mech(self, mock_repset, mock_name, mock_hosts, mock_load):

        """Function:  test_no_auth_mech

        Description:  Test with no auth_mech passed.

        Arguments:

        """

        mock_repset.return_value = self.repset
        mock_hosts.return_value = "RepSetHosts"
        mock_name.return_value = "RepSetName"
        mock_load.return_value = self.cfg

        self.assertFalse(mongo_db_data.run_program(self.args_array,
                                                   self.func_dict))

    @mock.patch("mongo_db_data.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.gen_libs.load_module")
    @mock.patch("mongo_db_data.get_repset_hosts")
    @mock.patch("mongo_db_data.get_repset_name")
    @mock.patch("mongo_db_data.mongo_class.RepSet")
    def test_run_program(self, mock_repset, mock_name, mock_hosts, mock_load):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_repset.return_value = self.repset
        mock_hosts.return_value = "RepSetHosts"
        mock_name.return_value = "RepSetName"
        mock_load.return_value = self.cfg

        self.assertFalse(mongo_db_data.run_program(self.args_array,
                                                   self.func_dict))


if __name__ == "__main__":
    unittest.main()
