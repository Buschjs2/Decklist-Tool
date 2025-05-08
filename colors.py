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
        "image_bg": "#ffffff" # white for image backgrounds
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
        "image_bg": "#d0e7f9" # light blue for image backgrounds
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
        "image_bg": "#1e1e1e" # black for image backgrounds
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
        "image_bg": "#5a1d1d" # deep red for image backgrounds
},
    "Green": {
        "bg": "#23331f",       # deep green for the main background
        "accent": "#46663f",   # medium green for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#6a995e",   # light green for buttons
        "highlight": "#9ee68d" # very light green for highlights/selections
},
    "Colorless": {
        "bg": "#efefef",       # very light gray for the main background
        "accent": "#d7d7d7",   # subtle accent panel
        "text": "#3A3A3A",     # softened near-black for less strain
        "button": "#bfbfbf",   # light gray for buttons
        "highlight": "#8f8f8f" # darker gray for selected/hovered states
},
    "Azorius": {
        "bg": "#e7f0f8",       # light blue for the main background
        "accent": "#c3d5e6",   # medium blue for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#a0b8cf",   # slightly darker blue for buttons
        "highlight": "#708fa6" # darker blue for highlights/selections
},
    "Boros": {
        "bg": "#f8f7f3",       # very light gray for the main background
        "accent": "#e49273",   # medium red for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#b84a39",   # light red for buttons
        "highlight": "#5a1d1d" # deep red for highlights/selections
},
    "Dimir": {
        "bg": "#2e4c6d",       # deep blue for the main background
        "accent": "#1e1e1e",   # black for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#4f78a0",   # medium blue for buttons
        "highlight": "#91b3d7" # light blue for highlights/selections
},
    "Orzhov": {
        "bg": "#f8f7f3",       # very light gray for the main background
        "accent": "#1e1e1e",   # black for sidebars/panels
        "text": "#000000",     # black for high contrast text
        "button": "#bbb6a6",   # medium gray for buttons
        "highlight": "#7a7a7a" # dark gray for highlights/selections
},
    "Rakdos": {
        "bg": "#1e1e1e",       # deep black for the main background
        "accent": "#5a1d1d",   # deep red for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#b84a39",   # light red for buttons
        "highlight": "#f6d6b3" # very light red for highlights/selections
},
    "Gruul": {
        "bg": "#5a1d1d",       # deep red for the main background
        "accent": "#23331f",   # deep green for sidebars/panels
        "text": "#FFFFFF",     # bright white for high contrast text
        "button": "#6a995e",   # light green for buttons
        "highlight": "#e49273" # light red for highlights/selections
},
    
    
    "Rakdos": {"bg": "#1e1e1e", "accent": "#5a1d1d", "text": "#FFFFFF", "button": "#b84a39", "highlight": "#f6d6b3"},
    "Gruul": {"bg": "#5a1d1d", "accent": "#23331f", "text": "#FFFFFF", "button": "#6a995e", "highlight": "#e49273"},
    "Selesnya": {"bg": "#f8f7f3", "accent": "#6a995e", "text": "#000000", "button": "#8dcc7e", "highlight": "#bbb6a6"},
    "Orzhov": {"bg": "#1e1e1e", "accent": "#f8f7f3", "text": "#FFFFFF", "button": "#bbb6a6", "highlight": "#7a7a7a"},
    "Simic": {"bg": "#d0e7f9", "accent": "#6a995e", "text": "#000000", "button": "#91b3d7", "highlight": "#4f78a0"},
    "Izzet": {"bg": "#d0e7f9", "accent": "#e49273", "text": "#000000", "button": "#b84a39", "highlight": "#4f78a0"},
    "Golgari": {"bg": "#1e1e1e", "accent": "#46663f", "text": "#FFFFFF", "button": "#6a995e", "highlight": "#8dcc7e"},
    "Esper": {"bg": "#f8f7f3", "accent": "#2e4c6d", "text": "#000000", "button": "#1e1e1e", "highlight": "#91b3d7"},
    "Grixis": {"bg": "#2e4c6d", "accent": "#5a1d1d", "text": "#FFFFFF", "button": "#3c3c3c", "highlight": "#f6d6b3"},
    "Jund": {"bg": "#1e1e1e", "accent": "#b84a39", "text": "#FFFFFF", "button": "#6a995e", "highlight": "#e49273"},
    "Naya": {"bg": "#f8f7f3", "accent": "#6a995e", "text": "#000000", "button": "#b84a39", "highlight": "#e49273"},
    "Bant": {"bg": "#f8f7f3", "accent": "#6a995e", "text": "#000000", "button": "#d0e7f9", "highlight": "#91b3d7"},
    "Abzan": {"bg": "#1e1e1e", "accent": "#f8f7f3", "text": "#FFFFFF", "button": "#6a995e", "highlight": "#8dcc7e"},
    "Mardu": {"bg": "#1e1e1e", "accent": "#f6d6b3", "text": "#FFFFFF", "button": "#b84a39", "highlight": "#e49273"},
    "Sultai": {"bg": "#1e1e1e", "accent": "#6a995e", "text": "#FFFFFF", "button": "#2e4c6d", "highlight": "#4f78a0"},
    "Temur": {"bg": "#6a995e", "accent": "#d0e7f9", "text": "#000000", "button": "#b84a39", "highlight": "#4f78a0"},
    "Glint": {"bg": "#1e1e1e", "accent": "#f6d6b3", "text": "#FFFFFF", "button": "#4f78a0", "highlight": "#6a995e"},
    "Dune": {"bg": "#f8f7f3", "accent": "#5a1d1d", "text": "#000000", "button": "#6a995e", "highlight": "#b84a39"},
    "Ink": {"bg": "#1e1e1e", "accent": "#4f78a0", "text": "#FFFFFF", "button": "#5a1d1d", "highlight": "#d0e7f9"},
    "Witch": {"bg": "#1e1e1e", "accent": "#6a995e", "text": "#FFFFFF", "button": "#4f78a0", "highlight": "#000000"},
    "Yore": {"bg": "#f8f7f3", "accent": "#b84a39", "text": "#000000", "button": "#d0e7f9", "highlight": "#6a995e"},
    "Jeskai": {"bg": "#f8f7f3", "accent": "#d0e7f9", "text": "#000000", "button": "#e49273", "highlight": "#4f78a0"},
    "FiveColor": {"bg": "#f0f0f0", "accent": "#8dcc7e", "text": "#000000", "button": "#91b3d7", "highlight": "#b84a39"}
}
