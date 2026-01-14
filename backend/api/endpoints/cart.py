from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.db.schemas import Product, Cart
from backend.api.models.cart import CartAdd

router = APIRouter(tags=["cart"])

@router.post("/api/cart")
def add_to_cart(item: CartAdd, db: Session = Depends(get_db)):
    cart_item = Cart(
        product_id=item.product_id,
        quantity=item.quantity or 1
    )
    db.add(cart_item)
    db.commit()

    return {"status": "ok"}


@router.get("/api/cart")
def get_cart(db: Session = Depends(get_db)):
    items = (
        db.query(
            Cart.id,
            Product.name,
            Product.price,
            Cart.quantity
        )
        .join(Product, Product.id == Cart.product_id)
        .all()
    )

    return [
        {
            "id": i.id,
            "name": i.name,
            "price": i.price,
            "quantity": i.quantity
        }
        for i in items
    ]


@router.post("/api/cart/clear")
def clear_cart(db: Session = Depends(get_db)):
    db.query(Cart).delete()
    db.commit()
    return {"status": "cleared"}
