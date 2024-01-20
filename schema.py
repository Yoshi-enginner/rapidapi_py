from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    Message: str

class Items(BaseModel):
    data:List[Item]