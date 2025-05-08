from tkinter import Tk
from gui_core import DeckGUI

def launch_app():
    root = Tk()
    app = DeckGUI(root)
    root.mainloop()
