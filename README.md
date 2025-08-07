# 🧱 Low Level Architecture Generator

## 🚀 Project Overview  
This is a web-based blueprint generation tool designed to turn plain English software requirements into **technical architecture** in seconds.  
Built using **Python** and **Streamlit** (developed on VS Code), the application helps developers, analysts, and students generate:

🔹 Relevant software modules  
🔹 SQL database schemas  
🔹 Pseudocode for core functionalities  

Think of it as your instant **technical architect** — no prior coding needed for inputs!

---

## 🛠️ Key Features

📝 **Natural Language Input**  
Just write what you want your software to do — no coding, no formatting.

🧩 **Module Detection**  
Automatically identifies standard modules based on your input, such as:  
- 🔐 User Authentication  
- 🛍️ Product Catalog  
- 📦 Order Management  
- 🛒 Shopping Cart  
- 💳 Payment Processing

🗃️ **Database Schema Generation**  
For every module, the app outputs ready-to-use SQL tables with meaningful fields and foreign key relationships:  
- `users` – for login and registration  
- `products` – for inventory/catalog  
- `orders` – to manage transactions  
- `cart_items` – to handle shopping cart logic  
- `payments` – for tracking completed orders  

💡 **Pseudocode Output**  
Visualize how your system would operate with high-level logic steps.  
For example, placing an order would involve:
- Adding items to cart  
- Verifying stock  
- Creating an order  
- Processing payment  
- Clearing the cart

🌐 **Interactive Streamlit UI**  
No terminal needed — open the app in your browser, paste your requirement, and watch the technical structure appear!

---

## 🔍 How It Works

1. 💬 User inputs a requirement like:  
   `"Build an app where users can register, view items, and place orders"`

2. 🧠 App detects modules like authentication, catalog, and ordering

3. 🧱 Generates SQL tables for each module

4. 🧾 Produces pseudocode showing step-by-step processes

5. ✅ Provides everything instantly for review or implementation

---

## 🧪 Example Use Case

Say you’re a developer building an e-commerce MVP. Instead of drafting schemas manually, just describe your features:
> “Users should be able to log in, browse products, add to cart, and pay online.”

The tool returns:
- 🔐 Auth system with `users` table  
- 🛍️ Catalog with `products`  
- 🛒 Cart logic with `cart_items`  
- 📦 Order and `orders` table  
- 💳 Payment with `payments` table  
Plus pseudocode for the full checkout flow!

---

## 🧯 Error Faced During Deployment

⚠️ While attempting to push the notebook to GitHub, the following error was encountered:  
**Failed to save notebook to `https://github.com/AdityaGaur19/SEO-Blog-Post-Creation/blob/main/SEO_Post_Creation.ipynb`**

This was unrelated to the current project but occurred during a repo management step.

---

## 📂 Tech Stack

- Language: Python 🐍  
- IDE: Visual Studio Code 🧑‍💻  
- Web Framework: Streamlit 🌐  
- Output: SQL Schema + Pseudocode 🧾  

---

## 🤝 Contribution & Usage

This project is an open blueprint generator for quick prototyping and design drafts. Ideal for:
- Students working on semester projects  
- Freelance developers planning MVPs  
- Analysts creating system flow diagrams

Feel free to fork, improve, or use in your own builds. Happy hacking! 🛠️🚀

