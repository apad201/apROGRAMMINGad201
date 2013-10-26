#!/usr/bin/python
from datetime import datetime
import time

def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + float(offset)
PITIME = time.time()
print(PITIME)
current = datetime_from_utc_to_local(PITIME)
print(current)
