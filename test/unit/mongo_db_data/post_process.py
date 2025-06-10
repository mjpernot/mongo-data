# Classification (U)

"""Program:  post_process.py

    Description:  Unit testing of post_process in mongo_db_data.py.

    Usage:
        test/unit/mongo_db_data/post_process.py

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


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val
        arg_exist
        arg_dir_chk

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {
            "-b": "DbName", "-t": "TableName", "-f": ["/path/filename"]}
        self.dir_perms_chk = None
        self.dir_perms_chk_results = True

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

    def arg_dir_chk(self, dir_perms_chk):

        """Method:  arg_dir_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_dir_chk.

        Arguments:

        """

        self.dir_perms_chk = dir_perms_chk

        return self.dir_perms_chk_results


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_r_option_rm_failed
        test_r_option_no_files
        test_r_option
        test_m_dir_perms
        test_m_not_removable
        test_m_option_no_files
        test_m_option
        test_no_option

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.file = "test/unit/mongo_db_data/test_files/insert_doc2_data.py"

    @mock.patch("mongo_db_data.gen_libs.rm_file",
                mock.Mock(return_value=(True, "ErrorMessage")))
    def test_r_option_rm_failed(self):

        """Function:  test_r_option_rm_failed

        Description:  Test with -r option selected, but remove failed.

        Arguments:

        """

        self.args.args_array["-r"] = True

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_data.post_process(self.args))

    @mock.patch("mongo_db_data.gen_libs.rm_file",
                mock.Mock(return_value=(False, None)))
    def test_r_option_no_files(self):

        """Function:  test_r_option_no_files

        Description:  Test with -r option selected, but no files passed.

        Arguments:

        """

        self.args.args_array["-r"] = True
        self.args.args_array["-f"] = []

        self.assertFalse(mongo_db_data.post_process(self.args))

    @mock.patch("mongo_db_data.gen_libs.rm_file",
                mock.Mock(return_value=(False, None)))
    def test_r_option(self):

        """Function:  test_r_option

        Description:  Test with -r option selected.

        Arguments:

        """

        self.args.args_array["-r"] = True

        self.assertFalse(mongo_db_data.post_process(self.args))

    @mock.patch("mongo_db_data.is_file_deletable",
                mock.Mock(return_value=True))
    def test_m_dir_perms(self):

        """Function:  test_m_dir_perms

        Description:  Test with -m option selected, but directory permissions
            are incorrect.

        Arguments:

        """

        self.args.dir_perms_chk_results = False

        self.args.args_array["-m"] = "/path"

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_data.post_process(self.args))

    @mock.patch("mongo_db_data.is_file_deletable",
                mock.Mock(return_value=False))
    def test_m_not_removable(self):

        """Function:  test_m_not_removable

        Description:  Test with -m option selected, but file is not deletable.

        Arguments:

        """

        self.args.args_array["-m"] = "/path"

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_data.post_process(self.args))

    def test_m_option_no_files(self):

        """Function:  test_m_option_no_files

        Description:  Test with -m option selected, but no files passed.

        Arguments:

        """

        self.args.args_array["-m"] = "/path"
        self.args.args_array["-f"] = []

        self.assertFalse(mongo_db_data.post_process(self.args))

    @mock.patch("mongo_db_data.gen_libs.mv_file2",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.is_file_deletable",
                mock.Mock(return_value=True))
    def test_m_option(self):

        """Function:  test_m_option

        Description:  Test with -m option selected.

        Arguments:

        """

        self.args.args_array["-m"] = "/path"

        self.assertFalse(mongo_db_data.post_process(self.args))

    def test_no_option(self):

        """Function:  test_no_option

        Description:  Test with no option selected.

        Arguments:

        """

        self.assertFalse(mongo_db_data.post_process(self.args))


if __name__ == "__main__":
    unittest.main()
