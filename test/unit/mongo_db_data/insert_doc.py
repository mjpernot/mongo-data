# Classification (U)

"""Program:  insert_doc.py

    Description:  Unit testing of insert_doc in mongo_db_data.py.

    Usage:
        test/unit/mongo_db_data/insert_doc.py

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


class SubProcess():                                     # pylint:disable=R0903

    """Class:  SubProcess

    Description:  Class which is a representation of the subprocess class.

    Methods:
        __init__
        wait

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the ZipFile class.

        Arguments:

        """

    def wait(self):

        """Method:  wait

        Description:  Mock representation of subprocess.wait method.

        Arguments:

        """


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_file_m_r_option
        test_file_r_option
        test_file_m_option
        test_file_no_move
        test_insert_nonrep
        test_insert_rep
        test_empty_list
        test_insert_doc
        test_no_files

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.subproc = SubProcess()
        self.opt_rep = {"-f": "--file="}
        self.repcoll = mongo_class.RepSetColl("ServerName", "root", "japd")
        self.coll = mongo_class.Coll("ServerName", "root", "japd")
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args.args_array = {"-f": ["File1"]}
        self.args2.args_array = {"-f": []}

    @mock.patch("mongo_db_data.post_process", mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.gen_libs.add_cmd")
    @mock.patch("mongo_db_data.gen_libs.subprocess.Popen")
    @mock.patch("mongo_db_data.mongo_libs.create_cmd")
    def test_file_m_r_option(self, mock_cmd, mock_open, mock_add):

        """Function:  test_file_m_r_option

        Description:  Test with post processing of file using -m and -r option.

        Arguments:

        """

        self.args.args_array["-m"] = "/path"
        self.args.args_array["-r"] = True

        mock_cmd.return_value = ["Command", "List"]
        mock_add.return_value = ["Command", "List", "Updated"]
        mock_open.return_value = self.subproc

        self.assertFalse(
            mongo_db_data.insert_doc(
                self.repcoll, self.args, opt_rep=self.opt_rep))

    @mock.patch("mongo_db_data.post_process", mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.gen_libs.add_cmd")
    @mock.patch("mongo_db_data.gen_libs.subprocess.Popen")
    @mock.patch("mongo_db_data.mongo_libs.create_cmd")
    def test_file_r_option(self, mock_cmd, mock_open, mock_add):

        """Function:  test_file_r_option

        Description:  Test with post processing of file using -r option.

        Arguments:

        """

        self.args.args_array["-r"] = True

        mock_cmd.return_value = ["Command", "List"]
        mock_add.return_value = ["Command", "List", "Updated"]
        mock_open.return_value = self.subproc

        self.assertFalse(
            mongo_db_data.insert_doc(
                self.repcoll, self.args, opt_rep=self.opt_rep))

    @mock.patch("mongo_db_data.post_process", mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.gen_libs.add_cmd")
    @mock.patch("mongo_db_data.gen_libs.subprocess.Popen")
    @mock.patch("mongo_db_data.mongo_libs.create_cmd")
    def test_file_m_option(self, mock_cmd, mock_open, mock_add):

        """Function:  test_file_m_option

        Description:  Test with post processing of file using -m option.

        Arguments:

        """

        self.args.args_array["-m"] = "/path"

        mock_cmd.return_value = ["Command", "List"]
        mock_add.return_value = ["Command", "List", "Updated"]
        mock_open.return_value = self.subproc

        self.assertFalse(
            mongo_db_data.insert_doc(
                self.repcoll, self.args, opt_rep=self.opt_rep))

    @mock.patch("mongo_db_data.gen_libs.add_cmd")
    @mock.patch("mongo_db_data.gen_libs.subprocess.Popen")
    @mock.patch("mongo_db_data.mongo_libs.create_cmd")
    def test_file_no_move(self, mock_cmd, mock_open, mock_add):

        """Function:  test_file_no_move

        Description:  Test with no post processing of file.

        Arguments:

        """

        mock_cmd.return_value = ["Command", "List"]
        mock_add.return_value = ["Command", "List", "Updated"]
        mock_open.return_value = self.subproc

        self.assertFalse(
            mongo_db_data.insert_doc(
                self.repcoll, self.args, opt_rep=self.opt_rep))

    @mock.patch("mongo_db_data.gen_libs.add_cmd")
    @mock.patch("mongo_db_data.gen_libs.subprocess.Popen")
    @mock.patch("mongo_db_data.mongo_libs.create_cmd")
    def test_insert_nonrep(self, mock_cmd, mock_open, mock_add):

        """Function:  test_insert_nonrep

        Description:  Test with inserting using standalone.

        Arguments:

        """

        mock_cmd.return_value = ["Command", "List"]
        mock_add.return_value = ["Command", "List", "Updated"]
        mock_open.return_value = self.subproc

        self.assertFalse(
            mongo_db_data.insert_doc(
                self.coll, self.args, opt_rep=self.opt_rep))

    @mock.patch("mongo_db_data.gen_libs.add_cmd")
    @mock.patch("mongo_db_data.gen_libs.subprocess.Popen")
    @mock.patch("mongo_db_data.mongo_libs.create_cmd")
    def test_insert_rep(self, mock_cmd, mock_open, mock_add):

        """Function:  test_insert_rep

        Description:  Test with inserting using replica set.

        Arguments:

        """

        mock_cmd.return_value = ["Command", "List"]
        mock_add.return_value = ["Command", "List", "Updated"]
        mock_open.return_value = self.subproc

        self.assertFalse(
            mongo_db_data.insert_doc(
                self.repcoll, self.args, opt_rep=self.opt_rep))

    @mock.patch("mongo_db_data.mongo_libs.create_cmd")
    def test_empty_list(self, mock_cmd):

        """Function:  test_empty_list

        Description:  Test with empty list passed.

        Arguments:

        """

        mock_cmd.return_value = ["Command", "List"]

        self.assertFalse(mongo_db_data.insert_doc(self.repcoll, self.args2))

    @mock.patch("mongo_db_data.gen_libs.add_cmd")
    @mock.patch("mongo_db_data.gen_libs.subprocess.Popen")
    @mock.patch("mongo_db_data.mongo_libs.create_cmd")
    def test_insert_doc(self, mock_cmd, mock_open, mock_add):

        """Function:  test_insert_doc

        Description:  Test with passing files to function.

        Arguments:

        """

        mock_cmd.return_value = ["Command", "List"]
        mock_add.return_value = ["Command", "List", "Updated"]
        mock_open.return_value = self.subproc

        self.assertFalse(
            mongo_db_data.insert_doc(
                self.repcoll, self.args, opt_rep=self.opt_rep))

    def test_no_files(self):

        """Function:  test_no_files

        Description:  Test with no -f option.

        Arguments:

        """

        self.assertFalse(mongo_db_data.insert_doc(self.repcoll, self.args3))


if __name__ == "__main__":
    unittest.main()
