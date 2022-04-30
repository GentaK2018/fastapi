from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.get("/items/", response_model=List[Item])
async def get_item():
    item = [
        {
            "name": "foo",
            "description": None,
            "price": 458,
            "tax": 0.1,
        },
        {
            "name": "paa",
            "description": None,
            "price": 781,
            "tax": 0.1,
        },
        {
            "name": "pee",
            "description": None,
            "price": 412,
            "tax": 0.05,
        }
    ]
    return item