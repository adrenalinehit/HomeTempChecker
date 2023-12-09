import time
import aqi
from fluentmetrics import FluentMetric

pm2 = FluentMetric().with_namespace("AirQual").with_stream_id("pm2")
pm10 = FluentMetric().with_namespace("AirQual").with_stream_id("pm10")
pmaqi = FluentMetric().with_namespace("AirQual").with_stream_id("aqi")

ser = serial.Serial('/dev/ttyUSB0')

try:
    while True:
      data = []
      
      for index in range(0,10):
          datum = ser.read()
          data.append(datum)
      
      pmtwo = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
      pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10
      myaqi = aqi.to_aqi([(aqi.POLLUTANT_PM25, str(pmtwo)),
                          (aqi.POLLUTANT_PM10, str(pmten))])
      aqi = float(myaqi)
      
      pm2.log(MetricName="CurrentPM25", Value=pmtwo, Unit="None")
      pm10.log(MetricName="CurrentPM10", Value=pmten, Unit="None")
      pmaqi.log(MetricName="CurrentAQI", Value=aqi, Unit="None")
      
      time.sleep(300)
      
except KeyboardInterrupt:
    pass
  
