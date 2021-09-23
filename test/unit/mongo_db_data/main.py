#!/usr/bin/python
# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in mongo_db_data.py.

    Usage:
        test/unit/mongo_db_data/main.py

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
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_help_true
        test_help_false
        test_arg_req_true
        test_arg_req_false
        test_arg_dir_chk_crt_true
        test_arg_dir_chk_crt_false
        test_arg_xor_dict_false
        test_arg_xor_dict_true
        test_arg_cond_req_false
        test_arg_cond_req_true
        test_arg_noreq_xor_false
        test_arg_noreq_xor_true
        test_arg_file_chk_true
        test_arg_file_chk_false
        test_process_f_option
        test_run_program

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {"-c": "CfgFile", "-d": "CfgDir"}
        self.args_array2 = {"-c": "CfgFile", "-d": "CfgDir", "-f": True}

    @mock.patch("mongo_db_data.gen_libs.help_func")
    @mock.patch("mongo_db_data.arg_parser")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test help if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = True

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func")
    @mock.patch("mongo_db_data.arg_parser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_help_false

        Description:  Test help if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func")
    @mock.patch("mongo_db_data.arg_parser")
    def test_arg_req_true(self, mock_arg, mock_help):

        """Function:  test_arg_req_true

        Description:  Test arg_require if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func")
    @mock.patch("mongo_db_data.arg_parser")
    def test_arg_req_false(self, mock_arg, mock_help):

        """Function:  test_arg_req_false

        Description:  Test arg_require if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func")
    @mock.patch("mongo_db_data.arg_parser")
    def test_arg_dir_chk_crt_true(self, mock_arg, mock_help):

        """Function:  test_arg_dir_chk_crt_true

        Description:  Test arg_dir_chk_crt if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func")
    @mock.patch("mongo_db_data.arg_parser")
    def test_arg_dir_chk_crt_false(self, mock_arg, mock_help):

        """Function:  test_arg_dir_chk_crt_false

        Description:  Test arg_dir_chk_crt if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_xor_dict.return_value = False

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func")
    @mock.patch("mongo_db_data.arg_parser")
    def test_arg_xor_dict_false(self, mock_arg, mock_help):

        """Function:  test_arg_xor_dict_false

        Description:  Test arg_xor_dict if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_xor_dict.return_value = False

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func")
    @mock.patch("mongo_db_data.arg_parser")
    def test_arg_xor_dict_true(self, mock_arg, mock_help):

        """Function:  test_arg_xor_dict_true

        Description:  Test arg_xor_dict if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_xor_dict.return_value = True
        mock_arg.arg_cond_req.return_value = False

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func")
    @mock.patch("mongo_db_data.arg_parser")
    def test_arg_cond_req_false(self, mock_arg, mock_help):

        """Function:  test_arg_cond_req_false

        Description:  Test arg_cond_req if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_xor_dict.return_value = True
        mock_arg.arg_cond_req.return_value = False

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func")
    @mock.patch("mongo_db_data.arg_parser")
    def test_arg_cond_req_true(self, mock_arg, mock_help):

        """Function:  test_arg_cond_req_true

        Description:  Test arg_cond_req if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_xor_dict.return_value = True
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_noreq_xor.return_value = False

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func")
    @mock.patch("mongo_db_data.arg_parser")
    def test_arg_noreq_xor_false(self, mock_arg, mock_help):

        """Function:  test_arg_noreq_xor_false

        Description:  Test arg_noreq_xor if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_xor_dict.return_value = True
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_noreq_xor.return_value = False

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func")
    @mock.patch("mongo_db_data.arg_parser")
    def test_arg_noreq_xor_true(self, mock_arg, mock_help):

        """Function:  test_arg_noreq_xor_true

        Description:  Test arg_noreq_xor if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_xor_dict.return_value = True
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_file_chk.return_value = True

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func")
    @mock.patch("mongo_db_data.arg_parser")
    def test_arg_file_chk_true(self, mock_arg, mock_help):

        """Function:  test_arg_file_chk_true

        Description:  Test arg_file_chk if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_xor_dict.return_value = True
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_file_chk.return_value = True

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.run_program")
    @mock.patch("mongo_db_data.gen_libs.help_func")
    @mock.patch("mongo_db_data.arg_parser")
    def test_arg_file_chk_false(self, mock_arg, mock_help, mock_run):

        """Function:  test_arg_file_chk_false

        Description:  Test arg_file_chk if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_xor_dict.return_value = True
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_file_chk.return_value = False
        mock_run.return_value = True

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.run_program")
    @mock.patch("mongo_db_data.gen_libs")
    @mock.patch("mongo_db_data.arg_parser")
    def test_process_f_option(self, mock_arg, mock_lib, mock_run):

        """Function:  test_process_f_option

        Description:  Test with processing -f option.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array2
        mock_lib.help_func.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_xor_dict.return_value = True
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_file_chk.return_value = False
        mock_run.return_value = True
        mock_lib.rm_dup_list.return_value = ["File1"]

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.run_program")
    @mock.patch("mongo_db_data.gen_libs.help_func")
    @mock.patch("mongo_db_data.arg_parser")
    def test_run_program(self, mock_arg, mock_help, mock_run):

        """Function:  test_run_program

        Description:  Test with run_program.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_xor_dict.return_value = True
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_file_chk.return_value = False
        mock_run.return_value = True

        self.assertFalse(mongo_db_data.main())


if __name__ == "__main__":
    unittest.main()
