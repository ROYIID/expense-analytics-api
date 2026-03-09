from fastapi import FastAPI

app = FastAPI(title="Expense Analytics API", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Hello from Expense Analytics API"}



@app.get("/health")
def health_check():
    return {"status": "healthy"}