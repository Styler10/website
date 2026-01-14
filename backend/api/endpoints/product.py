from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.db.schemas import Product
from backend.api.models.product import ProductCreate

router = APIRouter(tags=["products"])

@router.post("/api/products")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


@router.get("/api/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
