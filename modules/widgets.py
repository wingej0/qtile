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
    qtile.cmd_spawn("xfce4-session-logout")

def power_management():
    qtile.cmd_spawn("xfce4-power-manager-settings")

def init_widgets(instance):
    widgets_list = [
        widget.Sep(
            linewidth = 0,
            **powerline_right
        ),
        widget.TextBox(
            background=theme.color2,
            fontsize=24,
            foreground=theme.bg,
            text="",
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

def init_bottom_widgets(instance):
    bottom_widgets = [
        widget.TextBox(
            background=theme.color2,
            fontsize = 20,
            foreground=theme.bg,
            text=" ",   
        ),
        widget.GenPollText(
            background=theme.color2,
            foreground=theme.bg,
            func = lambda: subprocess.check_output("/home/wingej0/.config/qtile/scripts/hostname.sh").decode("utf-8").strip(),
            update_interval = 6000,
        ),
        widget.TextBox(
            background=theme.color2,
            foreground=theme.bg,
            text=" ", 
            **powerline_left  
        ),
        widget.TextBox(
            background=theme.color3,
            fontsize = 20,
            foreground=theme.bg,
            text=" ",   
        ),
        widget.Net(
            background=theme.color3,
            format="{interface} : {down} ↓↑ {up}",
            foreground=theme.bg,
        ),
        widget.TextBox(
            background=theme.color3,
            foreground=theme.bg,
            text=" ", 
            **powerline_left  
        ),
        widget.TextBox(
            background=theme.color6,
            fontsize = 20,
            foreground=theme.bg,
            text="ﱖ",   
        ),
        widget.CurrentLayout(
            background=theme.color6,
            foreground=theme.bg,
            **powerline_left
        ),
        widget.TaskList(
            foreground = theme.fg,
            background = theme.bg,
            border = None,
            margin=3,
            padding=0,
            highlight_method = "block",
            title_width_method = "uniform",
            rounded = False,
            txt_floating = "🗗 ",
            txt_maximized = "🗖 ",
            txt_minimized = "🗕 ",
            urgent_alert_method="text",
            urgent_border=theme.bg,
        ),
        widget.Systray(),
        widget.TextBox(
            background=theme.bg,
            foreground=theme.bg,
            text=" ", 
            **powerline_right  
        ),
        widget.TextBox(
            background=theme.color1,
            fontsize = 20,
            foreground=theme.bg,
            text="", 
        ),
        widget.Battery(
            background=theme.color1,
            foreground=theme.bg,
            format = "{percent:2.0%} ({hour:d}:{min:02d})",
            mouse_callbacks = {
                'Button1' : power_management,
            },
        ),
        widget.TextBox(
            background=theme.color1,
            foreground=theme.bg,
            text=" ", 
            **powerline_right  
        ),
        widget.TextBox(
            background=theme.color6,
            fontsize = 20,
            foreground=theme.bg,
            text="", 
        ),
        widget.CPU(
            background=theme.color6,
            foreground=theme.bg,
            format="{freq_current}GHz {load_percent}%"
        ),
        widget.TextBox(
            background=theme.color6,
            foreground=theme.bg,
            text=" ", 
            **powerline_right  
        ),
        widget.TextBox(
            background=theme.color3,
            foreground=theme.bg,
            text="﨎",
        ),
        widget.ThermalSensor(
            background=theme.color3,
            foreground=theme.bg,
        ),
        widget.TextBox(
            background=theme.color3,
            foreground=theme.bg,
            text=" ",
            **powerline_right
        ),
        widget.TextBox(
            background=theme.color2,
            fontsize = 20,
            foreground=theme.bg,
            text="",
        ),
        widget.Memory(
            background=theme.color2,
            foreground=theme.bg,
            mouse_callbacks = {
                'Button1' : launch_htop,
            },
        ),
        widget.TextBox(
            background=theme.color2,
            fontsize = 20,
            foreground=theme.bg,
            text=" ",
        ),
    ]

    return bottom_widgets