#!/bin/sh
# Bash script for getting cpu usage in flux line protocol format

cpu=$(grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage "%"}')
time=$(date +%s%N)

echo "cpu_load,main_host=lin_server cpu_busy=$cpu $time"
