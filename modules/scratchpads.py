from .groups import groups

from libqtile.config import ScratchPad, DropDown, Match

# Define scratchpads
groups.append(ScratchPad("scratchpad", [
    DropDown("term", "alacritty", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("calendar", "/usr/bin/google-chrome-stable --app=https://calendar.google.com", 
        width=0.9, height=0.9, x=0.05, y=0.05, opacity=0.9, match=Match(wm_class="calendar.google.com")),
    DropDown("volume", "pavucontrol", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown("newTask", "alacritty -e python /home/wingej0/.local/bin/task.py",
        width=0.7, height=0.05, x=0.15, y=0.475, opacity=1),
    DropDown("alo-scraper", "alacritty -e sh /home/wingej0/.config/qtile/scripts/alo-update.sh",
        width=0.7, height=0.5, x=0.15, y=0.25, opacity=1),
    DropDown("md-notes", "alacritty -e vim Documents/wingej0-notes/Scratchpad.md",
        width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
]))