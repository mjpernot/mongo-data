#!/bin/bash
# Unit test code coverage for program module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#   that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mongo_db_data test/unit/mongo_db_data/delete_docs.py
coverage run -a --source=mongo_db_data test/unit/mongo_db_data/help_message.py
coverage run -a --source=mongo_db_data test/unit/mongo_db_data/insert_doc.py
coverage run -a --source=mongo_db_data test/unit/mongo_db_data/insert_doc2.py
coverage run -a --source=mongo_db_data test/unit/mongo_db_data/is_file_deletable.py
coverage run -a --source=mongo_db_data test/unit/mongo_db_data/main.py
coverage run -a --source=mongo_db_data test/unit/mongo_db_data/post_process.py
coverage run -a --source=mongo_db_data test/unit/mongo_db_data/process_args.py
coverage run -a --source=mongo_db_data test/unit/mongo_db_data/run_program.py
coverage run -a --source=mongo_db_data test/unit/mongo_db_data/truncate_coll.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
