import sys
import urllib2
import urllib

def Aggregation_Transit_Centralized(conf,inputs,outputs):

	start_point = inputs["StartPoint"]["value"]
	walkshed_collection = inputs["WalkshedCollection"]["value"]
	walkshed_union = inputs["WalkshedUnion"]["value"]
	poi = inputs["POI"]["value"]
	crime = inputs["Crime"]["value"]
	transit = inputs["Transit"]["value"]
	walking_time_period = inputs["WalkingTimePeriod"]["value"]
	distance_decay_function = inputs["DistanceDecayFunction"]["value"]

	params = urllib.urlencode({'start_point': start_point, 'walkshed_collection': walkshed_collection, 'walkshed_union': walkshed_union, 'poi': poi, 'crime': crime, 'transit': transit, 'walking_time_period': walking_time_period ,'distance_decay_function': distance_decay_function})
	
	aggregation_service_url = "http://127.0.0.1:9364/aggregation"

	try:
		aggregation_data = urllib2.urlopen(aggregation_service_url, params).read()
		
	except urllib2.HTTPError, e:
		print "HTTP error: %d" % e.code
	except urllib2.URLError, e:
		print "Network error: %s" % e.reason.args[1]

	outputs["AggregationResult"]["value"] = aggregation_data

	return 3

