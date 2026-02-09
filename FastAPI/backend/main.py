from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from datetime import datetime
import aiomysql

from schemas import (
    Product,
    ProductCreate,
    ProductUpdate,
    ProductPatch
)

app = FastAPI(
    title="Products API",
    description="Документація для перевірки API",
    version="1.0.0",
)
# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- DB ----------
async def get_db_connection():
    return await aiomysql.connect(
        host="127.0.0.1",
        user="root",
        password="usbw",
        db="testdb",
        port=3307,
        charset="utf8mb4",
        cursorclass=aiomysql.DictCursor,
        autocommit=True,
    )

# ---------- GET ----------
@app.get("/api/products", response_model=List[Product])
async def get_products():
    conn = await get_db_connection()
    async with conn.cursor() as cursor:
        await cursor.execute("SELECT * FROM products ORDER BY created_at")
        products = await cursor.fetchall()
    conn.close()
    return products

# ---------- POST ----------
@app.post("/api/products", status_code=201)
async def add_product(product: ProductCreate):
    conn = await get_db_connection()
    async with conn.cursor() as cursor:

        await cursor.execute("""
            SELECT id, quantity
            FROM products
            WHERE name=%s AND model=%s AND price=%s
        """, (product.name, product.model, product.price))

        existing = await cursor.fetchone()

        if existing:
            await cursor.execute("""
                UPDATE products
                SET quantity = quantity + %s
                WHERE id=%s
            """, (product.quantity, existing["id"]))
        else:
            await cursor.execute("""
                INSERT INTO products (name, model, price, quantity, created_at)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                product.name,
                product.model,
                product.price,
                product.quantity,
                datetime.utcnow()
            ))

    conn.close()
    return {"message": "Product saved"}

# ---------- PUT (повне оновлення) ----------
@app.put("/api/products/{id}")
async def update_product(id: int, product: ProductUpdate):
    conn = await get_db_connection()
    async with conn.cursor() as cursor:
        await cursor.execute("""
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

    conn.close()
    return {"message": "Product updated"}

# ---------- PATCH (часткове оновлення) ----------
@app.patch("/api/products/{id}")
async def patch_product(id: int, product: ProductPatch):
    fields = []
    values = []

    for field, value in product.dict(exclude_unset=True).items():
        fields.append(f"{field}=%s")
        values.append(value)

    if not fields:
        raise HTTPException(status_code=400, detail="No fields to update")

    query = f"""
        UPDATE products
        SET {', '.join(fields)}
        WHERE id=%s
    """

    conn = await get_db_connection()
    async with conn.cursor() as cursor:
        await cursor.execute(query, (*values, id))

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Product not found")

    conn.close()
    return {"message": "Product partially updated"}

# ---------- DELETE ----------
@app.delete("/api/products/{id}")
async def delete_product(id: int):
    conn = await get_db_connection()
    async with conn.cursor() as cursor:

        await cursor.execute(
            "SELECT quantity FROM products WHERE id=%s",
            (id,)
        )
        product = await cursor.fetchone()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        if product["quantity"] > 1:
            await cursor.execute("""
                UPDATE products
                SET quantity = quantity - 1
                WHERE id=%s
            """, (id,))
        else:
            await cursor.execute(
                "DELETE FROM products WHERE id=%s",
                (id,)
            )

    conn.close()
    return {"message": "Product deleted"}
