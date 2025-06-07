from sqlalchemy.orm import Session
from . import models, schemas

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def list_orders(db: Session, skip: int = 0, limit: int = 10, status: str = None, customer_name: str = None):
    query = db.query(models.Order)
    if status:
        query = query.filter(models.Order.status == status)
    if customer_name:
        query = query.filter(models.Order.customer_name == customer_name)
    return query.offset(skip).limit(limit).all()

def update_order_status(db: Session, order_id: int, status: str):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if order:
        order.status = status
        db.commit()
        db.refresh(order)
    return order

# Error messages
from fastapi import HTTPException
from app.models import Order

def get_order(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order