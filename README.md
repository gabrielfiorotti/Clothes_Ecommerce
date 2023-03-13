# CLOTHES E-Commerce

#### Video Demo: https://www.youtube.com/watch?v=eBy-MJG4fH4

#### Description:
    This is my final project for CS50x course: a sports clothes e-commerce web application.

<img src="/static/assets/readme_banner.png">

- **Step 1: Design**

I started with the creative and design part of the whole project by using **Figma** to create mock ups and all the fundamental design structures, including a logo for the store, each page of the application and the products that would be commercialized.
<br><br>

- **Step 2: Stacks**

With my previous background and the knowledge acquired during the course, I decided the stacks of the project, as follows:
<br>
*Back-end:* **Python, Flask and SQLite.**
<br>
*Front-end:* **HTML, CSS and JavaScript.**
<br><br>
    
- **Step 3: The project itself**
    
The project consists in a web application e-commerce. I wanted to create something that could be useful for clients and users in general, but also dedicate much effort in an admin interface that could easily manage the store.
<br>
<br>
When you first enter into the project, the user is prompted for his username and password credentials. If you don't have one, just follow the link indicated for the register route. The application does some interaction with the database and store the credentials for user's log in and uses Flask session.
<br>
Sessions use a unique id to retrieve the stored values. Whenever a session is created, a cookie containing the unique session id is stored on the user’s computer and is returned with every request to the server.
When the user revisits the site, he returns the Cookie containing the session ID. The server then reads the session ID and retrieves the corresponding session data.
<br>
<br>
In sequence, the user get into the homepage of the store. The header indicates 3 sections: Man, Woman and Kids. For now, just "Man Section" it's available, for example purposes only.
Scrolling down the page, all the products available shows up and the user can choose what he/she likes and add them to cart. Each user has his own cart, also developed with Flask session. 
<br>
When the user click in the Cart button, all the items selected are in a list and you can just "buy" all the products selected. At the same time, an order is generated and added to the "orders" table in the database.
<br>
In addition, the user can see all the orders that he has done in the store. This is possible with a interaction with database "orders" table, getting all the information stored for the validation where username is equal to the username that is logged in.
<br>
<br>
On the other hand, in the log in page, there is also a button that goes to the admin's route. Admin have access to the admin panel, where products, users and orders can be managed.
<br>
<br>
In "Manage Products" you can add a new one, remove some product available or update the stock quantity stored in database.
<br>
<br>
In "Manage Users", you can see all the users registered in the site, with a unique ID and username. Passwords are not shown for security and privacy. Originally, admin could also delete any user registered, but I remove this feature because I am sharing the admin's credentials further in this document, and someone could maliciously delete some user account.
<br>
<br>
In "Manage Orders", all orders placed by customers are stored in the database with the following data: id, name of the product, how many items of each product, total purchase price, witch username ordered and the date/time that the order was made.
<br>
<br>
Admin's Credentials:
username: *admin* | password: *admin*
<br>
<br>
***NOTE: PLEASE, don't delete or add any products or users! I am sharing the admin's credentials with anyone that may have some interest to check inside this part of the application.***


