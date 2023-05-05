#!/bin/bash
# Unit testing program for the program module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing..."
/usr/bin/python3 test/unit/mongo_db_data/delete_docs.py
/usr/bin/python3 test/unit/mongo_db_data/get_repset_hosts.py
/usr/bin/python3 test/unit/mongo_db_data/get_repset_name.py
/usr/bin/python3 test/unit/mongo_db_data/help_message.py
/usr/bin/python3 test/unit/mongo_db_data/insert_doc.py
/usr/bin/python3 test/unit/mongo_db_data/main.py
/usr/bin/python3 test/unit/mongo_db_data/process_args.py
/usr/bin/python3 test/unit/mongo_db_data/run_program.py
/usr/bin/python3 test/unit/mongo_db_data/truncate_coll.py
