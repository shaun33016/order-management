from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
from fastapi import Query

# Ensure tables are created
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)

@app.get("/orders/{order_id}", response_model=schemas.OrderOut)
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = crud.get_order(db, order_id)
    return order

@app.get("/orders/", response_model=list[schemas.OrderOut])
def list_orders(
    skip: int = 0,
    limit: int = 10,
    status: str = Query(None),
    customer_name: str = Query(None),
    db: Session = Depends(get_db)
):
    orders = crud.list_orders(db, skip=skip, limit=limit, status=status, customer_name=customer_name)
# Add error message
    if not orders:
        raise HTTPException(status_code=404, detail="No matching orders found.")
    return orders


@app.put("/orders/{order_id}", response_model=schemas.OrderOut)
def update_status(order_id: int, update: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order = crud.update_order_status(db, order_id, update.status)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order