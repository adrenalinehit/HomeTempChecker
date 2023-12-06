# Useful command line incantations

## Rudimentary get shit working
- you'll need an AWS account and some creds in an AWS profile configured somewhere (for the logging to work)
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

## AWS
- I've shared the cloudwatch dashboard publicly - that's up to you

## Running it!

- chmod +x logtemp.sh
- sh logtemp.sh

(_all with various levels of sudo'ing!_)
