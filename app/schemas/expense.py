from pydantic import BaseModel, Field

class ExpenseCreate(BaseModel):
    amount : float = Field(gt=0, description="The amount of the expense")
    category : str = Field(min_length=1,max_length=50, description="The category of the expense")
    description : str = Field(max_length=200, description="A brief description of the expense",default=None)
    date : str= None


class ExpenseUpdate(BaseModel):
    amount : float =None
    category : str =None
    description : str = None
    date : str = None


class ExpenseResponse(BaseModel):
    id : int
    amount : float
    category : str
    description : str = None
    date : str = None