from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QHBoxLayout, QLineEdit, QGroupBox
from style import MODERN_STYLE
from theme_manager import apply_theme
from colors import THEMES
from suggestion_box import SuggestionBox

class CardSuggestionsWindow(QMainWindow):
    def __init__(self, shared_state, launcher):
        super().__init__()
        self.shared_state = shared_state
        self.launcher = launcher
        self.setStyleSheet(MODERN_STYLE)
        self.setWindowTitle("Card Suggestions")
        self.setGeometry(210, 210, 500, 400)
        self.init_ui()

    def init_ui(self):
        central = QWidget()
        layout = QVBoxLayout()

        group = QGroupBox("Suggested Cards")
        group_layout = QVBoxLayout()

        self.suggestions_list = QListWidget()
        self.suggestions_list.addItems(self.shared_state.suggestions)
        group_layout.addWidget(self.suggestions_list)

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Type card name...")
        self.search_input.textChanged.connect(self.on_text_changed)
        search_layout.addWidget(QLabel("Search:"))
        search_layout.addWidget(self.search_input)
        group_layout.addLayout(search_layout)

        group_layout.addWidget(QPushButton("Add to Deck"))
        group.setLayout(group_layout)
        layout.addWidget(group)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self._nav_button("Preview", self.launcher.open_preview))
        nav_layout.addWidget(self._nav_button("Editor", self.launcher.open_editor))
        layout.addLayout(nav_layout)

        central.setLayout(layout)
        self.setCentralWidget(central)

        self.suggestion_box = SuggestionBox(self)
        self.suggestion_box.set_callback(self.select_suggestion)

    def _nav_button(self, label, callback):
        btn = QPushButton(f"Go to {label}")
        btn.clicked.connect(lambda: (self.close(), callback()))
        return btn

    def on_text_changed(self, text):
        if not text:
            self.suggestion_box.hide()
            return
        matches = [card for card in self.shared_state.suggestions if text.lower() in card.lower()]
        self.suggestion_box.update_suggestions(matches)
        self.position_suggestion_box()

    def select_suggestion(self, card_name):
        self.search_input.setText(card_name)
        self.suggestions_list.addItem(card_name)

    def position_suggestion_box(self):
        if not self.search_input.isVisible():
            return
        pos = self.search_input.mapToGlobal(self.search_input.rect().bottomLeft())
        self.suggestion_box.move(pos)
        self.suggestion_box.resize(self.search_input.width(), 120)
        self.suggestion_box.raise_()
