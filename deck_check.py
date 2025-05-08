import os
import difflib
import copy

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

def find_multiple_matches(input_name, deck, max_matches=3):
    names = list(deck.keys())
    matches = difflib.get_close_matches(input_name.lower(), [name.lower() for name in names], n=max_matches, cutoff=0.5)
    match_dict = []
    for match in matches:
        for original in names:
            if original.lower() == match:
                match_dict.append(original)
    return match_dict

def get_matching_card(input_name, deck):
    lowered_input = input_name.lower()
    all_cards = list(deck.keys())

    # Exact match
    card_lookup = {name.lower(): name for name in all_cards}
    if lowered_input in card_lookup:
        return card_lookup[lowered_input]

    # Partial match
    partial_matches = [name for name in all_cards if lowered_input in name.lower()]
    if len(partial_matches) == 1:
        return partial_matches[0]
    elif len(partial_matches) > 1:
        print("Multiple partial matches found:")
        for i, name in enumerate(partial_matches):
            print(f"{i + 1}: {name}")
        print("0: Cancel")
        selection = input("Enter number to select or 0 to cancel: ").strip()
        if selection.isdigit():
            idx = int(selection)
            if 1 <= idx <= len(partial_matches):
                return partial_matches[idx - 1]
        return None

    # Fuzzy match fallback
    close_matches = find_multiple_matches(input_name, deck)
    if close_matches:
        print("Card not found. Did you mean:")
        for i, name in enumerate(close_matches):
            print(f"{i + 1}: {name}")
        print("0: Cancel")
        selection = input("Enter number to select or 0 to cancel: ").strip()
        if selection.isdigit():
            idx = int(selection)
            if 1 <= idx <= len(close_matches):
                return close_matches[idx - 1]

    return None

def main():
    decklists = show_decklist_menu()
    choice = int(input("\nSelect a decklist by number: ")) - 1
    filename = decklists[choice]

    load_decklist_original(filename)
    deck = load_decklist(filename)
    history = []

    while True:
        print("\n--- Current Deck ---")
        display_deck(deck)
        print("\nOptions: [R]emove card, [U]ndo last change, [Q]uit")
        action = input("Enter action: ").strip().lower()

        if action == 'q':
            save_decklist(filename, deck)
            print(f"Saved changes to {filename}")
            break

        elif action == 'u':
            if history:
                deck = history.pop()
                print("Undo successful. Restored previous deck state.")
            else:
                print("Nothing to undo.")

        elif action == 'r':
            input_name = input("Enter card name to remove: ").strip()
            selected_card = get_matching_card(input_name, deck)

            if selected_card and selected_card in deck:
                max_qty = deck[selected_card]
                qty = int(input(f"How many to remove? (1-{max_qty}): "))
                history.append(copy.deepcopy(deck))
                if qty >= max_qty:
                    del deck[selected_card]
                    print(f"Removed all copies of {selected_card}")
                else:
                    deck[selected_card] -= qty
                    print(f"Removed {qty}x {selected_card}")
                print("\nUpdated deck:")
                display_deck(deck)
            else:
                print("Card not found or removal cancelled.")

        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()
