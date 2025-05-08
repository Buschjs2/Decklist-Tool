import tkinter as tk

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
