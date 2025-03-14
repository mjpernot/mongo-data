# Classification (U)

"""Program:  get_repset_name.py

    Description:  Unit testing of get_repset_name in mongo_db_data.py.

    Usage:
        test/unit/mongo_db_data/get_repset_name.py

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


class Coll2():

    """Class:  Coll2

    Description:  Class stub holder for mongo_class.Coll class.

    Methods:
        __init__
        coll_cnt
        coll_find1
        connect

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cnt = 0
        self.find = {"_id": "UniqueIdentifier"}
        self.status = True
        self.err_msg = None

    def coll_cnt(self):

        """Method:  coll_cnt

        Description:  Stub holder for mongo_class.Coll.coll_cnt method.

        Arguments:

        """

        return self.cnt

    def coll_find1(self):

        """Method:  coll_find1

        Description:  Stub holder for mongo_class.Coll.coll_find1 method.

        Arguments:

        """

        return self.find

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.Coll.connect method.

        Arguments:

        """

        return self.status, self.err_msg


class Coll():

    """Class:  Coll

    Description:  Class stub holder for mongo_class.Coll class.

    Methods:
        __init__
        coll_cnt
        coll_find1
        connect

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cnt = 1
        self.find = {"_id": "RepSetName2"}
        self.status = True
        self.err_msg = None

    def coll_cnt(self):

        """Method:  coll_cnt

        Description:  Stub holder for mongo_class.Coll.coll_cnt method.

        Arguments:

        """

        return self.cnt

    def coll_find1(self):

        """Method:  coll_find1

        Description:  Stub holder for mongo_class.Coll.coll_find1 method.

        Arguments:

        """

        return self.find

    def connect(self):

        """Method:  connect

        Description:  Stub holder for mongo_class.Coll.connect method.

        Arguments:

        """

        return self.status, self.err_msg


class CfgTest():                                        # pylint:disable=R0903

    """Class:  CfgTest

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.name = "MongoName"
        self.user = "root"
        self.japd = None
        self.host = "HostName"
        self.port = 27017
        self.auth = True
        self.conf_file = "ConFile"
        self.repset = "RepSetName"
        self.ssl_client_ca = None
        self.ssl_client_cert = None
        self.ssl_client_key = None
        self.ssl_client_phrase = None
        self.auth_type = None
        self.tls_ca_certs = None
        self.tls_certkey = None
        self.tls_certkey_phrase = None


class CfgTest2():                                       # pylint:disable=R0903

    """Class:  CfgTest2

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.name = "MongoName"
        self.user = "root"
        self.japd = None
        self.host = "HostName"
        self.port = 27017
        self.auth = True
        self.conf_file = "ConFile"
        self.ssl_client_ca = None
        self.ssl_client_cert = None
        self.ssl_client_key = None
        self.ssl_client_phrase = None
        self.auth_type = None
        self.tls_ca_certs = None
        self.tls_certkey = None
        self.tls_certkey_phrase = None


class CfgTest3():                                       # pylint:disable=R0903

    """Class:  CfgTest3

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.name = "MongoName"
        self.user = "root"
        self.japd = None
        self.host = "HostName"
        self.port = 27017
        self.auth = True
        self.conf_file = "ConFile"
        self.auth_mech = "SCRAM-SHA-1"
        self.ssl_client_ca = None
        self.ssl_client_cert = None
        self.ssl_client_key = None
        self.ssl_client_phrase = None
        self.auth_type = None
        self.tls_ca_certs = None
        self.tls_certkey = None
        self.tls_certkey_phrase = None


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_connection_fail
        test_connection_success
        test_auth_mech
        test_no_auth_mech
        test_no_repset_name
        test_mongo_repset_name
        test_cfg_repset_name

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = CfgTest()
        self.cfg2 = CfgTest2()
        self.cfg3 = CfgTest3()
        self.coll = Coll()
        self.coll2 = Coll2()

    @mock.patch("mongo_db_data.mongo_class.Coll")
    def test_connection_fail(self, mock_coll):

        """Function:  test_connection_fail

        Description:  Test with failed connection.

        Arguments:

        """

        self.coll.status = False
        self.coll.err_msg = "Error Connection Message"

        mock_coll.return_value = self.coll

        with gen_libs.no_std_out():
            self.assertIsNone(mongo_db_data.get_repset_name(self.cfg2))

    @mock.patch("mongo_db_data.mongo_libs.disconnect")
    @mock.patch("mongo_db_data.mongo_class.Coll")
    def test_connection_success(self, mock_coll, mock_disconnect):

        """Function:  test_connection_success

        Description:  Test with successful connection.

        Arguments:

        """

        mock_coll.return_value = self.coll
        mock_disconnect.return_value = True

        self.assertEqual(mongo_db_data.get_repset_name(self.cfg2),
                         "RepSetName2")

    @mock.patch("mongo_db_data.mongo_libs.disconnect")
    @mock.patch("mongo_db_data.mongo_class.Coll")
    def test_auth_mech(self, mock_coll, mock_disconnect):

        """Function:  test_auth_mech

        Description:  Test with auth_mech passed.

        Arguments:

        """

        mock_coll.return_value = self.coll
        mock_disconnect.return_value = True

        self.assertEqual(mongo_db_data.get_repset_name(self.cfg3),
                         "RepSetName2")

    @mock.patch("mongo_db_data.mongo_libs.disconnect")
    @mock.patch("mongo_db_data.mongo_class.Coll")
    def test_no_auth_mech(self, mock_coll, mock_disconnect):

        """Function:  test_no_auth_mech

        Description:  Test with no auth_mech passed.

        Arguments:

        """

        mock_coll.return_value = self.coll
        mock_disconnect.return_value = True

        self.assertEqual(mongo_db_data.get_repset_name(self.cfg2),
                         "RepSetName2")

    @mock.patch("mongo_db_data.mongo_libs.disconnect")
    @mock.patch("mongo_db_data.mongo_class.Coll")
    def test_no_repset_name(self, mock_coll, mock_disconnect):

        """Function:  test_no_repset_name

        Description:  Test with no repset name found.

        Arguments:

        """

        mock_coll.return_value = self.coll2
        mock_disconnect.return_value = True

        self.assertIsNone(mongo_db_data.get_repset_name(self.cfg2))

    @mock.patch("mongo_db_data.mongo_libs.disconnect")
    @mock.patch("mongo_db_data.mongo_class.Coll")
    def test_mongo_repset_name(self, mock_coll, mock_disconnect):

        """Function:  test_mongo_repset_name

        Description:  Test with Mongo db setting repset name.

        Arguments:

        """

        mock_coll.return_value = self.coll
        mock_disconnect.return_value = True

        self.assertEqual(mongo_db_data.get_repset_name(self.cfg2),
                         "RepSetName2")

    def test_cfg_repset_name(self):

        """Function:  test_cfg_repset_name

        Description:  Test with cfg module setting repset name.

        Arguments:

        """

        self.assertEqual(mongo_db_data.get_repset_name(self.cfg), "RepSetName")


if __name__ == "__main__":
    unittest.main()
