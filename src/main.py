import json
import logging

from preparation import *
from database import add_to_table, check_of_existence_tables


JSON_FILE = "../data/data-20230124-structure-20160713.json"
LIMIT = 1000
COUNT_COLUMNS_FOR_EDUCATIONS_TABLE = 26

logging.basicConfig(filename="../process.log",
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.info("Running program...")

error_message = check_of_existence_tables()
if error_message:exit(error_message)

try:
    data = json.load(open(JSON_FILE, "r", encoding="utf-8"))["OpenData"]["Certificates"]["Certificate"]
    logging.info("Collected data from JSON...")
except FileNotFoundError:
    exit(f"No such file or directory: {JSON_FILE}")

for index in range(0, len(data), LIMIT):
    items = data[index:][:LIMIT]
    items_len = len(items)
    
    certificates = prepare_certificates(items)
    logging.info(f"Collected {items_len} certificates")
    
    educations = prepare_educations(items)
    logging.info(f"Collected {items_len} educations")
    
    add_to_table(tablename="certificate", data=certificates)
    logging.info(f"Added {items_len} certificates")
    
    add_to_table(tablename="actual_education_organization", data=educations, columns_count=COUNT_COLUMNS_FOR_EDUCATIONS_TABLE)
    logging.info(f"Added {items_len} educations")


print("Successful!")