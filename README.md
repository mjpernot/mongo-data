# Python project containing program for data manipulation in a Mongo database.
# Classification (U)

# Description:
  This program is used to take an external JSON document and insert into a Mongo database, delete a document from a Mongo database collection based on passed key(s) and value(s), or truncate a collection within a Mongo database.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Description
  * Program Help Function
  * Help Message
  * Testing
    - Unit
    - Integration
    - Blackbox


# Features:
  * Insert JSON document into database.
  * Truncate collection in database.
  * Delete JSON document from database.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/arg_parser
    - lib/gen_libs
    - lib/cmds_gen
    - mongo_lib/mongo_class
    - mongo_lib/mongo_libs


# Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-data.git
```

Install/upgrade system modules.

```
cd mongo-data
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.
```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:

Create Mongodb configuration file.
```
cd config
cp mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - user = "USER"
    - passwd = "PASSWORD"
    - host = "IP_ADDRESS"
    - name = "HOSTNAME"

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```


# Program Descriptions:
### Program: mongo_db_data.py
##### Description: Performance monitoring program for a Mongo database.


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/mongo-data/mongo_db_data.py -h
```


# Help Message:
  Below is the help message for the program.  Recommend running the -h option on the command line to see the latest help message.

    Program:  mongo_db_data.py

    Description:  Program to either take a external JSON document and insert
        into a Mongo database, delete a document from a Mongo database
        collection based on passed key(s) and value(s), or truncate a
        collection within a Mongo database.

    Usage:
        mongo_db_data.py -c file -d path [-I {-f [ file | file*]} |
            -D {[-b name | -t name | -k1 "key_name" | -l1 "value1"
            {"value2" "value3" ...}
            {-k2 "key_name" | -l2 "value1" {"value2" "value3" ...} ...] |
            -f [file | file* ] }
            | -T [-b name | -t name]] {-a name | -p path} [-v | -h]

    Arguments:
        -c file => Mongo configuration file.  Required arg.
        -d dir path => Config directory path.  Required arg.
        -T => Truncate collection in database.
        -I => Insert JSON document into database.
        -D => Delete JSON document from database.
        -k[1-5] key_name => Name of key in document to delete on.
        -l[1-5] value(s) => One or more values for associated key.
            values are enclosed in quotes (") and space-delimited ( ).
        -b name => Database Name.  Required arg.
        -t name => Collection Name.  Required arg.
        -f file(s) => JSON Document to be inserted for -I option or
            search criteria for -D option.  Requires full
            Directory Path/File Name.
        -a name => Authentication Database Name.  Required for accounts
            not in database (-b).
        -p => Path to Mongo binaries.  Only required if the user
            running the program does not have the Mongo binaries in their path.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v and/or -h overrides all other options.

        NOTE 2:  -I and -D are XOR options.

        NOTE 3:  -k1 and -l1 are required for -D option.  -k[2-5] and
            -l[2-5] are optional, but are required to be paired.

    Notes:
        Mongo configuration file format (mongo.py).  The configuration
            file format for the Mongo connection used for inserting data into
            a database.  There are two ways to connect:  single or replica set.

            1.)  Single database connection:

            # Single Configuration file for Mongo Database Server.
            user = "root"
            passwd = "ROOT_PASSWORD"
            host = "IP_ADDRESS"
            name = "HOSTNAME"
            port = PORT_NUMBER (default of mysql is 27017)
            conf_file = None
            auth = True

            2.)  Replica Set connection:  Same format as above, but with these
                additional entries at the end of the configuration file:
            
            repset = "REPLICA_SET_NAME"
            repset_hosts = "HOST1:PORT, HOST2:PORT, HOST3:PORT, [...]"
            db_auth = "AUTHENTICATION_DATABASE"

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Example:
        mongo_db_data.py -c mongo -d config -b GMI -t FAC -f ins_doc -I


# Testing:


# Unit Testing:

### Description: Testing consists of unit testing for the functions in the mongo_db_data.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-data.git
```

Install/upgrade system modules.

```
cd mongo-data
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Unit test runs for mongo_db_data.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-data
```

### Unit:  help_message
```
test/unit/mongo_db_data/help_message.py
```

### Unit:  
```
test/unit/mongo_db_data/
```

### Unit:  
```
test/unit/mongo_db_data/
```

### Unit:  run_program
```
test/unit/mongo_db_data/run_program.py
```

### Unit:  main
```
test/unit/mongo_db_data/main.py
```

### All unit testing
```
test/unit/mongo_db_data/unit_test_run.sh
```

### Code coverage program
```
test/unit/mongo_db_data/code_coverage.sh
```


# Integration Testing:

### Description: Testing consists of integration testing of functions in the mongo_db_data.py program.

### Installation:

Install the project using git.
  *  Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-data.git
```

Install/upgrade system modules.

```
cd mongo-data
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create Mongodb configuration file.
```
cd test/integration/mongo-data/config
cp ../../../../config/mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - user = "USER"
    - passwd = "PASSWORD"
    - host = "IP_ADDRESS"
    - name = "HOSTNAME"

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```

# Integration test runs for mongo_db_data.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-data
```


### Integration:  
```
test/integration/mongo_db_data/
```

### All integration testing
```
test/integration/mongo_db_data/integration_test_run.sh
```

### Code coverage program
```
test/integration/mongo_db_data/code_coverage.sh
```


# Blackbox Testing:

### Description: Testing consists of blackbox testing of the mongo_db_data.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-data.git
```

Install/upgrade system modules.

```
cd mongo-data
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.
```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create Mongodb configuration file.
```
cd test/blackbox/mongo-data/config
cp ../../../../config/mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database. 
    - user = "USER"
    - passwd = "PASSWORD"
    - host = "IP_ADDRESS"
    - name = "HOSTNAME"

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```

# Blackbox test run for mongo_db_data.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-data
```

### Blackbox:  
```
test/blackbox/mongo_db_data/blackbox_test.sh
```

