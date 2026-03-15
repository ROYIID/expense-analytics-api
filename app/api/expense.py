from fastapi import APIRouter, HTTPException

from app.schemas.expense import ExpenseCreate

router = APIRouter()

expenses_db = []

@router.post("/expenses", status_code=201)
def create_expense(expense: ExpenseCreate):
    expense_value = expense.model_dump()
    expense_value["id"]= len(expenses_db) + 1
    expenses_db.append(expense_value)

    return expense_value


@router.get("/expenses")
def get_expenses():    
    return expenses_db

@router.get("/expenses/{expense_id}")
def get_expense(expense_id: int):
    for expense in expenses_db:
        if expense["id"] == expense_id:
            return expense
    raise HTTPException(status_code=404, detail="Expense not found")
    