from flask import Flask, render_template, request
import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    port=3307,
    database="testdb",
    user="root",
    password="mysql"
)

cursor = connection.cursor()
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/products')
def products():
    cursor.execute("select * from products")
    value=cursor.fetchall()
    return render_template('products.html', value=value)

