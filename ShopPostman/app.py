from flask import Flask, request, jsonify, render_template
from datetime import datetime
import pymysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # дозволяє доступ з HTML / Postman

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

@app.route('/')
def index():
    return render_template('products.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products ORDER BY created_at")
    products = cursor.fetchall()

    cursor.close()
    conn.close()
    return jsonify(products), 200

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()

    required = ['name', 'model', 'price', 'quantity']
    if not all(k in data for k in required):
        return jsonify({"error": "Missing fields"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

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

    return jsonify({"message": "Product added"}), 201

@app.route('/api/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE products
        SET name=%s, model=%s, price=%s, quantity=%s
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

    return jsonify({"message": "Product updated"}), 200

@app.route('/api/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products WHERE id=%s", (id,))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Product deleted"}), 200

# ------------------------------- # Запуск # -------------------------------
if __name__ == "__main__":
    app.run(debug=True)