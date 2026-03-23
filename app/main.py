from fastapi import FastAPI
from app.api import expense
from app.core.config import settings


app = FastAPI(title=settings.app_name, version="0.1.0")

app.include_router(expense.router)

@app.get("/")
def read_root():
    return {"message": "Hello from Expense Analytics API"}



@app.get("/health")
def health_check():
    return {"status": "healthy"}