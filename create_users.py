import sqlite3

# create the database 
connection = sqlite3.connect("user_data.db")

# create the cursor
cursor = connection.cursor()


# first query to create the table
# command = """CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT,
#     password TEXT)"""

# cursor.execute(command)


# --------------------------- NOTES -------------------------- #


# SEQUENCE IS:
# cursor.execute("queryQueVcQuiser")
# connection.commit()
# run in the terminal: python3 nomeDoArquivo.py


# keep all the queries you already used in comment, because if you run the terminal it will run again.
# without comment you leave just the query you want to run in the moment.


# add row
# cursor.execute("INSERT INTO users (username, password) VALUES ('teste3', '1234')")
# connection.commit()


# delete row
# cursor.execute("DELETE FROM users WHERE id=5")
# connection.commit()



# -------------------------- QUERIES ------------------------- #

# cursor.execute("INSERT INTO users (username, password) VALUES ('gabrielfiorotti', '102033') ")
# connection.commit()


# cursor.execute("""CREATE TABLE IF NOT EXISTS admins(
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      username TEXT,
#      password TEXT)""")


# cursor.execute("INSERT INTO admins (username, password) VALUES ('admin', 'admin') ")
# connection.commit()