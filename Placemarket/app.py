from flask import Flask, render_template, request, redirect
from datetime import datetime
import pymysql

app = Flask(__name__)


# -------------------------------
# Підключення до MySQL (PyMySQL)
# -------------------------------
def get_db_connection():
    return pymysql.connect(
        host='127.0.0.1',   # НЕ localhost
        user='root',
        password='usbw',
        database='testdb',
        port=3307,          # 🔴 КЛЮЧОВИЙ РЯДОК
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )


# -------------------------------
# Головна сторінка
# -------------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        model = request.form['model']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])

        # шукаємо такий самий товар
        cursor.execute("""SELECT id, quantity FROM products 
            WHERE name=%s AND model=%s AND price=%s""",
            (name, model, price))

        product = cursor.fetchone()

        if product:
            cursor.execute("""
                UPDATE products
                SET quantity = quantity + %s
                WHERE id = %s
            """, (quantity, product['id']))
        else:
            cursor.execute("""
                INSERT INTO products (name, model, price, quantity, created_at)
                VALUES (%s, %s, %s, %s, %s)
            """, (name, model, price, quantity, datetime.utcnow()))

        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')

    cursor.execute("SELECT * FROM products ORDER BY created_at")
    products = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template('index.html', products=products)


# -------------------------------
# Видалення
# -------------------------------
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT quantity FROM products WHERE id=%s", (id,))
    product = cursor.fetchone()

    if product:
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
    return redirect('/')


# -------------------------------
# Оновлення
# -------------------------------
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        cursor.execute("""
            UPDATE products
            SET name=%s, model=%s, price=%s, quantity=%s
            WHERE id=%s
        """, (
            request.form['name'],
            request.form['model'],
            float(request.form['price']),
            int(request.form['quantity']),
            id
        ))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')

    cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
    product = cursor.fetchone()

    cursor.close()
    conn.close()

    if not product:
        return "Product not found"

    return render_template('update.html', product=product)


# -------------------------------
# Запуск
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)