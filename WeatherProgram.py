import subprocess
import re
import time

filebuffer = ''
i = 0
while True:
    i = 0
    pi = subprocess.Popen(['./WeatherReport2.sh'],stdout=subprocess.PIPE)
    for line in iter(pi.stdout.readline, ''):    
     #   print line.rstrip()
        if i==1:
            match = re.search(r'(\s+)(-?\d+)', line)
            print match.group(2)
            filebuffer = match.group(2)
        i = i+1
        
    print filebuffer
    Myfile = open('TempOut.csv', 'a')
    Myfile.write(filebuffer + ',')
    Myfile.close()
    time.sleep(900)
    
    
