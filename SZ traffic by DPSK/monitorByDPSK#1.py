import requests
import warnings
import sys

HOST = "10.0.0.98"
SZUSER = "admin"
SZPASSWORD = "ruckus123!"
ZONE = "Solar System"
WLAN = "dpsk"
DPSK = "BatchDPSK_User_4"

from vSZapi import vSZ_calls
from time import sleep
warnings.filterwarnings("ignore", message="Unverified HTTPS request")
mySmartZone = vSZ_calls()

def getTrafficCounters(wlanID, token):
    wirelessClients = mySmartZone.getWirelessClientsByDpskID(HOST, wlanID, DPSK, token)
    initialClientMacAddress = wirelessClients['list'][0]['clientMac']
    aggregatedTxBytesCounter = wirelessClients['list'][0]['txBytes']
    aggregatedRxBytesCounter = wirelessClients['list'][0]['rxBytes']
    lastTxBytesCounter = wirelessClients['list'][0]['txBytes']
    lastRxBytesCounter = wirelessClients['list'][0]['rxBytes']
    
    while True:
        wirelessClients = mySmartZone.getWirelessClientsByDpskID(HOST, wlanID, DPSK, token)
        currentClientMacAddress = wirelessClients['list'][0]['clientMac']
        if currentClientMacAddress == initialClientMacAddress:
            aggregatedTxBytesCounter = aggregatedTxBytesCounter + (wirelessClients['list'][0]['txBytes'] - lastTxBytesCounter)
            aggregatedRxBytesCounter = aggregatedRxBytesCounter + (wirelessClients['list'][0]['rxBytes'] - lastRxBytesCounter)
            print ('{:<16s} {:<18s} {:<10s} {:<10s} {:<10s} {:<10s}'.format(str(wirelessClients['list'][0]['userName']), str(wirelessClients['list'][0]['clientMac']), \
            str(wirelessClients['list'][0]['txBytes']), str(aggregatedTxBytesCounter), str(wirelessClients['list'][0]['rxBytes']), str(aggregatedRxBytesCounter)))
        else:
            aggregatedTxBytesCounter = aggregatedTxBytesCounter + wirelessClients['list'][0]['txBytes']
            aggregatedRxBytesCounter = aggregatedRxBytesCounter + wirelessClients['list'][0]['rxBytes']
            print ('{:<16s} {:<18s} {:<10s} {:<10s} {:<10s} {:<10s}'.format(str(wirelessClients['list'][0]['userName']), str(wirelessClients['list'][0]['clientMac']), \
            str(wirelessClients['list'][0]['txBytes']), str(aggregatedTxBytesCounter), str(wirelessClients['list'][0]['rxBytes']), str(aggregatedRxBytesCounter)))
            initialClientMacAddress = currentClientMacAddress
        lastTxBytesCounter = wirelessClients['list'][0]['txBytes']
        lastRxBytesCounter = wirelessClients['list'][0]['rxBytes']
        sleep(10)   

def main(argv):
    token = mySmartZone.getToken(HOST, SZUSER, SZPASSWORD)
    zoneID = mySmartZone.getZoneID(HOST, ZONE, token)
    wlanID = mySmartZone.getWlanID(HOST, zoneID, WLAN, token)
    wirelessClients = mySmartZone.getWirelessClientsByDpskID(HOST, wlanID, DPSK, token)
    print ()
    print ('{:<13s} {:<20s}'.format("token: ", token))
    print ('{:<13s} {:<20s}'.format("zone ID: ", zoneID))
    print ('{:<13s} {:<20s}'.format("wlan ID: ", wlanID))
    print ('{:<13s} {:<20s}'.format("total count: ", str(wirelessClients['totalCount'])))
    print ('{:<13s} {:<20s}'.format("DPSK ID: ", str(wirelessClients['list'][0]['userName'])))
    print ('{:<13s} {:<20s}'.format("mac address: ", str(wirelessClients['list'][0]['clientMac'])))
    print ('{:<13s} {:<20s}'.format("ip address: ", str(wirelessClients['list'][0]['ipAddress'])))
    print ('{:<13s} {:<20s}'.format("host name: ", str(wirelessClients['list'][0]['hostname'])))
    print ('{:<13s} {:<20s}'.format("device type: ", str(wirelessClients['list'][0]['deviceType'])))
    print ()
    print ('{:<16s} {:<18s} {:<10s} {:<10s} {:<10s} {:<10s}'.format("DPSK ID", "mac address", "Tx Bytes", "Tx Agg.", "Rx Bytes", "Rx Agg."))
    getTrafficCounters(wlanID, token) 
    return

if __name__ == "__main__":
        main(sys.argv[1:])