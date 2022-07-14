import requests
import warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

# Import class with SmartZone API calls
from vSZapi import vSZ_calls

# You can change these parameters
host = "your ip address"
username = "username"
password = "password"
domain = "California"
zone = "SJC"
proxyAAAname = "Radius Proxy"
operatorName = "San Jose Int'l Airport"
operatorDomain = "sjairport.com"
operatorFriendlyName = "San Jose International Airport"
identityProviderName = "Santa Clara County"
zoneProfileName = "HS20 Profile"
homeOisName = "HS20 RCOI"
wlanName = "San Jose Airport HS20 wlan"
ssid = "SJC_HS20"

# Do not change these parameters
proxyAAAipAddress = "A.B.C.D"
sharedSecret = "password"
realmName = "sjc.airport.net"
homeOis = "5a03ba0000" 

# Instantiate class and variables
mySmartZone = vSZ_calls()
token = None
domainID = None
parentDomainID = None
zoneID = None
proxyAAAid = None
wifiOperatorID = None
identityProviderID = None
HS20zoneProfileID = None
wlanID = None
WISPRportalID = None
APgroupID = None
WLANgroupID = None

# SmartZone tasks
def getToken(host, username, password):
	global token
	token = mySmartZone.getToken(host, username, password)
	print ("token: " , token)

def createDomain(host, domain, token):
	global domainID
	domainID = mySmartZone.createDomain(host, domain, token)
	print ("domainID: " , domainID)

def getDomainID(host, domain, token):
	global domainID
	global parentDomainID
	response = mySmartZone.getDomainID(host, domain, token)
	domainID = response[0]
	parentDomainID = response[1]
	print ("domainID: " , domainID)
	print ("parentDomainID: " , parentDomainID)
 
def getDomains(host, token):
	domains = mySmartZone.getDomains(host, token)
	print ("domains: " , domains)

def createZone(host, domainID, zone, token):
	global zoneID
	zoneID = mySmartZone.createZone(host, domainID, zone, token)
	print ("zone: " , zoneID)
 
def getZoneID(host, zone, token):
	global zoneID
	zoneID = mySmartZone.getZoneID(host, zone, token)
	print ("zoneID: " , zoneID)    

def getZones(host, token):
	zones = mySmartZone.getZones(host, token)
	print ("zones: " , zones)

def createProxyAAA(host, domainID, proxyAAAname, proxyAAAipAddress, sharedSecret, token):
	global proxyAAAid
	proxyAAAid = mySmartZone.createProxyAAA(host, domainID, proxyAAAname, proxyAAAipAddress, sharedSecret, token)	
	print ("proxyAAAid: " , proxyAAAid)

def getProxyAAAid(host, domainID, proxyAAAname, token):
	global proxyAAAid
	proxyAAAid = mySmartZone.getProxyAAAid(host, domainID, proxyAAAname, token)
	print ("proxyAAAid: " , proxyAAAid)

def getProxyAAA(host, proxyAAAid, token):
	proxyAAA = mySmartZone.queryProxyAAA(host, proxyAAAid, token)
	print ("proxyAAA: " , proxyAAA)

def createWifiOperator(host, domainID, operatorName, operatorFriendlyName, operatorDomain, token):
	global wifiOperatorID
	wifiOperatorID = mySmartZone.createWifiOperator(host, domainID, operatorName, operatorFriendlyName, operatorDomain, token)
	print ("wifiOperatorID: " , wifiOperatorID)

def getWifiOperatorID(host, domainID, operatorName, token):
	global wifiOperatorID
	wifiOperatorID = mySmartZone.getWifiOperatorID(host, domainID, operatorName, token)
	print ("wifiOperatorID: " , wifiOperatorID)

def getWifiOperator(host, wifiOperatorID, token):
	wifiOperator = mySmartZone.queryWifiOperator(host, wifiOperatorID, token)
	print ("proxyAAA: " , wifiOperator)

