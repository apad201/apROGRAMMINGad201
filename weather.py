import urllib2
import json
import smbus
import time
bus = smbus.SMBus(1)
address = 0x04
p = 1
i = 0
transmit_chars = []
f=urllib2.urlopen('http://api.wunderground.com/api/fa0de6f4ede37dd9/geolookup/conditions/q/NC/Durham.json')
json_string = f.read()
parsed_json = json.loads(json_string)
temp_f = parsed_json['current_observation']['temp_f']
print temp_f
f.close()
for char in temp_f:
    bus.write_byte_data(4,0,ord(char))

