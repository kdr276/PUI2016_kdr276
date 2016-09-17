from __future__ import print_function
import sys
import json
import urllib as ulr

MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&" \
      "VehicleMonitoringDetailLevel=calls&LineRef=%s" %(MTA_KEY,BUS_LINE)

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

print("Bus Line: " +
      data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney'][
          'PublishedLineName'])
count = 0
for bus in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
    count += 1
print("Number of Active Buses: " + str(count))

count = 0
for bus in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
    count +=1
    print ("Bus " + str(count) + " is at longitude " +
           (str(bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])) +
            " and latitude " + str(bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']))