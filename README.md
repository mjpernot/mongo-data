# Python project containing program for data manipulation in a Mongo database.
# Classification (U)

# Description:
  Used to take an external JSON document and insert into a Mongo database, delete a document from a Mongo database collection based on passed key(s) and value(s), or truncate a collection within a Mongo database.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
    - Secure Environment
  * Installation
  * Configuration
  * Program Help Function
  * Testing
    - Unit


# Features:
  * Insert JSON document into database.
  * Truncate collection in database.
  * Delete JSON document from database.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python3-pip
    - python3-devel
    - gcc

  * Secure Environment:  If operating in a secure environment, this package will require at least a minimum of pymongo==3.8.0 or better.  It will also require a manual change to the auth.py module in the pymongo package.  See below for changes to auth.py.
    - Locate the auth.py file python installed packages on the system in the pymongo package directory.
    - Edit the file and locate the \_password_digest function.
    - In the \_password_digest function there is an line that should match: "md5hash = hashlib.md5()".  Change it to "md5hash = hashlib.md5(usedforsecurity=False)".
    - Lastly, it will require the configuration file entry auth_mech to be set to: SCRAM-SHA-1 or SCRAM-SHA-256.


# Installation:

Install the project using git.

```
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-data.git
```

Install/upgrade system modules.

NOTE: Install as the user that will run the program.

Redhat 8 (Running Python 3.9 and 3.12):

```
python -m pip install --user -r requirements39.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```

Install supporting classes and libraries.

```
python -m pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
python -m pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
python -m pip install -r requirements-mongo-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Configuration:

Create Mongodb configuration file.
Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - user = "USER"
    - japd = "PWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"

  * Change these entries only if required:
    - port = 27017
    - conf_file = None
    - auth = True
    - auth_db = "admin"
    - auth_mech = "SCRAM-SHA-1"

  * If connecting to a Mongo replica set:
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

  * Notes for auth_mech configuration entry:
    - NOTE 1:  SCRAM-SHA-256 only works for Mongodb 4.0 and better.
    - NOTE 2:  FIPS 140-2 environment requires SCRAM-SHA-1 or SCRAM-SHA-256.

  * If Mongo is set to use TLS or SSL connections, then one or more of the following entries will need to be completed to connect using TLS or SSL protocols.  Note:  Read the configuration file to determine which entries will need to be set.
    - SSL:
        -> auth_type = None
        -> ssl_client_ca = None
        -> ssl_client_key = None
        -> ssl_client_cert = None
        -> ssl_client_phrase = None
    - TLS:
        -> auth_type = None
        -> tls_ca_certs = None
        -> tls_certkey = None
        -> tls_certkey_phrase = None

  * Secure Environment for Mongo:  See Prerequisites -> Secure Environment section for details.

```
cp config/mongo.py.TEMPLATE config/mongo.py
chmod 600 config/mongo.py
vim config/mongo.py
```


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:

```
mongo_db_data.py -h
```


# Testing:

# Unit Testing:

### Installation:

Install the project using the procedures in the Installation section.

### Testing:

```
test/unit/mongo_db_data/unit_test_run.sh
test/unit/mongo_db_data/code_coverage.sh
```
