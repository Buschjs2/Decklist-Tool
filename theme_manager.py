# theme_manager.py

import tkinter as tk
from tkinter import ttk
from colors import THEMES

def apply_theme(root, theme_name):
    theme = THEMES.get(theme_name)
    if not theme:
        return

    root.configure(bg=theme.get("bg", "#FFFFFF"))
    style = ttk.Style()
    style.theme_use("clam")

    # Global ttk styles
    style.configure("TButton", background=theme.get("button"), foreground=theme.get("text"))
    style.configure("TLabel", background=theme.get("bg"), foreground=theme.get("text"))
    style.configure("TCombobox", fieldbackground=theme.get("entry"), background=theme.get("entry"), foreground=theme.get("text"))

    def update_widget(widget):
        cls = widget.winfo_class()

        try:
            if cls == "Frame":
                widget.configure(bg=theme.get("panel", theme["bg"]))
            elif cls == "Label":
                widget.configure(bg=theme.get("panel", theme["bg"]), fg=theme["text"])
            elif cls == "Button":
                widget.configure(bg=theme.get("button"), fg=theme["text"])
            elif cls == "Listbox":
                widget.configure(
                    bg=theme.get("listbox", theme["bg"]),
                    fg=theme["text"],
                    selectbackground=theme.get("highlight"),
                    selectforeground=theme["text"]
                )
            elif cls == "Entry":
                widget.configure(bg=theme.get("entry"), fg=theme["text"])
        except:
            pass

        for child in widget.winfo_children():
            update_widget(child)

    update_widget(root)
