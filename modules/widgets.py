import subprocess

from libqtile import widget
from colors import theme
from .widget_defaults import widget_defaults

def init_widgets(instance):
    widgets_list = [
        widget.GroupBox(
            active=theme.fg,
            background=theme.bg,
            disable_drag = True,
            font="FontAwesome6Free",
            fontsize=17,
            hide_unused=True,
            highlight_method="block",
            inactive=theme.fg,
            margin=3,
            other_current_screen_border = theme.color5,
            other_screen_border = theme.color5,
            padding=7,
            rounded=True,
            this_current_screen_border=theme.color2,
            this_screen_border = theme.color4,
            urgent_alert_method = "block",
            urgent_border = theme.color1,
            urgent_text = theme.color1,
            use_mouse_wheel = False,
        ),
        widget.TaskList(
            border = theme.color2,
            borderwidth = 1,
            font = "Fira Code Nerd Font Bold",
            fontsize = 12,
            highlight_method = "block",
            icon_size = 0,
            margin = 3,
            max_title_width=250,
            padding_y = 7,
            padding_x = 20,
            rounded = True,
            title_width_method = "uniform",
            urgent_alert_method = "border",
            urgent_border = theme.color1,
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10
        ),
        widget.Systray(
            icon_size = 20,
            padding = 4,
            **widget_defaults
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10
        ),
        widget.CurrentLayoutIcon(
            scale = 0.5,
            **widget_defaults
        ),
        widget.CurrentLayout(**widget_defaults),
        widget.Sep(
            linewidth = 0,
            padding = 10
        ),
        widget.TextBox(
            font = "FontAwesome6Free",
            fontsize = 18,
            foreground = theme.color1,
            text = " ",
        ),
        widget.Battery(
            format = "{percent:2.0%} | {hour:d}:{min:02d}",
            **widget_defaults
        ),
        widget.GenPollText(
            fmt = "{}",
            func = lambda: subprocess.check_output("/home/wingej0/.config/qtile/scripts/charge-thresholds.sh").decode("utf-8").strip(),
            update_interval = 300,
            **widget_defaults
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10
        ),
        widget.TextBox(
            font = "FontAwesome6Free",
            fontsize = 18,
            foreground = theme.color3,
            text = "",
        ),
        widget.Memory(**widget_defaults),
        widget.Sep(
            linewidth = 0,
            padding = 10
        ),
        widget.GenPollText(
            fmt = "{}",
            font = "FontAwesome6Free",
            fontsize = 18,
            foreground = theme.color4,
            func = lambda: subprocess.check_output("/home/wingej0/.config/qtile/scripts/check-spotify.sh").decode("utf-8").strip(),
            update_interval = 60,
        ),
        widget.Mpris2(
            display_metadata = ['xesam:title', 'xesam:artist', 'xesam:album'],
            fmt = " {} ",
            name = "Spotify",
            objname = "org.mpris.MediaPlayer2.spotify",
            padding = 10,
            paused_text = " {track}",
            width = 175,
            **widget_defaults
        ),
        widget.TextBox(
            font = "FontAwesome6Free",
            fontsize = 18,
            foreground = theme.color5,
            text = " ",
        ),
        widget.Clock(
            format='%b %d | %I:%M %p',
            **widget_defaults
        ),
        widget.Sep(
            linewidth = 0,
            padding = 20,
        ),
    ]

    return widgets_list