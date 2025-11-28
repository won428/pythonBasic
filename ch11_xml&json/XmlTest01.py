from xml.etree.ElementTree import Element, SubElement, ElementTree



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

# <student address="상수동" birth="19951225">
#    <name>김대호</name>
#    <age>20</age>
#    <gender>남자</gender>
#    <grade>A</grade>
#    <university>서강대</university>
# </student>

xmldata = Element('student', address = '상수동')

def addSub(xmldata, tag, text):
    SubElement(xmldata, tag).text = text


xmldata.attrib['birth'] ='19951225'

addSub(xmldata,'name','김대호')
addSub(xmldata,'age','20')
addSub(xmldata,'gender','남자')
addSub(xmldata,'grade','A')
addSub(xmldata,'university','서강대')

xmlFile = 'XmlTest01.xml'
indent(xmldata)

ElementTree(xmldata).write(xmlFile, encoding= 'utf-8')