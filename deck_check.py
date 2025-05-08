import os

BACKUP_DIR = "backups"

def list_decklists():
    return [f for f in os.listdir() if f.endswith('.txt') and not f.startswith(BACKUP_DIR)]

def load_decklist(filename):
    deck = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('x ', 1)
            if len(parts) == 2:
                count, name = parts
                deck[name.strip()] = int(count.strip())
    return deck

def save_decklist(filename, deck):
    with open(filename, 'w') as file:
        for name, count in deck.items():
            file.write(f"{count}x {name}\n")

def display_deck(deck):
    if not deck:
        print("(No cards left in this deck)")
    else:
        for name, count in sorted(deck.items()):
            print(f"{count}x {name}")

def load_decklist_original(filename):
    """Creates a backup of the original full decklist the first time it's accessed."""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    backup_path = os.path.join(BACKUP_DIR, f"{filename}.bak")
    if not os.path.exists(backup_path):
        with open(filename, 'r') as f_orig, open(backup_path, 'w') as f_backup:
            f_backup.write(f_orig.read())
    return load_decklist(backup_path)

def show_decklist_menu():
    decklists = list_decklists()
    print("Available decklists (remaining cards):")
    for i, name in enumerate(decklists):
        current = load_decklist(name)
        unique = len(current)
        total = sum(current.values())
        print(f"{i + 1}: {name} - {unique} unique cards, {total} total cards")
    return decklists

def main():
    decklists = show_decklist_menu()
    choice = int(input("\nSelect a decklist by number: ")) - 1
    filename = decklists[choice]

    # Ensure original is backed up
    load_decklist_original(filename)

    deck = load_decklist(filename)

    while True:
        print("\n--- Current Deck ---")
        display_deck(deck)
        print("\nOptions: [R]emove card, [Q]uit")
        action = input("Enter action: ").strip().lower()

        if action == 'q':
            save_decklist(filename, deck)
            print(f"Saved changes to {filename}")
            break
        elif action == 'r':
            card = input("Enter card name to remove: ").strip()
            if card in deck:
                max_qty = deck[card]
                qty = int(input(f"How many to remove? (1-{max_qty}): "))
                if qty >= max_qty:
                    del deck[card]
                    print(f"Removed all copies of {card}")
                else:
                    deck[card] -= qty
                    print(f"Removed {qty}x {card}")
                print("\nUpdated deck:")
                display_deck(deck)
            else:
                print("Card not found in deck.")
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()
