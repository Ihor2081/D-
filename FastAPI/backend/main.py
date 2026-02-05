from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from datetime import datetime

from database import get_db_connection
from schemas import Product, ProductCreate, ProductUpdate

app = FastAPI(title="Products API")

# CORS — щоб Frontend працював
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/products", response_model=List[Product])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products ORDER BY created_at")
    products = cursor.fetchall()

    cursor.close()
    conn.close()
    return products

@app.post("/api/products", status_code=201)
def add_product(product: ProductCreate):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, quantity
        FROM products
        WHERE name=%s AND model=%s AND price=%s
    """, (product.name, product.model, product.price))

    existing = cursor.fetchone()

    if existing:
        cursor.execute("""
            UPDATE products
            SET quantity = quantity + %s
            WHERE id = %s
        """, (product.quantity, existing["id"]))
    else:
        cursor.execute("""
            INSERT INTO products (name, model, price, quantity, created_at)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            product.name,
            product.model,
            product.price,
            product.quantity,
            datetime.utcnow()
        ))

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Product saved"}


@app.put("/api/products/{id}")
def update_product(id: int, product: ProductUpdate):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE products
        SET name=%s, model=%s, price=%s, quantity=%s
        WHERE id=%s
    """, (
        product.name,
        product.model,
        product.price,
        product.quantity,
        id
    ))

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Product updated"}

@app.delete("/api/products/{id}")
def delete_product(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT quantity FROM products WHERE id=%s", (id,))
    product = cursor.fetchone()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product["quantity"] > 1:
        cursor.execute("""
            UPDATE products
            SET quantity = quantity - 1
            WHERE id=%s
        """, (id,))
    else:
        cursor.execute("DELETE FROM products WHERE id=%s", (id,))

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Product updated"}