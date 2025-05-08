import json
import os
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(os.path.dirname(sys.executable), relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

STORAGE_FOLDER = resource_path("storage")
SETTINGS_FILE = os.path.join(STORAGE_FOLDER, "settings.json")

os.makedirs(STORAGE_FOLDER, exist_ok=True)

DEFAULT_SETTINGS = {
    "sort_order": "Alphabetical",
    "last_deck": "",
    "window_width": 800,
    "window_height": 700
}

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    return DEFAULT_SETTINGS.copy()

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=2)
