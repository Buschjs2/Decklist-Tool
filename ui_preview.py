from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QComboBox, QPushButton, QListWidget, QLineEdit, QSplitter, QFrame,
    QGroupBox, QSizePolicy
)
from PyQt6.QtCore import Qt
from theme_manager import apply_theme
from colors import THEMES
import sys

class DeckToolRedesigned(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Deck Tool - Modern UI")
        self.setGeometry(100, 100, 1200, 700)
        self.current_theme = "Azorius"

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.init_ui()
        apply_theme(self, self.current_theme)

    def init_ui(self):
        main_layout = QVBoxLayout()

        # === Top Control Bar ===
        top_controls = QHBoxLayout()
        self.theme_box = QComboBox()
        self.theme_box.addItems(sorted(THEMES.keys()))
        self.theme_box.setCurrentText(self.current_theme)
        self.theme_box.currentTextChanged.connect(self.change_theme)

        self.deck_box = QComboBox()
        load_button = QPushButton("Load")
        sort_box = QComboBox()
        sort_box.addItems(["Alphabetical", "Highest Value", "Card Type"])

        top_controls.addWidget(QLabel("Theme:"))
        top_controls.addWidget(self.theme_box)
        top_controls.addSpacing(10)
        top_controls.addWidget(QLabel("Select Deck:"))
        top_controls.addWidget(self.deck_box)
        top_controls.addWidget(load_button)
        top_controls.addStretch()
        top_controls.addWidget(QLabel("Sort By:"))
        top_controls.addWidget(sort_box)
        main_layout.addLayout(top_controls)

        # === Search Bar ===
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        search_layout.addWidget(QLabel("Search:"))
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(QPushButton("Clear"))
        main_layout.addLayout(search_layout)

        # === Main Content Area (Split) ===
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Deck List Group
        deck_group = QGroupBox("Deck List")
        deck_layout = QVBoxLayout()
        self.deck_list = QListWidget()
        for i in range(40):
            self.deck_list.addItem(f"{i+1}x Placeholder Card Name")
        deck_layout.addWidget(self.deck_list)
        deck_group.setLayout(deck_layout)
        splitter.addWidget(deck_group)

        # Card Preview Group
        preview_group = QGroupBox("Card Preview")
        preview_layout = QVBoxLayout()
        self.image_label = QLabel("Card Image\n[Placeholder]")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Sunken)
        preview_layout.addWidget(self.image_label)
        preview_group.setLayout(preview_layout)
        splitter.addWidget(preview_group)

        # Deck Stats Group
        stats_group = QGroupBox("Deck Stats")
        stats_layout = QVBoxLayout()
        self.stats_label = QLabel("Mana Curve:\n- 1 Drop: 5\n- 2 Drop: 10\n- ...\n\nCard Types:\n- Creatures: 24\n- Spells: 12")
        stats_label_title = QLabel("Auto-generated stats based on deck content.")
        stats_label_title.setWordWrap(True)
        stats_layout.addWidget(stats_label_title)
        stats_layout.addWidget(self.stats_label)
        stats_group.setLayout(stats_layout)
        splitter.addWidget(stats_group)

        splitter.setSizes([500, 350, 300])
        main_layout.addWidget(splitter)

        # === Bottom Bar ===
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(QLabel("Total Deck Price: $123.45"))
        bottom_layout.addStretch()
        bottom_layout.addWidget(QPushButton("Save and Exit"))
        main_layout.addLayout(bottom_layout)

        self.central_widget.setLayout(main_layout)

    def change_theme(self, theme_name):
        self.current_theme = theme_name
        apply_theme(self, self.current_theme)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DeckToolRedesigned()
    window.show()
    sys.exit(app.exec())
