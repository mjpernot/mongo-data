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
        self.repset = "RepSetInstance"
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args.args_array = {"-f": ["File1"]}
        self.args2.args_array = {"-f": []}

    @mock.patch("mongo_db_data.mongo_libs.create_cmd")
    def test_empty_list(self, mock_cmd):

        """Function:  test_empty_list

        Description:  Test with empty list passed.

        Arguments:

        """

        mock_cmd.return_value = ["Command", "List"]

        self.assertFalse(mongo_db_data.insert_doc(self.repset, self.args2))

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
                self.repset, self.args, opt_rep=self.opt_rep))

    def test_no_files(self):

        """Function:  test_no_files

        Description:  Test with no -f option.

        Arguments:

        """

        self.assertFalse(mongo_db_data.insert_doc(self.repset, self.args3))


if __name__ == "__main__":
    unittest.main()
