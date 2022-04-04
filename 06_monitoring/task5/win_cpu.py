#!/bin/env python3
import psutil
import datetime, time

cpu = psutil.cpu_percent()
timestamp = time.mktime(datetime.datetime.now().timetuple())

print("cpu_busy,main_host=server1 cpu_busy{} {}".format(cpu, timestamp))