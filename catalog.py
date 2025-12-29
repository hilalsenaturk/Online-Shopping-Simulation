from storage import load_json, write_json
import json
import os
product_data = load_json('products.json')

def load_products(path: str):
    return load_json('products.json')

def save_products(path: str, products: list):
    write_json('products.json', products)

def search_products(products: list, keyword: str):
    results = []
    keyword = keyword.lower()
    for product in products:
        if keyword in product['title'].lower():
            results.append(product)
    return results

def filter_by_category(products: list,keyword: str):
    results =  []
    for product in products:
        if product['category'].lower() == keyword:
            results.append(product)
    return results

def update_product_stock(products: list):
    for product in products:
        if product['id'] == product['product_id']:
            product['stock'] += product['quantity']
            if product['quantity'] < 0:
                print(f"Error! Stock cannot be negative!")
                return False
            else:
                product['stock'] = product['stock'] - product['quantity']
                return True
    print("Error! Product not found!")
    return False

def add_new_products(products):
    for product in products:
        if product['id'] == product_data['id']:
            print(f"Error: product already exists!")
            return False
    products.append(product)
    print(f"Product added: {product}")
    return True