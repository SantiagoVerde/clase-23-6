from fastapi import FastAPI
from rutas import router
from mangum import Mangum

app = FastAPI()
app.include_router(router)
app.get("/")
