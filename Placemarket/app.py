from flask import Flask, render_template, request, redirect
from datetime import datetime
import json
import os

app = Flask(__name__)
FILE_NAME = 'products.json'


# -------------------------------
# Функції для роботи з файлом
# -------------------------------
def load_products():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_products(products):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=4, ensure_ascii=False)


def get_next_id(products):
    if not products:
        return 1
    return max(p['id'] for p in products) + 1


# -------------------------------
# Головна сторінка
# -------------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    products = load_products()

    if request.method == 'POST':
        name = request.form['name']
        model = request.form['model']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])

        # шукаємо такий самий товар
        found = None
        for p in products:
            if p['name'] == name and p['model'] == model and p['price'] == price:
                found = p
                break

        if found:
            found['quantity'] += quantity
        else:
            new_product = {
                'id': get_next_id(products),
                'name': name,
                'model': model,
                'price': price,
                'quantity': quantity,
                'created_at': datetime.utcnow().isoformat()
            }
            products.append(new_product)

        save_products(products)
        return redirect('/')

    # сортуємо по даті створення
    products.sort(key=lambda x: x['created_at'])
    return render_template('index.html', products=products)


# -------------------------------
# Видалення
# -------------------------------
@app.route('/delete/<int:id>')
def delete(id):
    products = load_products()
    for p in products:
        if p['id'] == id:
            if p['quantity'] > 1:
                p['quantity'] -= 1
            else:
                products.remove(p)
            break
    save_products(products)
    return redirect('/')


# -------------------------------
# Оновлення
# -------------------------------
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    products = load_products()
    product = next((p for p in products if p['id'] == id), None)
    if not product:
        return 'Product not found'

    if request.method == 'POST':
        product['name'] = request.form['name']
        product['model'] = request.form['model']
        product['price'] = float(request.form['price'])
        product['quantity'] = int(request.form['quantity'])
        save_products(products)
        return redirect('/')

    return render_template('update.html', product=product)


if __name__ == "__main__":
    app.run(debug=True)
