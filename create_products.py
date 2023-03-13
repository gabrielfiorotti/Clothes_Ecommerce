import sqlite3

# create the database 
connection = sqlite3.connect("products_data.db")

# create the cursor
cursor = connection.cursor()


# first query to create the table
# command = """CREATE TABLE IF NOT EXISTS products(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     quantity INTEGER,
#     price REAL,
#     img_path TEXT)"""

# cursor.execute(command)


# cursor.execute("INSERT INTO products (name, quantity, price, img_path) VALUES ('Shirt Adidas', '200', '49', '/static/assets/shirt_adidas.svg')")
# connection.commit()


