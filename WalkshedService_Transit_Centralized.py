import sys
import urllib2
from time import strftime

def Walkshed_Transit_Centralized(conf,inputs,outputs):

	fromPlace = inputs["StartPoint"]["value"]
	walkTime = inputs["WalkingPeriod"]["value"]
	walkSpeed = inputs["WalkingSpeed"]["value"]
	output = inputs["WalkshedOutput"]["value"]
	
	time = strftime("%Y-%m-%dT%H:%M:%S")

	otp_url = "http://gisciencegroup.ucalgary.ca:8080/opentripplanner-api-webapp/ws/iso?layers=traveltime&styles=mask&batch=true&fromPlace="+fromPlace+"&toPlace=51.09098935,-113.95179705&time="+time+"&mode=WALK&maxWalkDistance=10000&walkTime="+walkTime+"&walkSpeed="+walkSpeed+"&output="+output

	try:
		data = urllib2.urlopen(otp_url).read()
		
	except urllib2.HTTPError, e:
		print "HTTP error: %d" % e.code
	except urllib2.URLError, e:
		print "Network error: %s" % e.reason.args[1]

	outputs["WalkshedResult"]["value"] = data

	return 3

