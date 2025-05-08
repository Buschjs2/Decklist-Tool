import tkinter as tk
import os
from tkinter import ttk, messagebox, simpledialog
from backend import (
    list_decklists, load_decklist_original, save_decklist,
    get_deck_price
)
from config import load_settings, save_settings

class Tooltip:
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None

    def show(self, text, x, y):
        self.hide()
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.geometry(f"+{x+20}+{y+10}")
        label = tk.Label(tw, text=text, background="lightyellow", relief="solid", borderwidth=1, font=("Segoe UI", 9))
        label.pack()

    def hide(self):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None

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

def launch_app():
    root = tk.Tk()
    app = DeckGUI(root)
    root.mainloop()

class DeckGUI:
    def __init__(self, root):
        self.root = root
        self.settings = load_settings()
        self.deck = {}
        self.filtered = {}
        self.prices = {}
        self.total_price = 0.0
        self.card_types = {}
        self.filename = ""

        self.tooltip = Tooltip(root)
        self.setup_window()
        self.build_ui()
        if self.settings.get("last_deck"):
            self.load_deck(self.settings["last_deck"])

    def setup_window(self):
        w = self.settings.get("window_width", 800)
        h = self.settings.get("window_height", 600)
        self.root.geometry(f"{w}x{h}")
        self.root.title("Deck Viewer")

    def build_ui(self):

        menubar = tk.Menu(self.root)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Export to CSV", command=lambda: self.export_deck("csv"))
        filemenu.add_command(label="Export to Arena", command=lambda: self.export_deck("arena"))
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        toolsmenu = tk.Menu(menubar, tearoff=0)
        toolsmenu.add_command(label="Category Summary", command=self.show_category_summary)
        menubar.add_cascade(label="Tools", menu=toolsmenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Deck Tool v1.0 by Joe Busch"))
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.root.config(menu=menubar)

        top = ttk.Frame(self.root)
        top.pack(padx=10, pady=10, fill='x')

        ttk.Label(top, text="Select Deck:").pack(side='left')
        self.deck_var = tk.StringVar()
        self.deck_menu = ttk.Combobox(top, textvariable=self.deck_var, values=list_decklists(), state='readonly', width=40)
        self.deck_menu.pack(side='left', padx=5)
        self.deck_menu.bind("<Enter>", self.show_deck_tooltip)
        self.deck_menu.bind("<Leave>", lambda e: self.tooltip.hide())
        ttk.Button(top, text="Load", command=self.on_load_click).pack(side='left', padx=5)

        ttk.Label(top, text="Sort By:").pack(side='left', padx=(15, 0))
        self.sort_var = tk.StringVar(value=self.settings.get("sort_order", "Alphabetical"))
        self.sort_menu = ttk.Combobox(top, textvariable=self.sort_var, values=["Alphabetical", "Highest Value", "Card Type"], state='readonly', width=18)
        self.sort_menu.pack(side='left', padx=5)
        self.sort_menu.bind("<<ComboboxSelected>>", self.update_display)

        search_frame = ttk.Frame(self.root)
        search_frame.pack(padx=10, pady=(0, 10), fill='x')

        ttk.Label(search_frame, text="Search:").pack(side='left')
        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.pack(side='left', fill='x', expand=True, padx=5)
        self.search_entry.bind("<KeyRelease>", self.on_search)
        self.search_entry.bind("<Down>", self.focus_suggestion_box)
        ttk.Button(search_frame, text="Clear", command=self.clear_search).pack(side='left', padx=5)

        self.suggestion_box = SuggestionBox(self.root, self.search_entry, self.apply_suggestion)

        list_frame = ttk.Frame(self.root)
        list_frame.pack(padx=10, pady=5, fill='both', expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical")
        self.listbox = tk.Listbox(list_frame, width=80, height=25, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        self.listbox.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        self.listbox.bind("<Double-Button-1>", self.on_remove_card)
        self.listbox.bind("<Motion>", self.show_tooltip)
        self.listbox.bind("<Leave>", lambda e: self.tooltip.hide())
        self.listbox.bind("<Button-3>", self.open_card_link)

        self.price_label = ttk.Label(self.root, text="", font=('Segoe UI', 10, 'bold'))
        self.price_label.pack()

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=(0, 10))
        ttk.Button(button_frame, text="Remove Selected Card", command=self.remove_selected_card).pack(side='left', padx=10)
        ttk.Button(button_frame, text="Save and Exit", command=self.save_and_exit).pack(side='left', padx=10)

    def on_load_click(self):
        selected = self.deck_var.get()
        if selected:
            self.load_deck(selected)

    def load_deck(self, filename):
        self.filename = filename
        self.settings["last_deck"] = filename
        self.deck = load_decklist_original(filename)
        self.update_prices()
        self.update_display()
        if not self.deck:
            messagebox.showinfo("Deck Complete", "You’ve removed all cards from the deck!")

    def update_prices(self):
        self.prices, self.total_price, self.card_types = get_deck_price(self.deck)      

    def update_display(self, event=None):
        query = self.search_entry.get().lower().strip()
        self.listbox.delete(0, tk.END)
        self.filtered = {k: v for k, v in self.deck.items() if query in k.lower()}

        items = list(self.filtered.items())
        if self.sort_var.get() == "Card Type":
            items.sort(key=lambda x: self.card_types.get(x[0], "Other"))
        elif self.sort_var.get() == "Highest Value":
            items.sort(key=lambda x: (self.prices.get(x[0]) or 0) * x[1], reverse=True)
        else:
            items.sort(key=lambda x: x[0].lower())

        for name, count in items:
            total = (self.prices.get(name) or 0) * count
            self.listbox.insert(tk.END, f"{count}x {name} @ ${total:.2f}" if total else f"{count}x {name}")

        self.price_label.config(text=f"Total deck price: ${self.total_price:.2f}")

    def show_tooltip(self, event):
        index = self.listbox.nearest(event.y)
        if index >= 0 and index < self.listbox.size():
            line = self.listbox.get(index)
            count_str, name_part = line.split('x ', 1)
            name = name_part.split('@')[0].strip()
            count = self.deck.get(name, 0)
            price = self.prices.get(name)
            if price is not None:
                total = count * price
                self.tooltip.show(f"{count} × ${price:.2f} = ${total:.2f}", event.x_root, event.y_root)
            else:
                self.tooltip.hide()
        else:
            self.tooltip.hide()

    def on_remove_card(self, event):
        self._remove_selected_card()

    def remove_selected_card(self):
        self._remove_selected_card()

    def _remove_selected_card(self):
        selection = self.listbox.curselection()
        if not selection:
            return
        index = selection[0]
        selected_text = self.listbox.get(index)
        count_str, name_part = selected_text.split('x ', 1)
        name = name_part.split('@')[0].strip()
        if name in self.deck:
            total = self.deck[name]
            if total == 1:
                del self.deck[name]
            else:
                qty = simpledialog.askinteger("Remove Copies", f"{total} copies of '{name}' found. How many to remove?", minvalue=1, maxvalue=total)
                if qty:
                    if qty >= total:
                        del self.deck[name]
                    else:
                        self.deck[name] -= qty
            self.update_prices()
            self.update_display()
        if not self.deck:
            messagebox.showinfo("Deck Complete", "You’ve removed all cards from the deck!")

    def on_search(self, event=None):
        query = self.search_entry.get().lower().strip()
        matches = [name for name in self.deck if query in name.lower()]
        self.suggestion_box.show(matches[:10])
        self.update_display()
        if not self.deck:
            messagebox.showinfo("Deck Complete", "You’ve removed all cards from the deck!")

    def apply_suggestion(self, text):
        self.search_entry.delete(0, tk.END)
        self.search_entry.insert(0, text)
        self.update_display()
        if not self.deck:
            messagebox.showinfo("Deck Complete", "You’ve removed all cards from the deck!")

    def focus_suggestion_box(self, event):
        if self.suggestion_box and self.suggestion_box.listbox.size() > 0:
            self.suggestion_box.listbox.focus_set()
            self.suggestion_box.listbox.selection_set(0)

    def clear_search(self):
        self.search_entry.delete(0, tk.END)
        self.update_display()
        if not self.deck:
            messagebox.showinfo("Deck Complete", "You’ve removed all cards from the deck!")

    def save_and_exit(self):
        self.settings["sort_order"] = self.sort_var.get()
        self.settings["window_width"] = self.root.winfo_width()
        self.settings["window_height"] = self.root.winfo_height()
        save_settings(self.settings)
        if self.filename:
            save_decklist(self.filename, self.deck)
        self.root.quit()
    def export_deck(self, fmt):
        from backend import export_to_csv, export_to_arena
        if not self.deck:
            messagebox.showwarning("No Deck", "Load a deck first.")
            return
        name = os.path.splitext(self.filename)[0]
        if fmt == "csv":
            export_to_csv(self.deck, f"{name}.csv")
            messagebox.showinfo("Exported", f"{name}.csv saved in storage/")
        elif fmt == "arena":
            export_to_arena(self.deck, f"{name}.arena")
            messagebox.showinfo("Exported", f"{name}.arena saved in storage/")

    def show_category_summary(self):
        from backend import summarize_by_category
        if not self.deck:
            messagebox.showwarning("No Deck", "Load a deck first.")
            return
        summary = summarize_by_category(self.deck, self.prices, self.card_types)
        text = "\n".join(f"{k.capitalize()}: ${v:.2f}" for k, v in summary.items() if v > 0)
        messagebox.showinfo("Price Breakdown by Category", text or "No prices found.")

    def show_deck_tooltip(self, event):
        deck = self.deck_var.get()
        if deck:
            count = len(self.deck)
            self.tooltip.show(f"{deck} ({count} cards)", event.x_root, event.y_root)

    def open_card_link(self, event):
        index = self.listbox.nearest(event.y)
        if index >= 0:
            line = self.listbox.get(index)
            name = line.split('x ', 1)[1].split('@')[0].strip()
            import webbrowser
            webbrowser.open(f"https://scryfall.com/search?q={name.replace(' ', '+')}")