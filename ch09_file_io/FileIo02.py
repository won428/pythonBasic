filename = 'test.txt'
myencoding =  'UTF-8'

print('readline() 함수는 1줄을 읽어 옵니다.')
myfile01 = open(file= filename, mode='rt', encoding= myencoding)

while True:
    oneline = myfile01.readline().strip()
    # print(type(oneline))
    if not oneline: # 마지막 줄에 도달하면
        print(oneline)
        break
    print(f'[{oneline}]')

myfile01.close()

print('readlines() 함수는 모든 줄을 읽어서 list로 반환해 줍니다.')
myfile02 = open(file= filename, mode='rt', encoding= myencoding)
sentences = [txt.strip() for txt in myfile02.readlines()]
# print(type(sentences))
print(sentences)

myfile02.close()

print('read() 함수는 파일 내용 전체를 문자열로 반환해 줍니다.')

myfile03 = open(file= filename, mode='rt', encoding= myencoding)
sentences = myfile03.read()
# print(type(sentences))
print(sentences)

myfile03.close()