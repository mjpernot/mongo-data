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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_db_data                            # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val
        update_arg
        arg_exist
        arg_cond_req
        arg_file_chk
        arg_dir_chk
        arg_require
        arg_xor_dict
        arg_noreq_xor
        arg_parse2

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = {}
        self.update_arg_key = None
        self.update_arg_val = None
        self.update_arg2 = True
        self.opt_req = None
        self.opt_req2 = True
        self.dir_perms_chk = None
        self.dir_perms_chk2 = True
        self.dir_chk = None
        self.opt_xor_val = None
        self.opt_xor_val2 = True
        self.file_perm_chk = None
        self.file_crt = None
        self.arg_file_chk2 = True
        self.opt_con_req = None
        self.opt_con_req2 = True
        self.xor_noreq = None
        self.xor_noreq2 = True
        self.argparse2 = True

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)

    def update_arg(self, arg_key, arg_val):

        """Method:  update_arg

        Description:  Method stub holder for gen_class.ArgParser.update_arg.

        Arguments:

        """

        self.update_arg_key = arg_key
        self.update_arg_val = arg_val

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return arg in self.args_array

    def arg_cond_req(self, opt_con_req):

        """Method:  arg_cond_req

        Description:  Method stub holder for gen_class.ArgParser.arg_cond_req.

        Arguments:

        """

        self.opt_con_req = opt_con_req

        return self.opt_con_req2

    def arg_file_chk(self, file_perm_chk):

        """Method:  arg_file_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_file_chk.

        Arguments:

        """

        self.file_perm_chk = file_perm_chk

        return self.arg_file_chk2

    def arg_dir_chk(self, dir_perms_chk):

        """Method:  arg_dir_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_dir_chk.

        Arguments:

        """

        self.dir_perms_chk = dir_perms_chk

        return self.dir_perms_chk2

    def arg_require(self, opt_req):

        """Method:  arg_require

        Description:  Method stub holder for gen_class.ArgParser.arg_require.

        Arguments:

        """

        self.opt_req = opt_req

        return self.opt_req2

    def arg_xor_dict(self, opt_xor_val):

        """Method:  arg_xor_dict

        Description:  Method stub holder for gen_class.ArgParser.arg_xor_dict.

        Arguments:

        """

        self.opt_xor_val = opt_xor_val

        return self.opt_xor_val2

    def arg_noreq_xor(self, xor_noreq):

        """Method:  arg_noreq_xor

        Description:  Method stub holder for gen_class.ArgParser.arg_noreq_xor.

        Arguments:

        """

        self.xor_noreq = xor_noreq

        return self.xor_noreq2

    def arg_parse2(self):

        """Method:  arg_parse2

        Description:  Method stub holder for gen_class.ArgParser.arg_parse2.

        Arguments:

        """

        return self.argparse2


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_arg_parse2_false
        test_arg_parse2_true
        test_help_true
        test_help_false
        test_arg_req_false
        test_arg_req_true
        test_arg_dir_chk_crt_false
        test_arg_dir_chk_crt_true
        test_arg_xor_dict_false
        test_arg_xor_dict_true
        test_arg_cond_req_false
        test_arg_cond_req_true
        test_arg_noreq_xor_false
        test_arg_noreq_xor_true
        test_arg_file_chk_true
        test_arg_file_chk_false
        test_run_program

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args.args_array = {"-c": "CfgFile", "-d": "CfgDir"}

    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_arg_parse2_false(self, mock_arg):

        """Function:  test_arg_parse2_false

        Description:  Test arg_parse2 returns false.

        Arguments:

        """

        self.args.argparse2 = False

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_arg_parse2_true(self, mock_arg):

        """Function:  test_arg_parse2_true

        Description:  Test arg_parse2 returns true.

        Arguments:

        """

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_help_true(self, mock_arg):

        """Function:  test_help_true

        Description:  Test help if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_help_false(self, mock_arg):

        """Function:  test_help_false

        Description:  Test help if returns false.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_arg_req_false(self, mock_arg):

        """Function:  test_arg_req_false

        Description:  Test arg_require if returns false.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_arg_req_true(self, mock_arg):

        """Function:  test_arg_req_true

        Description:  Test arg_require if returns true.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_arg_dir_chk_crt_false(self, mock_arg):

        """Function:  test_arg_dir_chk_crt_false

        Description:  Test arg_dir_chk_crt if returns false.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_arg_dir_chk_crt_true(self, mock_arg):

        """Function:  test_arg_dir_chk_crt_true

        Description:  Test arg_dir_chk_crt if returns true.

        Arguments:

        """

        self.args.opt_xor_val2 = False

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_arg_xor_dict_false(self, mock_arg):

        """Function:  test_arg_xor_dict_false

        Description:  Test arg_xor_dict if returns false.

        Arguments:

        """

        self.args.opt_xor_val2 = False

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_arg_xor_dict_true(self, mock_arg):

        """Function:  test_arg_xor_dict_true

        Description:  Test arg_xor_dict if returns true.

        Arguments:

        """

        self.args.opt_con_req2 = False

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_arg_cond_req_false(self, mock_arg):

        """Function:  test_arg_cond_req_false

        Description:  Test arg_cond_req if returns false.

        Arguments:

        """

        self.args.opt_con_req2 = False

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_arg_cond_req_true(self, mock_arg):

        """Function:  test_arg_cond_req_true

        Description:  Test arg_cond_req if returns true.

        Arguments:

        """

        self.args.xor_noreq2 = False

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_arg_noreq_xor_false(self, mock_arg):

        """Function:  test_arg_noreq_xor_false

        Description:  Test arg_noreq_xor if returns false.

        Arguments:

        """

        self.args.xor_noreq2 = False

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_arg_noreq_xor_true(self, mock_arg):

        """Function:  test_arg_noreq_xor_true

        Description:  Test arg_noreq_xor if returns true.

        Arguments:

        """

        self.args.arg_file_chk2 = False

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_arg_file_chk_false(self, mock_arg):

        """Function:  test_arg_file_chk_false

        Description:  Test arg_file_chk if returns false.

        Arguments:

        """

        self.args.arg_file_chk2 = False

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_data.run_program", mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_arg_file_chk_true(self, mock_arg):

        """Function:  test_arg_file_chk_true

        Description:  Test arg_file_chk if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())

    @mock.patch("mongo_db_data.gen_libs.help_func",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_data.run_program", mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.gen_class.ArgParser")
    def test_run_program(self, mock_arg):

        """Function:  test_run_program

        Description:  Test with run_program.

        Arguments:

        """

        mock_arg.return_value = self.args

        self.assertFalse(mongo_db_data.main())


if __name__ == "__main__":
    unittest.main()
