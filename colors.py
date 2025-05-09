# colors.py - Centralized color definitions for MTG color combinations

THEMES = {
    "White": {
        "bg": "#efefef",        # very light gray background
        "accent": "#d7d7d7",    # subtle accent panel
        "text": "#3A3A3A",      # softened near-black for less strain
        "button": "#bfbfbf",    # light gray button
        "highlight": "#8f8f8f",   # darker gray for selected/hovered states
        "panel": "#d7d7d7",  # subtle accent panel for sidebars
        "entry": "#ffffff",  # white for entry fields
        "listbox": "#ffffff", # white for listboxes
        "image_bg": "#ffffff", # white for image backgrounds
        "search_bar_bg": "#d7d7d7"  # New color for the search bar
},
    "Blue": {
        "bg": "#d0e7f9",       # light blue background
        "accent": "#a0b8cf",   # medium blue for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#91b3d7",   # slightly darker blue for buttons
        "highlight": "#4f78a0", # darker blue for highlights/selections
        "panel": "#c3d5e6",  # medium blue for panels
        "entry": "#d0e7f9",  # light blue for entry fields
        "listbox": "#d0e7f9", # light blue for listboxes
        "image_bg": "#d0e7f9", # light blue for image backgrounds
        "search_bar_bg": "#c3d5e6"  # New color for the search bar
},
    "Black": {
        "bg": "#1e1e1e",       # deep black for the main background
        "accent": "#3c3c3c",   # dark gray for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#7a7a7a",   # medium gray for buttons
        "highlight": "#d7d7d7", # light gray for highlights/selections
        "panel": "#3c3c3c",  # dark gray for panels
        "entry": "#1e1e1e",  # black for entry fields
        "listbox": "#1e1e1e", # black for listboxes
        "image_bg": "#1e1e1e", # black for image backgrounds
        "search_bar_bg": "#3c3c3c"  # New color for the search bar
},
    "Red": {
        "bg": "#5a1d1d",       # deep red for the main background
        "accent": "#b84a39",   # medium red for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#e49273",   # light red for buttons
        "highlight": "#f6d6b3", # very light red for highlights/selections
        "panel": "#b84a39",  # medium red for panels
        "entry": "#5a1d1d",  # deep red for entry fields
        "listbox": "#5a1d1d", # deep red for listboxes
        "image_bg": "#5a1d1d", # deep red for image backgrounds
        "search_bar_bg": "#b84a39"  # New color for the search bar
},
    "Green": {
        "bg": "#23331f",       # deep green for the main background
        "accent": "#6a995e",   # light green for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#8dcc7e",   # medium green for buttons
        "highlight": "#4f78a0", # darker blue for highlights/selections
        "panel": "#6a995e",  # light green for panels
        "entry": "#23331f",  # deep green for entry fields
        "listbox": "#23331f", # deep green for listboxes
        "image_bg": "#23331f", # deep green for image backgrounds
        "search_bar_bg": "#6a995e"  # New color for the search bar
},
    "Colorless": {
        "bg": "#efefef",       # very light gray for the main background
        "accent": "#d7d7d7",   # subtle accent panel
        "text": "#3A3A3A",     # softened near-black for less strain
        "button": "#bfbfbf",   # light gray for buttons
        "highlight": "#8f8f8f", # darker gray for selected/hovered states
        "panel": "#d7d7d7",  # subtle accent panel for sidebars
        "entry": "#ffffff",  # white for entry fields
        "listbox": "#ffffff", # white for listboxes
        "image_bg": "#ffffff", # white for image backgrounds
        "search_bar_bg": "#d7d7d7"  # New color for the search bar
},
    "Azorius": {
        "bg": "#e7f0f8",       # light blue for the main background
        "accent": "#c3d5e6",   # medium blue for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#a0b8cf",   # slightly darker blue for buttons
        "highlight": "#708fa6", # darker blue for highlights/selections
        "panel": "#c3d5e6",  # medium blue for panels
        "entry": "#e7f0f8",  # light blue for entry fields
        "listbox": "#e7f0f8", # light blue for listboxes
        "image_bg": "#e7f0f8", # light blue for image backgrounds
        "search_bar_bg": "#c3d5e6"  # New color for the search bar
},
    "Boros": {
        "bg": "#f8f7f3",       # very light gray for the main background
        "accent": "#e49273",   # medium red for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#b84a39",   # light red for buttons
        "highlight": "#5a1d1d", # deep red for highlights/selections
        "panel": "#e49273",  # medium red for panels
        "entry": "#f8f7f3",  # very light gray for entry fields
        "listbox": "#f8f7f3", # very light gray for listboxes
        "image_bg": "#f8f7f3", # very light gray for image backgrounds
        "search_bar_bg": "#e49273"  # New color for the search bar
},
    "Dimir": {
        "bg": "#2e4c6d",       # deep blue for the main background
        "accent": "#1e1e1e",   # black for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#4f78a0",   # medium blue for buttons
        "highlight": "#91b3d7", # light blue for highlights/selections
        "panel": "#1e1e1e",  # black for panels
        "entry": "#2e4c6d",  # deep blue for entry fields
        "listbox": "#2e4c6d", # deep blue for listboxes
        "image_bg": "#2e4c6d", # deep blue for image backgrounds
        "search_bar_bg": "#1e1e1e"  # New color for the search bar
},
    "Orzhov": {
        "bg": "#f8f7f3",       # very light gray for the main background
        "accent": "#1e1e1e",   # black for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#bbb6a6",   # medium gray for buttons
        "highlight": "#7a7a7a", # dark gray for highlights/selections
        "panel": "#1e1e1e",  # black for panels
        "entry": "#f8f7f3",  # very light gray for entry fields
        "listbox": "#f8f7f3", # very light gray for listboxes
        "image_bg": "#f8f7f3", # very light gray for image backgrounds
        "search_bar_bg": "#1e1e1e"  # New color for the search bar
},
    "Rakdos": {
        "bg": "#1e1e1e",       # deep black for the main background
        "accent": "#5a1d1d",   # deep red for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#b84a39",   # light red for buttons
        "highlight": "#f6d6b3", # very light red for highlights/selections
        "panel": "#5a1d1d",  # deep red for panels
        "entry": "#1e1e1e",  # black for entry fields
        "listbox": "#1e1e1e", # black for listboxes
        "image_bg": "#1e1e1e", # black for image backgrounds
        "search_bar_bg": "#5a1d1d"  # New color for the search bar
},
    "Gruul": {
        "bg": "#5a1d1d",       # deep red for the main background
        "accent": "#23331f",   # deep green for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#6a995e",   # light green for buttons
        "highlight": "#e49273", # light red for highlights/selections
        "panel": "#23331f",  # deep green for panels
        "entry": "#5a1d1d",  # deep red for entry fields
        "listbox": "#5a1d1d", # deep red for listboxes
        "image_bg": "#5a1d1d", # deep red for image backgrounds
        "search_bar_bg": "#23331f"  # New color for the search bar
},
    "Selesnya": {
        "bg": "#f8f7f3",       # very light gray for the main background
        "accent": "#6a995e",   # light green for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#8dcc7e",   # medium green for buttons
        "highlight": "#bbb6a6", # light gray for highlights/selections
        "panel": "#6a995e",  # light green for panels
        "entry": "#f8f7f3",  # very light gray for entry fields
        "listbox": "#f8f7f3", # very light gray for listboxes
        "image_bg": "#f8f7f3", # very light gray for image backgrounds
        "search_bar_bg": "#6a995e"  # New color for the search bar
},
    "Simic": {
        "bg": "#d0e7f9",       # light blue for the main background
        "accent": "#6a995e",   # light green for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#91b3d7",   # slightly darker blue for buttons
        "highlight": "#4f78a0", # darker blue for highlights/selections
        "panel": "#6a995e",  # light green for panels
        "entry": "#d0e7f9",  # light blue for entry fields
        "listbox": "#d0e7f9", # light blue for listboxes
        "image_bg": "#d0e7f9", # light blue for image backgrounds
        "search_bar_bg": "#6a995e"  # New color for the search bar        
},
    "Izzet": {
        "bg": "#d0e7f9",       # light blue for the main background
        "accent": "#e49273",   # medium red for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#b84a39",   # light red for buttons
        "highlight": "#4f78a0", # darker blue for highlights/selections
        "panel": "#e49273",  # medium red for panels
        "entry": "#d0e7f9",  # light blue for entry fields
        "listbox": "#d0e7f9", # light blue for listboxes
        "image_bg": "#d0e7f9", # light blue for image backgrounds
        "search_bar_bg": "#e49273"  # New color for the search bar
},
    "Golgari": {
        "bg": "#1e1e1e",       # deep black for the main background
        "accent": "#46663f",   # deep green for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#6a995e",   # light green for buttons
        "highlight": "#8dcc7e", # light green for highlights/selections
        "panel": "#46663f",  # deep green for panels
        "entry": "#1e1e1e",  # black for entry fields
        "listbox": "#1e1e1e", # black for listboxes
        "image_bg": "#1e1e1e", # black for image backgrounds
        "search_bar_bg": "#46663f"  # New color for the search bar
},
    "Esper": {
        "bg": "#f8f7f3",       # very light gray for the main background
        "accent": "#2e4c6d",   # deep blue for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#1e1e1e",   # black for buttons
        "highlight": "#91b3d7", # light blue for highlights/selections
        "panel": "#2e4c6d",  # deep blue for panels
        "entry": "#f8f7f3",  # very light gray for entry fields
        "listbox": "#f8f7f3", # very light gray for listboxes
        "image_bg": "#f8f7f3", # very light gray for image backgrounds
        "search_bar_bg": "#2e4c6d"  # New color for the search bar
},
    "Grixis": {
        "bg": "#2e4c6d",       # deep blue for the main background
        "accent": "#5a1d1d",   # deep red for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#3c3c3c",   # dark gray for buttons
        "highlight": "#f6d6b3", # very light red for highlights/selections
        "panel": "#5a1d1d",  # deep red for panels
        "entry": "#2e4c6d",  # deep blue for entry fields
        "listbox": "#2e4c6d", # deep blue for listboxes
        "image_bg": "#2e4c6d", # deep blue for image backgrounds
        "search_bar_bg": "#5a1d1d"  # New color for the search bar
},
    "Jund": {
        "bg": "#1e1e1e",       # deep black for the main background
        "accent": "#b84a39",   # medium red for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#6a995e",   # light green for buttons
        "highlight": "#e49273", # light red for highlights/selections
        "panel": "#b84a39",  # medium red for panels
        "entry": "#1e1e1e",  # black for entry fields
        "listbox": "#1e1e1e", # black for listboxes
        "image_bg": "#1e1e1e", # black for image backgrounds
        "search_bar_bg": "#b84a39"  # New color for the search bar
},
    "Naya": {
        "bg": "#f8f7f3",       # very light gray for the main background
        "accent": "#6a995e",   # light green for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#b84a39",   # light red for buttons
        "highlight": "#e49273", # light red for highlights/selections
        "panel": "#6a995e",  # light green for panels
        "entry": "#f8f7f3",  # very light gray for entry fields
        "listbox": "#f8f7f3", # very light gray for listboxes
        "image_bg": "#f8f7f3", # very light gray for image backgrounds
        "search_bar_bg": "#6a995e"  # New color for the search bar
},
    "Bant": {
        "bg": "#f8f7f3",       # very light gray for the main background
        "accent": "#6a995e",   # light green for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#d0e7f9",   # light blue for buttons
        "highlight": "#91b3d7", # light blue for highlights/selections
        "panel": "#6a995e",  # light green for panels
        "entry": "#f8f7f3",  # very light gray for entry fields
        "listbox": "#f8f7f3", # very light gray for listboxes
        "image_bg": "#f8f7f3", # very light gray for image backgrounds
        "search_bar_bg": "#6a995e"  # New color for the search bar
},
    "Abzan": {
        "bg": "#1e1e1e",       # deep black for the main background
        "accent": "#f8f7f3",   # very light gray for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#6a995e",   # light green for buttons
        "highlight": "#8dcc7e", # light green for highlights/selections
        "panel": "#f8f7f3",  # very light gray for panels
        "entry": "#1e1e1e",  # black for entry fields
        "listbox": "#1e1e1e", # black for listboxes
        "image_bg": "#1e1e1e", # black for image backgrounds
        "search_bar_bg": "#f8f7f3"  # New color for the search bar
},
    "Mardu": {
        "bg": "#1e1e1e",       # deep black for the main background
        "accent": "#f6d6b3",   # very light red for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#b84a39",   # light red for buttons
        "highlight": "#e49273", # light red for highlights/selections
        "panel": "#f6d6b3",  # very light red for panels
        "entry": "#1e1e1e",  # black for entry fields
        "listbox": "#1e1e1e", # black for listboxes
        "image_bg": "#1e1e1e", # black for image backgrounds
        "search_bar_bg": "#f6d6b3"  # New color for the search bar
},
    "Sultai": {
        "bg": "#1e1e1e",       # deep black for the main background
        "accent": "#6a995e",   # light green for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#2e4c6d",   # deep blue for buttons
        "highlight": "#4f78a0", # darker blue for highlights/selections
        "panel": "#6a995e",  # light green for panels
        "entry": "#1e1e1e",  # black for entry fields
        "listbox": "#1e1e1e", # black for listboxes
        "image_bg": "#1e1e1e", # black for image backgrounds
        "search_bar_bg": "#6a995e"  # New color for the search bar
},
    "Temur": {
        "bg": "#6a995e",       # light green for the main background
        "accent": "#d0e7f9",   # light blue for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#b84a39",   # light red for buttons
        "highlight": "#4f78a0", # darker blue for highlights/selections
        "panel": "#d0e7f9",  # light blue for panels
        "entry": "#6a995e",  # light green for entry fields
        "listbox": "#6a995e", # light green for listboxes
        "image_bg": "#6a995e", # light green for image backgrounds
        "search_bar_bg": "#d0e7f9"  # New color for the search bar
},
    "Glint": {
        "bg": "#1e1e1e",       # deep black for the main background
        "accent": "#f6d6b3",   # very light red for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#4f78a0",   # medium blue for buttons
        "highlight": "#6a995e", # light green for highlights/selections
        "panel": "#f6d6b3",  # very light red for panels
        "entry": "#1e1e1e",  # black for entry fields
        "listbox": "#1e1e1e", # black for listboxes
        "image_bg": "#1e1e1e", # black for image backgrounds
        "search_bar_bg": "#f6d6b3"  # New color for the search bar
},
    "Dune": {
        "bg": "#f8f7f3",       # very light gray for the main background
        "accent": "#5a1d1d",   # deep red for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#6a995e",   # light green for buttons
        "highlight": "#b84a39", # light red for highlights/selections
        "panel": "#5a1d1d",  # deep red for panels
        "entry": "#f8f7f3",  # very light gray for entry fields
        "listbox": "#f8f7f3", # very light gray for listboxes
        "image_bg": "#f8f7f3", # very light gray for image backgrounds
        "search_bar_bg": "#5a1d1d"  # New color for the search bar
},
    "Ink": {
        "bg": "#1e1e1e",       # deep black for the main background
        "accent": "#4f78a0",   # medium blue for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#5a1d1d",   # deep red for buttons
        "highlight": "#d0e7f9", # light blue for highlights/selections
        "panel": "#4f78a0",  # medium blue for panels
        "entry": "#1e1e1e",  # black for entry fields
        "listbox": "#1e1e1e", # black for listboxes
        "image_bg": "#1e1e1e", # black for image backgrounds
        "search_bar_bg": "#4f78a0"  # New color for the search bar
},
    "Witch": {
        "bg": "#1e1e1e",       # deep black for the main background
        "accent": "#6a995e",   # light green for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#4f78a0",   # medium blue for buttons
        "highlight": "#000000", # black for highlights/selections
        "panel": "#6a995e",  # light green for panels
        "entry": "#1e1e1e",  # black for entry fields
        "listbox": "#1e1e1e", # black for listboxes
        "image_bg": "#1e1e1e", # black for image backgrounds
        "search_bar_bg": "#6a995e"  # New color for the search bar
},
    "Yore": {
        "bg": "#f8f7f3",       # very light gray for the main background
        "accent": "#b84a39",   # light red for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#d0e7f9",   # light blue for buttons
        "highlight": "#6a995e", # light green for highlights/selections
        "panel": "#b84a39",  # light red for panels
        "entry": "#f8f7f3",  # very light gray for entry fields
        "listbox": "#f8f7f3", # very light gray for listboxes
        "image_bg": "#f8f7f3", # very light gray for image backgrounds
        "search_bar_bg": "#b84a39"  # New color for the search bar
},
    "Jeskai": {
        "bg": "#f8f7f3",       # very light gray for the main background
        "accent": "#d0e7f9",   # light blue for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#e49273",   # medium red for buttons
        "highlight": "#4f78a0", # darker blue for highlights/selections
        "panel": "#d0e7f9",  # light blue for panels
        "entry": "#f8f7f3",  # very light gray for entry fields
        "listbox": "#f8f7f3", # very light gray for listboxes
        "image_bg": "#f8f7f3", # very light gray for image backgrounds
        "search_bar_bg": "#d0e7f9"  # New color for the search bar
},
    "FiveColor": {
        "bg": "#f8f7f3",       # very light gray for the main background
        "accent": "#6a995e",   # light green for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#b84a39",   # light red for buttons
        "highlight": "#4f78a0", # darker blue for highlights/selections
        "panel": "#6a995e",  # light green for panels
        "entry": "#f8f7f3",  # very light gray for entry fields
        "listbox": "#f8f7f3", # very light gray for listboxes
        "image_bg": "#f8f7f3", # very light gray for image backgrounds
        "search_bar_bg": "#6a995e"  # New color for the search bar
},
}
