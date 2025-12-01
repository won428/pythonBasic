import sqlite3
from xml.etree.ElementTree import parse

# step01 : xml 파일 읽기
tree = parse('sungjuk.xml')
myroot = tree.getroot()

# step02 : sqlite DB 열기
conn = sqlite3.connect('student.db')
mycursor = conn.cursor()

# step03 : 테이블 삭제 후 생성
try:
    mycursor.execute('drop table sungjuk')
except sqlite3.OperationalError:
    print('테이블이 존재하지 않습니다.')
# end try

sql = """
create table sungjuk(
    id text,
    subject text,
    jumsu integer
)
"""

mycursor.execute(sql)

# stap04 : xml 데이터를 DB에 추가하기
data_list = [] # 데이터 베이스에 추가할 행 목록
for student in myroot.iter('student'):
    sid = student.find('id').text
    subject = student.find('subject').text
    jumsu = student.find('jumsu').text
    data_list.append((sid,subject,jumsu))
# end for
# print(data_list)

sql = "insert into sungjuk values (?,?,?)"
mycursor.executemany(sql,data_list)

# step05: 전체 목록을 보여주는 함수 생성
def getAllStudents(dbcursor):
    for onetuple in dbcursor:
        print(f'아이디 : {onetuple[0]}', end= '')
        print(f', 과목 : {onetuple[1]}', end= '')
        print(f', 점수 : {onetuple[2]}')
    # end for
# end def

# stap06 : 테이블의 내용 출력
sql = 'select * from sungjuk'
mycursor.execute(sql)
getAllStudents(mycursor)

conn.commit() # 데이터 베이스 커밋

# step07 : 작업 객체를 닫기
mycursor.close()
conn .close()

