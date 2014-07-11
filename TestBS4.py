import requests
import urlparse



from bs4 import BeautifulSoup



req = requests.get("http://httpbin.org")

if req.status_code == requests.codes.ok:
	soup = BeautifulSoup(req.text)
	print soup.get_text()
