import re

def reg(patternList, regEx):
    pattern = re.compile(regEx)
    regList = list()
    for item in patternList:
        if pattern.match(item):
            regList.append(item)
        # end if
    # end for
    print(f'결과 : {regList}')
# end def

# ^와 $를 명시하면 '전체 완전 일치', 명시하지 않으면  '부분 일치'
print('알파벳 3개 + 숫자 2개로 구성된 항목 찾기')
mylist01 = ['abc12','abcd12','xy345','pq678','abcd1']
regEx = '^[a-zA-Z]{3}\d{2}$' # 정규 표현식
reg(mylist01, regEx)

print('file + 영문자 최소 2개이상 + .png')
print('주의 : 점은 임의의 한문자(줄바꿈 제외), 역슬래시 점은 점 기호를 의미')
mylist02 = ['filea.png','fileab.png','fileabc.png','file.png','file99.png']
regEx = '^file[a-zA-Z]{2,}\.png$' # 정규 표현식
reg(mylist02, regEx)

print('b로 시작하고, g로 끝나는 단어중 사이에 e가 2번 이상 반복')
mylist03 = ['beg','beeg','beeeg','bg']
regEx = '^be{2,}g$'
reg(mylist03,regEx)

print('숫자로 시작하고, 이후에 알파벳이 1개 이상인 항목 찾기')
mylist04 = ['1a','2abc','9xyz','0ab']
regEx = '^\d[a-zA-Z]+$' # + 기호는 최소 1번 이상
reg(mylist04,regEx)

print('hello 또는 hi로 시작하는 항목들 찾기')
mylist05 = ['hello123','hi999','hey77','hello']
regEx = '^(hello|hi).*$'
reg(mylist05,regEx)