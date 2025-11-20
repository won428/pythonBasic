breadString = '바게트,크로와상,스콘,치아바타,나쵸,식빵,스콘,호밀빵,베이글'
breadList = breadString.split(',')
breadTuple = tuple(breadList)

print(breadTuple.count('스콘'))
print(breadTuple.index('스콘'))

breadNewTuple = breadTuple[:3] + breadTuple[-3:]

print(breadNewTuple)

breadNewList = list(breadNewTuple)
breadNewList.sort()
print(breadNewList)