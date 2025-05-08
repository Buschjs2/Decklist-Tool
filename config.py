import os
import json
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(os.path.dirname(sys.executable), relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

STORAGE_FOLDER = resource_path("storage")
CONFIG_FILE = os.path.join(STORAGE_FOLDER, "settings.json")

os.makedirs(STORAGE_FOLDER, exist_ok=True)

def load_settings():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_settings(settings):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(settings, f, indent=2)
