from datetime import datetime
import warnings
import csv
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

# Import class with SmartZone API calls
from vSZ_calls_Q322 import vSZ_calls

clusterA = "host" # This is the cluster which normally has all online APs
usernameClusterA = "admin"
passwordClusterA = "password"

clusterB = "host" # This is the cluster which SHOULD NOT have any online APs
usernameClusterB = "admin"
passwordClusterB = "password"

csvFile = 'movedAPsTable_' + str(datetime.now().strftime("%m%d%Y%H:%M")) + '.csv'
APlistToMove = []
lines = 0
limit = 2

# Initialize class, get serviceTicket, system domainID and zoneID for the Staging Zone
SmartZone = vSZ_calls()
tokenClusterB = SmartZone.getToken(clusterB, usernameClusterB, passwordClusterB)
tokenClusterA = SmartZone.getToken(clusterA, usernameClusterA, passwordClusterA)
domains = SmartZone.getDomains(clusterB, tokenClusterB)
systemDomainID = domains[0]['parentDomainId']
stagingZoneID = SmartZone.getZoneID(clusterB, "Staging Zone", tokenClusterB)

# Check status of cluster A
destClusterData = SmartZone.getClusterState(clusterA, tokenClusterA)
destClusterState = destClusterData['clusterState']
print('Cluster A status in ' + datetime.now().strftime("%c") +  ' is ' + destClusterState + '\n')

# If cluster A is in service, print the values for all online APs and create a .csv file with APs not in the staging zone
if destClusterState == 'In_Service':
	APs = SmartZone.queryOnlineAPs(clusterB, "DOMAIN", systemDomainID, limit, tokenClusterB) # Get all APs in the system domain that are online
	with open(csvFile, mode='w') as csv_file:
		fieldnames = ['mac', 'zoneId', 'zoneName', 'apGroupId', 'serial', 'name', 'status'] # Defines the .csv file header
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()
		for AP in APs['list']:
			print ('mac:', AP['apMac'])
			print ('zoneId:', AP['zoneId'])
			if AP['zoneId'] != stagingZoneID: # Ignore APs that are in the staging zone
				print ('zoneName:', AP['zoneName'])
				print ('apGroupId:', AP['apGroupId'])
				print ('serial:', AP['serial'])
				print ('name:', AP['deviceName'])
				print ('status:', AP['status'] + '\n')
				writer.writerow({'mac': AP['apMac'],'zoneId': AP['zoneId'],'zoneName': AP['zoneName'],'apGroupId': AP['apGroupId'],'serial': AP['serial'],'name': AP['deviceName'],'status': AP['status']})
				lines = lines + 1
				APlistToMove.append(AP['apMac']) #Create list with mac address of APs to move to cluster A
	if lines > 0: # Move the APs back to cluster A
		response = SmartZone.moveAPtoNewCluster(clusterB, clusterA, APlistToMove, False, tokenClusterB)
		if response.status_code == 204:
			print('The APs in the following list moved back to cluster A in ' + datetime.now().strftime("%c") + ' :','\n')
			print(APlistToMove)
		else:
			print('The API call to move the APs failed with error ' + str(response.status_code))
	else:
		print('There are no online APs to move to cluster A in ' + datetime.now().strftime("%c"))
	print ()
# Release the serviceTickets
r = SmartZone.deleteToken(clusterA,tokenClusterA)
r = SmartZone.deleteToken(clusterB,tokenClusterB)
