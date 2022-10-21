import requests
from tkinter import *

class vSZ_calls:
	# Get authentication token and return it
	def getToken(self, host, username, password):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/serviceTicket"
		body = {'username': username,'password': password}
		r = requests.post(url, json = body, verify=False).json()
		token = r['serviceTicket']
		return token

	# Release authentication token
	def deleteToken(self, host, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/serviceTicket?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return

	# Create Domain Partner and return the Domain Partner id just created
	def createDomainPartner(self, host, domainName, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/domains?serviceTicket=" + token
		body= {
  			"name": domainName,
  			"domainType": "PARTNER"
		}
		r = requests.post(url, json = body, verify=False).json()
		domainID = r['id']
		return domainID

	# Create zone and return the AP Zone id just created
	def createZone(self, host, name, domainId, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones?serviceTicket=" + token
		body = {
  				"domainId": domainId,
  				"name": name,
  				"description": "",
  				"countryCode": "FR",
				"timezone": {
					"customizedTimezone": {
				    "abbreviation": "CET",
				    "gmtOffset": 0,
				    "gmtOffsetMinute": 0
				    }
				},
				"login": {
				    "apLoginName": "admin",
				    "apLoginPassword": "password123!"
				}
			}
		r = requests.post(url, json = body, verify=False).json()
		APZoneID = r['id']
		return APZoneID

	# Create Wlan
	def createWlan(self, host, zoneID, wlanName, ssid, passphrase, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones/" + zoneID + "/wlans?serviceTicket=" + token
		body = { "name": wlanName, "ssid": ssid, "encryption": { "method": "WPA2", "algorithm": "AES", "passphrase": passphrase } }
		r = requests.post(url, json = body, verify=False).json()
		wlanID = r['id']
		return wlanID

	# Delete Wlan
	def deleteWlan(self, host, zoneID, wlanID, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/rkszones/" + zoneID + "/wlans/" + wlanID + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)
		return r

	# Create access point
	def createAP(self, host, mac, zoneId, name, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/aps?serviceTicket=" + token
		body = {
				"mac": mac,
				"zoneId": zoneId,
				"name": name
				}
		r = requests.post(url, json = body, verify=False)	
		return r

	# Delete access point
	def deleteAP(self, host, mac, token):
		url = "https://" + host + ":8443" + "/wsg/api/public/v11_0/aps/" + mac + "?serviceTicket=" + token
		r = requests.delete(url, verify=False)	
		return r

class UserInteractivity:
	def CollectDomainAPZoneWLANNamePSKbyGUI(self):
		#Input value for Domain Name, AP Zone name, WLAN name and WLAN PSK
		#open the windows
		userInput = Tk()
		userInput.title('Enter Customer Information')

		space1 = Label(userInput, text=" ")
		space1.pack()

		#Domain Name Collect
		DomainNameLabel = Label(userInput, text="Domain Name ")
		DomainNameLabel.pack()
		DomainNameInput = Entry(userInput, width=30)
		DomainNameInput.pack()

		#APZone Name Collect
		APZoneNameLabel = Label(userInput, text="\n\nAP Zone Name")
		APZoneNameLabel.pack()
		APZoneNameInput = Entry(userInput, width=30)
		APZoneNameInput.pack()

		#WLAN Name Collect
		WLANNameLabel = Label(userInput, text="\n\nWLAN Name")
		WLANNameLabel.pack()
		WLANNameInput = Entry(userInput, width=30)
		WLANNameInput.pack()

		#PSK Collect
		PSKLabel = Label(userInput, text="\nPSK")
		PSKLabel.pack()
		PSKInput = Entry(userInput, show="*", width=30)
		PSKInput.pack()

		# Sent information
		space2 = Label(userInput, text=" ")
		space2.pack()
		Close=Button(userInput, text="Send information", command=userInput.quit)
		Close.pack()
		space3 = Label(userInput, text=" ")
		space3.pack()

		userInput.mainloop()

		information =  {
        	'DomainName': DomainNameInput.get(),
        	'APZoneName': APZoneNameInput.get(),
        	'WLANName': WLANNameInput.get(),  
        	'PSK' : PSKInput.get()
		}

		return information

	def CollectDomainAPZoneWLANNamePSKbyterminal(self):
		#Input value for Domain Name, AP Zone name, WLAN name and WLAN PSK
		print (" ##### Enter domain name ##### ")
		domainname = input()

		print ("\n ##### Enter AP Zone name ##### ")
		apzonename = input()

		print ("\n ##### Enter WLAN name ##### ")
		wlanname = input()

		print ("\n ##### Enter WLAN PSK ##### ")
		wlanpsk = input()
		
		information =  {
        	'DomainName': domainname,
        	'APZoneName': apzonename,
        	'WLANName': wlanname,  
        	'PSK' : wlanpsk
		}

		return information