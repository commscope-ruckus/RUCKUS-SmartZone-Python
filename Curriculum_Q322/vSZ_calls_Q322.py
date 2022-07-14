import requests

class vSZ_calls:
	# Get authentication token
	def getToken(self, host, username, password):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/serviceTicket"
		body = {'username': username,'password': password}
		r = requests.post(url, json = body, verify=False)
		token = r.json()['serviceTicket']
		return token

	# Get domains
	def getDomains(self, host, token):
		listSize = 1000
		index = 0
		hasMore = True
		domainList = []
		while hasMore == True:
			url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/domains?listSize=" + str(listSize) + "&index=" + str(index) + "&serviceTicket=" + token
			r = requests.get(url, verify=False).json()
			domainList = domainList + r['list']
			if r['hasMore'] ==  False:
				hasMore = False
			index = index + listSize
		return domainList

	# Get domainID
	def getDomainID(self, host, domain, token):
		listSize = 1000
		index = 0
		hasMore = True
		domainList = []
		while hasMore == True:
			url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/domains?listSize=" + str(listSize) + "&index=" + str(index) + "&serviceTicket=" + token
			r = requests.get(url, verify=False).json()
			domainList = domainList + r['list']
			if r['hasMore'] ==  False:
				hasMore = False
			index = index + listSize
		for item in domainList:
			if item['name'] == domain:
				domainID = item['id']
				parentDomainID = item['parentDomainId']
				return (domainID, parentDomainID)

	# Get zoneID
	def getZoneID(self, host, zone, token):
		listSize = 1000
		index = 0
		hasMore = True
		zoneList = []
		while hasMore == True:
			url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones?listSize=" + str(listSize) + "&index=" + str(index) + "&serviceTicket=" + token
			r = requests.get(url, verify=False).json()
			zoneList = zoneList + r['list']
			if r['hasMore'] ==  False:
				hasMore = False
			index = index + listSize
		for item in zoneList:
			if item['name'] == zone:
				zoneID = item['id']
				return zoneID

	# Get cluster state
	def getClusterState(self, host, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/cluster/state?serviceTicket=" + token
		r = requests.get(url, verify=False)	
		return r.json()

	# Query Online APs
	def queryOnlineAPs(self, host, filter, domainID, limit, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/query/ap?serviceTicket=" + token
		body = {
				"filters": [
					{
					"type": filter,
					"value": domainID
					}
				],
				"fullTextSearch": {
				"type": "AND",
				"value": "Online"
					},
					"sortInfo": {
					"sortColumn": "apMac",
					"dir": "ASC"
					},
					"page": 1,
					"limit": limit
				}
		r = requests.post(url, json = body, verify=False)
		return r.json()

	# Query zone
	def queryZone(self, host, zoneID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones/" + zoneID + "?serviceTicket=" + token
		r = requests.get(url, verify=False)	
		return r.json()

	# Move AP to new cluster
	def moveAPtoNewCluster(self, host, newCluster, apList, deleteRecord, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/aps/switchoverCluster?serviceTicket=" + token
		body = {"ipOrFqdn":newCluster,"apMacList":apList,"deleteRecord":deleteRecord}
		r = requests.post(url, json = body, verify=False)	
		return r

	# Release authentication token
	def deleteToken(self, host, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/serviceTicket?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return

	def getWlanGroupID(self, host, zoneID, wlanGroupName,  token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones/" + zoneID + "/wlangroups?listSize=500&serviceTicket=" + token
		r = requests.get(url, verify=False)	
		for item in r.json()['list']:
			if item['name'] == wlanGroupName:
				wlanGroupID = item['id']
				return wlanGroupID

	def createWlanGroup(self, host, zoneID, wlanGroupName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones/" + zoneID + "/wlangroups?serviceTicket=" + token
		body = {"name": wlanGroupName, "description": ""}
		r = requests.post(url, json = body, verify=False)
		wlanGroupID = r.json()['id']
		return wlanGroupID

	def createWlan(self, host, zoneID, wlanName, ssid, passphrase, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones/" + zoneID + "/wlans?serviceTicket=" + token
		body = { "name": wlanName, "ssid": ssid, "encryption": { "method": "WPA2", "algorithm": "AES", "passphrase": passphrase } }
		r = requests.post(url, json = body, verify=False)
		wlanID = r.json()['id']
		return wlanID

	def addMemberToWlanGroup(self, host, zoneID, wlanGroupID, wlanID, vlanID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones/" + zoneID + "/wlangroups/" + wlanGroupID + "/members" + "?serviceTicket=" + token
		body = { "id": wlanID, "accessVlan": vlanID }
		r = requests.post(url, json = body, verify=False)
		return r

	def removeMemberFromWlanGroup(self, host, zoneID, wlanGroupID, wlanID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones/" + zoneID + "/wlangroups/" + wlanGroupID + "/members/" + wlanID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	def getWlanID(self, host, zoneID, wlanName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones/" + zoneID + "/wlans?listSize=500&serviceTicket=" + token
		r = requests.get(url, verify=False)
		for item in r.json()['list']:
			if item['name'] == wlanName:
				wlanID = item['id']
				return wlanID

	def deleteWlanGroup(self, host, zoneID, WLANgroupID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones/" + zoneID + "/wlangroups/" + WLANgroupID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	def deleteWlan(self, host, zoneID, wlanID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones/" + zoneID + "/wlans/" + wlanID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

