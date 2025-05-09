from PyQt6.QtWidgets import QListWidget, QListWidgetItem
from PyQt6.QtCore import Qt, QPoint

class SuggestionBox(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.Popup)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setMouseTracking(True)
        self.itemClicked.connect(self.on_item_clicked)
        self._callback = None

    def set_callback(self, callback):
        self._callback = callback

    def update_suggestions(self, items):
        self.clear()
        for item in items:
            QListWidgetItem(item, self)
        if items:
            self.setCurrentRow(0)
            self.show()
        else:
            self.hide()

    def on_item_clicked(self, item):
        if self._callback:
            self._callback(item.text())
        self.hide()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return and self.currentItem():
            self.on_item_clicked(self.currentItem())
        elif event.key() in (Qt.Key.Key_Up, Qt.Key.Key_Down):
            super().keyPressEvent(event)
        elif event.key() == Qt.Key.Key_Escape:
            self.hide()
        else:
            self.hide()
