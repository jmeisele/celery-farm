from time import sleep
from pprint import pprint

from celery.utils.log import get_task_logger
from pymongo import MongoClient
from optimizer.solver import Solver

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

    # Run Solver

    # Update data in MongoDB with results by ID
    # doc = my_col.find_one_and_update(
    #     {"_id": doc_id},
    #     {"$set":
    #         {
    #             "something_new": "added"
    #         }
    #     }, upsert=True
    # )
    
    # new_data = my_col.find_one({"_id": doc_id})
    
    solver_params = data["solver_params"]
    logger.info(f"Solver Parameters: {solver_params}")
    
    problem_data = data["problem_data"]
    logger.info(f"Problem Data: {problem_data}")
    
    # logger.info(f"New Data: {new_data}")
    # return doc

@celery_app.task
def optimization(doc_id: str):
    # Pull data out of MongoDB by ID
    data = my_col.find_one({"_id": doc_id})

    problem_data = data["problem_data"]
    solver_params = data["solver_params"]

    solver = Solver(**problem_data)
    solver.build_model()
    solver.set_solver_parameters(solver_params)
    solver.solve_instance()
    solution = solver.get_solution_status()
    logger.info(f"ID: {doc_id} solved")
    doc = my_col.find_one_and_update(
        {"_id": doc_id},
        {"$set":
            {
                "solution": solution
            }
        }, upsert=True
    )
    updated_doc = my_col.find_one({"_id": doc_id})
    logger.info(f"Updated doc: {updated_doc}")