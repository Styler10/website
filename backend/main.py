from fastapi import FastAPI, Request, UploadFile, File, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from backend.db.schemas import Product
from pathlib import Path
from uuid import uuid4
import shutil

from backend.db.database import get_db
from backend.api.endpoints import product, cart

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI()

# API
app.include_router(product.router)
app.include_router(cart.router)

# Templates & static
templates = Jinja2Templates(directory=BASE_DIR / "frontend" / "templates")

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "frontend" / "static"),
    name="static"
)

# Pages
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.get("/products", response_class=HTMLResponse)
def products_page(request: Request):
    return templates.TemplateResponse(
        "products.html",
        {"request": request}
    )

@app.get("/cart", response_class=HTMLResponse)
def cart_page(request: Request):
    return templates.TemplateResponse(
        "cart.html",
        {"request": request}
    )

@app.get("/products/add")
def add_product_page(request: Request):
    return templates.TemplateResponse(
        "add_product.html",
        {"request": request}
    )

@app.post("/products/add")
def add_product_form(
    name: str = Form(...),
    price: float = Form(...),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    image_path = None

    if image and image.filename:
        ext = image.filename.split(".")[-1]
        filename = f"{uuid4()}.{ext}"
        save_path = BASE_DIR / "frontend" / "static" / "img" / filename

        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        image_path = f"/static/img/{filename}"

    product = Product(
        name=name,
        price=price,
        image=image_path
    )

    db.add(product)
    db.commit()

    return RedirectResponse("/", status_code=303)