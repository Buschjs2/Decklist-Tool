# theme_manager.py

import tkinter as tk
from tkinter import ttk
from colors import THEMES

def apply_theme(root, theme_name):
    theme = THEMES.get(theme_name)
    if not theme:
        return

    root.configure(bg=theme["bg"])

    def update_widget(widget):
        widget_type = widget.winfo_class()
        try:
            if widget_type in ["Frame", "Label", "Button", "TLabel", "TButton"]:
                widget.configure(bg=theme["bg"], fg=theme["text"])
            elif widget_type == "Listbox":
                widget.configure(bg=theme["bg"], fg=theme["text"], selectbackground=theme["highlight"], selectforeground=theme["text"])
            elif widget_type == "TCombobox":
                style = ttk.Style()
                style.theme_use("clam")
                style.configure("TCombobox", fieldbackground=theme["accent"], background=theme["accent"], foreground=theme["text"])
        except:
            pass
        for child in widget.winfo_children():
            update_widget(child)

    update_widget(root)
