import os
import time
from collections import deque
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY
from prometheus_client import start_http_server

class CustomCollector1():

    def __init__(self):
        pass


    def collect(self):
        with open("out.txt", "r") as file:
            [dd_progress] = deque(file, maxlen=1) or ['']
        value = CounterMetricFamily("SERVER_STATUS", 'Help text', labels='value')
        value.add_metric(["dd_progress"], dd_progress)
        yield value


if __name__ == '__main__':
    start_http_server(8000)
    REGISTRY.register(CustomCollector1())
    while True:
        time.sleep(5)
