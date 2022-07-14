import warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

from vSZ_calls_Q322 import vSZ_calls
SmartZone = vSZ_calls()

HOST = "host"
USERNAME = "admin"
PASSWORD = "password"
ZONE = 'zone'

def main():
	token = SmartZone.getToken(HOST, USERNAME, PASSWORD)
	zoneID = SmartZone.getZoneID(HOST, ZONE, token)
	for i in range (0, 5):	
		wlanGroupName = "wg" + str(i)
		wlanGroupID = SmartZone.getWlanGroupID(HOST, zoneID, wlanGroupName, token)
		r = SmartZone.deleteWlanGroup(HOST, zoneID, wlanGroupID, token)
		wlanName = "wlan" + str(i)
		wlanID = SmartZone.getWlanID(HOST, zoneID, wlanName, token)
		r = SmartZone.deleteWlan(HOST, zoneID, wlanID, token)
		print (r)

if __name__ == "__main__":
	main()

 