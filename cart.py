
# SHOPPING CART MANAGEMENT SYSTEM

# 1. PRODUCT DETAILS

products = {
    1: {"Name": "TV", "Price": 20000, "Stock": 5},
    2: {"Name": "Laptop", "Price": 70000, "Stock": 2},
    3: {"Name": "Mobile", "Price": 120000, "Stock": 1},
    4: {"Name": "Headphone", "Price": 13000, "Stock": 4},
    5: {"Name": "Adapter - 45w", "Price": 1200, "Stock": 13},
    6: {"Name": "EarBuds", "Price": 1700, "Stock": 6},
    7: {"Name": "Washing Machine", "Price": 30000, "Stock": 0},
    8: {"Name": "Fridge", "Price": 24000, "Stock": 9}
}

cart = {}
order_history = []
applied_coupon = None
order_id = 1


# 2. DISPLAY PRODUCTS

def display_products():

    print("\n-------- AVAILABLE PRODUCTS --------")
    print(f"{'ID':<10}{'Name':<22}{'Price':<15}{'Stock':<10}")
    print("=" * 55)

    for product_id, item in products.items():

        available_stock = item["Stock"] - cart.get(product_id, 0)

        print(
            f"{product_id:<10}{item['Name']:<22}"
            f"{item['Price']:<15}{available_stock:<10}"
        )


# 3. ADD PRODUCTS TO CART

def add_to_cart():

    product_id = int(input("Enter the product ID: "))

    if product_id in products:

        quantity = int(input("Enter the quantity: "))

        if quantity <= 0:

            print("Please enter a quantity greater than zero")

        else:

            available_stock = products[product_id]["Stock"] - cart.get(product_id, 0)

            if available_stock <= 0:

                print("This product is out of stock")

            elif quantity > available_stock:

                print("Insufficient stock available")
                print("Available stock:", available_stock)

            else:

                cart[product_id] = cart.get(product_id, 0) + quantity

                print("Product added to cart successfully")

                print("Remaining stock:", available_stock - quantity)

    else:

        print("Invalid product ID")


# 4. REMOVE PRODUCTS FROM CART

def remove_from_cart():

    product_id = int(input("Enter the product ID to remove: "))

    if product_id in cart:

        del cart[product_id]

        print("Product removed from cart")

        print("Stock is available again")

    else:

        print("Product not found in cart")


# 5. UPDATE PRODUCT QUANTITY

def update_quantity():

    product_id = int(input("Enter the product ID: "))

    if product_id in cart:

        new_quantity = int(input("Enter the new quantity: "))

        if new_quantity < 0:

            print("Quantity cannot be negative")

        elif new_quantity == 0:

            del cart[product_id]

            print("Product removed from cart")

        elif new_quantity <= products[product_id]["Stock"]:

            cart[product_id] = new_quantity

            print("Quantity updated successfully")

        else:

            print("Insufficient stock available")
            print("Maximum available quantity:", products[product_id]["Stock"])

    else:

        print("Product not found in cart")


# 6. CALCULATE TOTAL AMOUNT

def calculate_total():

    subtotal = 0

    for product_id, quantity in cart.items():

        price = products[product_id]["Price"]

        subtotal += price * quantity

    automatic_discount = 0

    if subtotal > 5000:

        automatic_discount = subtotal * 0.10

    amount_after_discount = subtotal - automatic_discount

    coupon_discount = 0

    if applied_coupon == "SAVE5":

        coupon_discount = amount_after_discount * 0.05

    final_amount = amount_after_discount - coupon_discount

    print("\n-------- BILL SUMMARY --------")
    print("Subtotal:", subtotal)
    print("Automatic Discount:", automatic_discount)
    print("Coupon Discount:", coupon_discount)
    print("Final Payable Amount:", final_amount)

    return final_amount


# 7. APPLY DISCOUNT COUPON

