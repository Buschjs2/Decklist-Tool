from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import requests
from io import BytesIO
import os

CACHE_DIR = os.path.join(os.path.dirname(__file__), "image_cache")
os.makedirs(CACHE_DIR, exist_ok=True)

class ImagePanel(QWidget):
    def __init__(self):
        super().__init__()
        self.shared_state = None
        self.front_url = None
        self.back_url = None
        self.showing_back = False

        layout = QVBoxLayout()

        self.image_label = QLabel("Card Image\n[Placeholder]")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setWordWrap(True)
        self.image_label.setObjectName("cardPreview")
        self.image_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.meta_label = QLabel("")
        self.meta_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.meta_label.setWordWrap(True)
        self.meta_label.setStyleSheet("color: gray; font-size: 10pt;")

        self.toggle_button = QPushButton("Show Back")
        self.toggle_button.clicked.connect(self.toggle_face)
        self.toggle_button.hide()

        layout.addWidget(self.image_label)
        layout.addWidget(self.meta_label)
        layout.addWidget(self.toggle_button)
        self.setLayout(layout)

    def set_shared_state(self, shared_state):
        self.shared_state = shared_state

    def toggle_face(self):
        if self.showing_back and self.front_url:
            self.set_image(self.front_url)
            self.toggle_button.setText("Show Back")
            self.showing_back = False
        elif not self.showing_back and self.back_url:
            self.set_image(self.back_url)
            self.toggle_button.setText("Show Front")
            self.showing_back = True

    def update_preview(self, card_name):
        from scryfall_fetcher import fetch_card_info
        self.image_label.setText(f"Loading image for {card_name}...")
        self.meta_label.setText("")
        self.image_label.clear()
        self.toggle_button.hide()

        self.front_url = None
        self.back_url = None
        self.showing_back = False

        card_info = None
        if self.shared_state:
            card_info = self.shared_state.deck_metadata.get("metadata", {}).get(card_name)

        if not card_info:
            card_info = fetch_card_info(card_name)

        if card_info:
            meta_text = f"{card_info.get('set_name', '')} | {card_info.get('rarity', '').capitalize()} | {card_info.get('type_line', '')}"
            self.meta_label.setText(meta_text)

            self.front_url = card_info.get("image_uris", {}).get("normal")
            if not self.front_url and card_info.get("card_faces"):
                self.front_url = card_info["card_faces"][0].get("image_uris", {}).get("normal")
                if len(card_info["card_faces"]) > 1:
                    self.back_url = card_info["card_faces"][1].get("image_uris", {}).get("normal")
                    self.toggle_button.show()

            if self.front_url:
                self.set_image(self.front_url)
            else:
                self.image_label.setText(f"{card_name}\n[Image Not Found]")
                self.meta_label.setText("")

    def set_image(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                pixmap = QPixmap()
                pixmap.loadFromData(BytesIO(response.content).read())
                scaled = pixmap.scaledToWidth(250, Qt.TransformationMode.SmoothTransformation)
                self.image_label.setPixmap(scaled)
        except Exception:
            pass
