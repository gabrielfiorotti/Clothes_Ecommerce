
// change the content in the screen when you click on the sidebar options


let option_products = window.document.querySelector('.option1')
let option_users = window.document.querySelector('.option2')
let option_orders = window.document.querySelector('.option3')

let manage_products = window.document.querySelector('.manage_products')
let manage_users = window.document.querySelector('.manage_users')
let manage_orders = window.document.querySelector('.manage_orders')



// ============ PRODUCTS =========================


function productsSelected()
{
    option_products.classList.add("isActive");
    option_users.classList.remove("isActive");
    option_orders.classList.remove("isActive");

    manage_products.style.display = 'flex';
    manage_users.style.display = 'none';
    manage_orders.style.display = 'none';
}


let features = window.document.querySelector('.add_features')

let newProduct = window.document.querySelector('#newProduct')

let newQuantity = window.document.querySelector('#newQuantity')


// hide and show features to the products panel
function featureNewProduct()
{
    newProduct.style.display = 'block';
    newQuantity.style.display = 'none';
}

function featureNewQuantity()
{
    newProduct.style.display = 'none';
    newQuantity.style.display = 'block';
}






// ============ USERS =========================

function usersSelected()
{
    option_products.classList.remove("isActive");
    option_users.classList.add("isActive");
    option_orders.classList.remove("isActive");


    manage_products.style.display = 'none';
    manage_users.style.display = 'flex';
    manage_orders.style.display = 'none';
}




// ============ ORDERS  =========================

function ordersSelected()
{
    option_products.classList.remove("isActive");
    option_users.classList.remove("isActive");
    option_orders.classList.add("isActive");

    manage_products.style.display = 'none';
    manage_users.style.display = 'none';
    manage_orders.style.display = 'flex';
}