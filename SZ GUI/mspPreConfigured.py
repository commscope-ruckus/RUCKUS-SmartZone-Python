import warnings
import os
from dotenv import load_dotenv
from datetime import datetime
warnings.filterwarnings("ignore", message = "Unverified HTTPS request")

# Import class with require calls
from calls_WLPC import vSZ_calls

# Your constants go here. Some values are stored in the .env file
load_dotenv()
HOST = os.getenv('HOST')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
DOMAINNAME = 'Milk Way'
APZONENAME = 'Solar System'
WLANNAME = 'Earth'
WLANPSK = os.getenv('WLANPSK')

def main():
	# Initialize class and get serviceTicket (Connect SmartZone)
	SmartZone = vSZ_calls()
	token = SmartZone.getToken(HOST, USERNAME, PASSWORD)
	print ("\nSession with SmartZone is initiated")

	#Create Domain
	myDomainID = SmartZone.createDomainPartner(HOST, DOMAINNAME, token)
	print ("\nThe domain " + DOMAINNAME + " has been created")

	#Create AP ZONE
	MyAPZoneID = SmartZone.createZone(HOST, APZONENAME, myDomainID, token)
	print ("\nThe AP zone " + APZONENAME + " has been created")

	#Create WLAN
	r = SmartZone.createWlan(HOST, MyAPZoneID, WLANNAME, WLANNAME, WLANPSK, token)
	print ("\nYour WLAN " + WLANNAME + " has been created")

	#release the serviceTicket (Disconnect SmartZone)
	r = SmartZone.deleteToken(HOST,token)
	print ("\nThe session with SmartZone has been terminated\n\n")

if __name__ == '__main__':
	main()