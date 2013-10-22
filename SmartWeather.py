import subprocess
import re
import time

while True:
    ts = time.time()
    subprocess.call(['./durhamWeather2.sh'])
    time.sleep(2)
    readFile = open('weatherDump.txt', 'r')
    writeFile = open('TempOut2.csv', 'a')
    for line in readFile:
        match = re.search('Images\s+(-?\d+)', line)
        if match is not None:
            print(match.group(1))
            writeFile.write('\n' + str(ts) + ',' + match.group(1))
            break
    readFile.close()
    writeFile.close()
    time.sleep(3600)
