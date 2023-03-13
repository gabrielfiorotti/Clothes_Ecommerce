import sqlite3
from datetime import datetime

# create the database 
connection = sqlite3.connect("clothes_Ecommerce.db")

# create the cursor
cursor = connection.cursor()


# queries to create tables

# user
# command1 = """CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT,
#     password TEXT)"""


# admin
command2 = """CREATE TABLE IF NOT EXISTS admins(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     username TEXT,
     password TEXT)"""


# product
# command3 = """CREATE TABLE IF NOT EXISTS products(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     quantity INTEGER,
#     price REAL,
#     img_path TEXT)"""


# orders
# command4 = """CREATE TABLE IF NOT EXISTS orders(
#     order_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     product_name TEXT,
#     order_qty INTEGER,
#     total_price REAL,
#     user_name TEXT,
#     date TEXT,
#     FOREIGN KEY (product_name) REFERENCES products(name),
#     FOREIGN KEY (user_name) REFERENCES users(name))
#     """



# cursor.execute(command4)




# ================= QUERIES ======================== #

# cursor.execute("INSERT INTO admins(username, password) VALUES ('admin', 'admin') ")

# connection.commit()