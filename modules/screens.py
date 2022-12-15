from .widgets import init_widgets
from colors import theme

from qtile_extras import widget
from libqtile import bar
from libqtile.config import Screen

# Initialize widgets
main_widgets = init_widgets(1)
secondary_widgets = init_widgets(2)
vertical_widgets = init_widgets(3)

# Remove systray from second monitor (Qtile only supports systray on one monitor)
del secondary_widgets[8:9]

# Remove all widgets from vertical monitor except groupbox and layout
# Add a spacer for aesthetics
del vertical_widgets[7:30]
vertical_widgets.insert(3, widget.Spacer())

# Define 3 monitors
screens = [
    Screen(
        top=bar.Bar(
            widgets=main_widgets,
            size=30,
            background="#00000000",
            margin=8, 
            opacity=0.9
        ),
    ),
    Screen(
        top=bar.Bar(
            widgets=secondary_widgets,
            size=30,
            background="#00000000",
            margin=8, 
            opacity=0.9
        ),
    ),
    Screen(
        top=bar.Bar(
            widgets=vertical_widgets,
            size=30,
            background="#00000000",
            margin=8, 
            opacity=0.9
        ),
    ),
]
