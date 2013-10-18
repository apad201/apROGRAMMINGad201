import subprocess
import re
import time

filebuffer = ''
while True:
    i = 0
    pi = subprocess.Popen(['./WeatherReport2.sh'],stdout=subprocess.PIPE)
    for line in iter(pi.stdout.readline, ''):
        print(line.decode("utf-8"))
        if i==1:
            temp = re.search('Images(\s+)(-?\d+).+F', line.decode("utf-8"))
        #    print(temp.group(2))
        if i==4:   
            humidity = re.search('Humidity:(\s+)(\d+)', line.decode("utf-8"))
        #    print(humidity.group(2))
        i = i+1

    filebuffer = temp.group(2) + ',' + humidity.group(2)    
    #print(filebuffer)
    Myfile = open('NewTempOut.csv', 'a')
    Myfile.write(filebuffer + '\n')
    Myfile.close()
    time.sleep(86400)
    
