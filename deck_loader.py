from scryfall_fetcher import fetch_card_info

def load_deck_from_file(path: str):
    deck = []
    metadata = {}
    total_price = 0.0

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "x " in line.lower():
                parts = line.lower().split("x", 1)
                try:
                    qty = int(parts[0].strip())
                    name = parts[1].strip()
                except ValueError:
                    qty, name = 1, line.strip()
            else:
                qty, name = 1, line.strip()
            deck.append((name, qty))

            if name not in metadata:
                info = fetch_card_info(name)
                if info:
                    price_str = info.get("prices", {}).get("usd")
                    price = float(price_str) if price_str else 0.0
                    metadata[name] = info
                    total_price += price * qty

    return deck, metadata, total_price
