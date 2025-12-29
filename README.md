# Online-Shopping-Simulation
* The purpose of this project is to provide a text-based e-commerce platform simulation. It allows customers to browse products, manage a shopping cart, and simulate the checkour process while providing administrators with sales analytics. All data is saved locally using JSON, ensuring persistence without internet access.
  
# Technologies Used
* **Python 3.x** (Standard library only)
* **JSON** for data persistence (products and orders)
* **File I/O** for generating receipts and reports
* No external packages are required

# Features
* |catalog| -> Browse products, search by keyword,filter by category,real time stock tracking.
* |cart| -> Add/remove items, updte quantites, tax and total calculations.
* |checkout| -> Create orders, validate stock, simulate payment, generate receipts.
* |admin| -> View total revenue and top selling products, track order history.

# Project structure
* main.py - Entry point, main menu, and user flow.
* catalog.py - Product loading, searching, and inventory updates.
* cart.py - Cart state management and pricing logic.
* orders.py - Order creation, receipt generation, and saving data.
* products.json - Database for product details (ID, price, stock).
* receipts/  - Folder where transaction receipts are saved.


