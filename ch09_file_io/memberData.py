from collections import Counter

fileName = 'memdata01.txt'
encoding = 'utf-8'
file01 = open(file=fileName, mode= 'rt', encoding= encoding)

users = [user.strip().split(',') for user in file01.readlines()]
print(users)
userDict = dict()

for user in users:
    userDict [user[0]] = user[1]
# end for

valueCounter = Counter(userDict.values())
print(valueCounter)

userList = list()
for user in users:
    userList.append([user[0], user[3], user[4],user[5]])

# end for
def totalGrade(a, b, c):
    total = (a/1000*80) + (b/100*10) + (c/100*10)
    return total

print(userList)
userGrade = dict()
for user in userList:
    total = round(float(totalGrade(int(user[1]), int(user[2]), int(user[3]))), 2)
    userGrade [user[0]] = total
# end for

print(userGrade)

file01.close()