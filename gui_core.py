import tkinter as tk
from tkinter import ttk, messagebox
from backend import save_decklist
from config import load_settings, save_settings
from gui_utils import DeckLogic, SuggestionBox, Tooltip, ImagePanel

class DeckGUI:
    def __init__(self, root):
        self.root = root
        self.settings = load_settings()
        self.deck_logic = DeckLogic(self)
        self.tooltip = Tooltip(root)
        self.image_panel = ImagePanel(root)
        self.setup_window()
        self.build_ui()

        if self.settings.get("last_deck"):
            self.deck_logic.load_deck(self.settings["last_deck"])

    def setup_window(self):
        w = self.settings.get("window_width", 1000)
        h = self.settings.get("window_height", 600)
        self.root.geometry(f"{w}x{h}")
        self.root.title("Deck Viewer")

    def build_ui(self):
        self.build_menu_bar()

        # --- Top frame: deck and sort controls ---
        top = ttk.Frame(self.root)
        top.pack(padx=10, pady=10, fill='x')

        ttk.Label(top, text="Select Deck:").pack(side='left')
        self.deck_var = tk.StringVar()
        self.deck_menu = ttk.Combobox(top, textvariable=self.deck_var, values=self.deck_logic.list_decks(), state='readonly', width=40)
        self.deck_menu.pack(side='left', padx=5)
        self.deck_menu.bind("<Enter>", self.show_deck_tooltip)
        self.deck_menu.bind("<Leave>", lambda e: self.tooltip.hide())
        ttk.Button(top, text="Load", command=self.on_load_click).pack(side='left', padx=5)

        ttk.Label(top, text="Sort By:").pack(side='left', padx=(15, 0))
        self.sort_var = tk.StringVar(value=self.settings.get("sort_order", "Alphabetical"))
        self.sort_menu = ttk.Combobox(top, textvariable=self.sort_var, values=["Alphabetical", "Highest Value", "Card Type"], state='readonly', width=18)
        self.sort_menu.pack(side='left', padx=5)
        self.sort_menu.bind("<<ComboboxSelected>>", self.deck_logic.update_display)

        # --- Search bar ---
        search_frame = ttk.Frame(self.root)
        search_frame.pack(padx=10, pady=(0, 10), fill='x')

        ttk.Label(search_frame, text="Search:").pack(side='left')
        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.pack(side='left', fill='x', expand=True, padx=5)
        self.search_entry.bind("<KeyRelease>", self.deck_logic.on_search)
        self.search_entry.bind("<Down>", self.deck_logic.focus_suggestion_box)
        ttk.Button(search_frame, text="Clear", command=self.deck_logic.clear_search).pack(side='left', padx=5)

        self.deck_logic.set_search_entry(self.search_entry)
        self.suggestion_box = SuggestionBox(self.root, self.search_entry, self.deck_logic.apply_suggestion)
        self.deck_logic.set_suggestion_box(self.suggestion_box)

        # --- Deck list display and scrollbar ---
        display_frame = ttk.Frame(self.root)
        display_frame.pack(padx=10, pady=5, fill='both', expand=True)

        scrollbar = ttk.Scrollbar(display_frame, orient="vertical")
        self.listbox = tk.Listbox(display_frame, width=80, height=25, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        self.listbox.bind("<<ListboxSelect>>", self.deck_logic.on_card_select)
        self.listbox.bind("<Button-3>", self.deck_logic.show_context_menu)
        self.listbox.bind("<Leave>", lambda e: self.image_panel.hide())

        self.deck_logic.set_listbox(self.listbox)

        # --- Bottom controls ---
        self.price_label = ttk.Label(self.root, text="", font=('Segoe UI', 10, 'bold'))
        self.price_label.pack()
        self.deck_logic.set_price_label(self.price_label)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=(0, 10))
        ttk.Button(button_frame, text="Save and Exit", command=self.save_and_exit).pack(side='left', padx=10)

        # --- Image Panel ---
        self.image_panel.build_panel(self.root)

    def build_menu_bar(self):
        menubar = tk.Menu(self.root)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Export to CSV", command=lambda: self.deck_logic.export_deck("csv"))
        filemenu.add_command(label="Export to Arena", command=lambda: self.deck_logic.export_deck("arena"))
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        toolsmenu = tk.Menu(menubar, tearoff=0)
        toolsmenu.add_command(label="Category Summary", command=self.deck_logic.show_category_summary)
        menubar.add_cascade(label="Tools", menu=toolsmenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Deck Tool v1.7 by Joe Busch"))
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.root.config(menu=menubar)

    def on_load_click(self):
        selected = self.deck_var.get()
        if selected:
            self.deck_logic.load_deck(selected)

    def show_deck_tooltip(self, event):
        deck = self.deck_var.get()
        if deck:
            count = len(self.deck_logic.deck)
            self.tooltip.show(f"{deck} ({count} cards)", event.x_root, event.y_root)

    def save_and_exit(self):
        self.settings["sort_order"] = self.sort_var.get()
        self.settings["window_width"] = self.root.winfo_width()
        self.settings["window_height"] = self.root.winfo_height()
        save_settings(self.settings)
        if self.deck_logic.filename:
            save_decklist(self.deck_logic.filename, self.deck_logic.deck)
        self.root.quit()
