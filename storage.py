import json
import os
import shutil
from datetime import datetime

def ensure_storage_structure(base_dir="data"):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"Directory {base_dir} created")

def load_json(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading json file {e}")
        return []
def write_json(path, data):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error writing json file {e}")
        return []






