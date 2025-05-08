import tkinter as tk
from tkinter import ttk
from theme_manager import apply_theme
from colors import THEMES

def launch_preview_ui():
    root = tk.Tk()
    root.title("Deck Tool - Preview UI")
    root.geometry("1000x600")

    current_theme = tk.StringVar(value="Green")  # default theme

    def on_theme_change(event=None):
        apply_theme(root, current_theme.get())

    # Top control bar
    control_frame = tk.Frame(root)
    control_frame.pack(fill='x', padx=10, pady=10)

    tk.Label(control_frame, text="Theme:").pack(side='left')
    theme_selector = ttk.Combobox(
        control_frame,
        textvariable=current_theme,
        values=sorted(THEMES.keys()),
        state='readonly',
        width=20
    )
    theme_selector.pack(side='left', padx=5)
    theme_selector.bind("<<ComboboxSelected>>", on_theme_change)

    tk.Label(control_frame, text="Select Deck:").pack(side='left', padx=(20, 0))
    ttk.Combobox(control_frame, values=["Deck 1", "Deck 2"], state='readonly', width=30).pack(side='left', padx=5)
    ttk.Button(control_frame, text="Load").pack(side='left', padx=5)

    tk.Label(control_frame, text="Sort By:").pack(side='left', padx=(20, 0))
    ttk.Combobox(control_frame, values=["Alphabetical", "Highest Value", "Card Type"], state='readonly', width=20).pack(side='left', padx=5)

    # Search bar
    search_frame = tk.Frame(root)
    search_frame.pack(fill='x', padx=10)

    tk.Label(search_frame, text="Search:").pack(side='left')
    ttk.Entry(search_frame, width=40).pack(side='left', padx=5, fill='x', expand=True)
    ttk.Button(search_frame, text="Clear").pack(side='left', padx=5)

    # Main content
    content_frame = tk.Frame(root)
    content_frame.pack(fill='both', expand=True, padx=10, pady=10)

    deck_frame = tk.Frame(content_frame)
    deck_frame.pack(side='left', fill='both', expand=True)

    deck_list = tk.Listbox(
        deck_frame,
        font=("Segoe UI", 10),
        activestyle='none'
    )
    for i in range(40):
        deck_list.insert(tk.END, f"{i+1}x Placeholder Card Name")
    deck_list.pack(fill='both', expand=True)

    image_frame = tk.Frame(content_frame, width=250)
    image_frame.pack(side='right', fill='y', padx=(10, 0))

    image_label = tk.Label(
        image_frame,
        text="Card Image\n[Placeholder]",
        anchor="center",
        relief="solid",
        width=30,
        font=("Segoe UI", 10, "italic"),
        padx=10,
        pady=10,
        justify="center"
    )
    image_label.pack(fill='y', expand=True)

    # Bottom bar
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(fill='x', padx=10, pady=(5, 10))

    tk.Label(bottom_frame, text="Total Deck Price: $123.45", font=("Segoe UI", 10, "bold")).pack(side='left')
    ttk.Button(bottom_frame, text="Save and Exit").pack(side='right')

    apply_theme(root, current_theme.get())  # apply default theme
    root.mainloop()

if __name__ == "__main__":
    launch_preview_ui()
