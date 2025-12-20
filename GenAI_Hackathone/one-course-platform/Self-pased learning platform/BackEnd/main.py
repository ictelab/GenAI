###  main.py

from fastapi import FastAPI
from app.api import router

app = FastAPI(title="AI Learning Platform")
app.include_router(router)

