function loadCartFromLocalStorage() {
  loadCart();
  updateCart();
}

function calculateTotal() {
  return cart.reduce((acc, item) => acc + item.price, 0);
}

function loadCart() {
  const storedCart = sessionStorage.getItem("cartText");
  cart = storedCart ? JSON.parse(storedCart) : [];
  console.log(cart);
  total = calculateTotal();
  console.log("Total: ", total);
}

function updateCart() {
  const cartItemsElement = document.getElementById("cart-items");
  const cartTotalElement = document.getElementById("cart-total");
  const cartCounterElement = document.getElementById("cartText");

  // Clear existing cart items
  cartItemsElement.textContent = "";

  if (Array.isArray(cart) && cart.length) {
    document.getElementById("empty").textContent = " ";
  }

  // Populate cart items
  cart.forEach((item) => {
    li = document.createElement("li");
    li.setAttribute("id", item.id, "price", item.price * item.quantity, "quantity", item.quantity);
    li.textContent = `${item.name} - ${(item.price * item.quantity).toFixed(2)} - ${item.quantity}`;
    cartItemsElement.appendChild(li);

    // Add remove button
    const removeButton = document.createElement("button");
    removeButton.textContent = "Remove";
    removeButton.addEventListener("click", () => removeFromCart(item.id));

    li.appendChild(removeButton);
    cartItemsElement.appendChild(li);
  });

  // Update total and counter
  if (cart.length > 0) {
    cartCounterElement.textContent = String(cart.length);
  } else {
    cartCounterElement.textContent = "";
  }
  cartTotalElement.textContent = `${total.toFixed(2)}`;
}

window.paypal
  .Buttons({
    style: {
      shape: "rect",
      layout: "vertical",
    },
    async createOrder() {
      // Assuming 'cart' is an array of items where each item has 'id', 'price', and 'quantity'
      loadCartFromLocalStorage(); // Load the cart from local storage or any other source
      console.log("Cart: ", cart);
      const items = cart.map((item) => ({ id: item.id, quantity: item.quantity, amount: item.price }));
      const total = items.reduce((acc, item) => acc + item.amount * item.quantity, 0).toFixed(2); // Calculate the total

      try {
        const response = await fetch("/api/orders", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            cart: items,
            total: total, // You might need to adjust your Flask route to handle the total
          }),
        });

        const orderData = await response.json();

        if (orderData.id) {
          return orderData.id;
        } else {
          throw new Error("Failed to create order.");
        }
      } catch (error) {
        console.error("Create order error:", error);
        alert("Error creating the order. Please try again.");
      }
    },
    async onApprove(data, actions) {
      try {
        const response = await fetch(`/api/orders/${data.orderID}/capture`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
        });

        const orderData = await response.json();
        // Three cases to handle:
        //   (1) Recoverable INSTRUMENT_DECLINED -> call actions.restart()
        //   (2) Other non-recoverable errors -> Show a failure message
        //   (3) Successful transaction -> Show confirmation or thank you message

        const errorDetail = orderData?.details?.[0];

        if (errorDetail?.issue === "INSTRUMENT_DECLINED") {
          // (1) Recoverable INSTRUMENT_DECLINED -> call actions.restart()
          // recoverable state, per https://developer.paypal.com/docs/checkout/standard/customize/handle-funding-failures/
          return actions.restart();
        } else if (errorDetail) {
          // (2) Other non-recoverable errors -> Show a failure message
          throw new Error(`${errorDetail.description} (${orderData.debug_id})`);
        } else if (!orderData.purchase_units) {
          throw new Error(JSON.stringify(orderData));
        } else {
          // (3) Successful transaction -> Show confirmation or thank you message
          // Or go to another URL:  actions.redirect('thank_you.html');
          const transaction = orderData?.purchase_units?.[0]?.payments?.captures?.[0] || orderData?.purchase_units?.[0]?.payments?.authorizations?.[0];
          resultMessage(`Transaction ${transaction.status}: ${transaction.id}<br><br>See console for all available details`);
          console.log("Capture result", orderData, JSON.stringify(orderData, null, 2));
        }
      } catch (error) {
        console.error(error);
        resultMessage(`Sorry, your transaction could not be processed...<br><br>${error}`);
      }
    },
  })
  .render("#paypal-button-container");

// Example function to show a result to the user. Your site's UI library can be used instead.
function resultMessage(message) {
  const container = document.querySelector("#result-message");
  container.innerHTML = message;
}
