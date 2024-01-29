

document.addEventListener('DOMContentLoaded', function () {
    // Add click event listener to the common parent container
    

    // Sample product data
    const products = [
        { id: 1, name: 'Product 1', price: 20.00 },
        { id: 2, name: 'Product 2', price: 25.00 }
        // Add more product objects as needed
    ];

    // Initialize cart and total
    let cart = [];
    let total = 0.00;

    // Function to add a product to the cart
    function addToCart(productId) {
        const product = products.find(item => item.id === parseInt(productId));

        if (product) {
            cart.push(product);
            if (Array.isArray(cart) && cart.length){
                document.getElementById('empty').textContent=' ';
            }
            total += product.price;
    
            updateCart();
            saveCartToLocalStorage();
        }
    }

    // Function to update the cart display
    function updateCart() {
        const cartItemsElement = document.getElementById('cart-items');
        const cartTotalElement = document.getElementById('cart-total');

        // Clear existing cart items
        cartItemsElement.textContent = '';

        // Populate cart items
        cart.forEach(item => {
            li = document.createElement('li');
            li.textContent = `${item.name} - ${item.price.toFixed(2)}`;
            cartItemsElement.appendChild(li);

            // Add remove button
            const removeButton = document.createElement('button');
            removeButton.textContent = 'Remove';
            removeButton.addEventListener('click', () => removeFromCart(item.id));

            li.appendChild(removeButton);
            cartItemsElement.appendChild(li);
        });

        // Update total
        cartTotalElement.textContent = `${total.toFixed(2)}`;
    }
    function saveCartToLocalStorage() {
        localStorage.setItem('cart', JSON.stringify(cart));
    }
    // Function to load the cart from localStorage
    function loadCartFromLocalStorage() {
        const storedCart = localStorage.getItem('cart');
        cart = storedCart ? JSON.parse(storedCart) : [];
        total = calculateTotal();
        updateCart();
    }

    // Function to calculate the total based on the current cart
    function calculateTotal() {
        return cart.reduce((acc, item) => acc + item.price, 0);
    }
    // Function to remove an item from the cart
    function removeFromCart(productId) {
        const index = cart.findIndex(item => item.id === parseInt(productId));

        if (index !== -1) {
            total -= cart[index].price;
            cart.splice(index, 1);
            if (Array.isArray(cart) && cart.length){}
            else{
                document.getElementById('empty').textContent='Your cart is Empty.';
            }
            updateCart();
            saveCartToLocalStorage();
        }
    }
    

    document.addEventListener('click', function (event) {
        if (event.target.classList.contains('itemButton')) {
            // If a button with class 'itemButton' is clicked, extract the data-id attribute
            const productId = event.target.getAttribute('id');
            addToCart(productId);
        }
    });

    loadCartFromLocalStorage();

});




    




