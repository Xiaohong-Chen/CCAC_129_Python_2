import json
import csv

csvDataList = []

# convert json file into python
def getSearchCriteriaDict(FileName):
    with open(FileName, 'r') as jsonFile:
        return json.load(jsonFile)

# get Fiscal Year Search Criterial
def getFiscalYearCriteria(CriteriaDict):
    return CriteriaDict['fiscal_year']

# get Start Date Search Criterial
def getStartDate(CriteriaDict):
    return CriteriaDict['start_date']

# get Area Search Criterial
def getArea(CriteriaDict):
    return CriteriaDict['area']

# get Asset_type Criterial
def getAsset_type(CriteriaDict):
    return CriteriaDict['asset_type']

# get Planning Status Criterial
def getPlanningStatus(CriteriaDict):
    return CriteriaDict['planning_status']

# get whole CSV Data Dict
def getCsvList(csvName, csvDataList):
    with open(csvName, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            csvDataList.append(row)
    return csvDataList

def getMatchingList(criteriaList, inputList, criteriaName):
    outputList = []
    for n in inputList:
        for m in criteriaList:
            if m == "" or m == n[criteriaName]:
                outputList.append(n)
    return outputList

def getFinalMatchingList():

    criteriaDict = getSearchCriteriaDict('criteria.json')

    fyc = getFiscalYearCriteria(criteriaDict)
    sdc = getStartDate(criteriaDict)
    arc = getArea(criteriaDict)
    atc = getAsset_type(criteriaDict)
    psc = getPlanningStatus(criteriaDict)

    csvlist = getCsvList('capital.csv', csvDataList)

    fiscalYearList = getMatchingList(fyc, csvlist, 'fiscal_year')
    startDateList = getMatchingList(sdc, fiscalYearList, 'start_date')
    areaList = getMatchingList(arc, startDateList, 'area')
    assetTpyeList = getMatchingList(atc, areaList, 'asset_type')
    statusList = getMatchingList(psc, assetTpyeList, 'status')

    return statusList


def main():

    finalMatchingList = getFinalMatchingList()

    if finalMatchingList != []:
        print(finalMatchingList)
    else:
        print('Sorry! No matching!')


main()
