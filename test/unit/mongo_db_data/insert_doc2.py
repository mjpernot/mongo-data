# Classification (U)

"""Program:  insert_doc2.py

    Description:  Unit testing of insert_doc2 in mongo_db_data.py.

    Usage:
        test/unit/mongo_db_data/insert_doc2.py

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
import lib.gen_libs as gen_libs              # pylint:disable=E0401,C0413,R0402
import mongo_lib.mongo_class as mongo_class  # pylint:disable=E0401,C0413,R0402
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

        self.args_array = {"-b": "DbName", "-t": "TableName", "-f": []}

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
        test_file_m_r_option
        test_file_r_option
        test_file_m_option
        test_file_no_move
        test_insert_fail
        test_multiple_files
        test_one_file
        test_no_files

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.coll = mongo_class.Coll("ServerName", "root", "japd")
        self.file = "test/unit/mongo_db_data/test_files/insert_doc2_data.txt"

    @mock.patch("mongo_db_data.post_process", mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.mongo_libs.ins_doc",
                mock.Mock(return_value=(True, None)))
    def test_file_m_r_option(self):

        """Function:  test_file_m_r_option

        Description:  Test with post processing of file using -m and -r option.

        Arguments:

        """

        self.args.args_array["-f"] = [self.file]
        self.args.args_array["-m"] = "/path"
        self.args.args_array["-r"] = True

        self.assertFalse(mongo_db_data.insert_doc2(self.coll, self.args))

    @mock.patch("mongo_db_data.post_process", mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.mongo_libs.ins_doc",
                mock.Mock(return_value=(True, None)))
    def test_file_r_option(self):

        """Function:  test_file_r_option

        Description:  Test with post processing of file using -r option.

        Arguments:

        """

        self.args.args_array["-f"] = [self.file]
        self.args.args_array["-r"] = True

        self.assertFalse(mongo_db_data.insert_doc2(self.coll, self.args))

    @mock.patch("mongo_db_data.post_process", mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.mongo_libs.ins_doc",
                mock.Mock(return_value=(True, None)))
    def test_file_m_option(self):

        """Function:  test_file_m_option

        Description:  Test with post processing of file using -m option.

        Arguments:

        """

        self.args.args_array["-f"] = [self.file]
        self.args.args_array["-m"] = "/path"

        self.assertFalse(mongo_db_data.insert_doc2(self.coll, self.args))

    @mock.patch("mongo_db_data.mongo_libs.ins_doc",
                mock.Mock(return_value=(True, None)))
    def test_file_no_move(self):

        """Function:  test_file_no_move

        Description:  Test with no post processing of file.

        Arguments:

        """

        self.args.args_array["-f"] = [self.file]

        self.assertFalse(mongo_db_data.insert_doc2(self.coll, self.args))

    @mock.patch("mongo_db_data.mongo_libs.ins_doc",
                mock.Mock(return_value=(False, "ErrorMessage")))
    def test_insert_fail(self):

        """Function:  test_insert_fail

        Description:  Test with insertion failure.

        Arguments:

        """

        self.args.args_array["-f"] = [self.file]

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_data.insert_doc2(self.coll, self.args))

    @mock.patch("mongo_db_data.mongo_libs.ins_doc",
                mock.Mock(return_value=(True, None)))
    def test_multiple_files(self):

        """Function:  test_multiple_files

        Description:  Test with multiple files passed in.

        Arguments:

        """

        self.args.args_array["-f"] = [self.file, self.file]

        self.assertFalse(mongo_db_data.insert_doc2(self.coll, self.args))

    @mock.patch("mongo_db_data.mongo_libs.ins_doc",
                mock.Mock(return_value=(True, None)))
    def test_one_file(self):

        """Function:  test_one_file

        Description:  Test with one file passed in.

        Arguments:

        """

        self.args.args_array["-f"] = [self.file]

        self.assertFalse(mongo_db_data.insert_doc2(self.coll, self.args))

    def test_no_files(self):

        """Function:  test_no_files

        Description:  Test with no files passed in.

        Arguments:

        """

        self.assertFalse(mongo_db_data.insert_doc2(self.coll, self.args))


if __name__ == "__main__":
    unittest.main()
