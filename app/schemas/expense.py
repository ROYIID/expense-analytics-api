from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    amount : float
    category : str
    description : str = None
    date : str= None


class ExpenseUpdate(BaseModel):
    amount : float =None
    category : str =None
    description : str = None
    date : str = None