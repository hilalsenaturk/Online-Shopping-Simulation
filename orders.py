import datetime
import random

def create_order(cart: dict, customer: dict, payment_method: str):
    random_num = random.randint(1, 100)
    order_id = "order_" + str(random_num)
    now = datetime.datetime.now()
    current_time = str(now)
    tax_val = cart.get("tax_amount", cart.get("tax", 0))
    order = {
        "order_id": order_id,
        "customer_id": customer["id"],
        "date": current_time,
        "payment_method" : payment_method,
        "total" : cart["total"],
        "tax": cart["tax"],
        "items" : cart["items"]
    }
    if 'discount' in cart:
        order["discount"] = cart["discount"]
    else:
        order["discount"] = 0
    print(f"Your order is {order_id}")
    return order

import json
import os
def save_order(path: str, order: dict):
    all_orders = []
    if os.path.exists(path):
        try:
            with open(path, "r") as file:
                all_orders = json.load(file)
        except:
            all_orders = []
    all_orders.append(order)
    with open(path, "w") as file:  # <--- (BURASI DEĞİŞTİ)
        json.dump(all_orders, file, indent=4)
        print(f"Your order is saved to {path}")
    print(f"your order is saved to {path}")

def generate_receipt(order: dict, directory: str):
    now = datetime.datetime.now()
    current_time = str(now)
    order_id = order["id"]
    filename = directory + str(order_id) + ".txt"
    f = open(filename, "w")
    f.write(order["receipt date:" + current_time] + "\n")
    f.write(order["order_id"] + "\n")
    customer_name =order["customer"]["name"]
    f.write(customer_name + "\n")
    f.write("---------------\n")
    f.write("items: \"n")
    items = order["items"]
    for item_id in items:
        item = items[item_id]
        for_each_item = item["name"] + " (x" + str(item["quantity"]) + ") : " + str(item["price"])
        f.write(for_each_item)
        f.write("total " + str(item["total"])+ "\n")
        f.close()
        return filename



