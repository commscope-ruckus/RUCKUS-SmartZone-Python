import requests
import os

class ZD_calls:
	# Get cookie and CSRF token
	def getToken(self, host, username, password):
		url = "https://" + host + "/admin10/login.jsp?username=admin&action=login.jsp&password=admin&ok=were" 
		body = {'username': username,'password': password}
		r = requests.get(url, verify=False)
		#cookie = r.json()['cookie']
		#token = r.json()['serviceTicket']
		#return token
		return r

class vSZ_calls:
	# Get authentication token
	def getToken(self, host, username, password):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/serviceTicket"
		body = {'username': username,'password': password}
		r = requests.post(url, json = body, verify=False)
		token = r.json()['serviceTicket']
		return token

	# Create domain
	def createDomain(self, host, domain, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/domains?serviceTicket=" + token
		body = {
				"name": domain,
				"domainType": "PARTNER"
				}
		r = requests.post(url, json = body, verify=False)	
		domainID = r.json()['id']
		return domainID

	# Get domainID
	def getDomainID(self, host, domain, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/domains?serviceTicket=" + token
		r = requests.get(url, verify=False)
		for item in r.json()['list']:
			if item['name'] == domain:
				domainID = item['id']
				parentDomainID = item['parentDomainId']
				return (domainID, parentDomainID)

	# Get domains
	def getDomains(self, host, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/domains?serviceTicket=" + token
		r = requests.get(url, verify=False)	
		return r.json()

	# Create zone
	def createZone(self, host, domainID, zone, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones?serviceTicket=" + token
		body = {
				"domainId": domainID,
				"name": zone,
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
					"apLoginPassword": "ruckus123!"
				},
				"apHccdEnabled": True
				}
		r = requests.post(url, json = body, verify=False)	
		zoneID = r.json()['id']
		return zoneID

	# Get zoneID
	def getZoneID(self, host, zone, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones?listSize=500&serviceTicket=" + token
		r = requests.get(url, verify=False)	
		for item in r.json()['list']:
			if item['name'] == zone:
				zoneID = item['id']
				return zoneID

	# Get zones
	def getZones(self, host, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones?listSize=500&serviceTicket=" + token
		r = requests.get(url, verify=False)	
		return r.json()

	# Query zone
	def queryZone(self, host, zoneID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "?serviceTicket=" + token
		r = requests.get(url, verify=False)	
		return r.json()

	# Upgrade zone
	def upgradeZoneFirmware(self, host, zoneID, requiredFirmware, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/apFirmware?serviceTicket=" + token
		body = {
					"firmwareVersion": requiredFirmware
				}
		r = requests.put(url, json = body, verify=False)	
		return r

	# Create proxy authenticator
	def createProxyAAA(self, host, domainID, proxyAAAname, proxyAAAipAddress, sharedSecret, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/services/auth/radius?serviceTicket=" + token
		body = {
					"domainId": domainID,
					"name": proxyAAAname,
					"friendlyName": "",
					"description": "",
					"type": "RADIUS",
					"locationDeliveryEnabled": False,
					"primary": {
						"ip": proxyAAAipAddress,
						"port": 1812,
						"sharedSecret": sharedSecret
					},
					"healthCheckPolicy": {
						"responseWindow": 20,
						"zombiePeriod": 40,
						"reviveInterval": 120,
						"responseFail": False
					},
					"rateLimiting": {
						"maxOutstandingRequestsPerServer": 0,
						"threshold": 0,
						"sanityTimer": 10
					},
					"mappings": []
				}
		r = requests.post(url, json = body, verify=False)
		proxyAAAid = r.json()['id']
		return proxyAAAid

	# Get proxyAAAid
	def getProxyAAAid(self, host, domainID, proxyAAAname, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/services/auth/query?serviceTicket=" + token
		body = {
				"filters": [
					{
					"type": "DOMAIN",
					"value": domainID
					}
				],
				"page": 1,
				"limit": 8
				}
		r = requests.post(url, json = body, verify=False)
		for item in r.json()['list']:
			if item['name'] == proxyAAAname:
				proxyAAAid = item['id']
				return proxyAAAid

	# Query proxy authenticator
	def queryProxyAAA(self, host, proxyAAAid, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/services/auth/radius/" + proxyAAAid + "?serviceTicket=" + token
		r = requests.get(url, verify=False)	
		return r.json()

	# Create Wifi operator
	def createWifiOperator(self, host, domainID, operatorName, operatorFriendlyName, operatorDomain, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/profiles/hs20/operators?serviceTicket=" + token
		body = {
				"domainId": domainID,
				"name": operatorName,
				"description": "",
				"domainNames": [
					operatorDomain
				],
				"friendlyNames": [
					{
					"language": "English",
					"name": operatorFriendlyName
					}
				]
				}
		r = requests.post(url, json = body, verify=False)
		wifiOperatorID = r.json()['id']
		return wifiOperatorID

	# Get Wifi operatorID
	def getWifiOperatorID(self, host, domainID, operatorName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/profiles/hs20/operators/query?serviceTicket=" + token
		body = {
				"filters": [
					{
					"type": "DOMAIN",
					"value": domainID
					}
				],
				"page": 1,
				"limit": 8
				}
		r = requests.post(url, json = body, verify=False)
		for item in r.json()['list']:
			if item['name'] == operatorName:
				wifiOperatorID = item['id']
				return wifiOperatorID

	# Query WiFi operator
	def queryWifiOperator(self, host, operatorID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/profiles/hs20/operators/" + operatorID + "?serviceTicket=" + token
		r = requests.get(url, verify=False)	
		return r.json()

	# Create identity provider
	def createIdentityProvider(self, host, domainID, IdentityProviderName, realmName, homeOis, homeOisName, proxyAAAname, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/profiles/hs20/identityproviders?serviceTicket=" + token
		body = {
				"domainId": domainID,
				"name": IdentityProviderName,
				"description": "",
				"plmns": [],
				"realms": [
					{
						"name": realmName,
						"encoding": "RFC4282",
						"eapMethods": [
							{
								"type": "EAP_TTLS",
								"authSettings": [
									{
										"info": "Non",
										"type": "MSCHAPV2"
									}
								]
							},
							{
								"type": "NA"
							},
							{
								"type": "NA"
							},
							{
								"type": "NA"
							}
						]
					}
				],
				"homeOis": [
					{
						"name": homeOisName,
						"oi": homeOis
					}
				],
				"authentications": [
					{
						"realm": "No Match",
						"serviceType": "RADIUS",
						"name": proxyAAAname,
						"id": ""
					},
					{
						"realm": "Unspecified",
						"serviceType": "RADIUS",
						"name": proxyAAAname,
						"id": ""
					}
				]
			}
		r = requests.post(url, json = body, verify=False)
		identityProviderID = r.json()['id']
		return identityProviderID

	# Get identityProviderID
	def getIdentityProviderID(self, host, domainID, IdentityProviderName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/profiles/hs20/identityproviders/query?serviceTicket=" + token
		body = {
				"filters": [
					{
					"type": "DOMAIN",
					"value": domainID
					}
				],
				"page": 1,
				"limit": 8
				}
		r = requests.post(url, json = body, verify=False)
		for item in r.json()['list']:
			if item['name'] == IdentityProviderName:
				identityProviderID = item['id']
				return identityProviderID

	# Query identity provider
	def queryIdentityProvider(self, host, identityProviderID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/profiles/hs20/identityproviders/" + identityProviderID + "?serviceTicket=" + token
		r = requests.get(url, verify=False)
		return r.json()

	# Create HS20 zone profile
	def createHS20zoneProfile(self, host, zoneID, zoneProfileName, wifiOperatorID, identityProviderID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/hs20s?serviceTicket=" + token
		body = {
				"name": zoneProfileName,
				"description": "",
				"operator": {
					"id": wifiOperatorID
				},
				"defaultIdentityProvider": {
					"id": identityProviderID
				},
				"internetOption": True,
				"accessNetworkType": "PRIVATE",
				"ipv4AddressType": "SINGLE_NATED_PRIVATE",
				"ipv6AddressType": "UNAVAILABLE"
				}
		r = requests.post(url, json = body, verify=False)
		HS20zoneProfileID = r.json()['id']
		return HS20zoneProfileID

	# Get HS20zoneProfileID
	def getHS20zoneProfileID(self, host, zoneID, zoneProfileName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/hs20s?serviceTicket=" + token
		r = requests.get(url, verify=False)
		for item in r.json()['list']:
			if item['name'] == zoneProfileName:
				HS20zoneProfileID = item['id']
				return HS20zoneProfileID

	# Query HS20zoneProfile
	def getHS20zoneProfile(self, host, zoneID, HS20zoneProfileID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/hs20s/" + HS20zoneProfileID + "?serviceTicket=" + token
		r = requests.get(url, verify=False)
		return r.json()

	# Create HS20 wlan
	def createHS20wlan(self, host, zoneID, wlanName, ssid, HS20zoneProfileID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/wlans/hotspot20?serviceTicket=" + token
		body = {
				"name": wlanName,
				"ssid": ssid,
				"description": "",
				"hotspot20Profile": {
						"id": HS20zoneProfileID
					}
				}
		r = requests.post(url, json = body, verify=False)
		wlanID = r.json()['id']
		return wlanID

	# Get wlanID
	def getWLANid(self, host, zoneID, wlanName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/wlans?listSize=500&serviceTicket=" + token
		r = requests.get(url, verify=False)
		for item in r.json()['list']:
			if item['name'] == wlanName:
				wlanID = item['id']
				return wlanID

	# Query wlan
	def getWLAN(self, host, zoneID, wlanID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/wlans/" + wlanID + "?serviceTicket=" + token
		r = requests.get(url, verify=False)
		return r.json()

	# Create FIPS WPA wlan
	def createWPAwlan(self, host, zoneID, wlanName, ssid, passphrase, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/wlans?serviceTicket=" + token
		body = {
				"name": wlanName,
				"ssid": ssid,
				"encryption": {
					"method": "WPA2",
					"algorithm": "AES",
					"passphrase": passphrase},
				}
		r = requests.post(url, json = body, verify=False)
		wlanID = r.json()['id']
		return wlanID

	# Create FIPS WPA wlan
	def createFIPSwlan(self, host, zoneID, wlanName, ssid, passphrase, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/wlans?serviceTicket=" + token
		body = {
				"name": wlanName,
				"ssid": ssid,
				"encryption": {
					"method": "WPA2",
					"algorithm": "AES",
					"passphrase": passphrase,
					"mfp": "disabled"
				},
				"dpsk": {
					"dpskEnabled": True,
					"length": 62,
					"dpskType": "KeyboardFriendly",
					"expiration": "Unlimited"
				}
		}
		r = requests.post(url, json = body, verify=False)
		wlanID = r.json()['id']
		return wlanID

	# Create WISPr WLAN
	def createWISPRwlan(self, host, zoneID, wlanName, ssid, passphrase, wisprPortalID, proxyAaaID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/wlans/wispr?serviceTicket=" + token
		body = {
				"name": wlanName,
				"ssid": ssid,
				"description": "",
				"authServiceOrProfile": {
					"throughController": True,
					"id": proxyAaaID
				},
				"portalServiceProfile": {
					"id": wisprPortalID
				},
				"encryption": {
					"method": "WPA2",
					"algorithm": "AES",
					"passphrase": passphrase
				},
				"advancedOptions":{
					"clientFingerprintingEnabled": True
				}
			}
		r = requests.post(url, json = body, verify=False)
		wlanID = r.json()['id']
		return wlanID

	# Create WISPr portal
	def createWISPRportal(self, host, zoneID, WISPRportalName, WISPRportalURL, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/portals/hotspot/external?serviceTicket=" + token
		body = {
					"name" : WISPRportalName,
					"description" : "",
					"smartClientSupport" : "None",
					"portalUrl" : WISPRportalURL,
					"macAddressFormat" : 2,
					"httpsRedirect" : True
				}
		r = requests.post(url, json = body, verify=False)
		WISPRportalID = r.json()['id']
		return WISPRportalID

	# Get WISPRportalID
	def getWISPRportalID(self, host, zoneID, WISPRportalName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/portals/hotspot?serviceTicket=" + token
		r = requests.get(url, verify=False)
		for item in r.json()['list']:
			if item['name'] == WISPRportalName:
				WISPRportalID = item['id']
				return WISPRportalID

	# Query WISPRportal
	def getWISPRportal(self, host, zoneID, WISPRportalID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/portals/hotspot/" + WISPRportalID + "?serviceTicket=" + token
		r = requests.get(url, verify=False)
		return r.json()

	# Delete wlan
	def deleteWLAN(self, host, zoneID, wlanID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/wlans/" + wlanID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Delete HS20zoneProfile
	def deleteHS20zoneProfile(self, host, zoneID, HS20zoneProfileID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/hs20s/" + HS20zoneProfileID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Delete WISPRportal
	def deleteWISPRportal(self, host, zoneID, WISPRportalID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/portals/hotspot/" + WISPRportalID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Delete identity provider
	def deleteIdentityProvider(self, host, identityProviderID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/profiles/hs20/identityproviders/" + identityProviderID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Delete wifi operator
	def deleteWifiOperator(self, host, wifiOperatorID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/profiles/hs20/operators/" + wifiOperatorID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Delete proxy authenticator
	def deleteProxyAAA(self, host, proxyAAAid, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/services/auth/radius/" + proxyAAAid + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Delete zone
	def deleteZone(self, host, zoneID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Delete domain
	def deleteDomain(self, host, domainID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/domains/" + domainID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Create APgroup
	def createAPgroup(self, host, zoneID, APgroupName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/apgroups?serviceTicket=" + token
		body = {
				"name": APgroupName,
				"description": ""
			}
		r = requests.post(url, json = body, verify=False)
		APgroupID = r.json()['id']
		return APgroupID

	# Get APgroupID
	def getAPgroupID(self, host, zoneID, APgroupName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/apgroups?serviceTicket=" + token
		r = requests.get(url, verify=False)	
		for item in r.json()['list']:
			if item['name'] == APgroupName:
				APgroupID = item['id']
				return APgroupID

	# Delete APgroup
	def deleteWLANgroup(self, host, zoneID, WLANgroupID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/wlangroups/" + WLANgroupID + "?serviceTicket=" + token
		print (url)
		r = requests.delete(url, verify=False)
		return r

	# Create WLANgroup
	def createWLANgroup(self, host, zoneID, WLANgroupName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/wlangroups?serviceTicket=" + token
		body = {
				"name": WLANgroupName,
				"description": ""
			}
		r = requests.post(url, json = body, verify=False)
		WLANgroupID = r.json()['id']
		return WLANgroupID

	# Get WLANgroupID
	def getWLANgroupID(self, host, zoneID, WLANgroupName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/wlangroups?listSize=500&serviceTicket=" + token
		r = requests.get(url, verify=False)	
		for item in r.json()['list']:
			if item['name'] == WLANgroupName:
				WLANgroupID = item['id']
				return WLANgroupID

	# Delete WLANgroup
	def deleteWLANgroup(self, host, zoneID, WLANgroupID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/wlangroups/" + WLANgroupID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Add a member to a WLAN group
	def addMemberToWlanGroup(self, host, zoneID, WLANgroupID, wlanID, vlanID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/wlangroups/" + WLANgroupID + "/members" + "?serviceTicket=" + token
		body = {
				"id": wlanID,
				"accessVlan": vlanID
			}
		r = requests.post(url, json = body, verify=False)
		return r

	# Remove a member from a WLAN group
	def removeMemberFromWlanGroup(self, host, zoneID, WLANgroupID, wlanID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/rkszones/" + zoneID + "/wlangroups/" + WLANgroupID + "/members/" + wlanID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Upload SmartZone firmware
	def uploadFirmware(self, host, imageFile, token):
		script_dir = os.path.dirname(os.path.realpath('__file__'))
		file_path = os.path.join(script_dir, imageFile)
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/upgrade/upload?serviceTicket=" + token
		payload={}
		files=[('file',(imageFile, open(file_path,'rb'),'application/octet-stream'))]
		r = requests.post(url, files=files, verify=False)
		return r

	# Upgrade SmartZone firmware
	def upgradeFirmware(self, host, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/upgrade?serviceTicket=" + token
		r = requests.post(url, verify=False)
		return r

	# Create client certificate
	def createClientCertificate(self, host, clientCertificateName, certFile, privateKeyFile, token):
		script_dir = os.path.dirname(os.path.realpath('__file__'))
		file_path = os.path.join(script_dir, certFile)
		with open(file_path, 'r') as f:
			clientCert = f.read()
		file_path = os.path.join(script_dir, privateKeyFile)
		with open(file_path, 'r') as f:
			privateKey = f.read()
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/certstore/clientCert?serviceTicket=" + token
		body = {
				"name": clientCertificateName,
				"data": clientCert,
				"privateKeyData": privateKey
			}
		r = requests.post(url, json = body, verify=False)
		clientCertID = r.json()['id']
		return clientCertID

	# Create trust CA certificate
	def createTrustCaCertificate(self, host, trustCaCertificateName, certFile, token):
		script_dir = os.path.dirname(os.path.realpath('__file__'))
		file_path = os.path.join(script_dir, certFile)
		with open(file_path, 'r') as f:
			trustCaCert = f.read()
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/certstore/trustedCAChainCert?serviceTicket=" + token
		body = {
				"name": trustCaCertificateName,
				"rootCertData": trustCaCert
			}
		r = requests.post(url, json = body, verify=False)
		trustCaCertID = r.json()['id']
		return trustCaCertID

	# Create Proxy AAA using RADsec
	def createRADsecProxyAAA(self, host, domainID, proxyAAAname, cnSanIdentity, clientCertID, proxyAAAipAddress, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v10_0/services/auth/radius?serviceTicket=" + token
		body = {
				"domainId": domainID,
				"name": proxyAAAname,
				"type": "RADIUS",
				"tlsEnabled": True,
				"cnSanIdentity": cnSanIdentity,
				"clientCertId": clientCertID,
				"locationDeliveryEnabled": False,
				"primary": {
					"ip": proxyAAAipAddress,
					"port": 2083,
						},
			}		
		r = requests.post(url, json = body, verify=False)
		RADsecProxyAAAid = r.json()['id']
		return RADsecProxyAAAid

	# Get clientCertID
	def getClientCertID(self, host, clientCertificateName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/certstore/clientCert?serviceTicket=" + token
		r = requests.get(url, verify=False)
		for item in r.json()['list']:
			if item['name'] == clientCertificateName:
				clientCertID = item['id']
				return clientCertID

	# Get trustCaCertID
	def getTrustCaCertID(self, host, trustCaCertificateName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/certstore/trustedCAChainCert?serviceTicket=" + token
		r = requests.get(url, verify=False)	
		for item in r.json()['list']:
			if item['name'] == trustCaCertificateName:
				trustCaCertID = item['id']
				return trustCaCertID

	# Get RADsecProxyAAAid
	def getRADSecProxyAAAid(self, host, domainID, RADSecProxyAAAname, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/services/auth/query?serviceTicket=" + token
		body = {
				"filters": [
					{
					"type": "DOMAIN",
					"value": domainID
					}
				],
				"page": 1,
				"limit": 8
				}
		r = requests.post(url, json = body, verify=False)
		for item in r.json()['list']:
			if item['name'] == RADSecProxyAAAname:
				RADsecProxyAAAid = item['id']
				return RADsecProxyAAAid

	# Delete Proxy AAA using RADsec
	def deleteRADsecProxyAAA(self, host, RADsecProxyAAAid, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/services/auth/radius/" +  RADsecProxyAAAid + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Delete client certificate
	def deleteteClientCertificate(self, host, clientCertID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/certstore/clientCert/" +  clientCertID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Delete trust CA certificate
	def deleteteTrustCaCertificate(self, host, trustCaCertID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_0/certstore/trustedCAChainCert/" +  trustCaCertID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r