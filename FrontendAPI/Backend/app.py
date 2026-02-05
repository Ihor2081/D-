from flask import Flask, request, jsonify
from datetime import datetime
import pymysql
from flask_cors import CORS

app = Flask(__name__)

# Дозволяємо доступ з будь-якого Frontend
CORS(app, resources={r"/api/*": {"origins": "*"}})

def get_db_connection():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='usbw',
        database='testdb',
        port=3307,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

# -------------------- GET --------------------
@app.route('/api/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products ORDER BY created_at")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(products)

# -------------------- POST --------------------
@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # 1️⃣ Перевірка на існуючий товар
    cursor.execute("""
        SELECT id, quantity
        FROM products
        WHERE name=%s AND model=%s AND price=%s
    """, (data['name'], data['model'], float(data['price'])))

    existing = cursor.fetchone()

    if existing:
        # 2️⃣ Якщо товар є — збільшуємо кількість
        new_quantity = existing['quantity'] + int(data['quantity'])

        cursor.execute("""
            UPDATE products
            SET quantity=%s
            WHERE id=%s
        """, (new_quantity, existing['id']))
    else:
        # 3️⃣ Якщо товару нема — додаємо новий
        cursor.execute("""
            INSERT INTO products (name, model, price, quantity, created_at)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            data['name'],
            data['model'],
            float(data['price']),
            int(data['quantity']),
            datetime.utcnow()
        ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Product saved"}), 201

# -------------------- PUT --------------------
@app.route('/api/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE products
        SET name=%s,
            model=%s,
            price=%s,
            quantity=%s
        WHERE id=%s
    """, (
        data['name'],
        data['model'],
        float(data['price']),
        int(data['quantity']),
        id
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Product updated"})
# -------------------- DELETE --------------------
@app.route('/api/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT quantity FROM products WHERE id=%s", (id,))
    product = cursor.fetchone()

    if not product:
        return jsonify({"error": "Not found"}), 404

    if product['quantity'] > 1:
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

    return jsonify({"message": "Product updated"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
