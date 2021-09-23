#!/usr/bin/python
# Classification (U)

"""Program:  delete_docs.py

    Description:  Unit testing of delete_docs in mongo_db_data.py.

    Usage:
        test/unit/mongo_db_data/delete_docs.py

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


class RepSetColl(object):

    """Class:  RepSetColl

    Description:  Class stub holder for mongo_class.RepSetColl class.

    Methods:
        __init__
        connect
        coll_del_many

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.query = None
        self.status = True
        self.err_msg = None

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.RepSetColl.connect method.

        Arguments:

        """

        return self.status, self.err_msg

    def coll_del_many(self, query):

        """Method:  coll_del_many

        Description:  Stub holder mongo_class.RepSetColl.coll_del_many method.

        Arguments:
            (input) query -> Query command.

        """

        self.query = query


class RepSetCfg(object):

    """Class:  RepSetCfg

    Description:  Class which is a representation of a RepSet class.

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
        self.repset_hosts = ["List of hosts"]
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
        test_multiple_lines
        test_multiple_files
        test_empty_file
        test_file_list
        test_no_list_error
        test_no_file_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.repset = RepSetCfg()
        self.repcoll = RepSetColl()
        self.args_array = {"-b": "databasename", "-t": "tablename",
                           "-a": "authdatabase"}
        self.args_array2 = {"-b": "databasename", "-t": "tablename",
                            "-a": "authdatabase", "-f": ["file1"]}
        self.args_array3 = {"-b": "databasename", "-t": "tablename",
                            "-a": "authdatabase", "-f": ["file1", "file2"]}

    @mock.patch("mongo_db_data.mongo_class.RepSetColl")
    def test_connection_fail(self, mock_coll):

        """Function:  test_connection_fail

        Description:  Test with failed connection.

        Arguments:

        """

        self.repcoll.status = False
        self.repcoll.err_msg = "Error Connection Message"

        mock_coll.return_value = self.repcoll

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_data.delete_docs(self.repset,
                                                       self.args_array2))

    @mock.patch("mongo_db_data.mongo_libs.disconnect")
    @mock.patch("mongo_db_data.gen_libs")
    @mock.patch("mongo_db_data.mongo_class.RepSetColl")
    def test_connection_success(self, mock_coll, mock_lib, mock_disconnect):

        """Function:  test_connection_success

        Description:  Test with successful connection.

        Arguments:

        """

        mock_coll.return_value = self.repcoll
        mock_lib.file_2_list.return_value = ["File1"]
        mock_lib.str_2_type.return_value = {"query"}
        mock_disconnect.return_value = True

        self.assertFalse(mongo_db_data.delete_docs(self.repset,
                                                   self.args_array2))

    @mock.patch("mongo_db_data.mongo_libs.disconnect")
    @mock.patch("mongo_db_data.gen_libs")
    @mock.patch("mongo_db_data.mongo_class.RepSetColl")
    def test_multiple_lines(self, mock_coll, mock_lib, mock_disconnect):

        """Function:  test_multiple_lines

        Description:  Test with multiple lines per file passed.

        Arguments:

        """

        mock_coll.return_value = self.repcoll
        mock_lib.file_2_list.return_value = ["file1", "file2"]
        mock_lib.str_2_type.return_value = {"query"}
        mock_disconnect.return_value = True

        self.assertFalse(mongo_db_data.delete_docs(self.repset,
                                                   self.args_array2))

    @mock.patch("mongo_db_data.mongo_libs.disconnect")
    @mock.patch("mongo_db_data.gen_libs")
    @mock.patch("mongo_db_data.mongo_class.RepSetColl")
    def test_multiple_files(self, mock_coll, mock_lib, mock_disconnect):

        """Function:  test_multiple_files

        Description:  Test with multiple files passed.

        Arguments:

        """

        mock_coll.return_value = self.repcoll
        mock_lib.file_2_list.return_value = ["file1", "file2"]
        mock_lib.str_2_type.return_value = {"query"}
        mock_disconnect.return_value = True

        self.assertFalse(mongo_db_data.delete_docs(self.repset,
                                                   self.args_array3))

    @mock.patch("mongo_db_data.mongo_libs.disconnect")
    @mock.patch("mongo_db_data.gen_libs")
    @mock.patch("mongo_db_data.mongo_class.RepSetColl")
    def test_empty_file(self, mock_coll, mock_lib, mock_disconnect):

        """Function:  test_empty_file

        Description:  Test with file list passed.

        Arguments:

        """

        mock_coll.return_value = self.repcoll
        mock_lib.file_2_list.return_value = []
        mock_disconnect.return_value = True

        self.assertFalse(mongo_db_data.delete_docs(self.repset,
                                                   self.args_array2))

    @mock.patch("mongo_db_data.mongo_libs.disconnect")
    @mock.patch("mongo_db_data.gen_libs")
    @mock.patch("mongo_db_data.mongo_class.RepSetColl")
    def test_file_list(self, mock_coll, mock_lib, mock_disconnect):

        """Function:  test_file_list

        Description:  Test with file list passed.

        Arguments:

        """

        mock_coll.return_value = self.repcoll
        mock_lib.file_2_list.return_value = ["File1"]
        mock_lib.str_2_type.return_value = {"query"}
        mock_disconnect.return_value = True

        self.assertFalse(mongo_db_data.delete_docs(self.repset,
                                                   self.args_array2))

    @mock.patch("mongo_db_data.mongo_libs.disconnect")
    @mock.patch("mongo_db_data.process_args")
    @mock.patch("mongo_db_data.mongo_class.RepSetColl")
    def test_no_list_error(self, mock_coll, mock_proc, mock_disconnect):

        """Function:  test_no_list_error

        Description:  Test with no file list passed, but with error.

        Arguments:

        """

        mock_coll.return_value = self.repcoll
        mock_proc.return_value = (False, {"Query"})
        mock_disconnect.return_value = True

        self.assertFalse(mongo_db_data.delete_docs(self.repset,
                                                   self.args_array))

    @mock.patch("mongo_db_data.mongo_libs.disconnect")
    @mock.patch("mongo_db_data.process_args")
    @mock.patch("mongo_db_data.mongo_class.RepSetColl")
    def test_no_file_list(self, mock_coll, mock_proc, mock_disconnect):

        """Function:  test_no_file_list

        Description:  Test with no file list passed.

        Arguments:

        """

        mock_coll.return_value = self.repcoll
        mock_proc.return_value = (False, {"Query"})
        mock_disconnect.return_value = True

        self.assertFalse(mongo_db_data.delete_docs(self.repset,
                                                   self.args_array))


if __name__ == "__main__":
    unittest.main()
