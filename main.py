import cart
import storage
def customer_dashboard(products: list, orders:list):
    current_cart = cart.create_cart()
    while True:
        print("---------------")
        print("customer dashboard")
        print("---------------")
        print("1. Browse Products")
        print("2. Add to Cart")
        print("3. View Cart / Remove Item ")
        print("4. Checkout ")
        print("5. Log Out ")
        choice = input("your Choice (1-5): ").strip()
        if choice == "1":
            print("product catalog")
        elif choice == "2":
            product_id = input("Enter Product ID: ")
            selected_product = None
            for product in products:
                if str(product["id"]) == product_id:
                    selected_product = product
                    break
            if selected_product:
                if selected_product["stock"] > 0:
                    cart.add_to_cart(current_cart, selected_product)
                else:
                    print("this item is out of stock ")
            else:
                print("product id not found")
        elif choice == '3':
            cart.show_cart(current_cart)
            if current_cart:
                ask = input("\nType 'r' to remove an item, or ENTER to go back: ")
                if ask.lower() == 'r':
                    r_id = input("Enter Product ID to remove: ")
                    try:
                        cart.remove_from_cart(current_cart, int(r_id))
                    except ValueError:
                        print("Invalid ID format.")
        elif choice == '4':
            if not current_cart:
                print("Cart is empty! Cannot checkout.")
            else:
                total = cart.calculate_total(current_cart)
                print("-------------------")
                print("PAYMENT SUCCESSFUL")
                print("-------------------")
                print(f"Total Amount Paid: {total} ")
                print("Thank you for shopping!")
                current_cart = []
        elif choice == '5':
            print("Logging out from Customer Dashboard.")
            break
        else:
            print("Invalid selection. Please try again.")


def admin_dashboard(products: list, orders: list):
    while True:
        print("---------------")
        print("admin dashboard")
        print("---------------")
        print("1. view products")
        print("2. add products")
        print("3.view orders and log out")
        choice = input("your choice (1-3): ").strip()
        if choice == "1":
            print("current inventory")
        elif choice == "2":
            print("add new products")
            try:
                new_product = input("enter Product ID: ")
                new_quantity = input("enter Quantity: ")
                new_stock = input("enter Stock: ")
                new_price = float(input("enter Price: "))
                new_category = input("enter Category: ")
                new_product = {
                    "product_id": new_product,
                    "quantity": new_quantity,
                    "stock": new_stock,
                    "price": new_price,
                    "category": new_category,
                }
                products.append(new_product)
                print(f"product added: {new_product}")
            except ValueError:
                print("invalid input")
        elif choice == "3":
            storage.write_json(storage.products_path, products)
            print(f"product saved : {new_product}")
            print("logging out from admin dashboard")
            break
        else: print("invalid selection, try again")


def top_selling_products(orders: list, limit: int = 5):
    product_counts = {}
    for order in orders:
        items = order["items"]
        for item_id in items:
            product_id = item_id["product_id"]
            quantity = item_id["quantity"]
            if item_id in product_counts:
                product_counts[item_id] = product_counts[item_id] + quantity
            else: product_counts[item_id] = quantity
    sales_list = []
    for product_id in product_counts:
        sales_list.append([product_id, product_counts[product_id]])
    top_5_list = []
    counter = 0
    while counter < limit:
        if len(sales_list) == 0:
            break
        max_product = None
        max_quantity = 0
        for product in sales_list:
            current_quantity = product[1]
            if current_quantity > max_quantity:
                max_quantity = current_quantity
                max_product = product [0]
            if max_product:
                top_5_list.append(max_product)
                sales_list.remove(max_product)
            counter += 1
        return top_5_list


def sales_summary(orders: list):
   total_revenue = 0
   total_oders = len(orders)
   for order in orders:
       items = order["items"]
       total_revenue += items[0]["revenue"]
       summary = {
           "total_revenue" : total_revenue,
           "total_orders": len(orders),
       }
       return summary


def export_report(data: dict, filename: str):
    file_path = "reports/" + filename
    my_file = open(file_path, "w")
    my_file.write("------------------------\n")
    my_file.write("      SALES REPORT      \n")
    my_file.write("------------------------\n")
    revenue = data["total_revenue"]
    count = data["total_orders"]
    line1 = "total revenue:" + str(count) + "\n"
    my_file.write(line1)
    line2 = "total orders:" + str(count) + "\n"
    my_file.write(line2)
    my_file.close()
    return file_path



