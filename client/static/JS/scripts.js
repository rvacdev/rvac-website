document.addEventListener('DOMContentLoaded', function () {
    // Add click event listener to the common parent container
    

    // Sample product data
    const products = [

        //START OF PRODUCT LIST
        { id: "student", name: 'Sudent/Senior Membership', price: 25.00,quantity:0 },
        { id: "individual", name: 'Individual Membership', price: 45.00,quantity:0 },
        { id: "family", name: 'Family Membership', price: 65.00,quantity:0 },
        { id: "familyLarge", name: 'Family Degas Art Lovers', price: 100.00,quantity:0 },
        { id: "corporate", name: 'Matisse Corporate', price: 250.00,quantity:0 },
        { id: "benefactor", name: 'Picasso Benefactor', price: 500.00,quantity:0 },
        { id: "sponsor", name: 'Rembrant Sponsor', price: 1000.00,quantity:0 },
        { id: "patron", name: 'Da Vinci Patron', price: 2500.00,quantity:0 },
        { id: "monet", name: 'Monet Patron', price: 5000.00,quantity:0 },
        { id: "coolArtClass", name: 'Cool Art Class', price: 50.00,quantity:0 },
        { id: 'donate', name: 'Donation', price: 0.00,quantity:0 },
        // END OF PRODUCT LIST
    ];

    // Initialize cart and total
    let cart = [];
    let total = 0.00;

    // Function to add a product to the cart
    function addToCart(productId) {
        var product = products.find(item => item.id === (productId));
        var inCart = cart.find(item => item.id === (productId));

        if (product.id==='donate'){
            inputPrice=parseFloat(document.getElementById('donationInput').value);
            if (inCart===undefined){
                product.price=inputPrice;
            }
            else{
                product.price=inputPrice+inCart.price
            }
            if (product.price===NaN){
                return 0;
            }
        } 
        if(product.price>0){
            if (inCart===undefined){
                product.quantity+=1;
                cart.push(product);
            }
            else{
                inCart.quantity+=1;
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
        const cartCounterElement = document.getElementById('cartText');


        // Clear existing cart items
        cartItemsElement.textContent = '';

        if (Array.isArray(cart) && cart.length){
            document.getElementById('empty').textContent=' ';
        }

        // Populate cart items
        cart.forEach(item => {
            li = document.createElement('li');
            li.setAttribute("id", item.id, "price", (item.price)*(item.quantity), "quantity",item.quantity);
            li.textContent = `${item.name} - ${((item.price)*(item.quantity)).toFixed(2)} - ${item.quantity}`;
            cartItemsElement.appendChild(li);

            // Add remove button
            const removeButton = document.createElement('button');
            removeButton.textContent = 'Remove';
            removeButton.addEventListener('click', () => removeFromCart(item.id));

            li.appendChild(removeButton);
            cartItemsElement.appendChild(li);
        });

        // Update total and counter
        if(cart.length>0){
            cartCounterElement.textContent=String(cart.length);
        }
        else{
            cartCounterElement.textContent='';
        }
        cartTotalElement.textContent = `${total.toFixed(2)}`;
    }
    function saveCartToLocalStorage() {
        sessionStorage.setItem('cartText', JSON.stringify(cart));
    }

    function loadCart() {
        const storedCart = sessionStorage.getItem('cartText');
        cart = storedCart ? JSON.parse(storedCart) : [];
        console.log(cart)
        total = calculateTotal();
        console.log("Total: ", total)
    }
    // Function to load the cart from localStorage
    function loadCartFromLocalStorage() {
        loadCart();
        updateCart();
    }

    // Function to calculate the total based on the current cart
    function calculateTotal() {
        return cart.reduce((acc, item) => acc + item.price, 0);
    }
    // Function to remove an item from the cart
    function removeFromCart(productId) {
        const index = cart.findIndex(item => item.id === (productId));

        if (index !== -1) {
            total -= (cart[index].price)*(cart[index].quantity);
            cart.splice(index, 1);
            if (Array.isArray(cart) && cart.length){}
            else{
                document.getElementById('empty').textContent='Your cart is Empty.';
            }
            updateCart();
            saveCartToLocalStorage();
        }
    }
    
    loadCartFromLocalStorage();

    document.addEventListener('click', function (event) {
        if (event.target.classList.contains('itemButton')) {
            // If a button with class 'itemButton' is clicked, extract the data-id attribute
            const productId = event.target.getAttribute('id');
            addToCart(productId);
        }
    });
});