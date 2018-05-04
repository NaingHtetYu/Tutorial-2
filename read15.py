import urllib2, json, base64
accesstoken = "3RG0N6NVEWTN56RRH37L"
#accesstoken = "3RG0N6NVEWTN56RRH3"
url = "http://data.unistats.ac.uk/api/v4/KIS/Institutions.json"
#url = "http://data.unistats.ac.uk/api/v4/KIS/Binstitutions.json"
request = urllib2.Request(url)
request.add_header(
	"Authorazation",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n', ' ')
	)
#request.add_header(
#	"Basic " + base64.encodestring(accesstoken+":").replace('\n', ' ')
#	)

response = urllib2.urlopen(request)
data = json.load(response)
for c in data:
	print c['UKPRN'],c['Name']
