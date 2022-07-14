import requests
import warnings
import os
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

	def createAP(self, host, mac, zoneId, name, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/aps?serviceTicket=" + token
		body = {
				"mac": mac,
				"zoneId": zoneId,
				"name": name
				}
		r = requests.post(url, json = body, verify=False)	
		return r

	def createDomain(self, host, domain, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/domains?serviceTicket=" + token
		body = {
				"name": domain,
				"domainType": "PARTNER"
				}
		r = requests.post(url, json = body, verify=False)	
		domainID = r.json()['id']
		return domainID

	def getDomainID(self, host, domain, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/domains?serviceTicket=" + token
		r = requests.get(url, verify=False)
		for item in r.json()['list']:
			if item['name'] == domain:
				domainID = item['id']
				#parentDomainID = item['parentDomainId']
				#return (domainID, parentDomainID)
				return (domainID)

	def createZone(self, host, domainID, zone, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones?serviceTicket=" + token
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

	def upgradeZoneFirmware(self, host, zoneID, requiredFirmware, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/apFirmware?serviceTicket=" + token
		body = {
					"firmwareVersion": requiredFirmware
				}
		r = requests.put(url, json = body, verify=False)	
		#r = 204 #comment out this line and uncomment the previous to really make the upgrade
		return r

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

	def createWlanGroup(self, host, zoneID, wlanGroupName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlangroups?serviceTicket=" + token
		body = {"name": wlanGroupName, "description": ""}
		r = requests.post(url, json = body, verify=False)
		wlanGroupID = r.json()['id']
		return wlanGroupID

	def getWlanGroupID(self, host, zoneID, wlanGroupName,  token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlangroups?listSize=500&serviceTicket=" + token
		r = requests.get(url, verify=False)	
		for item in r.json()['list']:
			if item['name'] == wlanGroupName:
				wlanGroupID = item['id']
				return wlanGroupID

	def deleteWlanGroup(self, host, zoneID, WLANgroupID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlangroups/" + WLANgroupID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	def deleteWlan(self, host, zoneID, wlanID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlans/" + wlanID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	def addMemberToWlanGroup(self, host, zoneID, wlanGroupID, wlanID, vlanID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlangroups/" + wlanGroupID + "/members" + "?serviceTicket=" + token
		body = { "id": wlanID, "accessVlan": vlanID }
		r = requests.post(url, json = body, verify=False)
		return r

	def removeMemberFromWlanGroup(self, host, zoneID, wlanGroupID, wlanID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlangroups/" + wlanGroupID + "/members/" + wlanID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	def getProxyAAAid(self, host, domainID, proxyAAAname, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/services/auth/query?serviceTicket=" + token
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

	def createClientCertificate(self, host, clientCertificateName, certFile, privateKeyFile, token):
		script_dir = os.path.dirname(os.path.realpath('__file__'))
		file_path = os.path.join(script_dir, certFile)
		with open(file_path, 'r') as f:
			clientCert = f.read()
		file_path = os.path.join(script_dir, privateKeyFile)
		with open(file_path, 'r') as f:
			privateKey = f.read()
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/certstore/clientCert?serviceTicket=" + token
		body = {
				"name": clientCertificateName,
				"data": clientCert,
				"privateKeyData": privateKey
			}
		r = requests.post(url, json = body, verify=False)
		clientCertID = r.json()['id']
		return clientCertID

	def createTrustCaCertificate(self, host, trustCaCertificateName, certFile, token):
		script_dir = os.path.dirname(os.path.realpath('__file__'))
		file_path = os.path.join(script_dir, certFile)
		with open(file_path, 'r') as f:
			trustCaCert = f.read()
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/certstore/trustedCAChainCert?serviceTicket=" + token
		body = {
				"name": trustCaCertificateName,
				"rootCertData": trustCaCert
			}
		r = requests.post(url, json = body, verify=False)
		trustCaCertID = r.json()['id']
		return trustCaCertID

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

	def createWifiOperator(self, host, domainID, operatorName, operatorFriendlyName, operatorDomain, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/profiles/hs20/operators?serviceTicket=" + token
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
		operatorID = r.json()['id']
		return operatorID

	def createIdentityProvider(self, host, domainID, IdentityProviderName, realmName, homeOis, homeOisName, proxyAAAname, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/profiles/hs20/identityproviders?serviceTicket=" + token
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

	def createHS20zoneProfile(self, host, zoneID, zoneProfileName, wifiOperatorID, identityProviderID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/hs20s?serviceTicket=" + token
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
		zoneProfileID = r.json()['id']
		return zoneProfileID

	def createHS20wlan(self, host, zoneID, wlanName, ssid, HS20zoneProfileID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlans/hotspot20?serviceTicket=" + token
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

	def getHS20zoneProfileID(self, host, zoneID, zoneProfileName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/hs20s?serviceTicket=" + token
		r = requests.get(url, verify=False)
		for item in r.json()['list']:
			if item['name'] == zoneProfileName:
				zoneProfileID = item['id']
				return zoneProfileID

	def getIdentityProviderID(self, host, domainID, IdentityProviderName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/profiles/hs20/identityproviders/query?serviceTicket=" + token
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


	def getWifiOperatorID(self, host, domainID, operatorName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/profiles/hs20/operators/query?serviceTicket=" + token
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

	def getClientCertID(self, host, clientCertificateName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/certstore/clientCert?serviceTicket=" + token
		r = requests.get(url, verify=False)
		for item in r.json()['list']:
			if item['name'] == clientCertificateName:
				clientCertID = item['id']
				return clientCertID

	def getTrustCaCertID(self, host, trustCaCertificateName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/certstore/trustedCAChainCert?serviceTicket=" + token
		r = requests.get(url, verify=False)	
		for item in r.json()['list']:
			if item['name'] == trustCaCertificateName:
				trustCaCertID = item['id']
				return trustCaCertID

	def deleteWLAN(self, host, zoneID, wlanID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/wlans/" + wlanID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	def deleteHS20zoneProfile(self, host, zoneID, HS20zoneProfileID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "/hs20s/" + HS20zoneProfileID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	def deleteIdentityProvider(self, host, identityProviderID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/profiles/hs20/identityproviders/" + identityProviderID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	def deleteWifiOperator(self, host, wifiOperatorID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/profiles/hs20/operators/" + wifiOperatorID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	def deleteProxyAAA(self, host, proxyAAAid, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/services/auth/radius/" + proxyAAAid + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	def deleteZone(self, host, zoneID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/rkszones/" + zoneID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	def deleteDomain(self, host, domainID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/domains/" + domainID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	def deleteClientCertificate(self, host, clientCertID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/certstore/clientCert/" +  clientCertID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	def deleteTrustCaCertificate(self, host, trustCaCertID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/certstore/trustedCAChainCert/" +  trustCaCertID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r


	def getWlanTraffic(self, host, zoneId, wlanId, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/clients/byWlanName/" + wlanId + "?serviceTicket=" + token
		body = {
				"filters": [
					{
					"type": "ZONE",
					"value": zoneId
					}
				]
				}
		r = requests.post(url, json = body, verify=False)
		return r

	def getWlanTrafficByClient(self, host, zoneId, wlanId, clientMac, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v9_1/clients/byWlanName/" + wlanId + "?serviceTicket=" + token
		body = {
				"filters": [
					{
					"type": "ZONE",
					"value": zoneId
					}
				],
				"fullTextSearch": {
					"type": "AND",
					"value": clientMac
					},
				}
		r = requests.post(url, json = body, verify=False)
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
			"limit": 10,
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

class RC_API_calls:
	def getToken(self, session, host, username, password):
		url = "https://" + host + "/token"
		body = {'username': username,'password': password}
		r = session.post(url, json = body, verify=False).json()
		return r

	def getGuestUsers(self, session, host, tenantID):
		url = "https://" + host + "/api/tenant/" + tenantID + "/wifi/guest-user"
		r = session.get(url, verify=False).json()
		return r

class CP_API_calls:
	def getToken(self, host, username, password, cpApiKey):
		url = "http://" + host + "/admin/apiv2/" + cpApiKey + "/token"
		body = {"userName":username, "password":password}
		r = requests.post(url, json=body)
		return r

	def createdpsks(self, host, user, passphrase, vlanID, cpApiKey, cpDPSKpoolGuid, token ):
		url = "http://" + host + "/admin/apiv2/" + cpApiKey + "/dpskPools/" + cpDPSKpoolGuid +"/dpsks"
		body = {"name":user, "passphrase":passphrase, "vlanid":vlanID}
		headers = {"Content-Type":"application/json", "Authorization":token}
		r = requests.post(url, headers=headers, json=body)
		return r

class ICX_API_calls:
	def createVLAN(self, host, username, password, vlanID, vlanName):
		url = "https://" + host + "/restconf/data/network-instances/network-instance/default-vrf/vlans"
		headers = headers = {
			'Accept': 'application/yang-data+json',
			'Content-Type': 'application/json'
		}
		body = {
			"vlan": [
				{
					"vlan-id": vlanID,
					"config": {
						"vlan-id": vlanID,
						"name": vlanName
					}
				}
			]
		}
		r = requests.post(url, headers=headers, auth=(username, password), json = body, verify=False)
		return r