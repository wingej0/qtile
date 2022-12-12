from .widgets import init_widgets
from colors import theme

from libqtile import bar
from libqtile.config import Screen

# Initialize widgets
main_widgets = init_widgets(1)
secondary_widgets = init_widgets(2)
vertical_widgets = init_widgets(3)

# Remove SysTray from secondary monitors
# del secondary_widgets[3:4]
del vertical_widgets[3:4]

# Remove all but the layout widgets from vertical monitor
del vertical_widgets[6:18]

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
            widgets=secondary_widgets,
            size=30,
            background="#00000000",
            margin=0, 
            opacity=0.9
        ),
    ),
]
