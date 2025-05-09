import requests

def fetch_card_info(card_name):
    try:
        response = requests.get(f"https://api.scryfall.com/cards/named?exact={card_name}")
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error fetching card info: {e}")
    return None

def fetch_card_image_url(card_name):
    info = fetch_card_info(card_name)
    return info.get("image_uris", {}).get("normal", None) if info else None
