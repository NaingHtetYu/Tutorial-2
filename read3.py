import urllib2, json, base64
accesstoken = "3RG0N6NVEWTN56RRH37L"
institution = "10007772"
course = "U56119"
page = 0
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(institution, course)
request = urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n', ' ')
	)
response = urllib2.urlopen(request)
data = json.load(response)
print json.dumps(data, indent=2)
for a in data:
            if a['Code'] == "SALARY":
                        c = a['Details']
                        for d in c:
                                    if d['Code'] == "MED":
                                                print (d['Value'])

for a in data:
            if a['Code'] == "SALARY":
                        c = a['Details']
                        for d in c:
                                    if d['Code'] == "LDMED":
                                                print (d['Value'])

for a in data:
            if a['Code'] == "NSS":
                        c = a['Details']
                        for d in c:
                                    if d['Code'] == "Q1":
                                                print (d['Value'])

