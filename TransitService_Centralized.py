import sys
import urllib2

def Transit_Centralized(conf,inputs,outputs):

	start_time = inputs["StartTime"]["value"]
	walkshed = inputs["Walkshed"]["value"]
	walking_time_period = inputs["WalkingTime"]["value"]
	walking_speed = inputs["WalkingSpeed"]["value"]
	bus_waiting_time = inputs["BusWaitingTime"]["value"]
	bus_ride_time = inputs["BusRideTime"]["value"]

	walkshed = urllib2.quote(walkshed)

	transit_service_url = "http://127.0.0.1:9367/transit?start_time="+start_time+"&walkshed="+walkshed+"&walking_time_period="+walking_time_period+"&walking_speed="+walking_speed+"&bus_waiting_time="+bus_waiting_time+"&bus_ride_time="+bus_ride_time

	try:
		transit_data = urllib2.urlopen(transit_service_url).read()
		
	except urllib2.HTTPError, e:
		print "HTTP error: %d" % e.code
	except urllib2.URLError, e:
		print "Network error: %s" % e.reason.args[1]

	outputs["TransitResult"]["value"] = transit_data

	return 3

