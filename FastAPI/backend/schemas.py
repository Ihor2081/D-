from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Product(BaseModel):
    id: int
    name: str
    model: str
    price: float
    quantity: int
    created_at: datetime

class ProductCreate(BaseModel):
    name: str
    model: str
    price: float
    quantity: int

class ProductUpdate(BaseModel):
    name: str
    model: str
    price: float
    quantity: int

class ProductPatch(BaseModel):
    name: Optional[str] = None
    model: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
