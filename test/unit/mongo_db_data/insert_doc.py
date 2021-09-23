#!/usr/bin/python
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


class SubProcess(object):

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

        pass

    def wait(self):

        """Method:  wait

        Description:  Mock representation of subprocess.wait method.

        Arguments:

        """

        pass


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
        self.args_array = {"-f": ["File1"]}
        self.args_array2 = {"-f": []}

    def test_empty_list(self):

        """Function:  test_empty_list

        Description:  Test with empty list passed.

        Arguments:

        """

        self.assertFalse(mongo_db_data.insert_doc(self.repset,
                                                  self.args_array2))

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
                self.repset, self.args_array, opt_rep=self.opt_rep))

    def test_no_files(self):

        """Function:  test_no_files

        Description:  Test with no -f option passed.

        Arguments:

        """

        self.assertFalse(mongo_db_data.insert_doc(self.repset, {}))


if __name__ == "__main__":
    unittest.main()
