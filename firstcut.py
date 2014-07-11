import requests
import re
import urlparse

req = requests.get("http://httpbin.org")
print req.status_code

if req.status_code == requests.codes.ok:
	print req.encoding
	#print req.text
	#print req.headers
	for header in req.headers:
		print header, ':', req.headers[header]

#print "\n"

#print req.history



