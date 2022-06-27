#!/bin/env python3
# Python script for getting cpu usage in flux line protocol format

import psutil
import datetime, time, calendar

cpu = psutil.cpu_percent()
timestamp = int(time.mktime(datetime.datetime.now().timetuple())*1000000000)
# used_ram = psutil.virtual_memory().used // 1000000
free_ram = psutil.virtual_memory().free // 1000000
print("cpu_busy,main_host=win_server cpu_busy={},free_ram={} {}".format(cpu, free_ram, timestamp))