from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QHBoxLayout, QGroupBox
from style import MODERN_STYLE
from theme_manager import apply_theme
from colors import THEMES

class DeckEditorWindow(QMainWindow):
    def __init__(self, shared_state, launcher):
        super().__init__()
        self.shared_state = shared_state
        self.launcher = launcher
        self.setStyleSheet(MODERN_STYLE)
        self.setWindowTitle("Deck Editor")
        self.setGeometry(180, 180, 600, 500)
        self.init_ui()

    def init_ui(self):
        central = QWidget()
        layout = QVBoxLayout()

        group = QGroupBox("Deck Notes")
        group_layout = QVBoxLayout()

        self.editor = QTextEdit()
        self.editor.setText(self.shared_state.notes)
        group_layout.addWidget(self.editor)

        save_btn = QPushButton("Save Changes")
        save_btn.clicked.connect(self.save_notes)
        group_layout.addWidget(save_btn)

        group.setLayout(group_layout)
        layout.addWidget(group)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self._nav_button("Preview", self.launcher.open_preview))
        nav_layout.addWidget(self._nav_button("Suggestions", self.launcher.open_suggestions))
        layout.addLayout(nav_layout)

        central.setLayout(layout)
        self.setCentralWidget(central)

    def save_notes(self):
        self.shared_state.notes = self.editor.toPlainText()

    def _nav_button(self, label, callback):
        btn = QPushButton(f"Go to {label}")
        btn.clicked.connect(lambda: (self.close(), callback()))
        return btn
