import re

def reg(patternList, regEx):
    pattern = re.compile(regEx)

    for item in patternList:
        if pattern.match(item):
            print(f'문자열 {item}은(는) 조건에 적합합니다.')
        else:
            print(f'문자열 {item}은(는) 조건에 부적합합니다.')
    # end for
# end def

# 정규 표현식을 이용하여 다음 물음에 답해 주세요.
# 다음 리스트 목록 중에서 '문자열 2개와 숫자3개'로 구성된 항목들을 찾아 보세요.
print('[문자열 2개와 숫자 3개로 구성된 항목 찾기]')
mylist01 = ['ab123', 'cd456', 'ef789','abc12']
regEx = '^[a-zA-z]{2}\d{3}$'
reg(mylist01,regEx)
print()
# 다음 리스트 목록 중에서 'a'와 '.txt' 사이에숫자가 최소 3개 이상인 항목들을 찾아 보세요.
print('[\'a\'와 \'.txt\' 사이에 숫자가 최소 3개 이상인 항목 찾기]')
mylist02 = ['a1.txt', 'a12.txt', 'a123.txt','a1234.txt']
regEx = '^a\d{3,}.txt$'
reg(mylist02,regEx)
print()
# 다음 리스트 목록 중에서 'c'와 't' 사이에 'a'가 1번 이상인 항목들을 찾아 보세요.
print('[\'c\'와 \'t\'사이에 \'a\'가 1번 이상인 항목 찾기]')
mylist03 = ['ct', 'cat', 'caat', 'caaat']
regEx = '^ca{1,}t$'
reg(mylist03,regEx)