#!/bin/bash
# Unit test code coverage for SonarQube to cover all modules.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#       that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mongo_db_data test/unit/mongo_db_data/get_repset_hosts.py
coverage run -a --source=mongo_db_data test/unit/mongo_db_data/get_repset_name.py
coverage run -a --source=mongo_db_data test/unit/mongo_db_data/help_message.py


echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
coverage xml -i
