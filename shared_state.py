class SharedState:
    def __init__(self):
        self.deck = []  # List of tuples: (card_name: str, quantity: int)
        self.deck_metadata = {
            "path": None,
            "total_price": 0.0,
            "color_identity": set(),
            "metadata": {}  # card_name -> Scryfall info
        }
        self.notes = "These are initial deck notes."
        self.suggestions = []
