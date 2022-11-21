#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#start sxhkd to replace Qtile native key-bindings
run sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &

#starting utility applications at boot time
run nm-applet &
picom &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
# /usr/lib/xfce4/notifyd/xfce4-notifyd &
blueberry-tray &
caffeine &
nitrogen --restore &
system76-power daemon
