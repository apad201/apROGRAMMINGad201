import subprocess
import re
import time
from datetime import datetime, timedelta


    

while True:
    utc_dt = time.time()
    subprocess.call(['./durhamWeather2.sh'])
    time.sleep(2)
    readFile = open('weatherDump.txt', 'r')
    writeFile = open('TempOut3.csv', 'a')
    for line in readFile:
        match = re.search('Images\s+(-?\d+)', line)
        if match is not None:
            print(match.group(1))
            today = datetime.today()
            writeFile.write('\n' + str(utc_dt) + ',' + today.strftime('%H:%M on %b %d %Y') + ',' + match.group(1))
            break
    readFile.close()
    writeFile.close()
    time.sleep(3600)
 
