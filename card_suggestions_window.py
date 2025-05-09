from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QHBoxLayout, QLineEdit, QGroupBox
from style import MODERN_STYLE
from theme_manager import apply_theme
from colors import THEMES

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

    def _nav_button(self, label, callback):
        btn = QPushButton(f"Go to {label}")
        btn.clicked.connect(lambda: (self.close(), callback()))
        return btn
