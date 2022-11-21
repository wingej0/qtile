from types import SimpleNamespace

from themes.themes import *

# Options are nord, everforest, dracula, pop, arc, gruvbox, manjaro

selected_theme = arc
theme = SimpleNamespace(**selected_theme)