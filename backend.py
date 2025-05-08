import os
import json
import sys
import requests

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(os.path.dirname(sys.executable), relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

INPUT_FOLDER = resource_path("inputs")
STORAGE_FOLDER = resource_path("storage")
BACKUP_DIR = os.path.join(STORAGE_FOLDER, "backups")
CACHE_FILE = os.path.join(STORAGE_FOLDER, "price_cache.json")

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(STORAGE_FOLDER, exist_ok=True)
os.makedirs(BACKUP_DIR, exist_ok=True)

def list_decklists():
    return [f for f in os.listdir(INPUT_FOLDER) if f.endswith('.txt')]

def load_decklist(filename):
    path = os.path.join(INPUT_FOLDER, filename)
    deck = {}
    with open(path, 'r') as file:
        for line in file:
            parts = line.strip().split('x ', 1)
            if len(parts) == 2:
                count, name = parts
                deck[name.strip()] = int(count.strip())
    return deck

def save_decklist(filename, deck):
    path = os.path.join(INPUT_FOLDER, filename)
    with open(path, 'w') as file:
        for name, count in deck.items():
            file.write(f"{count}x {name}\n")

def load_decklist_original(filename):
    orig_path = os.path.join(INPUT_FOLDER, filename)
    backup_path = os.path.join(BACKUP_DIR, f"{filename}.bak")
    if not os.path.exists(backup_path):
        with open(orig_path, 'r') as f_orig, open(backup_path, 'w') as f_backup:
            f_backup.write(f_orig.read())
    return load_decklist(filename)

def export_to_csv(deck, filename):
    import csv
    path = os.path.join(STORAGE_FOLDER, filename)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Quantity", "Card Name"])
        for name, qty in deck.items():
            writer.writerow([qty, name])

def export_to_arena(deck, filename):
    path = os.path.join(STORAGE_FOLDER, filename)
    with open(path, 'w') as f:
        for name, qty in deck.items():
            f.write(f"{qty} {name}\n")

def summarize_by_category(deck, prices, types):
    categories = {
        "Land": 0.0, "Creature": 0.0, "Artifact": 0.0, "Enchantment": 0.0,
        "Instant": 0.0, "Sorcery": 0.0, "Planeswalker": 0.0, "Battle": 0.0, "Other": 0.0
    }
    for name, qty in deck.items():
        price = prices.get(name, 0.0)
        ctype = types.get(name, "Other")
        if ctype in categories:
            categories[ctype] += price * qty
        else:
            categories["Other"] += price * qty
    return categories

def load_price_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_price_cache(prices):
    with open(CACHE_FILE, 'w') as f:
        json.dump(prices, f, indent=2)

def get_card_price(name, cache):
    if name in cache and isinstance(cache[name], dict):
        return cache[name]["price"], cache[name]["type"]

    url = f"https://api.scryfall.com/cards/named?exact={name}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            price_str = data.get("prices", {}).get("usd")
            price = float(price_str) if price_str else 0.0
            type_line = data.get("type_line", "")
            primary_type = type_line.split("—")[0].strip().split(" ")[-1]
            cache[name] = {"price": price, "type": primary_type}
            return price, primary_type
    except Exception:
        pass

    cache[name] = {"price": 0.0, "type": "Other"}
    return 0.0, "Other"

def get_deck_price(deck):
    prices = load_price_cache()
    total = 0.0
    card_prices = {}
    card_types = {}
    for name, qty in deck.items():
        price, ctype = get_card_price(name, prices)
        total += price * qty
        card_prices[name] = price
        card_types[name] = ctype
    save_price_cache(prices)
    return card_prices, round(total, 2), card_types
