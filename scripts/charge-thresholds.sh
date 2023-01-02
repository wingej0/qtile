#! /bin/bash

profile=`tlp-stat -s | grep Mode | awk '{print ($(NF))}'`
printf "(%s)" $profile
