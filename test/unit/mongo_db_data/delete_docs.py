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
        __init__ -> Class initialization.
        connect -> Stub holder for mongo_class.RepSetColl.connect method.
        coll_del_many -> Stub holder for mongo_class.RepSetColl.coll_del_many.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.RepSetColl.connect method.

        Arguments:

        """

        pass

    def coll_del_many(self, query):

        """Method:  coll_del_many

        Description:  Stub holder mongo_class.RepSetColl.coll_del_many method.

        Arguments:
            (input) query -> Query command.

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_file_list -> Test with file list passed.
        test_no_list_error -> Test with no file list passed, but with error.
        test_no_file_list -> Test with no file list passed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        class RepSetCfg(object):

            """Class:  RepSetCfg

            Description:  Class which is a representation of a RepSet class.

            Methods:
                __init__ -> Initialize configuration environment.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the CfgTest class.

                Arguments:

                """

                self.name = "MongoName"
                self.user = "root"
                self.passwd = "pwd"
                self.host = "HostName"
                self.port = 27017
                self.db = "test"
                self.coll = "CollectionName"
                self.auth = True
                self.conf_file = "ConFile"
                self.repset = "RepSetName"
                self.repset_hosts = ["List of hosts"]

        self.repset = RepSetCfg()
        self.args_array = {"-b": "databasename", "-t": "tablename",
                           "-a": "authdatabase"}
        self.args_array2 = {"-b": "databasename", "-t": "tablename",
                            "-a": "authdatabase", "-f": ["file1"]}

    @mock.patch("mongo_db_data.cmds_gen.disconnect")
    @mock.patch("mongo_db_data.gen_libs")
    @mock.patch("mongo_db_data.mongo_class.RepSetColl")
    def test_file_list(self, mock_coll, mock_lib, mock_disconnect):

        """Function:  test_file_list

        Description:  Test with file list passed.

        Arguments:

        """

        mock_coll.return_value = RepSetColl()
        mock_lib.file_2_list.return_value = ["File1"]
        mock_lib.str_2_type.return_value = {"query"}
        mock_disconnect.return_value = True

        self.assertFalse(mongo_db_data.delete_docs(self.repset,
                                                   self.args_array2))


    @mock.patch("mongo_db_data.cmds_gen.disconnect")
    @mock.patch("mongo_db_data.process_args")
    @mock.patch("mongo_db_data.mongo_class.RepSetColl")
    def test_no_list_error(self, mock_coll, mock_proc, mock_disconnect):

        """Function:  test_no_list_error

        Description:  Test with no file list passed, but with error.

        Arguments:

        """

        mock_coll.return_value = RepSetColl()
        mock_proc.return_value = (False, {"Query"})
        mock_disconnect.return_value = True

        self.assertFalse(mongo_db_data.delete_docs(self.repset,
                                                   self.args_array))

    @mock.patch("mongo_db_data.cmds_gen.disconnect")
    @mock.patch("mongo_db_data.process_args")
    @mock.patch("mongo_db_data.mongo_class.RepSetColl")
    def test_no_file_list(self, mock_coll, mock_proc, mock_disconnect):

        """Function:  test_no_file_list

        Description:  Test with no file list passed.

        Arguments:

        """

        mock_coll.return_value = RepSetColl()
        mock_proc.return_value = (False, {"Query"})
        mock_disconnect.return_value = True

        self.assertFalse(mongo_db_data.delete_docs(self.repset,
                                                   self.args_array))


if __name__ == "__main__":
    unittest.main()
