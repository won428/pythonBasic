from xml.etree.ElementTree import Element, ElementTree, SubElement

def indent(elem, level=0):
    mytab = '\t'
    i = '\n' + level * mytab

    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + mytab

        if not elem.tail or not elem.tail.strip():
            elem.tail = i

        for elem in elem:
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
# end def


# root element 'human'을 생성하면서 속성 gender를 추가합니다.
xmldata = Element('human', gender = '남자')

# 기존 엘리먼트에 속성(attribute) 추가하기
xmldata.attrib['birht'] = '19951223'

SubElement(xmldata, 'name').text = '홍길동'
SubElement(xmldata, 'age').text = '30'
SubElement(xmldata, 'address').text = '마포구 공덕동'

xmlFile = 'XmlExam01.xml'

indent(xmldata)
ElementTree(xmldata).write(xmlFile, encoding= 'utf-8')
print(xmlFile + '파일 생성')