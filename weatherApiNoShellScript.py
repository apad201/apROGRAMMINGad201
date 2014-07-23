from urllib2 import urlopen
import xml.etree.ElementTree as ET
import re
import time
import re
from datetime import datetime,  timedelta


utc_dt = time.time()
today = datetime.today()
f = open('weatherOut.csv', 'a')
response = urlopen('http://api.wunderground.com/api/1935ba83adac87e6/conditions/q/NC/Charlotte.xml')
final = response.read()

info = re.search('<temp_f>(\d+\.\d+)', final)
if info is not None:
	temp = info.group(1)
else:
	temp = "Error getting temperature."
info = re.search('<relative_humidity>(\d+)%', final)
if info is not None:
	humidity = info.group(1)
else:
	humidity = "Error getting humidity."
info = re.search('<pressure_in>(\d+\.\d+)', final)
if info is not None:
	pressure = info.group(1)
else:
	pressure = "Error getting pressure."
info = re.search('<dewpoint_f>(\d+\.?\d*)', final)
if info is not None:
	dewPoint = info.group(1)
else:
	dewPoint = "Error getting dew point."
info = re.search('<precip_1hr_in>(\d+\.\d+)', final)
if info is not None:
	percip = info.group(1)
else:
	percip = "Error getting percipitaion."
f.write(str(utc_dt) + ', ' + today.strftime('%H:%M on %b %d %Y') + str(temp) + ', ' + str(humidity) + ', ' +	str(pressure) + ', ' + str(dewPoint) + ', ' + str(percip) + '\n')
f.close()
f = open('weatherOut.csv', 'r')
strFinal = f.read()
print strFinal
f.close()
