from xml.etree.ElementTree import Element, ElementTree, SubElement

mydict = {'hong': ('홍길동', 60, 80, 70), 'park': ('박영희', 50, 70, 95)}

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

xmldata = Element('students')
xmlFile = 'XmlTest02.xml'
for key, value in mydict.items():
    student = SubElement(xmldata, 'student', id = key)
    kor = value[1]
    eng = value[2]
    math = value[3]
    total = 0
    for grade in value:
        if isinstance(grade, (int, float)):
            total += grade
    avg = round(total / 3, 2)
    student.attrib['총점'] = str(total)
    student.attrib['평균'] = str(avg)

    SubElement(student, '이름').text = value[0]
    SubElement(student, '국어').text = str(kor)
    SubElement(student, '영어').text = str(eng)
    SubElement(student, '수학').text = str(math)

indent(xmldata)
ElementTree(xmldata).write(xmlFile, encoding= 'utf-8')