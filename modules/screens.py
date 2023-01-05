from .widgets import init_widgets, init_bottom_widgets
from colors import theme

from qtile_extras import widget
from libqtile import bar
from libqtile.config import Screen

# Initialize widgets
main_widgets = init_widgets(1)
secondary_widgets = init_widgets(2)
vertical_widgets = init_widgets(3)
bottom_widgets = init_bottom_widgets(1)
secondary_bottom_widgets = init_bottom_widgets(2)

# Remove all widgets from vertical monitor except groupbox and Mpris2
del vertical_widgets[10:15]

# Remove Systray from bottom bar for second monitor
del secondary_bottom_widgets[9:10]

# Define 3 monitors
screens = [
    Screen(
        top=bar.Bar(
            widgets=main_widgets,
            size=30,
            background="#00000000",
            margin=4, 
            opacity=0.9
        ),
        bottom=bar.Bar(
            widgets=bottom_widgets,
            size=24,
            background=theme.bg,
            margin=0, 
            opacity=0.9
        ),
        wallpaper=theme.wallpaper1,
        wallpaper_mode="fill"
    ),
    Screen(
        top=bar.Bar(
            widgets=vertical_widgets,
            size=30,
            background="#00000000",
            margin=4, 
            opacity=0.9
        ),
        wallpaper=theme.wallpaper3,
        wallpaper_mode="fill"
    ),
    Screen(
        top=bar.Bar(
            widgets=secondary_widgets,
            size=30,
            background="#00000000",
            margin=4, 
            opacity=0.9
        ),
        bottom=bar.Bar(
            widgets=secondary_bottom_widgets,
            size=24,
            background=theme.bg,
            margin=0, 
            opacity=0.9
        ),
        wallpaper=theme.wallpaper2,
        wallpaper_mode="fill"
    ),
]
