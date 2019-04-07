#Traversing and editing multi-level dictionary
studentInfoDict = {
	'Name': '',
	'Hobby': ['', ''],
	'Favorite OS': {'OS NAME': '', 'VERSION': ''},

}

studentInfoValueList = list(studentInfoDict.keys())


def checkValueTpye(s):
	if type(s) == str:
		return input('Please Input As str:')
	elif type(s) == list:
		return input('Please Input As list:')
	elif type(s) == dict:
		for x in list(s.keys()):
			print('-' + x)
			s[x] = input('Please Input As str:')
		return s


for item in studentInfoValueList:
	print(item)
	studentInfoDict[item] = checkValueTpye(studentInfoDict[item])

print('-----------------------------------------------------')
print('Student information')
print(studentInfoDict['Hobby'])
print(studentInfoDict['Name'])
print(studentInfoDict['Favorite OS'])