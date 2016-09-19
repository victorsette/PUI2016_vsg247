from __future__ import print_function
import sys
import pylab as pl
import numpy as np
import json
import urllib as ulr


# checking if number of arguments is correct
if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python show_bus_locations.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

# getting data from MTA API and storing in variable "data"  
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# counting active buses
active_buses = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']) - 2

# creating array where the location data is stored 
location = np.zeros((active_buses,3))

# printing initial information 
print("Bus Line: " + sys.argv[2])
print("Number of Active Buses : ", active_buses)

# collecting bus location info and printing it out
for i in range(active_buses):
    location[i,0] = i
    location[i,1] = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    location[i,2] = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    print("Bus ",'{:.0f}'.format(location[i,0])," is at latitude ",location[i,2], " and longitude ", location[i,1])