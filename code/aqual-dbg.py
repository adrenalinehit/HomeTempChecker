import time
import aqi
import serial

ser = serial.Serial('/dev/ttyUSB0')

data = []

for index in range(0,10):
    datum = ser.read()
    data.append(datum)

pmtwo = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10
myaqi = aqi.to_aqi([(aqi.POLLUTANT_PM25, str(pmtwo)),
                    (aqi.POLLUTANT_PM10, str(pmten))])
aqi = float(myaqi)

print(pmtwo)
print(pmten)
print(myaqi)
