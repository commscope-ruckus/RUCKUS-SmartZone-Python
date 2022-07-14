import requests
import warnings

host = "host"
szUser = "admin"
szPassword = "password"
requiredSoftware = '6.1.0.0.1595'
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

# Get serviceTicket
url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/serviceTicket"
body = {'username': szUser,'password': szPassword}
response = requests.post(url, json = body, verify=False)
token = response.json()['serviceTicket']
print(token)

# Get zones
url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones?serviceTicket=" + token
response = requests.get(url, verify=False)
zones = response.json()
print(zones)

# Verify the firmwware version in each zone, except the staging or default zone
for zone in zones['list']:
	if zone['name'] != 'Staging Zone' and zone['name'] != 'Default Zone':
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zone['id'] + "?serviceTicket=" + token
		response = requests.get(url, verify=False)
		zoneDetails = response.json()
		if zoneDetails['version'] != requiredSoftware:
			print ("need to upgrade software in zone " + zone['name'])
		else:
			print ("zone " + zone['name'] + " has the correct software")
