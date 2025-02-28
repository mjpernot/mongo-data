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
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_db_data                            # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val
        arg_exist

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {}

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return arg in self.args_array


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_empty_list
        test_one_key
        test_no_keys

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args4 = ArgParser()
        self.args5 = ArgParser()
        self.args.args_array = {"-k1": "key1", "-l1": "value1"}
        self.args2.args_array = {
            "-k1": "key1", "-l1": "value1", "-k2": "key2", "-l2": "value2"}
        self.args3.args_array = {
            "-k1": "key1", "-l1": "value1", "-k2": "key2", "-l3": "value2"}
        self.args4.args_array = {
            "-k1": "key1", "-l1": "value1", "-k3": "key2", "-l2": "value2"}
        self.result = {"key1": {"$in": "value1"}}
        self.result2 = {"key1": {"$in": "value1"}, "key2": {"$in": "value2"}}

    def test_missing_key(self):

        """Function:  test_missing_key

        Description:  Test with missing key for value.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_db_data.process_args(self.args4), (True, self.result))

    def test_missing_value(self):

        """Function:  test_missing_value

        Description:  Test with missing value for key.

        Arguments:

        """
        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_db_data.process_args(self.args3), (True, self.result))

    def test_two_keys(self):

        """Function:  test_two_keys

        Description:  Test with two key pairs passed.

        Arguments:

        """

        self.assertEqual(
            mongo_db_data.process_args(self.args2), (False, self.result2))

    def test_one_key(self, ):

        """Function:  test_one_key

        Description:  Test with one key pair passed.

        Arguments:

        """

        self.assertEqual(
            mongo_db_data.process_args(self.args), (False, self.result))

    def test_no_keys(self):

        """Function:  test_no_keys

        Description:  Test with no keys passed.

        Arguments:

        """

        self.assertEqual(mongo_db_data.process_args(self.args5), (False, {}))


if __name__ == "__main__":
    unittest.main()
