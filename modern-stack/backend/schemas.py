
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from decimal import Decimal
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    zip_code: Optional[str] = None
    phone_number: Optional[str] = None

class User(UserBase):
    id: str
    is_active: bool
    is_staff: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Product schemas
class ProductImageBase(BaseModel):
    url: str
    alt: Optional[str] = None
    is_primary: bool = False

class ProductImage(ProductImageBase):
    id: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    details: Optional[str] = None
    price: Decimal
    price_compare_to: Optional[Decimal] = None
    slug: str
    is_active: bool = True

class ProductCreate(ProductBase):
    category_id: Optional[str] = None
    manufacturer_id: Optional[str] = None

class Product(ProductBase):
    id: str
    created_at: datetime
    updated_at: datetime
    images: List[ProductImage] = []
    
    class Config:
        from_attributes = True

# Category schemas
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    image: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# Order schemas
class OrderItemBase(BaseModel):
    quantity: int
    price: Decimal
    product_id: str

class OrderItem(OrderItemBase):
    id: str
    product: Product
    
    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    total: Decimal
    status: str = "PENDING"

class OrderCreate(BaseModel):
    items: List[OrderItemBase]

class Order(OrderBase):
    id: str
    created_at: datetime
    items: List[OrderItem] = []
    
    class Config:
        from_attributes = True

# Auth schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
