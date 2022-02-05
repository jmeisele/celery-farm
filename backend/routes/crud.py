from typing import List

from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from models.model import UpdateTaskModel
from models.solver import SCIPInstance
from workers.tasks import optimization

router = APIRouter()


@router.post("/solve", name="Solve problem")
async def create_celery_instance(request: Request, payload: SCIPInstance) -> JSONResponse:
    # Encode our data
    data = jsonable_encoder(payload)

    # Insert the encoded data into MongoDB
    new_task = await request.app.mongodb["solver"].insert_one(data)

    # Get MongoDB doc back and return
    doc_id = await request.app.mongodb["solver"].find_one({"_id": new_task.inserted_id})

    # Send ID to celery for processing
    optimization.delay(payload.id)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=doc_id)


@router.get("/", name="List all solver problems")
async def list_solver_problems(request: Request) -> List[dict]:
    instances = []
    for doc in await request.app.mongodb["solver"].find().to_list(length=100):
        instances.append(doc)
    return instances


@router.get("/{id}", name="Get a single solver problem")
async def show_solver_problem(id: str, request: Request):
    if (task := await request.app.mongodb["solver"].find_one({"_id": id})) is not None:
        return task

    raise HTTPException(status_code=404, detail=f"Task {id} not found")


@router.put("/{id}", name="Update a Solver Problem")
async def update_task(id: str, request: Request, task: UpdateTaskModel = Body(...)):
    task = {k: v for k, v in task.dict().items() if v is not None}

    if len(task) >= 1:
        update_result = await request.app.mongodb["tasks"].update_one({"_id": id}, {"$set": task})

        if update_result.modified_count == 1:
            if (updated_task := await request.app.mongodb["tasks"].find_one({"_id": id})) is not None:
                return updated_task

    if (existing_task := await request.app.mongodb["tasks"].find_one({"_id": id})) is not None:
        return existing_task

    raise HTTPException(status_code=404, detail=f"Task {id} not found")


@router.delete("/{id}", name="Delete Solver Problem")
async def delete_solver_problem(id: str, request: Request):
    delete_result = await request.app.mongodb["solver"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(content={f"{id}": "Deleted"})

    raise HTTPException(status_code=404, detail=f"Solver id: {id} not found")
