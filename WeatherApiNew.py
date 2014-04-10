#!/usr/bin/python
import time
import re
from datetime import datetime,  timedelta
from subprocess import Popen, PIPE

dataFile = open('/Users/aram/Documents/Python/Files/weatherApiData.csv', 'a')
utc_dt = time.time()
today = datetime.today()

output = Popen(['curl', '-s', 'http://api.wunderground.com/api/72fa5852e40ed29a/conditions/q/NC/Durham.xml'], stdout=PIPE)
weatherReport = output.stdout.read()
info = re.search('<temp_f>(\d+\.\d+)', weatherReport)
if info is not None:
	temp = info.group(1)
else:
	temp = "Error getting temperature."
info = re.search('<relative_humidity>(\d+)%', weatherReport)
if info is not None:
	humidity = info.group(1)
else:
	humidity = "Error getting humidity."
info = re.search('<pressure_in>(\d+\.\d+)', weatherReport)
if info is not None:
	pressure = info.group(1)
else:
	pressure = "Error getting pressure."
info = re.search('<dewpoint_f>(\d+\.?\d*)', weatherReport)
if info is not None:
	dewPoint = info.group(1)
else:
	dewPoint = "Error getting dew point."
info = re.search('<precip_1hr_in>(\d+\.\d+)', weatherReport)
if info is not None:
	percip = info.group(1)
else:
	percip = "Error getting percipitaion."
dataFile.write(str(utc_dt) + ', ' + today.strftime('%H:%M on %b %d %Y') + str(temp) + ', ' + str(humidity) + ', ' +	str(pressure) + ', ' + str(dewPoint) + ', ' + str(percip) + '\n')
dataFile.close()
	