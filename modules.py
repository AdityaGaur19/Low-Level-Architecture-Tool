def detect_modules(requirement_text):
    # Basic keyword-based module detection for demo purposes
    modules = []
    text = requirement_text.lower()
    if "user" in text or "auth" in text or "login" in text:
        modules.append("User Authentication")
    if "product" in text or "catalog" in text:
        modules.append("Product Catalog")
    if "order" in text:
        modules.append("Order Management")
    if "cart" in text:
        modules.append("Shopping Cart")
    if "payment" in text or "checkout" in text:
        modules.append("Payment Processing")
    return modules

def generate_schema(modules):
    schema = []
    for module in modules:
        if module == "User Authentication":
            schema.append(
                """CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT,
    email TEXT UNIQUE
);"""
            )
        if module == "Product Catalog":
            schema.append(
                """CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    price REAL,
    stock INTEGER
);"""
            )
        if module == "Order Management":
            schema.append(
                """CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    order_date TEXT,
    total REAL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);"""
            )
        if module == "Shopping Cart":
            schema.append(
                """CREATE TABLE cart_items (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
);"""
            )
        if module == "Payment Processing":
            schema.append(
                """CREATE TABLE payments (
    id INTEGER PRIMARY KEY,
    order_id INTEGER,
    payment_method TEXT,
    payment_date TEXT,
    amount REAL,
    FOREIGN KEY(order_id) REFERENCES orders(id)
);"""
            )
    return "\n\n".join(schema)

def generate_pseudocode(modules):
    # Example: Order placement
    if "Order Management" in modules and "Shopping Cart" in modules:
        return """
# Pseudocode: Place an Order

1. User adds items to Cart
2. User proceeds to Checkout
3. System verifies stock for each Cart item
4. If all items available:
    a. Create new Order entry
    b. Deduct item stock from Products
    c. Create Payment entry
    d. Clear Cart
    e. Return order confirmation
5. Else:
    a. Inform user about out of stock items
"""
    else:
        return "# Pseudocode generation is context-dependent on modules."