def admin_dashboard(products: list, orders: list):
    print("---------------")
    print("admin dashboard")
    print("---------------")
    summary = sales_summary(orders)
    print("total orders: " + str[summary["total_orders"]])
    print("total revenue: " + str(summary["total_revenue"]))
    print("---------------")
    top_sellers = top_selling_products(orders, 5)
    if not top_sellers:
        print("no sale yet")
    else:
        for item in top_sellers:
            product_id = item[0]
            quantity = item[1]
            price = item[2]
    print("top sellers: ")
    print(top_sellers)
    print("---------------")


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


