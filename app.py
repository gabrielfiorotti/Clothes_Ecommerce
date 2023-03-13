from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_session import Session
import sqlite3 
from datetime import datetime

# Clothes E-Commerce
# A sports clothes e-commerce web application, with both user and admin interfaces.

# setup Flask
app = Flask(__name__, static_folder='static')
app.secret_key = 'g4D04fhWTv'
# I generate some secret key in a website(https://randomkeygen.com/)



# setup Session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/")
def index():
    
    # check if the user is logged in
    if "username" in session:

        connection = sqlite3.connect('clothes_Ecommerce.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM products')

        products = cursor.fetchall()

        connection.close()

        return render_template("homepage.html", css_file='css/homepage.css', products_database = products)

    else:
        return redirect("/login")
        




@app.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        # SQLite
        connection = sqlite3.connect('clothes_Ecommerce.db')
        cursor = connection.cursor()

        # HTML Form
        getUsername = request.form['username']
        getPassword = request.form['password']

        

        # check if all fields were provided
        if not getUsername or not getPassword:
            return render_template("fail_fields_users.html", css_file='css/error.css')
        
        
        # Query
        query = "SELECT username, password FROM users WHERE username='"+getUsername+"' and password='"+getPassword+"' "

        cursor.execute(query)

        # query the table data to SQLite and store the result in a variable only if what the user typed is == what is stored in the DB.

        results = cursor.fetchall()
        
        
        # validation
        if len(results) == 0:
            return render_template("fail_login_users.html", css_file='css/error.css')
        else:
            # store session information
            session['username'] = getUsername
            return redirect("/")


    else:    
        return render_template("login_user.html", css_file='css/login_user.css')





@app.route("/logout")
def logout():

    session.pop("username", None)
    session.pop("adminUsername", None)
    session.pop("cart", None)


    return redirect(url_for("index"))





@app.route("/register", methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        # SQLite
        connection = sqlite3.connect('clothes_Ecommerce.db')
        cursor = connection.cursor()

        # HTML Form
        createUsername = request.form['username']
        createPassword = request.form['password']
        confirmation = request.form['confirmation']
        
        # check if all the fields were provided
        if not createUsername or not createPassword or not confirmation:
            return render_template("fail_fields_register.html", css_file='css/error.css')

        # check if passwords match
        if confirmation != createPassword:
            return render_template("fail_password.html", css_file='css/error.css')


        # check for usernames in the DB
        cursor.execute("SELECT username FROM users WHERE username='"+createUsername+"' ")
        
        results = cursor.fetchall()

        # check if username already exists  
        if len(results) == 1:
            return render_template("fail_username.html", css_file='css/error.css')
        
        # when everything is right:
        else:
            
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (createUsername, createPassword))

            connection.commit()

            return redirect("/")
            

    # if request.method == 'GET'
    else:
        return render_template("register.html", css_file='css/register.css')






@app.route("/login_admin", methods=['GET', 'POST'])
def login_admin():

    if request.method == 'POST':

        # SQLite
        connection = sqlite3.connect('clothes_Ecommerce.db')
        cursor = connection.cursor()

        # HTML Form
        username = request.form['adminUsername']
        password = request.form['adminPassword']
        
        
        # check if all fields were provided
        if not username or not password:
            return render_template("fail_fields_admin.html", css_file='css/error.css')


        # Query
        query = "SELECT username, password FROM admins WHERE username='"+username+"' and password='"+password+"' "

        cursor.execute(query)

        # query the table data to SQLite and store the result in a variable only if what the user typed is == what is stored in the DB.

        resultsAdmin = cursor.fetchall()
        
        # validation
        if len(resultsAdmin) == 0:
            return render_template("fail_login_admin.html", css_file='css/error.css')
        else:
            # store in session
            session['adminUsername'] = username
            return redirect("/admin_panel")


    else:
        return render_template("login_admin.html", css_file='css/login_admin.css')




@app.route("/admin_panel", methods=['GET', 'POST'])
def admin_panel():

    if request.method == 'POST':
        
        # Checking if the field 'newProduct' is in the object request.form
        # If it is, it means that data from form1 were send.
        if 'newProduct' in request.form:
            # SQLite
            connection = sqlite3.connect('clothes_Ecommerce.db')
            cursor = connection.cursor()

            # add new products 
            newProduct = request.form["newProduct"]
            quantity = request.form["quantity"]
            price = request.form["price"]
            img_path = request.form["img_path"]

            # insert into DB
            cursor.execute("INSERT INTO products (name, quantity, price, img_path) VALUES (?, ?, ?, ?)", (newProduct, quantity, price, img_path))

            connection.commit()
            connection.close()

            return redirect(url_for('admin_panel'))


        # Checking if the field 'newQuantity' is in the object request.form
        # If it is, it means that data from form2 were send.
        elif 'newQuantity' in request.form:

            # SQLite
            connection = sqlite3.connect('clothes_Ecommerce.db')
            cursor = connection.cursor()

            # add quantity
            productName = request.form["productName"]
            newQuantity = request.form["newQuantity"]

            # update into DB
            cursor.execute("UPDATE products SET quantity=? WHERE name=?", (newQuantity, productName))

            connection.commit()
            connection.close()

            return redirect(url_for('admin_panel'))



    # check if the admin is logged in
    if "adminUsername" in session:

        # show tables when logged in

        # SQLite
        connection = sqlite3.connect("clothes_Ecommerce.db")

        cursor = connection.cursor()


        # Store all the products information from the DB into a variable
        products = cursor.execute("SELECT * FROM products")
        # results list
        products_results = products.fetchall()


        # Store all the products information from the DB into a variable
        users = cursor.execute("SELECT * FROM users")
        # results list
        users_results = users.fetchall()

        # store all orders information from DB
        orders = cursor.execute("SELECT * FROM orders")
        orders_result = orders.fetchall()

        # Close the connection with DB
        connection.close()
        
        return render_template("admin_panel.html", css_file='css/admin_panel.css', products_database = products_results, users_database = users_results, orders_database = orders_result)

    else:
        return redirect("/login_admin")




