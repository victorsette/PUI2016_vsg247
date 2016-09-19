from __future__ import print_function
import sys
import pylab as pl
import numpy as np
import json
import urllib as ulr
import csv

# checking if number of arguments is correct
if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python show_bus_locations.py <MTA_KEY> <BUS_LINE>")
    sys.exit()
    
# getting data from MTA API and storing in variable "data"  
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# counting active buses
active_buses = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

# getting the required data and storing in a list of lists
output = []
for i in range(active_buses):
    output.append(["","","",""])
    output[i][0] = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    output[i][1] = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    try:
        output[i][2] = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    except LookupError:
        output[i][2] = "N/A"
    try: 
        output[i][3] = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    except LookupError:
        output[i][3] = "N/A"
        
# writing the output on a .csv file
try:
    f = open(sys.argv[3], 'w')
    writer = csv.writer(f)
    for i in range(len(output)):
        writer.writerow((output[i][0],output[i][1],output[i][2],output[i][3]))
except IOError,e:
    print ('Error: ',e)
finally:
    if f:
        f.close()