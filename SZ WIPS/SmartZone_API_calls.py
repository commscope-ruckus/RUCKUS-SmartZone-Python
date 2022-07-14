import requests
import warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

class SZ_API_calls:
	def getToken(self, host, username, password):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/serviceTicket"
		body = {'username': username,'password': password}
		r = requests.post(url, json = body, verify=False)
		token = r.json()['serviceTicket']
		return token

	def deleteToken(self, host, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/serviceTicket?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	def getDomainID(self, host, domain, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/domains?serviceTicket=" + token
		r = requests.get(url, verify=False)
		for item in r.json()['list']:
			if item['name'] == domain:
				domainID = item['id']
				#parentDomainID = item['parentDomainId']
				#return (domainID, parentDomainID)
				return (domainID)

	def getZones(self, host, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones?listSize=500&serviceTicket=" + token
		r = requests.get(url, verify=False)	
		return r.json()

	def getZoneID(self, host, zone, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones?listSize=500&serviceTicket=" + token
		r = requests.get(url, verify=False)	
		for item in r.json()['list']:
			if item['name'] == zone:
				zoneID = item['id']
				return zoneID

	def queryZone(self, host, zoneID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "?serviceTicket=" + token
		r = requests.get(url, verify=False)	
		return r.json()

	def createWlan(self, host, zoneID, wlanName, ssid, passphrase, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlans?serviceTicket=" + token
		body = { "name": wlanName, "ssid": ssid, "encryption": { "method": "WPA2", "algorithm": "AES", "passphrase": passphrase } }
		r = requests.post(url, json = body, verify=False)
		wlanID = r.json()['id']
		return wlanID

	def getWlanID(self, host, zoneID, wlanName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlans?listSize=500&serviceTicket=" + token
		r = requests.get(url, verify=False)
		for item in r.json()['list']:
			if item['name'] == wlanName:
				wlanID = item['id']
				return wlanID

	def deleteWlan(self, host, zoneID, wlanID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlans/" + wlanID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	def markKnown(self, host, mac, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rogue/markKnown?serviceTicket=" + token
		body = {
			"rogueMacList": mac,
			}
		r = requests.post(url, json = body, verify=False)	
		return r

	def markRogue(self, host, mac, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rogue/markRogue?serviceTicket=" + token
		body = {
			"rogueMacList": mac,
			}
		r = requests.post(url, json = body, verify=False)	
		return r

	def markIgnore(self, host, mac, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rogue/markIgnore?serviceTicket=" + token
		body = {
			"rogueMacList": mac,
			}
		r = requests.post(url, json = body, verify=False)	
		return r

	def markMalicious(self, host, mac, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rogue/markMalicious?serviceTicket=" + token
		body = {
			"rogueMacList": mac,
			}
		r = requests.post(url, json = body, verify=False)	
		return r

	def getRogueDevices(self, host, filter, value, page, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/query/roguesInfoList?serviceTicket=" + token
		body = {
			"filters": [
					{
						"type": filter,
						"value": value
					}
				],
			"limit": 20,
			"page": page
			}
		r = requests.post(url, json = body, verify=False)	
		return r

	def getRoguePolicies(self, host, zoneID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/rogueApPolicies?serviceTicket=" + token
		r = requests.get(url, verify=False)	
		return r

	def queryRoguePolicy(self, host, zoneID, roguePolicyID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/rogueApPolicies/" + roguePolicyID + "?serviceTicket=" + token
		r = requests.get(url, verify=False)	
		return r

	def applyRoguePolicy(self, host, zoneID, body, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/rogueApPolicies?serviceTicket=" + token
		body = body
		r = requests.post(url, json = body, verify=False)	
		return r