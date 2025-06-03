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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_db_data                            # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():                                      # pylint:disable=R0903

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """


class Coll():                                           # pylint:disable=R0903

    """Class:  Coll

    Description:  Class stub holder for mongo_class.Coll class.

    Methods:
        __init__
        coll_del_many

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.query = None
        self.override = None

    def coll_del_many(self, query, override):

        """Method:  coll_del_many

        Description:  Stub holder mongo_class.Coll.coll_del_many method.

        Arguments:
            (input) query -> Query command.
            (input) override -> Override truncation command restriction.

        """

        self.query = query
        self.override = override


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_truncate_coll

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.coll = Coll()
        self.args = ArgParser()

    def test_truncate_coll(self):

        """Function:  test_truncate_coll

        Description:  Test truncate_coll method.

        Arguments:

        """

        self.assertFalse(mongo_db_data.truncate_coll(self.coll, self.args))


if __name__ == "__main__":
    unittest.main()
