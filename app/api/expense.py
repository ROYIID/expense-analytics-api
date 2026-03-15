from fastapi import APIRouter, HTTPException

from app.schemas.expense import ExpenseCreate, ExpenseUpdate, ExpenseResponse

router = APIRouter(prefix="/expenses", tags=["expenses"])

expenses_db = []

@router.post("/", status_code=201, response_model=ExpenseResponse)
def create_expense(expense: ExpenseCreate):
    expense_value = expense.model_dump()
    expense_value["id"]= len(expenses_db) + 1
    expenses_db.append(expense_value)

    return expense_value


@router.get("/", response_model=list[ExpenseResponse])
def get_expenses():    
    return expenses_db

@router.get("/{expense_id}", response_model=ExpenseResponse)
def get_expense(expense_id: int):
    for expense in expenses_db:
        if expense["id"] == expense_id:
            return expense
    raise HTTPException(status_code=404, detail="Expense not found")


@router.put("/{expense_id}", response_model=ExpenseResponse)
def update_expense(expense_id: int, expense_update: ExpenseUpdate):
    for expense in expenses_db:
        if expense['id'] == expense_id:
            update_data =expense_update.model_dump(exclude_unset=True)
            expense.update(update_data)
            return expense
    raise HTTPException(status_code=404, detail="Expense not found")



@router.delete("/{expense_id}")
def delete_expense(expense_id: int):
    for  expense in expenses_db:
        if expense['id'] == expense_id:
            expenses_db.remove(expense)
            return {"detail": "Expense deleted"}
    raise HTTPException(status_code=404, detail="Expense not found")
    

    