from xml.etree.ElementTree import parse
tree = parse(source='Car_Info.xml')
root = tree.getroot()
carList = root.findall('car')
print(f'총 자동차 수 : {len(carList)}')

for car in carList:
    brand = car[0].attrib['name']
    model = car[1].text
    year = car[2].text
    color = car[3].text
    print(f'브랜드 : {brand}, 모델명 : {model}, 생산년도 : {year}, 색상 : {color}')



