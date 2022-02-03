from time import sleep

from bson import ObjectId
from celery.utils.log import get_task_logger
from pymongo import MongoClient

from db.config import db_settings
from .main import celery_app

logger = get_task_logger(__name__)

my_client = MongoClient(f"mongodb://{db_settings.DB_URL}", connect=False)
my_db = my_client[f"{db_settings.DB_NAME}"]
my_col = my_db["solver"]


@celery_app.task
def reverse(text):
    sleep(5)
    return text[::-1]


@celery_app.task
def solve_problem(doc_id: str):
    # Pull data out of MongoDB by ID and log it
    data = my_col.find_one({"_id": doc_id})
    logger.info(f"Data: {data}")

    # Run Solver

    # Update data in MongoDB with results by ID
    doc = my_col.find_one_and_update(
        {"_id": doc_id},
        {"$set":
            {
                "something_new": "added"
            }
        }, upsert=True
    )
    new_data = my_col.find_one({"_id": doc_id})
    logger.info(f"New Data: {new_data}")
    return doc