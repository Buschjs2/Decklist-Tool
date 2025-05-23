from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QHBoxLayout, QComboBox, QSplitter,
    QFileDialog, QLineEdit, QTextEdit, QFrame, QVBoxLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextDocument
from style import MODERN_STYLE
from theme_manager import apply_theme
from colors import THEMES
from image_panel import ImagePanel
from deck_loader import load_deck_from_file
from stats_chart_panel import StatsChartPanel

class DeckPreviewWindow(QMainWindow):
    def __init__(self, shared_state, launcher):
        super().__init__()
        self.shared_state = shared_state
        self.launcher = launcher
        self.setStyleSheet(MODERN_STYLE)
        self.setWindowTitle("Deck Preview")
        self.setGeometry(150, 150, 1000, 600)
        self.init_ui()

    def init_ui(self):
        central = QWidget()
        layout = QVBoxLayout()

        # Theme + Load
        theme_layout = QHBoxLayout()
        theme_label = QLabel("Theme:")
        self.theme_box = QComboBox()
        for theme in sorted(THEMES.keys()):
            self.theme_box.addItem(theme)
        self.theme_box.setCurrentText("White")
        self.theme_box.currentTextChanged.connect(self.change_theme)
        theme_layout.addWidget(theme_label)
        theme_layout.addWidget(self.theme_box)

        load_btn = QPushButton("Load Deck")
        load_btn.clicked.connect(self.load_deck)
        theme_layout.addWidget(load_btn)
        layout.addLayout(theme_layout)

        # Search bar
        search_layout = QHBoxLayout()
        search_label = QLabel("Search:")
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Filter deck...")
        self.search_input.textChanged.connect(self.filter_deck_list)
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)
        layout.addLayout(search_layout)

        # Sorting
        sort_layout = QHBoxLayout()
        sort_label = QLabel("Sort By:")
        self.sort_box = QComboBox()
        self.sort_box.addItems(["Alphabetical", "Total Value"])
        self.sort_box.currentTextChanged.connect(self.sort_deck_list)
        sort_layout.addWidget(sort_label)
        sort_layout.addWidget(self.sort_box)
        layout.addLayout(sort_layout)

        # Main content: deck list on the left, image + charts side-by-side on the right
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Deck List
        self.deck_list = QListWidget()
        self.deck_list.setMinimumWidth(300)
        self.deck_list.itemClicked.connect(self.on_card_selected)
        splitter.addWidget(self.deck_list)

        # Right side: Image and Stats next to each other
        right_container = QWidget()
        right_layout = QHBoxLayout(right_container)

        self.image_panel = ImagePanel()
        self.image_panel.set_shared_state(self.shared_state)
        self.image_panel.setMinimumWidth(250)
        right_layout.addWidget(self.image_panel)

        self.stats_chart_panel = StatsChartPanel()
        right_layout.addWidget(self.stats_chart_panel)

        splitter.addWidget(right_container)
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 5)
        layout.addWidget(splitter)

        # Bottom bar
        self.total_price_label = QLabel("Total Deck Price: $0.00")
        self.total_price_label.setStyleSheet("font-weight: bold; padding: 4px;")
        layout.addWidget(self.total_price_label)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self._nav_button("Editor", self.launcher.open_editor))
        nav_layout.addWidget(self._nav_button("Suggestions", self.launcher.open_suggestions))
        layout.addLayout(nav_layout)

        central.setLayout(layout)
        self.setCentralWidget(central)

    def change_theme(self, theme_name):
        apply_theme(self, theme_name)

    def on_card_selected(self, item):
        doc = QTextDocument()
        doc.setHtml(item.text())
        plain_text = doc.toPlainText()
        if "x " in plain_text.lower():
            plain_text = plain_text.split("x ", 1)[1].strip()
        self.image_panel.update_preview(plain_text)

    def load_deck(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(
            self, "Open Deck File", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            parsed_deck, meta, total = load_deck_from_file(file_path)
            self.shared_state.deck = parsed_deck
            self.shared_state.deck_metadata["metadata"] = meta
            self.shared_state.deck_metadata["path"] = file_path
            self.shared_state.deck_metadata["total_price"] = total

            # Reset the deck list
            self.deck_list.clear()

            # Add cards to list
            for name, qty in parsed_deck:
                price_str = meta.get(name, {}).get("prices", {}).get("usd")
                price = float(price_str) if price_str else 0.0
                item = f"{qty}x {name}"
                tooltip = f"{qty} x ${price:.2f} = ${qty * price:.2f}" if price > 0 else "Price unavailable"
                list_item = QListWidgetItem(item)
                list_item.setToolTip(tooltip)
                self.deck_list.addItem(list_item)

            # Update charts
            self.stats_chart_panel.update_charts(parsed_deck, meta)

            # Update price label
            self.total_price_label.setText(f"Total Deck Price: ${total:.2f}")

            # Update theme
            self.update_theme_based_on_colors(parsed_deck)

    def sort_deck_list(self, mode):
        metadata = self.shared_state.deck_metadata.get("metadata", {})
        deck = self.shared_state.deck.copy()

        if mode == "Alphabetical":
            deck.sort(key=lambda x: x[0].lower())
        elif mode == "Total Value":
            def card_value(entry):
                name, qty = entry
                info = metadata.get(name, {})
                price_str = info.get("prices", {}).get("usd", "0")
                try:
                    return -qty * float(price_str or 0)
                except:
                    return 0
            deck.sort(key=card_value)

        self.deck_list.clear()
        for name, qty in deck:
            price_str = metadata.get(name, {}).get("prices", {}).get("usd")
            price = float(price_str) if price_str else 0.0
            item = f"{qty}x {name}"
            tooltip = f"{qty} x ${price:.2f} = ${qty * price:.2f}" if price > 0 else "Price unavailable"
            list_item = QListWidgetItem(item)
            list_item.setToolTip(tooltip)
            self.deck_list.addItem(list_item)
            
    def update_stats_panel(self):
        deck = self.shared_state.deck
        metadata = self.shared_state.deck_metadata.get("metadata", {})
        color_names = {"W": "White", "U": "Blue", "B": "Black", "R": "Red", "G": "Green"}
        color_styles = {
            "White": "#f0f0f0", "Blue": "#4e9eea", "Black": "#3b3b3b",
            "Red": "#ea4e4e", "Green": "#3bae62", "Multicolor": "#d19e28", "Colorless": "#aaaaaa"
        }

        self.color_data = {
            "Monocolor": {"White": 0, "Blue": 0, "Black": 0, "Red": 0, "Green": 0},
            "Multicolor": {},
            "Colorless": 0
        }
        self.type_data = {}

        for name, qty in deck:
            info = metadata.get(name, {})
            ci = info.get("color_identity", [])
            if not ci:
                self.color_data["Colorless"] += qty
            elif len(ci) == 1:
                cname = color_names.get(ci[0], "Unknown")
                self.color_data["Monocolor"][cname] += qty
            else:
                combo = " / ".join(color_names.get(c, c) for c in sorted(ci))
                self.color_data["Multicolor"][combo] = self.color_data["Multicolor"].get(combo, 0) + qty

            typeline = info.get("type_line", "Unknown")
            typename = typeline.split("—")[0].strip()
            self.type_data[typename] = self.type_data.get(typename, 0) + qty

        # Initial dropdown state
        self.update_color_section(self.color_dropdown.currentText())

        # Type display
        lines = []
        for t, v in self.type_data.items():
            lines.append(f"{t}: {v}")
        self.type_section.setPlainText("\n".join(lines))


    def update_theme_based_on_colors(self, parsed_deck):
        from colors import COLOR_THEME_MAP
        color_identity = set()
        for name, qty in parsed_deck:
            if "White" in name: color_identity.add("W")
            if "Blue" in name: color_identity.add("U")
            if "Black" in name: color_identity.add("B")
            if "Red" in name: color_identity.add("R")
            if "Green" in name: color_identity.add("G")
        self.shared_state.deck_metadata["color_identity"] = color_identity
        theme_name = COLOR_THEME_MAP.get(frozenset(color_identity))
        if theme_name:
            self.theme_box.setCurrentText(theme_name)
            apply_theme(self, theme_name)

    def filter_deck_list(self, text):
        self.deck_list.clear()
        for name, qty in self.shared_state.deck:
            entry = f"{qty}x {name}"
            if text.lower() in name.lower():
                self.deck_list.addItem(entry)
                
    def update_color_section(self, section):
        styles = {
            "White": "#f0f0f0", "Blue": "#4e9eea", "Black": "#3b3b3b",
            "Red": "#ea4e4e", "Green": "#3bae62", "Multicolor": "#d19e28", "Colorless": "#aaaaaa"
        }
        data = self.color_data
        lines = []

        if section == "Colorless":
            val = data.get("Colorless", 0)
            lines.append(f'<span style="color:{styles["Colorless"]}">■</span> Colorless: {val}')
        elif section == "Multicolor":
            for combo, count in sorted(data.get("Multicolor", {}).items()):
                lines.append(f'<span style="color:{styles["Multicolor"]}">■</span> {combo}: {count}')
        elif section == "Monocolor":
            for cname, count in sorted(data.get("Monocolor", {}).items()):
                lines.append(f'<span style="color:{styles[cname]}">■</span> {cname}: {count}')

        self.color_section.setHtml("<br>".join(lines))
        
    def _nav_button(self, label, callback):
        btn = QPushButton(f"Go to {label}")
        btn.clicked.connect(lambda: (self.close(), callback()))
        return btn

