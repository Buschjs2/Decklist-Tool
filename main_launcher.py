import sys
from PyQt6.QtWidgets import QApplication
from shared_state import SharedState
from deck_preview_window import DeckPreviewWindow
from deck_editor_window import DeckEditorWindow
from card_suggestions_window import CardSuggestionsWindow

class AppController:
    def __init__(self):
        self.shared_state = SharedState()

    def open_preview(self):
        self.preview_win = DeckPreviewWindow(self.shared_state, self)
        self.preview_win.show()

    def open_editor(self):
        self.editor_win = DeckEditorWindow(self.shared_state, self)
        self.editor_win.show()

    def open_suggestions(self):
        self.suggest_win = CardSuggestionsWindow(self.shared_state, self)
        self.suggest_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController()
    controller.open_preview() #Launch into Deck Preview directly
    sys.exit(app.exec())
