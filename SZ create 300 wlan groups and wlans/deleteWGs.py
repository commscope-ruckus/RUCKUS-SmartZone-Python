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

def createWPAwlan(host, zoneID, wlanName, ssid, passphrase, token):
	global wlanID
	wlanID = mySmartZone.createWPAwlan(host, zoneID, wlanName, ssid, passphrase, token)
	print ("wlanID: " , wlanID)

def getWLANgroupID(host, zoneID, WLANgroupName,  token):
	global WLANgroupID
	WLANgroupID = mySmartZone.getWLANgroupID(host, zoneID, WLANgroupName, token)
	print ("WLANgroupID: " , WLANgroupID)    

def deleteWLANgroup(host, zoneID, WLANgroupID, token):
	response = mySmartZone.deleteWLANgroup(host, zoneID, WLANgroupID, token)
	print (response)  

def deleteWLAN(host, zoneID, wlanID, token):
	response = mySmartZone.deleteWLAN(host, zoneID, wlanID, token)
	print (response)

def getWLANid(host, zoneID, wlanName, token):
	global wlanID
	wlanID = mySmartZone.getWLANid(host, zoneID, wlanName, token)
	print ("wlanID: " , wlanID)

getToken(host, username, password)
getZoneID(host, zone, token)
for i in range (0, 5):	
	wlanGroupName = "wg" + str(i)
	getWLANgroupID(host, zoneID, wlanGroupName, token)
	deleteWLANgroup(host, zoneID, WLANgroupID, token)
	wlanName = "wlan" + str(i)
	getWLANid(host, zoneID, wlanName, token)
	deleteWLAN(host, zoneID, wlanID, token)