import requests
import warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

# Import class with SmartZone API calls
from vSZapi import vSZ_calls

# SmartZone default information
host = 'your ip address'
username = 'username'
password = 'password'
zone = 'SanJose'
vlanID = 1
passphrase = 'password'

# Instantiate class and variables
mySmartZone = vSZ_calls()
token = None
zoneID = None
wlanID = None
WLANgroupID = None

# SmartZone tasks
def getToken(host, username, password):
	global token
	token = mySmartZone.getToken(host, username, password)
	print ("token: " , token)

def getZoneID(host, zone, token):
	global zoneID
	zoneID = mySmartZone.getZoneID(host, zone, token)
	print ("zoneID: " , zoneID)

def createFIPSwlan(host, zoneID, wlanName, ssid, passphrase, token):
	global wlanID
	wlanID = mySmartZone.createFIPSwlan(host, zoneID, wlanName, ssid, passphrase, token)
	print ("wlanID: " , wlanID)

def createWLANgroup(host, zoneID, WLANgroupName, token):
	global WLANgroupID	
	WLANgroupID = mySmartZone.createWLANgroup(host, zoneID, WLANgroupName, token)
	print ("WLAN group: " , WLANgroupID)

def getWLANgroupID(host, zoneID, WLANgroupName,  token):
	global WLANgroupID
	WLANgroupID = mySmartZone.getWLANgroupID(host, zoneID, WLANgroupName, token)
	print ("WLANgroupID: " , WLANgroupID)  

def addMemberToWlanGroup(host, zoneID, WLANgroupID, wlanID, vlanID, token):
	response = mySmartZone.addMemberToWlanGroup(host, zoneID, WLANgroupID, wlanID, vlanID, token)
	print (response)  

def removeMemberFromWlanGroup(host, zoneID, WLANgroupID, wlanID, token):
	response = mySmartZone.removeMemberFromWlanGroup(host, zoneID, WLANgroupID, wlanID, token)
	print (response)  

getToken(host, username, password)
getZoneID(host, zone, token)
getWLANgroupID(host, zoneID, "default", token)
defaultWG = WLANgroupID
for i in range (0, 5):
	wlanGroupName = "wg" + str(i)
	createWLANgroup(host, zoneID, wlanGroupName, token)
	wlanName = "wlan" + str(i)
	ssid = "SSID" + str(i)
	passphrase = passphrase
	createFIPSwlan(host, zoneID, wlanName, ssid, passphrase, token)
	addMemberToWlanGroup(host, zoneID, WLANgroupID, wlanID, vlanID, token)
	removeMemberFromWlanGroup(host, zoneID, defaultWG, wlanID, token)