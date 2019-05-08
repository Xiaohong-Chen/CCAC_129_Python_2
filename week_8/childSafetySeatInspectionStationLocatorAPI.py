import json, requests

# Getting the aip url
def getAPIUrl(StringZipCode):
	URL = 'https://one.nhtsa.gov/webapi/api/CSSIStation/zip/' + StringZipCode + '?format=json'
	print(URL)
	return URL

# Getting the Organization and Contact Phone from Child Safety Seat Inspection Station Locator
def getStationLocatorInfo(StringZipCode):
	url = getAPIUrl(StringZipCode)
	respond = requests.get(url)
	if (int(respond.status_code) == 200):
		locatorApiDict = json.loads(respond.text)
		for n in locatorApiDict['Results']:
			print("-----------------------------------------------------------")
			print('Organization: ' + n['Organization'])
			print("ContactNumber: " + n['Phone1'])

# Getting the Locator from Pittsburgh
def main():
	getStationLocatorInfo('15232')


main()
