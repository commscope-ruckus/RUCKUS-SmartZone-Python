import requests

class vSZ_calls:
	# Get authentication token
	def getToken(self, host, username, password):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/serviceTicket"
		body = {'username': username,'password': password}
		r = requests.post(url, json = body, verify=False)
		token = r.json()['serviceTicket']
		return token

	# Release authentication token
	def deleteToken(self, host, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/serviceTicket?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return

	# Get cluster state
	def getClusterState(self, host, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/cluster/state?serviceTicket=" + token
		r = requests.get(url, verify=False)	
		return r.json()

	# Get domains (uses pagination)
	def getDomains(self, host, token):
		listSize = 1000
		index = 0
		hasMore = True
		domainList = []
		while hasMore == True:
			url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/domains?listSize=" + str(listSize) + "&index=" + str(index) + "&serviceTicket=" + token
			r = requests.get(url, verify=False).json()
			domainList = domainList + r['list']
			if r['hasMore'] ==  False:
				hasMore = False
			index = index + listSize
		return domainList

	# Get domainID (uses pagination)
	def getDomainID(self, host, domain, token):
		listSize = 1000
		index = 0
		hasMore = True
		domainList = []
		while hasMore == True:
			url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/domains?listSize=" + str(listSize) + "&index=" + str(index) + "&serviceTicket=" + token
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

	# Get domain by name
	def getDomainByName(self, host, domainName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/domains/byName/" + domainName + "?serviceTicket=" + token
		r = requests.get(url, verify=False).json()
		return r

	# Get zones (uses pagination)
	def getZones(self, host, token):
		listSize = 1000
		index = 0
		hasMore = True
		zoneList = []
		while hasMore == True:
			url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones?listSize=" + str(listSize) + "&index=" + str(index) + "&serviceTicket=" + token
			r = requests.get(url, verify=False).json()
			zoneList = zoneList + r['list']
			if r['hasMore'] ==  False:
				hasMore = False
			index = index + listSize
		return zoneList

	# Get zoneID (uses pagination)
	def getZoneID(self, host, zone, token):
		listSize = 1000
		index = 0
		hasMore = True
		zoneList = []
		while hasMore == True:
			url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones?listSize=" + str(listSize) + "&index=" + str(index) + "&serviceTicket=" + token
			r = requests.get(url, verify=False).json()
			zoneList = zoneList + r['list']
			if r['hasMore'] ==  False:
				hasMore = False
			index = index + listSize
		for item in zoneList:
			if item['name'] == zone:
				zoneID = item['id']
				return zoneID

	# Query zone
	def queryZone(self, host, zoneID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "?serviceTicket=" + token
		r = requests.get(url, verify=False)
		print (r)
		return r.json()

	# Create zone
	def createZone(self, host, name, domainId, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones?serviceTicket=" + token
		body = {
  				"domainId": domainId,
  				"name": name,
  				"description": "",
  				"countryCode": "US",
				"timezone": {
					"customizedTimezone": {
				    "abbreviation": "TPE",
				    "gmtOffset": 0,
				    "gmtOffsetMinute": 0
				    }
				},
				"login": {
				    "apLoginName": "admin",
				    "apLoginPassword": "password123!"
				},
				"apHccdEnabled": True
			}
		r = requests.post(url, json = body, verify=False).json()
		return r

	# Delete zone
	def deleteZone(self, host, zoneId, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneId + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Get wlans (uses pagination)
	def getWlans(self, host, zoneID, token):
		listSize = 1000
		index = 0
		hasMore = True
		wlanList = []
		while hasMore == True:
			url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlans?listSize=" + str(listSize) + "&index=" + str(index) + "&serviceTicket=" + token
			r = requests.get(url, verify=False).json()
			wlanList = wlanList + r['list']
			if r['hasMore'] ==  False:
				hasMore = False
			index = index + listSize
		return wlanList

	# Get wlan configuration
	def getWlanConfig(self, host, zoneId, wlanId, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneId + "/wlans/" + wlanId + "?serviceTicket=" + token
		r = requests.get(url, verify=False)	
		return r.json()

	# Query WLANs (uses pagination)
	def queryWlans(self, host, filter, ID, limit, token):
		page = 1
		hasMore = True
		wlanList = []
		while hasMore == True:
			url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/query/wlan?serviceTicket=" + token
			body = {
					"filters": [
						{
						"type": filter,
						"value": ID
						}
					],
					"sortInfo": {
					"sortColumn": "name",
					"dir": "ASC"
					},
					"page": page,
					"limit": limit
					}
			r = requests.post(url, json = body, verify=False).json()
			wlanList = wlanList + r['list']
			if r['hasMore'] ==  False:
				hasMore = False
			page = page + 1
		return wlanList

	# Get WlanGroupID
	def getWlanGroupID(self, host, zoneID, wlanGroupName,  token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlangroups?listSize=500&serviceTicket=" + token
		r = requests.get(url, verify=False)	
		for item in r.json()['list']:
			if item['name'] == wlanGroupName:
				wlanGroupID = item['id']
				return wlanGroupID

	# Create WlanGroup
	def createWlanGroup(self, host, zoneID, wlanGroupName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlangroups?serviceTicket=" + token
		body = {"name": wlanGroupName, "description": ""}
		r = requests.post(url, json = body, verify=False)
		wlanGroupID = r.json()['id']
		return wlanGroupID

	# Create Wlan
	def createWlan(self, host, zoneID, wlanName, ssid, passphrase, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlans?serviceTicket=" + token
		body = { "name": wlanName, "ssid": ssid, "encryption": { "method": "WPA2", "algorithm": "AES", "passphrase": passphrase } }
		r = requests.post(url, json = body, verify=False)
		wlanID = r.json()['id']
		return wlanID

	# Add member to WlanGroup
	def addMemberToWlanGroup(self, host, zoneID, wlanGroupID, wlanID, vlanID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlangroups/" + wlanGroupID + "/members" + "?serviceTicket=" + token
		body = { "id": wlanID, "accessVlan": vlanID }
		r = requests.post(url, json = body, verify=False)
		return r

	# Remove member from WlanGroup
	def removeMemberFromWlanGroup(self, host, zoneID, wlanGroupID, wlanID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlangroups/" + wlanGroupID + "/members/" + wlanID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Get WlanID
	def getWlanID(self, host, zoneID, wlanName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlans?listSize=500&serviceTicket=" + token
		r = requests.get(url, verify=False)
		for item in r.json()['list']:
			if item['name'] == wlanName:
				wlanID = item['id']
				return wlanID

	# Delete WlanGroup
	def deleteWlanGroup(self, host, zoneID, WLANgroupID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlangroups/" + WLANgroupID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Delete Wlan
	def deleteWlan(self, host, zoneID, wlanID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlans/" + wlanID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Query Online APs
	def queryOnlineAPs(self, host, filter, domainID, limit, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/query/ap?serviceTicket=" + token
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

	# Query APs (uses pagination)
	def queryAPs(self, host, filter, ID, limit, token):
		page = 1
		hasMore = True
		apList = []
		while hasMore == True:
			url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/query/ap?serviceTicket=" + token
			body = {
					"filters": [
						{
						"type": filter,
						"value": ID
						}
					],
					"sortInfo": {
					"sortColumn": "apMac",
					"dir": "ASC"
					},
					"page": page,
					"limit": limit
					}
			r = requests.post(url, json = body, verify=False).json()
			apList = apList + r['list']
			if r['hasMore'] ==  False:
				hasMore = False
			page = page + 1
		return apList

	# Move AP to new cluster
	def moveAPtoNewCluster(self, host, newCluster, apList, deleteRecord, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/aps/switchoverCluster?serviceTicket=" + token
		body = {"ipOrFqdn":newCluster,"apMacList":apList,"deleteRecord":deleteRecord}
		r = requests.post(url, json = body, verify=False)	
		return r

	# Move AP to zone
	def moveAPtoZone(self, host, APmac, zoneId, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/aps/move?serviceTicket=" + token
		body = {
    			"targetZoneId": zoneId,
    			"apMacs": APmac
				}	
		r = requests.post(url, json = body, verify=False)	
		return r

	# Create access point
	def createAP(self, host, mac, zoneId, name, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/aps?serviceTicket=" + token
		body = {
				"mac": mac,
				"zoneId": zoneId,
				"name": name
				}
		r = requests.post(url, json = body, verify=False)	
		return r

	# Delete access point
	def deleteAP(self, host, mac, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/aps/" + mac + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)	
		return r

	# Get access point configuration
	def getAP(self, host, mac, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/aps/" + mac + "?serviceTicket=" + token
		r = requests.get(url, verify=False)	
		return r.json()

	# Create client traffic by Wlan (uses pagination)
	def getTrafficByWlan(self, host, zoneId, wlanName, limit, token):
		page = 1
		hasMore = True
		clientList = []
		while hasMore == True:
			url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/clients/byWlanName/" + wlanName + "?serviceTicket=" + token
			body = {
					"filters": [
						{
						"type": "ZONE",
						"value": zoneId
						}
					],
					"page": page,
					"limit": limit
					}
			r = requests.post(url, json = body, verify=False).json()
			clientList = clientList + r['list']
			if r['hasMore'] ==  False:
				hasMore = False
			page = page + 1
		return clientList

	# Get Wireless clients (uses pagination)
	def getClients(self, host, zoneId, limit, token):
		page = 1
		hasMore = True
		clientList = []
		while hasMore == True:
			url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/query/client?serviceTicket=" + token
			body = {
					"filters": [
						{
						"type": "ZONE",
						"value": zoneId
						}
					],
					"page": page,
					"limit": limit
					}
			r = requests.post(url, json = body, verify=False).json()
			clientList = clientList + r['list']
			if r['hasMore'] ==  False:
				hasMore = False
			page = page + 1
		return clientList

	# Get DPSKs
	def getDPSKs(self, host, zoneId, wlanId, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneId + "/wlans/" + wlanId + "/dpsk?serviceTicket=" + token
		r = requests.get(url, verify=False)	
		return r.json()

class vSZ_calls_pre_50:
	# Open session
	def getSession(self, session, host, username, password):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/session"
		body = {'username': username,'password': password}
		r = session.post(url, json = body, verify=False)
		return r

	# Close session
	def deleteSession(self, session, host):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/session"
		r = session.delete(url, verify=False)
		return r

	# Get domains (uses pagination)
	def getDomains(self, session, host):
		listSize = 1000
		index = 0
		hasMore = True
		domainList = []
		while hasMore == True:
			url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/domains?listSize=" + str(listSize) + "&index=" + str(index)
			r = session.get(url, verify=False).json()
			domainList = domainList + r['list']
			if r['hasMore'] ==  False:
				hasMore = False
			index = index + listSize
		return domainList

	# Get zones (uses pagination)
	def getZones(self, session, host):
		listSize = 1000
		index = 0
		hasMore = True
		zoneList = []
		while hasMore == True:
			url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones?listSize=" + str(listSize) + "&index=" + str(index)
			r = session.get(url, verify=False).json()
			zoneList = zoneList + r['list']
			if r['hasMore'] ==  False:
				hasMore = False
			index = index + listSize
		return zoneList

	# Query WLANs (uses pagination)
	def queryWlans(self, session, host, filter, ID, limit):
		page = 1
		hasMore = True
		wlanList = []
		while hasMore == True:
			url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/query/wlan"
			body = {
					"filters": [
						{
						"type": filter,
						"value": ID
						}
					],
					"sortInfo": {
					"sortColumn": "name",
					"dir": "ASC"
					},
					"page": page,
					"limit": limit
					}
			r = session.post(url, json = body, verify=False).json()
			wlanList = wlanList + r['list']
			if r['hasMore'] ==  False:
				hasMore = False
			page = page + 1
		return wlanList

	# Query APs (uses pagination)
	def queryAPs(self, session, host, filter, ID, limit):
		page = 1
		hasMore = True
		apList = []
		while hasMore == True:
			url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/query/ap"
			body = {
					"filters": [
						{
						"type": filter,
						"value": ID
						}
					],
					"sortInfo": {
					"sortColumn": "apMac",
					"dir": "ASC"
					},
					"page": page,
					"limit": limit
					}
			r = session.post(url, json = body, verify=False).json()
			apList = apList + r['list']
			if r['hasMore'] ==  False:
				hasMore = False
			page = page + 1
		return apList