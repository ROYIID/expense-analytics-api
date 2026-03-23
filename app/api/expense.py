from fastapi import APIRouter, HTTPException

from app.schemas.expense import ExpenseCreate, ExpenseUpdate, ExpenseResponse

router = APIRouter(prefix="/expenses", tags=["expenses"])

expenses_db = []

@router.post("/", status_code=201, response_model=ExpenseResponse)
async def create_expense(expense: ExpenseCreate):
    expense_value = expense.model_dump()
    expense_value["id"]= len(expenses_db) + 1
    expenses_db.append(expense_value)

    return expense_value


@router.get("/", response_model=list[ExpenseResponse])
async def get_expenses(
    category: str = None,
    min_amount: float = None,
    skip: int = 0,
    limit: int = 10
    ):
    
    filtered_expenses = expenses_db
    if category:
        filtered_expenses = [expense for expense in filtered_expenses if expense["category"].lower() == category.lower()]
    if min_amount is not None:
        filtered_expenses = [expense for expense in filtered_expenses if expense["amount"] >= min_amount]
    return filtered_expenses[skip: skip + limit]    




@router.get("/{expense_id}", response_model=ExpenseResponse)
async def get_expense(expense_id: int):
    for expense in expenses_db:
        if expense["id"] == expense_id:
            return expense
    raise HTTPException(status_code=404, detail=f"Expense {expense_id} not found")


@router.put("/{expense_id}", response_model=ExpenseResponse)
async def update_expense(expense_id: int, expense_update: ExpenseUpdate):
    for expense in expenses_db:
        if expense['id'] == expense_id:
            update_data =expense_update.model_dump(exclude_unset=True)
            expense.update(update_data)
            return expense
    raise HTTPException(status_code=404, detail=f"Expense {expense_id} not found")



@router.delete("/{expense_id}")
async def delete_expense(expense_id: int):
    for  expense in expenses_db:
        if expense['id'] == expense_id:
            expenses_db.remove(expense)
            return {"detail": "Expense deleted"}
    raise HTTPException(status_code=404, detail=f"Expense {expense_id} not found")
    

    