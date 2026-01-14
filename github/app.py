from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


# @app.route('/', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         task_content = request.form['content']
#         new_task = Todo(content=task_content)
#
#         try:
#             db.session.add(new_task)
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue adding your task'
#
#     else:
#         tasks = Todo.query.order_by(Todo.date_created).all()
#         return render_template('index.html', tasks=tasks)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])

        # 🔍 Шукаємо такий самий товар
        product = Product.query.filter_by(name=name, price=price).first()

        if product:
            # ➕ Якщо існує — збільшуємо кількість
            product.quantity += quantity
        else:
            # ➕ Якщо ні — створюємо новий
            product = Product(
                name=name,
                price=price,
                quantity=quantity
            )
            db.session.add(product)

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Помилка при додаванні товару'

    products = Product.query.order_by(Product.created_at).all()
    return render_template('index.html', products=products)@app.route('/delete/<int:id>')

def delete(id):
    product = Product.query.get_or_404(id)

    try:
        if product.quantity > 1:
            product.quantity -= 1
        else:
            db.session.delete(product)

        db.session.commit()
        return redirect('/')
    except:
        return 'Помилка при видаленні товару'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)