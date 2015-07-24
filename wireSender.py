import smbus
import time
bus = smbus.SMBus(1)
while True:
        p = 1
        i = 0
        transmit_chars = []
        message = raw_input("Message: ")
        address = raw_input("Address: ")
        for char in message:
                i = i + 1
                transmit_chars.append(char)

        for item in transmit_chars:
                bus.write_byte_data(int(address),0,ord(str(item)))

