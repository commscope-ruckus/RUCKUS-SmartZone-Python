from SmartZone_API_calls import SZ_API_calls
SmartZone = SZ_API_calls()

SZADDRESS = "<ip address>" # SmartZone IP address
SZUSER = "admin" # SmartZone user
SZPASSWORD = "password" # SmartZone password
ROGUESFILE = "rogue_list.csv" # .csv file with rogue device mac addresses

roguePolicyList = []
zoneIdList = []

token = SmartZone.getToken(SZADDRESS,SZUSER, SZPASSWORD)

zone = input("Enter the Zone name with the policy to be copied: ")
zoneId = SmartZone.getZoneID(SZADDRESS, zone, token)
roguePolicyList = SmartZone.getRoguePolicies(SZADDRESS, zoneId, token)

n = 1
for item in roguePolicyList.json()['list']:
    print(f'\t{str(n)} {item["name"]}' )
    n = n + 1
task = input("Enter the index for the Rogue Policy to copy to all zones: ")
roguePolicyId = roguePolicyList.json()['list'][int(task)-1]['id']
roguePolicy = SmartZone.queryRoguePolicy(SZADDRESS, zoneId, roguePolicyId, token)

body = roguePolicy.json()
del body['id']
del body['modifierUsername']
del body['modifiedDateTime']
del body['zoneId']

zones = SmartZone.getZones(SZADDRESS, token)
for item in zones['list']:
    if (item['id'] != zoneId):
        zoneIdList.append(item['id'])

zoneNumber = 1
for item in zoneIdList:
    response = SmartZone.applyRoguePolicy(SZADDRESS, item, body, token)
    print(f'Processed {zoneNumber} zones')
    zoneNumber += 1

r = SmartZone.deleteToken(SZADDRESS,token)