def createIdentityProvider(host, domainID, IdentityProviderName, realmName, homeOis, homeOisName, proxyAAAname, token):
	global identityProviderID
	identityProviderID = mySmartZone.createIdentityProvider(host, domainID, IdentityProviderName, realmName, homeOis, homeOisName, proxyAAAname, token)
	print ("wifiOperatorID: " , identityProviderID)

def getIdentityProviderID(host, domainID, IdentityProviderName, token):
	global identityProviderID
	identityProviderID = mySmartZone.getIdentityProviderID(host, domainID, IdentityProviderName, token)
	print ("identityProviderID: " , identityProviderID)

def getIdentityProvider(host, identityProviderID, token):
	identityProvider = mySmartZone.queryIdentityProvider(host, identityProviderID, token)
	print ("identityProvider: " , identityProvider)

def createHS20zoneProfile(host, zoneID, zoneProfileName, wifiOperatorID, identityProviderID, token):
	global HS20zoneProfileID
	HS20zoneProfileID = mySmartZone.createHS20zoneProfile(host, zoneID, zoneProfileName, wifiOperatorID, identityProviderID, token)
	print ("HS20zoneProfileID: " , HS20zoneProfileID)

def getHS20zoneProfileID(host, zoneID, zoneProfileName, token):
	global HS20zoneProfileID
	HS20zoneProfileID = mySmartZone.getHS20zoneProfileID(host, zoneID, zoneProfileName, token)
	print ("HS20zoneProfileID: " , HS20zoneProfileID)
 
def getHS20zoneProfile(host, zoneID, getHS20zoneProfileID, token):
	HS20zoneProfile = mySmartZone.getHS20zoneProfile(host, zoneID, HS20zoneProfileID, token)
	print ("HS20zoneProfile: " , HS20zoneProfile)

def createHS20wlan(host, zoneID, wlanName, ssid, HS20zoneProfileID, token):
	global wlanID
	wlanID = mySmartZone.createHS20wlan(host, zoneID, wlanName, ssid, HS20zoneProfileID, token)
	print ("wlanID: " , wlanID)

def createWPAwlan(host, zoneID, wlanName, ssid, passphrase, token):
	global wlanID
	wlanID = mySmartZone.createWPAwlan(host, zoneID, wlanName, ssid, passphrase, token)
	print ("wlanID: " , wlanID)
 
def createWISPRwlan(host, zoneID, wlanName, ssid, passphrase, WISPRportalID, proxyAAAid, token):
	global wlanID
	wlanID = mySmartZone.createWISPRwlan(host, zoneID, wlanName, ssid, passphrase, WISPRportalID, proxyAAAid, token)
	print ("wlanID: " , wlanID)
 
def getWLANid(host, zoneID, wlanName, token):
	global wlanID
	wlanID = mySmartZone.getWLANid(host, zoneID, wlanName, token)
	print ("wlanID: " , wlanID)

def getWLAN(host, zoneID, wlanID, token):
	wlan = mySmartZone.getWLAN(host, zoneID, wlanID, token)
	print ("wlan: " , wlan)

def createWISPRportal(host, zoneID, WISPRportalName, WISPRportalURL, token):
	global WISPRportalID	
	WISPRportalID = mySmartZone.createWISPRportal(host, zoneID, WISPRportalName, WISPRportalURL, token)
	print ("WISPr portal: " , WISPRportalID)

def getWISPRportalID(host, zoneID, WISPRportalName, token):
	global WISPRportalID
	WISPRportalID = mySmartZone.getWISPRportalID(host, zoneID, WISPRportalName, token)
	print ("WISPRportalID: " , WISPRportalID)

def getWISPRportal(host, zoneID, WISPRportalID, token):
	WISPRportal = mySmartZone.getWISPRportal(host, zoneID, WISPRportalID, token)
	print ("WISPRportal: " , WISPRportal)

def deleteWLAN(host, zoneID, wlanID, token):
	response = mySmartZone.deleteWLAN(host, zoneID, wlanID, token)
	print (response)
    
def deleteHS20zoneProfile(host, zoneID, HS20zoneProfileID, token):
	response = mySmartZone.deleteHS20zoneProfile(host, zoneID, HS20zoneProfileID, token)
	print (response)

