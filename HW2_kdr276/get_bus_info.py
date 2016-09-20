from __future__ import print_function
import sys
import json
import csv
import urllib as ulr

MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]
BUS_Linecsv = sys.argv[3]


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&" \
      "VehicleMonitoringDetailLevel=calls&LineRef=%s" %(MTA_KEY,BUS_LINE)

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

writer = csv.writer(open(sys.argv[3], "w"))
headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']

writer.writerow(headers)

for bus in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
    row = []
    row.append(str(bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
    row.append(str(bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']))
    if bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'] == " ":
        row.append('N/A')
    else:
        row.append(str(bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']))
    if bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances'][
                       'PresentableDistance'] == " ":
        row.append('N/A')
    else:
        row.append(str(bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances'][
                       'PresentableDistance']))
    writer.writerow(row)

"""
code used to generate .csv file found from
http://michelleminkoff.com/2011/02/01/making-the-structured-usable-transform-json-into-a-csv/
accessed Sept. 19 2016

"""
