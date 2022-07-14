import requests
import warnings

host = "host"
szUser = "admin"
szPassword = "password"
requiredSoftware = '6.1.0.0.1595'
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

def getToken(host, szUser, szPassword):
	url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/serviceTicket"
	body = {'username': szUser,'password': szPassword}
	response = requests.post(url, json = body, verify=False)
	token = response.json()['serviceTicket']
	return token

def getZones(host, token):
	url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones?serviceTicket=" + token
	response = requests.get(url, verify=False)
	zones = response.json()
	return zones

def main():
	token = getToken(host, szUser, szPassword)
	zones= getZones(host, token)
	for zone in zones['list']:
		if zone['name'] != 'Staging Zone' and zone['name'] != 'Default Zone':
			url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zone['id'] + "?serviceTicket=" + token
			response = requests.get(url, verify=False)
			zoneDetails = response.json()
			if zoneDetails['version'] != requiredSoftware:
				print ("need to upgrade software in zone " + zone['name'])
			else:
				print ("zone " + zone['name'] + " has the correct software")

if __name__ == '__main__':
	main()

 