#Get to know dictionary assembly
studentInfoDict = {
    'Name': 'Xiaohong Chen',
    'Hobby': ['Movie', 'Music'],
    'Favorite OS': {'OS NAME': 'MAC', 'VERSION': '10.0'},
}
print(studentInfoDict)

# for-loop practice
for m in range(0, 100, 2):
    print(m, end=',')
print("\n")

s = "KABOOM"
for n in s:
    for i in range(3):
        print(n, end=' ')
print("\n")

l = "askaliceithinkshe'llknow"
for h in range(0, len(l), 2):
    print(l[h], end=' ')
print("\n")

