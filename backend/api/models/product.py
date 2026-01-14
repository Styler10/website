from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    image: str

class Product(ProductCreate):
    id: int
