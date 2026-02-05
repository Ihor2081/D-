import pymysql

def get_db_connection():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="usbw",
        database="testdb",
        port=3307,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )