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
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_empty_list -> Test with empty list passed.
        test_insert_doc -> Test with passing files to function.
        test_no_files -> Test with no -f option passed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

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

    @mock.patch("mongo_db_data.cmds_gen")
    @mock.patch("mongo_db_data.mongo_libs.create_cmd")
    def test_insert_doc(self, mock_cmd, mock_gen):

        """Function:  test_insert_doc

        Description:  Test with passing files to function.

        Arguments:

        """

        mock_cmd.return_value = ["Command", "List"]
        mock_gen.add_cmd.return_value = ["Command", "List", "Updated"]
        mock_gen.run_prog.return_value = True

        self.assertFalse(mongo_db_data.insert_doc(self.repset,
                                                  self.args_array,
                                                  opt_rep=self.opt_rep))

    def test_no_files(self):

        """Function:  test_no_files

        Description:  Test with no -f option passed.

        Arguments:

        """

        self.assertFalse(mongo_db_data.insert_doc(self.repset, {}))


if __name__ == "__main__":
    unittest.main()
