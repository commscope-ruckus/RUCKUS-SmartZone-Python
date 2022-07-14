import requests
import warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

HOST = "host"
USERNAME = "admin"
PASSWORD = "password"
ZONE = 'zone'
wlanPassphrase = 'password'
vlanID = 1

def getToken(host, username, password):
	url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/serviceTicket"
	body = {'username': username,'password': password}
	r = requests.post(url, json = body, verify=False)
	token = r.json()['serviceTicket']
	return token

def getZoneID(host, zone, token):
	url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones?listSize=500&serviceTicket=" + token
	r = requests.get(url, verify=False)
	for item in r.json()['list']:
		if item['name'] == zone:
			zoneID = item['id']
			return zoneID

def createWlan(host, zoneID, wlanName, ssid, passphrase, token):
	url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones/" + zoneID + "/wlans?serviceTicket=" + token
	body = { "name": wlanName, "ssid": ssid, "encryption": { "method": "WPA2", "algorithm": "AES", "passphrase": passphrase } }
	r = requests.post(url, json = body, verify=False)
	wlanID = r.json()['id']
	return wlanID

def createWlanGroup(host, zoneID, wlanGroupName, token):
	url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones/" + zoneID + "/wlangroups?serviceTicket=" + token
	body = {"name": wlanGroupName, "description": ""}
	r = requests.post(url, json = body, verify=False)
	wlanGroupID = r.json()['id']
	return wlanGroupID

def getWlanGroupID(host, zoneID, wlanGroupName,  token):
	url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones/" + zoneID + "/wlangroups?listSize=500&serviceTicket=" + token
	r = requests.get(url, verify=False)	
	for item in r.json()['list']:
		if item['name'] == wlanGroupName:
			wlanGroupID = item['id']
			return wlanGroupID

def addMemberToWlanGroup(host, zoneID, wlanGroupID, wlanID, vlanID, token):
	url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones/" + zoneID + "/wlangroups/" + wlanGroupID + "/members" + "?serviceTicket=" + token
	body = { "id": wlanID, "accessVlan": vlanID }
	r = requests.post(url, json = body, verify=False)
	return r

def removeMemberFromWlanGroup(host, zoneID, wlanGroupID, wlanID, token):
	url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones/" + zoneID + "/wlangroups/" + wlanGroupID + "/members/" + wlanID + "?serviceTicket=" + token
	r = requests.delete(url, verify=False)
	return r

def main():
	token = getToken(HOST, USERNAME, PASSWORD)
	zoneID = getZoneID(HOST, ZONE, token)
	WLANgroupID = getWlanGroupID(HOST, zoneID, "default", token)
	defaultWG = WLANgroupID
	for i in range (0, 5):
		wlanGroupName = "wg" + str(i)
		WLANgroupID = createWlanGroup(HOST, zoneID, wlanGroupName, token)
		wlanName = "wlan" + str(i)
		ssid = "SSID" + str(i)
		passphrase = wlanPassphrase
		wlanID = createWlan(HOST, zoneID, wlanName, ssid, passphrase, token)
		r = addMemberToWlanGroup(HOST, zoneID, WLANgroupID, wlanID, vlanID, token)
		s = removeMemberFromWlanGroup(HOST, zoneID, defaultWG, wlanID, token)
		print(WLANgroupID, wlanID, r, s)

if __name__ == '__main__':
	main()