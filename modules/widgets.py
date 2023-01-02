import subprocess

from libqtile import qtile
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from colors import theme
from .widget_defaults import widget_defaults

from libqtile.log_utils import logger

powerline_left = {
    "decorations": [
        PowerLineDecoration(
            path="rounded_left",
        )
    ]
}

powerline_right = {
    "decorations": [
        PowerLineDecoration(
            path="rounded_right",
        )
    ]
}

# Mouse callback functions
def launch_htop():
    qtile.cmd_spawn("alacritty -e htop")

def powermenu():
    qtile.cmd_spawn("sh /home/wingej0/.config/rofi/powermenu/type-4/powermenu.sh")

def power_management():
    qtile.cmd_spawn("sh /home/wingej0/.config/qtile/scripts/power-options.sh")

def init_widgets(instance):
    widgets_list = [
        widget.Sep(
            linewidth = 0,
            **powerline_right
        ),
        widget.TextBox(
            background=theme.color2,
            fontsize=30,
            foreground=theme.bg,
            text="",
            **powerline_left
        ),
        widget.GroupBox(
            background=theme.bg,
            disable_drag = True,
            font="FontAwesome6Free",
            fontsize=14,
            hide_unused=True,
            highlight_method="line",
            inactive=theme.fg,
            other_current_screen_border = theme.color5,
            other_screen_border = theme.color5,
            padding=3,
            this_current_screen_border=theme.color2,
            this_screen_border = theme.color4,
            urgent_alert_method = "line",
            urgent_border = theme.color1,
            urgent_text = theme.color1,
            use_mouse_wheel = False,
            **powerline_left
        ),
        widget.Sep(
            linewidth = 0,
            padding = 20
        ),
        widget.Sep(
            linewidth = 0,
            **powerline_right
        ),
        widget.CurrentLayoutIcon(
            scale = 0.6,
            background=theme.color6,
            foreground=theme.bg,
            **powerline_left
        ),
        widget.CurrentLayout(
            padding=10,
            **widget_defaults,
            **powerline_left
        ),
        widget.Sep(
            linewidth = 0,
            padding = 20,
        ),
        widget.WidgetBox(
            foreground=theme.bg,
            text_closed="",
            text_open="",
            widgets=[
                widget.Systray(),
            ]
        ),
        widget.Spacer(),
        widget.Sep(
            linewidth = 0,
            **powerline_right
        ),
        widget.TextBox(
            background = theme.color5,
            font = "FontAwesome6Free",
            fontsize = 18,
            foreground = theme.bg,
            text = "",
            **powerline_left
        ),
        widget.Clock(
            format=' %b %d, %Y | %I:%M %p',
            **widget_defaults,
        ),
        widget.TextBox(
            text=" ",
            mouse_callbacks = {
                'Button1' : powermenu,
            },
            **widget_defaults,
            **powerline_left,
        ),
        widget.Spacer(),
        widget.Sep(
            linewidth = 0,
            **powerline_right
        ),
        widget.TextBox(
            background=theme.color1,
            font = "FontAwesome6Free",
            fontsize = 18,
            foreground = theme.bg,
            text = "",
            **powerline_left
        ),
        widget.Battery(
            format = " {percent:2.0%}",
            **widget_defaults,
        ),
        widget.GenPollText(
            fmt = "{}",
            func = lambda: subprocess.check_output("/home/wingej0/.config/qtile/scripts/charge-thresholds.sh").decode("utf-8").strip(),
            update_interval = 300,
            **widget_defaults
        ),
        widget.TextBox(
            text="漣",
            mouse_callbacks = {
                'Button1' : power_management,
            },
            **widget_defaults,
            **powerline_left
        ),
        widget.Sep(
            linewidth = 0,
            padding = 20,
        ),
        widget.Sep(
            linewidth = 0,
            **powerline_right
        ),
         widget.TextBox(
            font = "FontAwesome6Free",
            fontsize = 18,
            background = theme.color3,
            foreground=theme.bg,
            text = "",
            **powerline_left
        ),
        widget.Memory(**widget_defaults),
        widget.TextBox(
            text="",
            mouse_callbacks = {
                 "Button1" : launch_htop
            },
            **widget_defaults,
            **powerline_left
        ),
        widget.Sep(
            linewidth = 0,
            padding = 20,
        ),
        widget.Sep(
            linewidth = 0,
            **powerline_right
        ),
        widget.TextBox(
            background=theme.color2_accent,
            font = "FontAwesome6Free",
            fontsize = 18,
            foreground = theme.bg,
            text = "",
            **powerline_left
        ),
        widget.Mpris2(
            display_metadata = ['xesam:title', 'xesam:artist', 'xesam:album'],
            fmt = "{}",
            name = "Spotify",
            objname = "org.mpris.MediaPlayer2.spotify",
            padding = 10,
            paused_text = " {track}",
            width = 175,
            **widget_defaults,
        ),
        widget.TextBox(
            text="",
            **widget_defaults,
            **powerline_left
        )
    ]

    return widgets_list
