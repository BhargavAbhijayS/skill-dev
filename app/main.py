#This file is the "entry point" of the application
from fastapi import FastAPI
from config import settings
from Database import ping_database

#Creating FastAPI app instance.
app=FastAPI(title=settings.APP_NAME)

#This function runs once when the server starts. It checks the DB connection.
@app.on_event("startup")
def on_startup()-> None:
    if not ping_database():
        raise RuntimeError("Could not connect to MongoDB")
    print(f"[startup]Connected to MongoDB. App:{settings.APP_NAME}")

#Checks basic health-check API endpoint & confirms.
#GET / is running and reachable. (/ is considered as 'root')
@app.get("/",tags=["Health"])
def health_check():
    return {"status":"ok","app":settings.APP_NAME}