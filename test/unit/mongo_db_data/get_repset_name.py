#!/usr/bin/python
# Classification (U)

"""Program:  get_repset_name.py

    Description:  Unit testing of get_repset_name in mongo_db_data.py.

    Usage:
        test/unit/mongo_db_data/get_repset_name.py

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


class Coll2(object):

    """Class:  Coll2

    Description:  Class stub holder for mongo_class.Coll class.

    Methods:
        __init__ -> Class initialization.
        coll_cnt -> Stub holder for mongo_class.Coll.coll_cnt method.
        coll_find1 -> Stub holder for mongo_class.Coll.coll_find1 method.
        connect -> Stub holder for mongo_class.Coll.connect method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass

    def coll_cnt(self):

        """Method:  coll_cnt

        Description:  Stub holder for mongo_class.Coll.coll_cnt method.

        Arguments:

        """

        return 0

    def coll_find1(self):

        """Method:  coll_find1

        Description:  Stub holder for mongo_class.Coll.coll_find1 method.

        Arguments:

        """

        return {"_id": "UniqueIdentifier"}

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.Coll.connect method.

        Arguments:

        """

        return True


class Coll(object):

    """Class:  Coll

    Description:  Class stub holder for mongo_class.Coll class.

    Methods:
        __init__ -> Class initialization.
        coll_cnt -> Stub holder for mongo_class.Coll.coll_cnt method.
        coll_find1 -> Stub holder for mongo_class.Coll.coll_find1 method.
        connect -> Stub holder for mongo_class.Coll.connect method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass

    def coll_cnt(self):

        """Method:  coll_cnt

        Description:  Stub holder for mongo_class.Coll.coll_cnt method.

        Arguments:

        """

        return 1

    def coll_find1(self):

        """Method:  coll_find1

        Description:  Stub holder for mongo_class.Coll.coll_find1 method.

        Arguments:

        """

        return {"_id": "RepSetName2"}

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.Coll.connect method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_no_repset_name -> Test with no repset name found.
        test_mongo_repset_name -> Test with Mongo db setting repset name.
        test_cfg_repset_name -> Test with cfg module setting repset name.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        class CfgTest2(object):

            """Class:  CfgTest2

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
        self.cfg2 = CfgTest2()

    @mock.patch("mongo_db_data.cmds_gen.disconnect")
    @mock.patch("mongo_db_data.mongo_class.Coll")
    def test_no_repset_name(self, mock_coll, mock_disconnect):

        """Function:  test_no_repset_name

        Description:  Test with no repset name found.

        Arguments:

        """

        mock_coll.return_value = Coll2()
        mock_disconnect.return_value = True

        self.assertEqual(mongo_db_data.get_repset_name(self.cfg2), None)

    @mock.patch("mongo_db_data.cmds_gen.disconnect")
    @mock.patch("mongo_db_data.mongo_class.Coll")
    def test_mongo_repset_name(self, mock_coll, mock_disconnect):

        """Function:  test_mongo_repset_name

        Description:  Test with Mongo db setting repset name.

        Arguments:

        """

        mock_coll.return_value = Coll()
        mock_disconnect.return_value = True

        self.assertEqual(mongo_db_data.get_repset_name(self.cfg2),
                         "RepSetName2")

    def test_cfg_repset_name(self):

        """Function:  test_cfg_repset_name

        Description:  Test with cfg module setting repset name.

        Arguments:

        """

        self.assertEqual(mongo_db_data.get_repset_name(self.cfg), "RepSetName")


if __name__ == "__main__":
    unittest.main()