def deleteWISPRportal(host, zoneID, WISPRportalID, token):
	response = mySmartZone.deleteWISPRportal(host, zoneID, WISPRportalID, token)
	print (response)

def deleteIdentityProvider(host, identityProviderID, token):
	response = mySmartZone.deleteIdentityProvider(host, identityProviderID, token)
	print (response)

def deleteWifiOperator(host, wifiOperatorID, token):
	response = mySmartZone.deleteWifiOperator(host, wifiOperatorID, token)
	print (response)   

def deleteProxyAAA(host, proxyAAAid, token):
	response = mySmartZone.deleteProxyAAA(host, proxyAAAid, token)
	print (response)  
 
def deleteZone(host, zoneID, token):
	response = mySmartZone.deleteZone(host, zoneID, token)
	print (response)   

def deleteDomain(host, domainID, token):
	response = mySmartZone.deleteDomain(host, domainID, token)
	print (response) 

def createAPgroup(host, zoneID, APgroupName, token):
	global APgroupID	
	APgroupID = mySmartZone.createAPgroup(host, zoneID, APgroupName, token)
	print ("AP group: " , APgroupID)

def getAPgroupID(host, zoneID, APgroupName,  token):
	global APgroupID
	APgroupID = mySmartZone.getAPgroupID(host, zoneID, APgroupName, token)
	print ("APgroupID: " , APgroupID) 

def deleteAPgroup(host, zoneID, APgroupID, token):
	response = mySmartZone.deleteAPgroup(host, zoneID, APgroupID, token)
	print (response)

def createWLANgroup(host, zoneID, WLANgroupName, token):
	global WLANgroupID	
	WLANgroupID = mySmartZone.createWLANgroup(host, zoneID, WLANgroupName, token)
	print ("WLAN group: " , WLANgroupID)

def getWLANgroupID(host, zoneID, WLANgroupName,  token):
	global WLANgroupID
	WLANgroupID = mySmartZone.getWLANgroupID(host, zoneID, WLANgroupName, token)
	print ("WLANgroupID: " , WLANgroupID)  

def deleteWLANgroup(host, zoneID, WLANgroupID, token):
	response = mySmartZone.deleteWLANgroup(host, zoneID, WLANgroupID, token)
	print (response) 

def addMemberToWlanGroup(host, zoneID, WLANgroupID, wlanID, vlanID, token):
	response = mySmartZone.addMemberToWlanGroup(host, zoneID, WLANgroupID, wlanID, vlanID, token)
	print (response) 

def removeMemberFromWlanGroup(host, zoneID, WLANgroupID, wlanID, token):
	response = mySmartZone.removeMemberFromWlanGroup(host, zoneID, WLANgroupID, wlanID, token)
	print (response)
 
#deleteWLAN(host, zoneID, wlanID, token)
#deleteHS20zoneProfile(host, zoneID, HS20zoneProfileID, token)
#deleteWISPRportal(host, zoneID, WISPRportalID, token)
#deleteIdentityProvider(host, identityProviderID, token)
#deleteWifiOperator(host, wifiOperatorID, token)
#deleteProxyAAA(host, proxyAAAid, token)
#deleteZone(host, zoneID, token)
#deleteDomain(host, domainID, token)

# steps to create a Hotspot 2.0 wlan
getToken(host, username, password)
createDomain(host, domain, token)
getDomainID(host, domain, token)
createZone(host, domainID, zone, token)
createProxyAAA(host, parentDomainID, proxyAAAname, proxyAAAipAddress, sharedSecret, token)
createWifiOperator(host, domainID, operatorName, operatorFriendlyName, operatorDomain, token)
createIdentityProvider(host, domainID, identityProviderName, realmName, homeOis, homeOisName, proxyAAAname, token)
createHS20zoneProfile(host, zoneID, zoneProfileName, wifiOperatorID, identityProviderID, token)
createHS20wlan(host, zoneID, wlanName, ssid, HS20zoneProfileID, token)