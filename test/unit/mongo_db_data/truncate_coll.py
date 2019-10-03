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

    def coll_del_many(self, query, override):

        """Method:  coll_del_many

        Description:  Stub holder mongo_class.RepSetColl.coll_del_many method.

        Arguments:
            (input) query -> Query command.
            (input) override -> Override truncation command restriction.

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_truncate_coll -> Test truncate_coll method.

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

    @mock.patch("mongo_db_data.cmds_gen.disconnect")
    @mock.patch("mongo_db_data.mongo_class.RepSetColl")
    def test_truncate_coll(self, mock_coll, mock_disconnect):

        """Function:  test_truncate_coll

        Description:  Test truncate_coll method.

        Arguments:

        """

        mock_coll.return_value = RepSetColl()
        mock_disconnect.return_value = True

        self.assertFalse(mongo_db_data.truncate_coll(self.repset,
                                                     self.args_array))


if __name__ == "__main__":
    unittest.main()
