from fastapi import APIRouter
from routes import crud

api_router = APIRouter()
api_router.include_router(crud.router, tags=["CRUD"])
