import requests
import warnings
import concurrent.futures
import threading
import json
import re
import time
import logging
import os
import csv

# Copy this script, the .ximg file and the .csv file with the SmartZone ip addresses and credentials to the same directory.
# Each line of the .csv file lists the SmartZone ip address, username and password. Do not use a header line.
# This script was tested with macOS and Ubuntu.

warnings.filterwarnings("ignore", message="Unverified HTTPS request")

# Initializing variables
tokenList = []
sysInfoList =[]
uploadedImageDetailsList = []
urlList = []
szList = []
thread_local = threading.local()
file_path = ""
image = "vscg-5.2.2.0.317.ximg"

# read csv file
def read_csv_file():
	script_dir = os.path.dirname(os.path.realpath('__file__'))
	file_path = os.path.join(script_dir, "szlist.csv")
	with open(file_path, newline='') as f:
		reader = csv.reader(f)
		szList = list(reader)
		for i in szList:
			szDict = {"url": "https://" + i[0]+ ":8443/wsg/api/public/v9_0/serviceTicket","username":i[1],"password":i[2]}
			urlList.append(szDict)
  
# Define threaded request
def get_session():
	if not hasattr(thread_local, "session"):
		thread_local.session = requests.Session()
	return thread_local.session

# Get token api call
def run_token_api_call(url):
	global tokenList
	session = get_session()
	body = {'username': url['username'],'password': url['password']}
	with session.post(url['url'], json = body, verify=False) as response:
		ipaddr = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url['url']).group()
		tokenDict = {"ipaddress": ipaddr, "token": json.loads(response.content.decode('utf-8'))['serviceTicket']}
		tokenList.append(tokenDict)

# Get system information call
def run_get_api_call(url):
	global sysInfoList
	session = get_session()
	response = session.get(url, verify=False)
	ipaddr = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url).group()
	sysInfoDict = {"ipaddress": ipaddr, "hostname": json.loads(response.content.decode('utf-8'))['list'][0]['hostName'], "version": json.loads(response.content.decode('utf-8'))['list'][0]['version']}
	sysInfoList.append(sysInfoDict)
 
# Get uploaded image details
def run_get_uploadedImages_call(url):
	global uploadedImageDetailsList
	session = get_session()
	#response = ""
	response = session.get(url, verify=False)
	success = json.loads(response.content.decode('utf-8'))['clusterOperationProgress']['previousOperationRecord']['success']
	ipaddr = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url).group()
	if success == False:
		uploadedImageDetailsDict = {"ipaddress": ipaddr, "version": "no image","controlbladeVersion": "no image","apVersion": "no image"}
	else:
		uploadedImageDetailsDict = {"ipaddress": ipaddr, "version": json.loads(response.content.decode('utf-8'))['uploadPatchInfo']['version'],"controlbladeVersion": json.loads(response.content.decode('utf-8'))['uploadPatchInfo']['controlbladeVersion'],"apVersion": json.loads(response.content.decode('utf-8'))['uploadPatchInfo']['apVersion']}
	uploadedImageDetailsList.append(uploadedImageDetailsDict)

# Upload image call
def run_uploadImage_api_call(url):
	session = get_session()
	files=[('file',(image,open(file_path,'rb'),'application/octet-stream'))]
	response = session.post(url, files=files, verify=False)
 
# Upgrade image call
def run_upgradeImage_api_call(url):
	session = get_session()
	response = session.post(url, verify=False)

# Check upload status
def checkUploadStatus(url):
	progress = ""
	clusterSubTaskState = ""
	verifyFlag = False
	ipaddr = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url).group()
	while progress != "90" and progress != "72":
		session = get_session()
		with session.get(url, verify=False) as response:
			state = json.loads(response.content.decode('utf-8'))['clusterOperationProgress']['bladeProgresss'][0]['state']
			progress = str(json.loads(response.content.decode('utf-8'))['clusterOperationProgress']['bladeProgresss'][0]['progress'])
			errorMsg = json.loads(response.content.decode('utf-8'))['clusterOperationProgress']['previousOperationRecord']['errorMsg']
			#print (state, progress)
			if state == "":
				state = "Copying"
			elif state == "Verifying" or state == "UploadFailed" :
				verifyFlag = True
			if errorMsg == "Unsupported Version" and verifyFlag == True:
				print( '{:<12s} {:<6s} {:<10s}'.format(ipaddr, "state:", "Failed - Unsupported version"))	
				return
		print( '{:<12s} {:<6s} {:<10s} {:<9s} {:<8s}'.format(ipaddr, "state:", state, "progress:", progress + "%"))
		time.sleep(5)
	while clusterSubTaskState != "Completed" and clusterSubTaskState != "Completed - Missing AP support licenses":
		session = get_session()
		with session.get(url, verify=False) as response:
			clusterSubTaskState = json.loads(response.content.decode('utf-8'))['clusterOperationProgress']['clusterSubTaskState']
		time.sleep(5)
		if clusterSubTaskState == "Failed":
			clusterOperationDisplayMsg = json.loads(response.content.decode('utf-8'))['clusterOperationProgress']['clusterOperationDisplayMsg']
			if clusterOperationDisplayMsg == "The volume of AP Support licenses detected is below the upcoming requirement of one (1) AP support license per managed AP. To enable future firmware upgrades please purchase and apply an AP Support license for each managed AP. For further assistance please contact Ruckus Support. (https://support.ruckuswireless.com/) ":
				clusterSubTaskState = "Completed - Missing AP support licenses"
			elif clusterOperationDisplayMsg == "The volume of AP Support licenses detected is below the upcoming requirement of one (1) AP support license per managed AP. To enable future firmware upgrades please purchase and apply an AP Support license for each managed AP. For further assistance please contact Ruckus Support. (https://support.ruckuswireless.com/) The volume of vSZ-D Support licenses detected is below the upcoming requirement of one (1) vSZ-D support license per managed vSZ-D. To enable future firmware upgrades please purchase and apply an vSZ-D Support license for each managed vSZ-D. For further assistance please contact Ruckus Support. (https://support.ruckuswireless.com/) ":
				clusterSubTaskState = "Completed - Missing AP support licenses"
			#	print("detected message")
			#print(clusterOperationDisplayMsg)
		print( '{:<12s} {:<6s} {:<12s} {:<10s} {:<8s}'.format(ipaddr, "state:", state, "task_state:", clusterSubTaskState))

