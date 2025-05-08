import tkinter as tk

class SuggestionBox(tk.Toplevel):
    def __init__(self, parent, entry_widget, callback):
        super().__init__(parent)
        self.withdraw()
        self.entry_widget = entry_widget
        self.callback = callback
        self.overrideredirect(True)
        self.listbox = tk.Listbox(self, width=40, height=6)
        self.listbox.pack()
        self.listbox.bind("<Double-Button-1>", self.on_mouse_select)
        self.listbox.bind("<Return>", self.on_keyboard_select)
        self.listbox.bind("<Escape>", lambda e: self.withdraw())
        self.listbox.bind("<FocusOut>", lambda e: self.withdraw())

    def show(self, suggestions):
        if not suggestions:
            self.withdraw()
            return
        self.listbox.delete(0, tk.END)
        for item in suggestions:
            self.listbox.insert(tk.END, item)
        x = self.entry_widget.winfo_rootx()
        y = self.entry_widget.winfo_rooty() + self.entry_widget.winfo_height()
        self.geometry(f"+{x}+{y}")
        self.deiconify()

    def on_mouse_select(self, event):
        self.on_select()

    def on_keyboard_select(self, event):
        self.on_select()

    def on_select(self):
        if self.listbox.curselection():
            selected = self.listbox.get(self.listbox.curselection()[0])
            self.callback(selected)
            self.withdraw()
