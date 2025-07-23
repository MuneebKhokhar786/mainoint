
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Order, OrderItem, Product, User
from schemas import Order as OrderSchema, OrderCreate
from routers.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[OrderSchema])
def get_orders(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.is_staff:
        orders = db.query(Order).offset(skip).limit(limit).all()
    else:
        orders = db.query(Order).filter(Order.user_id == current_user.id).offset(skip).limit(limit).all()
    return orders

@router.get("/{order_id}", response_model=OrderSchema)
def get_order(
    order_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    if not current_user.is_staff and order.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    return order

@router.post("/", response_model=OrderSchema)
def create_order(
    order_data: OrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Calculate total
    total = sum(item.price * item.quantity for item in order_data.items)
    
    # Create order
    db_order = Order(
        user_id=current_user.id,
        total=total
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
    # Create order items
    for item_data in order_data.items:
        # Verify product exists
        product = db.query(Product).filter(Product.id == item_data.product_id).first()
        if not product:
            db.delete(db_order)
            db.commit()
            raise HTTPException(status_code=404, detail=f"Product {item_data.product_id} not found")
        
        db_item = OrderItem(
            order_id=db_order.id,
            product_id=item_data.product_id,
            quantity=item_data.quantity,
            price=item_data.price
        )
        db.add(db_item)
    
    db.commit()
    db.refresh(db_order)
    return db_order
