#!/bin/bash
# Unit testing program for the program module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing..."
test/unit/mongo_db_data/delete_docs.py
test/unit/mongo_db_data/get_repset_hosts.py
test/unit/mongo_db_data/get_repset_name.py
test/unit/mongo_db_data/help_message.py
test/unit/mongo_db_data/insert_doc.py
test/unit/mongo_db_data/main.py
test/unit/mongo_db_data/process_args.py
test/unit/mongo_db_data/run_program.py
test/unit/mongo_db_data/truncate_coll.py
