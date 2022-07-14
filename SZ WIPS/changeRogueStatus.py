import csv
from SmartZone_API_calls import SZ_API_calls
SmartZone = SZ_API_calls()

SZADDRESS = "<ip_address>" # SmartZone IP address
SZUSER = "admin" # SmartZone user
SZPASSWORD = "password" # SmartZone password
ROGUESFILE = "rogue_list.csv" # .csv file with rogue device mac addresses

knownList = []
ignoreList = []
rogueList = []
maliciousList = []

#get SmartZone authentication token (valid for 24 hours)
token = SmartZone.getToken(SZADDRESS,SZUSER, SZPASSWORD)

#read the csv file and create tables with the rogue mac address for 
#the 4 categories: Known, Ignore, Rogue and Malicious
with open(ROGUESFILE, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'\tMAC address       Status')
        print(f'\t{row["mac_address"]} {row["status"]}')
        if (row["status"] == "Known"):
            knownList.append(row["mac_address"])
            line_count += 1
        if (row["status"] == "Ignore"):
            ignoreList.append(row["mac_address"])
            line_count += 1
        if (row["status"] == "Rogue"):
            rogueList.append(row["mac_address"])
            line_count += 1
        if (row["status"] == "Malicious"):
            maliciousList.append(row["mac_address"])
            line_count += 1
    print(f'Processed {line_count} lines')
    print(f'Executing API calls...')

#execute the API to change the rogue status (one call per each category)
if (len(knownList) > 0):
    SmartZone.markKnown(SZADDRESS, knownList, token)
if (len(ignoreList) > 0):
    SmartZone.markIgnore(SZADDRESS, ignoreList, token)
if (len(rogueList) > 0):
    SmartZone.markRogue(SZADDRESS, rogueList, token)
if (len(maliciousList) > 0):
    SmartZone.markMalicious(SZADDRESS, maliciousList, token)

#release the token
r = SmartZone.deleteToken(SZADDRESS,token)