# route disabled 

# @app.route("/delete_product", methods=['GET', 'POST'])
# def delete_product():

#     if request.method == "POST":
#         # connect SQL
#         connection = sqlite3.connect("clothes_Ecommerce.db")
#         cursor = connection.cursor()

#         getProduct = request.form["product_id"]

#         cursor.execute("DELETE FROM products WHERE id=:id", {"id": getProduct})

#         connection.commit()

#         return redirect("/admin_panel")




# route disabled 

# @app.route("/delete_user", methods=['GET', 'POST'])
# def delete_user():

#     if request.method == "POST":
#         # connect SQL
#         connection = sqlite3.connect("clothes_Ecommerce.db")
#         cursor = connection.cursor()

#         getUser = request.form["user_id"]

#         cursor.execute("DELETE FROM users WHERE id=:id", {"id": getUser})

#         connection.commit()

#         return redirect("/admin_panel")





@app.route('/cart', methods=['GET', 'POST'])
def cart():

    # check if the user is logged in
    if 'username' not in session:
        return redirect("/login")
    


    cart = session.get('cart', {})
    cart_items = []
    total = 0
    
    # connect SQL
    connection = sqlite3.connect("clothes_Ecommerce.db")
    cursor = connection.cursor()
    
    for product_id, quantity in cart.items():

        # get data from DB
        query = cursor.execute("SELECT * FROM products WHERE id =?", product_id)
        product = query.fetchone()
        
        # transform the data into a list
        product_as_list = list(product)

        # get the price of each product and calculate the subtotal
        subtotal = product_as_list[3] * quantity

        cart_items.append({
            'image_directory': product_as_list[4], 
            'name': product_as_list[1],
            'quantity': quantity,
            'subtotal': subtotal,
            'id': product_as_list[0]
        })

        total += subtotal
            
    return render_template('cart.html', css_file='css/cart.css',cart_items=cart_items, total=total)



    

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():

    # get the ID of the product that the user has clicked on the HTML form
    product_id = request.form['product_id']

    # get the cart
    cart = session.get('cart', {})

    # add the product
    cart[product_id] = cart.get(product_id, 0) + 1
    # get() prototype:
    # get(key, default=None, type=None)


    # update cart
    session['cart'] = cart

    return redirect("/#man")



@app.route('/clear_cart', methods=['GET', 'POST'])
def clear_cart():

    session.pop("cart", None)

    return redirect("/cart")





@app.route("/buy", methods=['GET', 'POST'])
def buy():

    if request.method == "POST":
        
        # get the session[username] that bought
        username = request.form["username"]

        # get all the products
        product_names = request.form.getlist("product_name[]")

        # get all the qty of products
        order_qtys = request.form.getlist("product_qty[]")

        # get the subtotal
        subtotals = request.form.getlist("subtotal[]")

        # get the datetime
        date = datetime.now()

        # format the date
        date_formated = date.strftime('%Y-%m-%d %H:%M:%S')

        # connect SQL
        connection = sqlite3.connect("clothes_Ecommerce.db")
        cursor = connection.cursor()

        # get the stock of itens

        for product_name, order_qty, subtotal in zip(product_names, order_qtys, subtotals):


            # get the current quantity of each item
            query = cursor.execute("SELECT quantity FROM products WHERE name=?", (product_name,))

            current_qty = query.fetchone()[0]
            
            # get the new quantity after the user purchase
            new_qty = current_qty - int(order_qty)

            # validation of stock qty
            if new_qty < 0:
                return render_template("fail_buy.html", css_file='css/fail_buy.css')
            else:

                # update DB tables
                cursor.execute("INSERT INTO orders (product_name, order_qty, total_price, user_name, date) VALUES (?, ?, ?, ?, ?)", (product_name, order_qty, subtotal, username, date_formated))

                cursor.execute("UPDATE products SET quantity=? WHERE name=?", (new_qty, product_name))

                # clear cart
                session.pop("cart", None)

        connection.commit()
        connection.close()
            

        return render_template("success_buy.html", css_file='css/success_buy.css')
    
    return redirect(url_for('cart'))






@app.route("/my_orders")
def my_orders():

    # check if the user is logged in
    if 'username' not in session:
        return redirect("/login")
    
    # get the username
    username = session['username']

    # connect SQL
    connection = sqlite3.connect("clothes_Ecommerce.db")
    cursor = connection.cursor()

    # get all the information I want
    users_orders = cursor.execute("SELECT * FROM orders WHERE user_name = ? ", (username,))

    # transform into a tuple
    users_orders_result = users_orders.fetchall()

    print(users_orders_result)

    # return "teste"
    return render_template("my_orders.html", css_file='css/my_orders.css', user_orders = users_orders_result) 
    


















if __name__ == "__main__":
    app.run(debug=True)

