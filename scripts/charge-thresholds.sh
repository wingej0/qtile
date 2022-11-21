#! /bin/bash

status=`acpi -a | cut -d' ' -f3 | cut -d- -f1`

if [ $status = "on" ]; then
	system76-power charge-thresholds | grep Profile | awk '{status=$(NF); sub("_", " ", status); print status}'
else
	profile=`system76-power profile | grep Profile | awk '{print ($(NF))}'`
	printf "(%s)" $profile
fi	
