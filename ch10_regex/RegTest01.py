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

print('\n커피 이름 2개 문자 + 숫자 3개로 구성된 항목 찾기')
coffee_list01 = ['am123', 'la456', 'mo789', 'lat12']
regEx = '^[a-zA-z]{2}\d{3}$'

reg(coffee_list01, regEx)


print('\n"c"로 시작하고 ".coffee"로 끝나며 숫자가 최소 2개 이상 포함된 항목 찾기')
coffee_list02 = ['c1.coffee', 'c12.coffee', 'c345.coffee', 'c9.coffee']
regEx = '^c\d{2,}.coffee$'
reg(coffee_list02, regEx)


print('\n"c"와 "e" 사이에 "a"가 1번 이상 반복되는 항목 찾기')
coffee_list03 = ['ce', 'cae', 'caae', 'caaae']
regEx = '^ca{1,}e$'
reg(coffee_list03, regEx)


# 실행 결과
# 커피 이름 2개 문자 + 숫자 3개로 구성된 항목 찾기
# 결과01 : ['am123', 'la456', 'mo789']
#
# "c"로 시작하고 ".coffee"로 끝나며 숫자가 최소 2개 이상 포함된 항목 찾기
# 결과02 : ['c12.coffee', 'c345.coffee']
#
# "c"와 "e" 사이에 "a"가 1번 이상 반복되는 항목 찾기
# 결과03 : ['cae', 'caae', 'caaae']