def apply_coupon():

    global applied_coupon

    if not cart:

        print("Your cart is empty")

    elif applied_coupon == "SAVE5":

        print("Coupon is already applied")

    else:

        coupon = input("Enter your coupon code: ").strip().upper()

        if coupon == "SAVE5":

            applied_coupon = "SAVE5"

            print("Coupon applied successfully! 5% discount")

        else:

            print("Invalid coupon code")


# 8. VIEW SHOPPING CART

def view_cart():

    if not cart:

        print("Your cart is empty")

    else:

        print("\n-------- YOUR SHOPPING CART --------")

        for product_id, quantity in cart.items():

            name = products[product_id]["Name"]
            price = products[product_id]["Price"]
            amount = price * quantity

            print(
                name,
                "| Quantity:", quantity,
                "| Price:", price,
                "| Amount:", amount
            )

        calculate_total()


# 9. SEARCH PRODUCTS

def search_products():

    search_name = input("Enter product name to search: ").strip()

    found = False

    for product_id, item in products.items():

        if search_name.lower() in item["Name"].lower():

            available_stock = item["Stock"] - cart.get(product_id, 0)

            print(
                "ID:", product_id,
                "| Name:", item["Name"],
                "| Price:", item["Price"],
                "| Available Stock:", available_stock
            )

            found = True

    if not found:

        print("No matching products found")


# 10. CHECKOUT

def checkout():

    global order_id, applied_coupon

    if not cart:

        print("Your cart is empty")

    else:

        print("\n-------- FINAL ORDER SUMMARY --------")

        for product_id, quantity in cart.items():

            name = products[product_id]["Name"]
            price = products[product_id]["Price"]

            print(name, "|", quantity, "x", price, "=", quantity * price)

        final_amount = calculate_total()

        confirm = input("\nConfirm your order? (yes/no): ").strip().lower()

        if confirm == "yes":

            purchased_products = []

            for product_id, quantity in cart.items():

                purchased_products.append({
                    "Name": products[product_id]["Name"],
                    "Price": products[product_id]["Price"],
                    "Quantity": quantity
                })

                # Permanently reduce stock after purchase
                products[product_id]["Stock"] -= quantity

            order = {
                "Order ID": order_id,
                "Products": purchased_products,
                "Total Amount": final_amount
            }

            order_history.append(order)

            print("\nOrder placed successfully!")
            print("Your Order ID:", order_id)

            order_id += 1

            # Empty cart for the next customer
            cart.clear()

            # Reset coupon for the next customer
            applied_coupon = None

        else:

            print("Order cancelled. Your cart is unchanged")


# 11. ORDER HISTORY

def show_order_history():

    if not order_history:

        print("No previous orders found")

    else:

        print("\n-------- ORDER HISTORY --------")

        for order in order_history:

            print("\nOrder ID:", order["Order ID"])

            for item in order["Products"]:

                print(
                    item["Name"],
                    "| Quantity:", item["Quantity"],
                    "| Price:", item["Price"]
                )

            print("Total Amount:", order["Total Amount"])


# 12. MAIN MENU

while True:

    print("\n====== SHOPPING CART MANAGEMENT SYSTEM ======")

    print("1. Display Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. Update Product Quantity")
    print("5. View Shopping Cart")
    print("6. Calculate Total Amount")
    print("7. Apply Discount Coupon")
    print("8. Search Products")
    print("9. Checkout")
    print("10. Order History")
    print("11. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        display_products()

    elif choice == 2:
        add_to_cart()

    elif choice == 3:
        remove_from_cart()

    elif choice == 4:
        update_quantity()

    elif choice == 5:
        view_cart()

    elif choice == 6:
        calculate_total()

    elif choice == 7:
        apply_coupon()

    elif choice == 8:
        search_products()

    elif choice == 9:
        checkout()

    elif choice == 10:
        show_order_history()

    elif choice == 11:
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice. Please try again.")

    input("\nPress Enter to return to Main Menu")
