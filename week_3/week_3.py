#Extracting summary data about 311 calls to the City of Pittsburgh
import csv

publicWorkDevDic = {}
requestOrigin = {}
neighborhood = {}

with open('pgh311Abbrev.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        # PUBLIC_WORKS_DIVISION
        n = row['PUBLIC_WORKS_DIVISION']
        if n not in publicWorkDevDic:
            publicWorkDevDic[n] = 1
        else:
            publicWorkDevDic[n] = publicWorkDevDic[n] + 1

        # MECHANISM
        m = row['REQUEST_ORIGIN']

        if m not in requestOrigin:
            requestOrigin[m] = 1
        else:
            requestOrigin[m] = requestOrigin[m] + 1

        l = row['NEIGHBORHOOD']
        if l not in neighborhood:
            neighborhood[l] = 1
        else:
            neighborhood[l] = neighborhood[l] + 1


def display(dict):

    for n in list(dict.keys()):
        print(n)


def countMax(dict, maxKey, maxValue, maxDict):

    for n in list(dict.keys()):
        if dict[n] > maxValue:
            maxValue = dict[n]
            maxKey = n
        else:
            maxValue = maxValue
            maxKey = maxKey

    maxDict[maxKey] = maxValue
    return maxDict


def countMin(dict, minKey, minValue):

    for n in list(dict.keys()):
        if dict[n] < minValue:
            minValue = dict[n]
            minKey = n
        else:
            minValue = minValue
            minKey = minKey

    print(minKey, minValue)


def main():

    print('------------------------------------------------------------------------------------')
    print(publicWorkDevDic)

    maxDictB = countMax(publicWorkDevDic, '', 0, {})

    for j in list(maxDictB.keys()):
        print('The heavy load of public work district: ', j, '. The Number is: ', maxDictB[j])
    print('------------------------------------------------------------------------------------')

    print(requestOrigin)
    maxDictM = countMax(requestOrigin, '', 0, {})

    for m in list(maxDictM.keys()):
        print('The most used Mechanism is: ', m, '. The Number of this Mechanism is: ', maxDictM[m])

    print('------------------------------------------------------------------------------------')

    print(neighborhood)
    maxDictN = countMax(neighborhood, '', 0, {})

    for n in list(maxDictN.keys()):
        print('The most request Neighborhood is:', n, '. The Number of request is:', maxDictN[n])
    print('------------------------------------------------------------------------------------')


main()
