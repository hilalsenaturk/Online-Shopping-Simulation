import json
import os
import shutil
from datetime import datetime

products_path = os.path.join("data", "products.json")
receipts_path = os.path.join("data", "receipts.json")

def ensure_storage_structure(base_dir="data"):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"Directory {base_dir} created")

def load_json(products_path):
    if not os.path.exists(products_path):
        return []
    try:
        with open(products_path, 'r') as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading json file {e}")
        return []

def save_receipt(receipt):
    existing_data = []
    if os.path.exists(receipts_path):
        with open(receipts_path, "r", encoding="utf-8") as file:
            try:
                existing_data = json.load(file)
            except:
                existing_data = []
    existing_data.append(receipt)
    with open(receipts_path, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=4, ensure_ascii=False)


def write_json(path, data):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error writing json file {e}")
        return []





