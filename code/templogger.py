import time
from fluentmetrics import FluentMetric

m = FluentMetric().with_namespace("HomeTemp").with_stream_id("HomeTemp")

try:
    while True:
        tempfile = open("/sys/bus/w1/devices/28-0000073e3ff8/w1_slave")
        thetext = tempfile.read()
        tempfile.close()
        tempdata = thetext.split("\n")[1].split(" ")[9]
        temperature = float(tempdata[2:])
        temperature = temperature / 1000
        m.log(MetricName="CurrentTemp", Value=temperature, Unit="None")
        # print temperature
        # print "logged"

        time.sleep(300)
except KeyboardInterrupt:
    pass
