import re


print('다음 주소 목록에서 숫자로 시작하는 마지막 상세 주소를 추출해 보세요.')
addressList = ["('강원 원주시 웅비2길8');", "('강원도 철원군 서면 와수로 181번길 7-16');", "('강원 평창군 봉평면 태기로68');", "('강원 강릉시 강변로 410번길36');"]

regEx = r"\d[^']*"
pattern = re.compile(regEx)
for address in addressList:
    result = pattern.search(address)
    print(result.group())
# end for

