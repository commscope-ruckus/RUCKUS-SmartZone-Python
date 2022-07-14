import csv
from SmartZone_API_calls import SZ_API_calls
SmartZone = SZ_API_calls()

SZADDRESS = "<ip address>" # SmartZone IP address
SZUSER = "admin" # SmartZone user
SZPASSWORD = "password" # SmartZone password
ROGUESFILE = "rogue_list.csv" # .csv file with rogue device mac addresses

rogueDevicesList = []

token = SmartZone.getToken(SZADDRESS,SZUSER, SZPASSWORD)

with open(ROGUESFILE, mode='w') as csv_file:
    fieldnames = ['mac_address', 'status']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    task = input("Do you want to export the rogue devices by Domain(1), Zone(2) or quit(q)? ")
    if task == "1":
        domain = input("Enter the Domain name: ")
        domainId = SmartZone.getDomainID(SZADDRESS, domain, token)
        hasMore = True
        page = 1
        while hasMore:
            response = SmartZone.getRogueDevices(SZADDRESS, "DOMAIN", domainId, page, token)
            for item in response.json()['list']:
                rogueDevicesList.append([item['rogueMac'],item['detectedByAP'][0]['rogueType']])
            page = page + 1
            hasMore = response.json()['hasMore']
        writer.writeheader()
        for item in rogueDevicesList:
            writer.writerow({'mac_address': item[0], 'status': item[1]})
    elif task == "2":
        zone = input("Enter the Zone name: ")
        zoneId = SmartZone.getZoneID(SZADDRESS, zone, token)
        hasMore = True
        page = 1
        while hasMore:
            response = SmartZone.getRogueDevices(SZADDRESS, "ZONE", zoneId, page, token)
            for item in response.json()['list']:
                rogueDevicesList.append([item['rogueMac'],item['detectedByAP'][0]['rogueType']])
            page = page + 1
            hasMore = response.json()['hasMore']
        writer.writeheader()
        for item in rogueDevicesList:
            writer.writerow({'mac_address': item[0], 'status': item[1]})

exportedRogues = str(len(rogueDevicesList))
print(f'Exported {exportedRogues} rogue devices')

r = SmartZone.deleteToken(SZADDRESS,token)