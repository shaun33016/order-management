from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrderBase(BaseModel):
    customer_name: str
    item_name: str
    quantity: int
    status: Optional[str] = "pending"

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class OrderOut(OrderBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class OrderUpdate(BaseModel):
    status: str