from fastapi import FastAPI
from routes.rutas import router
from mangum import Mangum

app = FastAPI()
app.include_router(router)
