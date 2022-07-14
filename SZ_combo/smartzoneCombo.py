import requests
import warnings
warnings.filterwarnings("ignore", message= "Unverified HTTPS request ")

host = 'https://10.0.0.98:8443'
username = "admin"
password = "ruckus123!"
r = requests.Session()

#Get authentication token
response = r.post(host + '/wsg/api/public/v9_0/serviceTicket', json={'username': username, 'password': password}, verify=False).json()
serviceTicket = response['serviceTicket']
print(serviceTicket)

#Create domain
response = r.post(host + '/wsg/api/public/v9_0/domains?serviceTicket=' + serviceTicket, json={'name': 'Texas'}, verify=False).json()
domainId = response['id']
print(domainId)

#Create zone
response = r.post(host + '/wsg/api/public/v9_0/rkszones?serviceTicket=' + serviceTicket, json={'domainId': domainId,'name': 'Dallas','description': '',
'countryCode': 'US','login': {'apLoginName': 'admin','apLoginPassword': 'ruckus123!'},'apHccdEnabled': True}, verify=False).json()
zoneId = response['id']
print(zoneId)

#Create AP
response = r.post(host + '/wsg/api/public/v9_0/aps?serviceTicket=' + serviceTicket, json={'mac': '00:11:22:33:44:56','zoneId': zoneId ,'serial': '00000123',
'model': 'R750','name': 'R750-A','location': 'San Jose','description': 'My first R750'}, verify=False)

#Query AP
response = r.post(host + '/wsg/api/public/v9_0/query/ap?serviceTicket=' + serviceTicket, json={'filters': [{'type': 'ZONE','value': zoneId}]},
verify=False).json()
apMacAddress = response['list'][0]['apMac']
print(apMacAddress)

#Create wlan
response = r.post(host + '/wsg/api/public/v9_0/rkszones/' + zoneId + '/wlans?serviceTicket=' + serviceTicket, json={"name": "Eiriksson",
"ssid": "Eiriksson","description": "my wlan","encryption": {"method": "WPA2","algorithm": "AES","passphrase": "ruckus123"},"advancedOptions":
{"clientFingerprintingEnabled": True,"avcEnabled": True}}, verify=False).json()
wlanId = response['id']
print(wlanId)