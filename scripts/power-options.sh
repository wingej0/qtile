#!/bin/bash

selected=$(ls /home/wingej0/.config/qtile/scripts/system76-power-options|rofi -dmenu -p "Run: ")&&
bash /home/wingej0/.config/qtile/scripts/system76-power-options/$selected