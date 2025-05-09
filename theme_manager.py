from colors import THEMES, COLOR_THEME_MAP
from PyQt6.QtWidgets import QWidget, QComboBox, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit

def apply_theme(window: QWidget, theme_name: str):
    theme = THEMES.get(theme_name)
    if not theme:
        return

    gradient_bg = f"""
    QMainWindow {{
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 {theme['bg']}, stop: 1 {theme['panel']}
        );
    }}

    QLabel#cardPreview {{
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 {theme['image_bg']}, stop: 1 {theme['panel']}
        );
        color: {theme['text']};
        border: 1px solid #888;
        padding: 8px;
        font-style: italic;
        qproperty-alignment: AlignCenter;
    }}

    QListWidget::item:selected {{
        background: qlineargradient(
            x1: 0, y1: 0, x2: 1, y2: 0,
            stop: 0 {theme['highlight']}, stop: 1 {theme['panel']}
        );
        color: {theme['text']};
    }}

    QGroupBox {{
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 {theme['panel']}, stop: 1 {theme['bg']}
        );
        border: 1px solid #aaa;
        border-radius: 5px;
        margin-top: 10px;
    }}
    QGroupBox::title {{
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 5px;
        color: {theme['text']};
    }}
    """

    window.setStyleSheet(gradient_bg + f"""
        QLabel {{
            color: {theme['text']};
            font-size: 14px;
        }}
        QListWidget {{
            background-color: {theme['listbox']};
            color: {theme['text']};
            border: 1px solid #aaa;
        }}
        QLineEdit, QTextEdit {{
            background-color: {theme['entry']};
            color: {theme['text']};
            border: 1px solid #aaa;
            padding: 4px;
        }}
        QComboBox {{
            background-color: {theme['entry']};
            color: {theme['text']};
        }}
        QPushButton {{
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 {theme['button']}, stop: 1 {theme['highlight']}
            );
            color: {theme['text']};
            border-radius: 5px;
            padding: 5px 10px;
        }}
        QPushButton:hover {{
            background-color: {theme['highlight']};
        }}
    """)

    def set_widget_style(widget):
        for child in widget.findChildren(QWidget):
            set_widget_style(child)

    set_widget_style(window)
