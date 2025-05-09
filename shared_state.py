class SharedState:
    def __init__(self):
        self.deck = [f"{i+1}x Placeholder Card Name" for i in range(40)]
        self.notes = "These are initial deck notes."
        self.suggestions = [f"Suggested Card {i+1}" for i in range(10)]
        self.current_card = None
        self.current_theme = "Azorius"