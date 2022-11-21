# Import external files
from modules.groups import groups
# from modules.hooks import *
from modules.keys import keys, mod
from modules.layouts import layouts, floating_layout
from modules.screens import screens
from modules.scratchpads import *

from typing import List  # noqa: F401

from libqtile import layout
from libqtile.config import Match

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = True
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True
wmname = "Qtile 0.22.1"
