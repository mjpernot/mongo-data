#!/usr/bin/python
# Classification (U)

"""Program:  truncate_coll.py

    Description:  Unit testing of truncate_coll in mongo_db_data.py.

    Usage:
        test/unit/mongo_db_data/truncate_coll.py

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
        self.override = None
        self.status = True
        self.err_msg = None

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.RepSetColl.connect method.

        Arguments:

        """

        return self.status, self.err_msg

    def coll_del_many(self, query, override):

        """Method:  coll_del_many

        Description:  Stub holder mongo_class.RepSetColl.coll_del_many method.

        Arguments:
            (input) query -> Query command.
            (input) override -> Override truncation command restriction.

        """

        self.query = query
        self.override = override


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
        test_truncate_coll

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
            self.assertFalse(mongo_db_data.truncate_coll(self.repset,
                                                         self.args_array))

    @mock.patch("mongo_db_data.mongo_libs.disconnect")
    @mock.patch("mongo_db_data.mongo_class.RepSetColl")
    def test_connection_success(self, mock_coll, mock_disconnect):

        """Function:  test_connection_success

        Description:  Test with successful connection.

        Arguments:

        """

        mock_coll.return_value = self.repcoll
        mock_disconnect.return_value = True

        self.assertFalse(mongo_db_data.truncate_coll(self.repset,
                                                     self.args_array))

    @mock.patch("mongo_db_data.mongo_libs.disconnect")
    @mock.patch("mongo_db_data.mongo_class.RepSetColl")
    def test_truncate_coll(self, mock_coll, mock_disconnect):

        """Function:  test_truncate_coll

        Description:  Test truncate_coll method.

        Arguments:

        """

        mock_coll.return_value = self.repcoll
        mock_disconnect.return_value = True

        self.assertFalse(mongo_db_data.truncate_coll(self.repset,
                                                     self.args_array))


if __name__ == "__main__":
    unittest.main()
