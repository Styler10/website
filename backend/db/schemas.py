from sqlalchemy import Column, Integer, String, Float, ForeignKey
from backend.db.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    image = Column(String, default="")


class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, default=1)
