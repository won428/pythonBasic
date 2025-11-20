breadString = '바게트,크로와상,스콘,치아바타,나쵸,식빵,스콘,호밀빵,베이글'
breadList = breadString.split(',')
print(breadList)
print(type(breadList))

breadList2 = breadList[0::3]
breadList2.append(breadList[1])

print(breadList2)