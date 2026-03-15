from fastapi import APIRouter, HTTPException

from app.schemas.expense import ExpenseCreate, ExpenseUpdate

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


@router.put("/expenses/{expense_id}")
def update_expense(expense_id: int, expense_update: ExpenseUpdate):
    for expense in expenses_db:
        if expense['id'] == expense_id:
            update_data =expense_update.model_dump(exclude_unset=True)
            expense.update(update_data)
            return expense
    raise HTTPException(status_code=404, detail="Expense not found")



@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    for  expense in expenses_db:
        if expense['id'] == expense_id:
            expenses_db.remove(expense)
            return {"detail": "Expense deleted"}
    raise HTTPException(status_code=404, detail="Expense not found")
    

    