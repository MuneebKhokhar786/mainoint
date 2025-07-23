
from sqlalchemy import Column, Integer, String, Decimal, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import uuid

class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    country = Column(String, nullable=True)
    zip_code = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    orders = relationship("Order", back_populates="user")

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    description = Column(Text, nullable=True)
    image = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    products = relationship("Product", back_populates="category")

class Manufacturer(Base):
    __tablename__ = "manufacturers"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    products = relationship("Product", back_populates="manufacturer")

class Product(Base):
    __tablename__ = "products"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    description = Column(Text, nullable=True)
    details = Column(Text, nullable=True)
    price = Column(Decimal(10, 2))
    price_compare_to = Column(Decimal(10, 2), nullable=True)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    category_id = Column(String, ForeignKey("categories.id"), nullable=True)
    manufacturer_id = Column(String, ForeignKey("manufacturers.id"), nullable=True)
    
    category = relationship("Category", back_populates="products")
    manufacturer = relationship("Manufacturer", back_populates="products")
    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")
    videos = relationship("ProductVideo", back_populates="product", cascade="all, delete-orphan")
    order_items = relationship("OrderItem", back_populates="product")

class ProductImage(Base):
    __tablename__ = "product_images"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    url = Column(String)
    alt = Column(String, nullable=True)
    is_primary = Column(Boolean, default=False)
    product_id = Column(String, ForeignKey("products.id"))
    created_at = Column(DateTime, server_default=func.now())
    
    product = relationship("Product", back_populates="images")

class ProductVideo(Base):
    __tablename__ = "product_videos"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    url = Column(String)
    title = Column(String, nullable=True)
    product_id = Column(String, ForeignKey("products.id"))
    created_at = Column(DateTime, server_default=func.now())
    
    product = relationship("Product", back_populates="videos")

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    total = Column(Decimal(10, 2))
    status = Column(String, default="PENDING")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    user_id = Column(String, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

class OrderItem(Base):
    __tablename__ = "order_items"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    quantity = Column(Integer)
    price = Column(Decimal(10, 2))
    created_at = Column(DateTime, server_default=func.now())
    order_id = Column(String, ForeignKey("orders.id"))
    product_id = Column(String, ForeignKey("products.id"))
    
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")
