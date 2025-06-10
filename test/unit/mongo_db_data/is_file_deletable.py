# Classification (U)

"""Program:  is_file_deletable.py

    Description:  Unit testing of is_file_deletable in mongo_db_data.py.

    Usage:
        test/unit/mongo_db_data/is_file_deletable.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_all_checks_pass
        test_dir_non_writable
        test_file_non_writable
        test_isfile_false

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.fname = "/path/filename.txt"

    @mock.patch("mongo_db_data.os.access", mock.Mock(return_value=True))
    @mock.patch("mongo_db_data.os.path.isfile",
                mock.Mock(side_effect=[True, True]))
    def test_all_checks_pass(self):

        """Function:  test_all_checks_pass

        Description:  Test with the directory not being writable.

        Arguments:

        """

        self.assertTrue(mongo_db_data.is_file_deletable(self.fname))

    @unittest.skip("Error: Unable to to get os.path.isfile to mock correctly.")
    @mock.patch("mongo_db_data.os.path.isfile",
                mock.Mock(side_effect=[True, False]))
    @mock.patch("mongo_db_data.os.access", mock.Mock(return_value=True))
    def test_dir_non_writable(self):

        """Function:  test_dir_non_writable

        Description:  Test with the directory not being writable.

        Arguments:

        """

        self.assertFalse(mongo_db_data.is_file_deletable(self.fname))

    @mock.patch("mongo_db_data.os.access", mock.Mock(return_value=False))
    @mock.patch("mongo_db_data.os.path.isfile", mock.Mock(return_value=True))
    def test_file_non_writable(self):

        """Function:  test_file_non_writable

        Description:  Test with the file not being writable.

        Arguments:

        """

        self.assertFalse(mongo_db_data.is_file_deletable(self.fname))

    @mock.patch("mongo_db_data.os.path.isfile", mock.Mock(return_value=False))
    def test_isfile_false(self):

        """Function:  test_isfile_false

        Description:  Test with is_file returns false.

        Arguments:

        """

        self.assertFalse(mongo_db_data.is_file_deletable(self.fname))


if __name__ == "__main__":
    unittest.main()
