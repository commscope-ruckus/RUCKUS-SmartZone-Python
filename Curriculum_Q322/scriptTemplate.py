import warnings
from datetime import datetime
import csv
warnings.filterwarnings("ignore", message = "Unverified HTTPS request")

# Import class with SmartZone API calls
from vSZ_calls_Q322 import vSZ_calls

# Your constants go here
HOST = "SmartZone IP address or FQDN"
USERNAME = "admin"
PASSWORD = "password"
csvFileName = 'fileName' + str(datetime.now().strftime("%m%d%Y%H%M")) + '.csv'

def main():
	# Initialize class and get serviceTicket
	SmartZone = vSZ_calls()
	token = SmartZone.getToken(HOST, USERNAME, PASSWORD)
	print (token)

	# Open the csv file for writing
	csv_file = open(csvFileName, mode='w', encoding='UTF8') 
	fieldnames = ['column1', 'column2', 'column3', 'columnX']
	writer = csv.writer(csv_file)
	writer.writerow(fieldnames)

	# Your code goes here
	#
	#
	# Your code goes here

	# Close the csv file
	csv_file.close()
	print(csvFileName)

	#release the serviceTicket
	r = SmartZone.deleteToken(HOST,token)

if __name__ == '__main__':
	main()


