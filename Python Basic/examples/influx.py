import argparse

from influxdb import InfluxDBClient
client = InfluxDBClient('192.168.100.39', '8086', 'meditech', 'meditech2017', 'collectd')
query = 'select value from cpu_load_short;'
print(client)