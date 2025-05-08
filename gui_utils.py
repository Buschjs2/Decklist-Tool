import os
import json
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import webbrowser
import urllib.request
from PIL import Image, ImageTk
import io
from backend import (
    list_decklists, load_decklist_original, save_decklist,
    export_to_csv, export_to_arena, summarize_by_category, get_deck_price
)

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

class ImagePanel:
    def __init__(self, root):
        self.root = root
        self.frame = None
        self.image_label = None
        self.text_label = None

    def build_panel(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.pack(side='right', padx=10, pady=10, anchor='n')
        self.image_label = ttk.Label(self.frame)
        self.image_label.pack()
        self.text_label = ttk.Label(self.frame, justify="center")
        self.text_label.pack()

    def show(self, card_name):
        url = f"https://api.scryfall.com/cards/named?exact={card_name}"
        try:
            with urllib.request.urlopen(url) as response:
                data = json.load(response)
                image_url = data["image_uris"]["normal"]
                prices = data.get("prices", {})
                usd = prices.get("usd") or "N/A"
                foil = prices.get("usd_foil") or "N/A"
                etched = prices.get("usd_etched") or "N/A"

            with urllib.request.urlopen(image_url) as img_response:
                img_data = img_response.read()
            image = Image.open(io.BytesIO(img_data)).resize((223, 310))
            tk_image = ImageTk.PhotoImage(image)

            self.image_label.config(image=tk_image)
            self.image_label.image = tk_image
            self.text_label.config(text=f"Market: ${usd}\nFoil: ${foil}\nEtched: ${etched}")
        except Exception:
            self.hide()

    def hide(self):
        if self.image_label:
            self.image_label.config(image='')
            self.image_label.image = None
        if self.text_label:
            self.text_label.config(text='')

class DeckLogic:
    def __init__(self, gui):
        self.gui = gui
        self.deck = {}
        self.filtered = {}
        self.prices = {}
        self.card_types = {}
        self.total_price = 0.0
        self.filename = ""
        self.suggestion_box = None
        self.search_entry = None
        self.listbox = None
        self.price_label = None

    def set_suggestion_box(self, sb): self.suggestion_box = sb
    def set_search_entry(self, entry): self.search_entry = entry
    def set_listbox(self, lb): self.listbox = lb
    def set_price_label(self, pl): self.price_label = pl

    def list_decks(self): return list_decklists()

    def load_deck(self, filename):
        self.filename = filename
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

        sort_method = self.gui.sort_var.get()
        if sort_method == "Card Type":
            grouped = {}
            for name, count in self.filtered.items():
                ctype = self.card_types.get(name, "Other")
                grouped.setdefault(ctype, []).append((name, count))
            for ctype in sorted(grouped.keys()):
                self.listbox.insert(tk.END, f"[{ctype}]")
                for name, count in sorted(grouped[ctype], key=lambda x: x[0].lower()):
                    self.listbox.insert(tk.END, f"  {count}x {name}")
            return
        elif sort_method == "Highest Value":
            items.sort(key=lambda x: (self.prices.get(x[0]) or 0) * x[1], reverse=True)
        else:
            items.sort(key=lambda x: x[0].lower())

        for name, count in items:
            self.listbox.insert(tk.END, f"{count}x {name}")

        if self.price_label:
            self.price_label.config(text=f"Total deck price: ${self.total_price:.2f}")

    def on_card_select(self, event=None):
        selection = self.listbox.curselection()
        if not selection: return
        index = selection[0]
        line = self.listbox.get(index)
        if line.startswith("["): return
        name = line.split('x ', 1)[1].strip()
        self.gui.image_panel.show(name)

    def show_context_menu(self, event):
        index = self.listbox.nearest(event.y)
        if index < 0 or index >= self.listbox.size(): return
        self.listbox.selection_clear(0, tk.END)
        self.listbox.selection_set(index)
        selected = self.listbox.get(index)
        if selected.startswith("["): return
        card_name = selected.split('x ', 1)[1].strip()
        menu = tk.Menu(self.gui.root, tearoff=0)
        menu.add_command(label="View on Scryfall", command=lambda: self.open_card_link(card_name))
        menu.add_command(label="Remove Card", command=self.remove_selected_card)
        menu.add_command(label="Copy Name", command=lambda: self.copy_to_clipboard(card_name))
        menu.tk_popup(event.x_root, event.y_root)

    def remove_selected_card(self):
        selection = self.listbox.curselection()
        if not selection: return
        index = selection[0]
        line = self.listbox.get(index)
        name = line.split('x ', 1)[1].strip()
        if name not in self.deck: return
        count = self.deck[name]
        if count == 1:
            del self.deck[name]
        else:
            qty = simpledialog.askinteger("Remove Copies", f"{count} copies of '{name}'. How many to remove?", minvalue=1, maxvalue=count)
            if qty:
                if qty >= count:
                    del self.deck[name]
                else:
                    self.deck[name] -= qty
        self.update_prices()
        self.update_display()

    def on_search(self, event=None):
        query = self.search_entry.get().lower().strip()
        matches = [name for name in self.deck if query in name.lower()]
        self.suggestion_box.show(matches[:10])
        self.update_display()

    def apply_suggestion(self, name):
        self.search_entry.delete(0, tk.END)
        self.search_entry.insert(0, name)
        self.update_display()

    def focus_suggestion_box(self, event):
        if self.suggestion_box and self.suggestion_box.listbox.size() > 0:
            self.suggestion_box.listbox.focus_set()
            self.suggestion_box.listbox.selection_set(0)

    def clear_search(self):
        self.search_entry.delete(0, tk.END)
        self.update_display()

    def open_card_link(self, name):
        webbrowser.open(f"https://scryfall.com/search?q={name.replace(' ', '+')}")

    def copy_to_clipboard(self, text):
        self.gui.root.clipboard_clear()
        self.gui.root.clipboard_append(text)
        self.gui.root.update()

    def export_deck(self, fmt):
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
        if not self.deck:
            messagebox.showwarning("No Deck", "Load a deck first.")
            return
        summary = summarize_by_category(self.deck, self.prices, self.card_types)
        text = "\n".join(f"{k.capitalize()}: ${v:.2f}" for k, v in summary.items() if v > 0)
        messagebox.showinfo("Price Breakdown by Category", text or "No prices found.")
