from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.api import expenses

load_dotenv()


app_name=os.environ.get("APP_NAME","Default Title")

app = FastAPI(title=app_name, version="0.1.0")

app.include_router(expenses.router)

@app.get("/")
def read_root():
    return {"message": "Hello from Expense Analytics API"}



@app.get("/health")
def health_check():
    return {"status": "healthy"}