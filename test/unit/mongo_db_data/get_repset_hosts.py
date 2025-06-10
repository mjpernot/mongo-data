# Classification (U)

"""Program:  get_repset_hosts.py

    Description:  Unit testing of get_repset_hosts in mongo_db_data.py.

    Usage:
        test/unit/mongo_db_data/get_repset_hosts.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_db_data                            # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class CfgTest2():                                       # pylint:disable=R0903

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


class CfgTest():                                        # pylint:disable=R0903

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
        self.repset_hosts = "RepHostName"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_repset_name
        test_mongo_repset_name
        test_cfg_repset_name

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = CfgTest()
        self.cfg2 = CfgTest2()

    def test_no_repset_name(self):

        """Function:  test_no_repset_name

        Description:  Test with no repset name found.

        Arguments:

        """

        self.assertIsNone(mongo_db_data.get_repset_hosts(self.cfg2))

    def test_cfg_repset_name(self):

        """Function:  test_cfg_repset_name

        Description:  Test with cfg module setting repset name.

        Arguments:

        """

        self.assertEqual(mongo_db_data.get_repset_hosts(self.cfg),
                         "RepHostName")


if __name__ == "__main__":
    unittest.main()
