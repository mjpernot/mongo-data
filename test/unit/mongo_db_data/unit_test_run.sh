#!/bin/bash
# Unit testing program for the program module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing..."
test/unit/mongo_db_data/get_repset_name.py
test/unit/mongo_db_data/help_message.py
