import sys
import urllib2

def POI_Transit_Centralized(conf,inputs,outputs):

	walkshed = inputs["Walkshed"]["value"]

	walkshed = urllib2.quote(walkshed)

	poi_service_url = "http://127.0.0.1:9365/poi?walkshed="+walkshed

	try:
		poi_data = urllib2.urlopen(poi_service_url).read()
		
	except urllib2.HTTPError, e:
		print "HTTP error: %d" % e.code
	except urllib2.URLError, e:
		print "Network error: %s" % e.reason.args[1]

	outputs["POIResult"]["value"] = poi_data

	return 3

