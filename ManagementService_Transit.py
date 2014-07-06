import sys
import urllib2

def Management_Transit(conf,inputs,outputs):

	start_point = inputs["StartPoint"]["value"]
	start_time = inputs["StartTime"]["value"]
	walking_time_period = inputs["WalkingTimePeriod"]["value"]
	walking_speed = inputs["WalkingSpeed"]["value"]
	bus_waiting_time = inputs["BusWaitingTime"]["value"]
	bus_ride_time = inputs["BusRideTime"]["value"]
	distance_decay_function = inputs["DistanceDecayFunction"]["value"]
	
	management_url = "http://127.0.0.1:9363/management?start_point="+start_point+"&start_time="+start_time+"&walking_time_period="+walking_time_period+"&walking_speed="+walking_speed+"&bus_waiting_time="+bus_waiting_time+"&bus_ride_time="+bus_ride_time+"&distance_decay_function="+distance_decay_function;


	try:
		data = urllib2.urlopen(management_url).read()
		
	except urllib2.HTTPError, e:
		print "HTTP error: %d" % e.code
	except urllib2.URLError, e:
		print "Network error: %s" % e.reason.args[1]

	outputs["AccessibilityScore"]["value"] = data

	return 3