# Check upgrade status
def checkUpgradeStatus(url):
	progress = ""
	clusterSubTaskState = ""
	ipaddr = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url).group()
	while progress != "7":
		session = get_session()
		with session.get(url, verify=False) as response:
			state = json.loads(response.content.decode('utf-8'))['clusterOperationProgress']['bladeProgresss'][0]['state']
			progress = str(json.loads(response.content.decode('utf-8'))['clusterOperationProgress']['bladeProgresss'][0]['progress'])
			if state == "":
				state = "Starting"
		print( '{:<12s} {:<6s} {:<10s} {:<9s} {:<8s}'.format(ipaddr, "state:", state, "progress:", progress + " of 7"))
		time.sleep(5)
	print( '{:<12s} {:<6s} {:<10s}'.format(ipaddr, "state:", "Rebooting"))

# Create concurrent processes for each api call
def start_concurrent_task(apiCallType):
	global file_path
	if apiCallType == "getToken":
		with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
			executor.map(run_token_api_call, urlList)
	elif apiCallType == "getSystem":
		with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
			urlList.clear()
			for i in tokenList:
				systemApiCall = "https://" + i['ipaddress'] + ":8443/wsg/api/public/v9_0/controller?serviceTicket=" + i['token']
				urlList.append(systemApiCall)
			executor.map(run_get_api_call, urlList)
	elif apiCallType == "verifyUploadedImage":
		with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
			urlList.clear()
			for i in tokenList:
				verifyUploadedImagesApiCall = "https://" + i['ipaddress'] + ":8443/wsg/api/public/v9_0/upgrade/patch?serviceTicket=" + i['token']
				urlList.append(verifyUploadedImagesApiCall)
			executor.map(run_get_uploadedImages_call, urlList)
	elif apiCallType == "uploadImage":
		with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
			script_dir = os.path.dirname(os.path.realpath('__file__'))
			file_path = os.path.join(script_dir, image)
			print ("Uploading file " + file_path)
			urlList.clear()
			for i in tokenList:
				uploadApiCall = "https://" + i['ipaddress'] + ":8443/wsg/api/public/v9_0/upgrade/upload?serviceTicket=" + i['token']
				urlList.append(uploadApiCall)
			executor.map(run_uploadImage_api_call, urlList)
			urlList.clear()
			for i in tokenList:
				checkStatusApiCall = "https://" + i['ipaddress'] + ":8443/wsg/api/public/v9_0/upgrade/status?serviceTicket=" + i['token']
				urlList.append(checkStatusApiCall)
			executor.map(checkUploadStatus, urlList)
	elif apiCallType == "upgradeImage":
		with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
			urlList.clear()
			for i in tokenList:
				uploadApiCall = "https://" + i['ipaddress'] + ":8443/wsg/api/public/v9_0/upgrade?serviceTicket=" + i['token']
				urlList.append(uploadApiCall)
			executor.map(run_upgradeImage_api_call, urlList)
			urlList.clear()
			for i in tokenList:
				checkStatusApiCall = "https://" + i['ipaddress'] + ":8443/wsg/api/public/v9_0/upgrade/status?serviceTicket=" + i['token']
				urlList.append(checkStatusApiCall)
			executor.map(checkUpgradeStatus, urlList)

# Get authentication token
read_csv_file()
start_concurrent_task("getToken")
print()
for i in tokenList:
	print('{:<15s} {:<6s} {:<6s}'.format(i['ipaddress'],"token:",i['token']))
print()

# Get system information
start_concurrent_task("getSystem")
for i in sysInfoList:
	print('{:<15s} {:<6s} {:<20s} {:<6s} {:<6s}'.format(i['ipaddress'],"hostname:",i['hostname'],"version:",i['version']))
print()

task = input("Do you want to upload the image(1), verify(2), upgrade(3) or quit(q)? ")
if task == "1":
	# Upload image
	print("Starting upload process")
	start_concurrent_task("uploadImage")

elif task == "2":
	# Verify uploaded image details
	print()
	start_concurrent_task("verifyUploadedImage")
	for i in uploadedImageDetailsList:
		print('{:<15s} {:<8s} {:<12s} {:<8s} {:<12s} {:<8s} {:<12s}'.format(i['ipaddress'],"version:",i['version'],"controlbladeVersion:",i['controlbladeVersion'],"apVersion:",i['apVersion']))
	print()

elif task == "3":
	# Upgrade image
	confirmation = input("Are you sure you want to upgrade (y/n) ? ")
	if confirmation == "y":
		print("Starting upgrade process")
		start_concurrent_task("upgradeImage")

# To-Do List
# Error checking & handling (bad credentials, connection time-out, unsupported images, upload failures)
# Create variable for image name
# Add __main__ section
# Add command line options
# Add message when there is no uploaded image to verify