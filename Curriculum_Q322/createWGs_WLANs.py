import warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

from vSZ_calls_Q322 import vSZ_calls
SmartZone = vSZ_calls()

HOST = "host"
USERNAME = "admin"
PASSWORD = "password"
ZONE = 'zone'

wlanPassphrase = 'password'
vlanID = 1

def main():
	token = SmartZone.getToken(HOST, USERNAME, PASSWORD)
	zoneID = SmartZone.getZoneID(HOST, ZONE, token)
	wlanGroupID = SmartZone.getWlanGroupID(HOST, zoneID, "default", token)
	defaultWG = wlanGroupID
	for i in range (0, 5):
		wlanGroupName = "wg" + str(i)
		wlanGroupID = SmartZone.createWlanGroup(HOST, zoneID, wlanGroupName, token)
		wlanName = "wlan" + str(i)
		ssid = "SSID" + str(i)
		passphrase = wlanPassphrase
		wlanID = SmartZone.createWlan(HOST, zoneID, wlanName, ssid, passphrase, token)
		r = SmartZone.addMemberToWlanGroup(HOST, zoneID, wlanGroupID, wlanID, vlanID, token)
		r = SmartZone.removeMemberFromWlanGroup(HOST, zoneID, defaultWG, wlanID, token)
		print ("WLAN group ID: ", wlanGroupID, " WLAN ID: ", wlanID)

if __name__ == "__main__":
	main()
