#! /bin/bash

spotify=`playerctl -l | grep spotify`

if [ "$spotify" = "spotify" ]; then
    echo ""
else
    echo ""
fi