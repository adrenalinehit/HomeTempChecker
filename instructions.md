# Useful command line incantations

## Rudimentary get shit working
- lsusb
- date --set="2023-12-05 20:50:00.000"
- lsmod
- modprobe w1_gpio //mounts/starts the temp sensor (https://www.waveshare.com/wiki/Raspberry_Pi_Tutorial_Series:_1-Wire_DS18B20_Sensor)

## Wifi and networking
- iwlist wlanX scan
- ifup
- service networking restart
- wpa_supplicant for the wifi

## Python stuff
- pip install cloudwatch-fluent-metrics
- apt-get install python-gpiozero

(_all with various levels of sudo'ing!_)
