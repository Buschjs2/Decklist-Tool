from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QHBoxLayout, QComboBox
from style import MODERN_STYLE
from theme_manager import apply_theme
from colors import THEMES

class DeckPreviewWindow(QMainWindow):
    def __init__(self, shared_state, launcher):
        super().__init__()
        self.shared_state = shared_state
        self.launcher = launcher
        self.setStyleSheet(MODERN_STYLE)
        self.setWindowTitle("Deck Preview")
        self.setGeometry(150, 150, 600, 400)
        self.init_ui()

    def init_ui(self):
        central = QWidget()
        layout = QVBoxLayout()

        # Theme selector
        theme_layout = QHBoxLayout()
        theme_label = QLabel("Theme:")
        self.theme_box = QComboBox()
        self.theme_box.addItems(sorted(THEMES.keys()))
        self.theme_box.setCurrentText("White")
        self.theme_box.currentTextChanged.connect(self.change_theme)
        theme_layout.addWidget(theme_label)
        theme_layout.addWidget(self.theme_box)
        layout.addLayout(theme_layout)

        layout.addWidget(QLabel("Deck List"))
        self.deck_list = QListWidget()
        self.deck_list.addItems(self.shared_state.deck)
        layout.addWidget(self.deck_list)

        self.image_label = QLabel("Card Image\n[Placeholder]")
        self.image_label.setObjectName("cardPreview")
        layout.addWidget(self.image_label)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self._nav_button("Editor", self.launcher.open_editor))
        nav_layout.addWidget(self._nav_button("Suggestions", self.launcher.open_suggestions))
        layout.addLayout(nav_layout)

        central.setLayout(layout)
        self.setCentralWidget(central)

    def _nav_button(self, label, callback):
        btn = QPushButton(f"Go to {label}")
        btn.clicked.connect(lambda: (self.close(), callback()))
        return btn

    def change_theme(self, theme_name):
        apply_theme(self, theme_name)
