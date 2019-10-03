#!/usr/bin/python
# Classification (U)

"""Program:  process_args.py

    Description:  Unit testing of process_args in mongo_db_data.py.

    Usage:
        test/unit/mongo_db_data/process_args.py

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

# Local
sys.path.append(os.getcwd())
import mongo_db_data
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_empty_list -> Test with empty list passed.
        test_one_key -> Test with one key pair passed.
        test_no_keys -> Test with no keys passed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {"-k1": "key1", "-l1": "value1"}
        self.args_array2 = {"-k1": "key1", "-l1": "value1",
                            "-k2": "key2", "-l2": "value2"}
        self.args_array3 = {"-k1": "key1", "-l1": "value1",
                            "-k2": "key2", "-l3": "value2"}
        self.args_array4 = {"-k1": "key1", "-l1": "value1",
                            "-k3": "key2", "-l2": "value2"}
        self.result = {"key1": {"$in": "value1"}}
        self.result2 = {"key1": {"$in": "value1"}, "key2": {"$in": "value2"}}

    def test_missing_key(self):

        """Function:  test_missing_key

        Description:  Test with missing key for value.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertEqual(mongo_db_data.process_args(self.args_array4),
                             (True, self.result))

    def test_missing_value(self):

        """Function:  test_missing_value

        Description:  Test with missing value for key.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertEqual(mongo_db_data.process_args(self.args_array3),
                             (True, self.result))

    def test_two_keys(self):

        """Function:  test_two_keys

        Description:  Test with two key pairs passed.

        Arguments:

        """

        self.assertEqual(mongo_db_data.process_args(self.args_array2),
                         (False, self.result2))

    def test_one_key(self, ):

        """Function:  test_one_key

        Description:  Test with one key pair passed.

        Arguments:

        """

        self.assertEqual(mongo_db_data.process_args(self.args_array),
                         (False, self.result))

    def test_no_keys(self):

        """Function:  test_no_keys

        Description:  Test with no keys passed.

        Arguments:

        """

        self.assertEqual(mongo_db_data.process_args({}), (False, {}))


if __name__ == "__main__":
    unittest.main()
