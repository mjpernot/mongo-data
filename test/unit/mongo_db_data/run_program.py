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


def insert_doc(repset, args_array, **kwargs):

    """Function:  insert_doc

    Description:  Stub holder for mongo_db_data.insert_doc function.

    Arguments:
        (input) repset -> Replication set instance.
        (input) args_array -> Array of command line options and values.

    """

    return True


class RepSet(object):

    """Class:  RepSet

    Description:  Class stub holder for mongo_class.RepSet class.

    Super-Class:

    Sub-Classes:

    Methods:
        __init__ -> Class initialization.
        connect -> Stub holder for mongo_class.RepSet.connect method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_run_program -> Test run_program function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        class CfgTest(object):

            """Class:  CfgTest

            Description:  Class which is a representation of a cfg module.

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

        self.cfg = CfgTest()
        self.repset = RepSet()
        self.args_array = {"-I": True, "-c": "config", "-d": "dir/path"}
        self.func_dict = {"-I": insert_doc}

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
