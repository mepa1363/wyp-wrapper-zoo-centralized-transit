import sys
import urllib2

def Crime_Transit_Centralized(conf,inputs,outputs):

	walkshed = inputs["Walkshed"]["value"]

	walkshed = urllib2.quote(walkshed)

	crime_service_url = "http://127.0.0.1:9366/crime?walkshed="+walkshed

	try:
		crime_data = urllib2.urlopen(crime_service_url).read()
		
	except urllib2.HTTPError, e:
		print "HTTP error: %d" % e.code
	except urllib2.URLError, e:
		print "Network error: %s" % e.reason.args[1]

	outputs["CrimeResult"]["value"] = crime_data

	return 3

