import sys
import urllib2
import urllib

def Union_Centralized(conf,inputs,outputs):

	walkshed_collection = inputs["WalkshedCollection"]["value"]
	
	params = urllib.urlencode({'walkshed_collection': walkshed_collection})

	union_service_url = "http://127.0.0.1:9368/union"

	try:
		union_data = urllib2.urlopen(union_service_url, params).read()
		
	except urllib2.HTTPError, e:
		print "HTTP error: %d" % e.code
	except urllib2.URLError, e:
		print "Network error: %s" % e.reason.args[1]

	outputs["UnionResult"]["value"] = union_data

	return 3

