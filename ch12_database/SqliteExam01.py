import sqlite3

conn = sqlite3.connect('student.db')
mycursor = conn.cursor()


try:
    mycursor.execute("drop table students")
except sqlite3.OperationalError:
    print('테이블이 존재하지 않습니다.')
# end try

mycursor.execute("""
    create table students(
        id text primary key,
        name text not null,
        birth text,
        gender text,
        major text,
        grade integer,
        phone text
    )
    """)

# 기본 데이터 추가하기
mycursor.execute("""
insert into students
values (
    'lee',
    '이민혁',
    '1989/12/12',
    'M',
    '컴퓨터공학',
    4,
    '010-1234-5678'
)
""")

mycursor.execute("""
insert into students
values (
    'kang',
    '강호사',
    '1970/07/17',
    'M',
    '수학과',
    2,
    '010-3456-7890'
)
""")
# 리스트를 이용한 데이터 추가하기
studentList = [
    ('jo','조용원','1970/07/17','F','체육학과', 2,'010-3333-1234'),
    ('ko','고두식','1970/07/17','M','디자인과', 2,'010-8888-7777'),
    ('sim','심유이','1970/07/17','F','연극영화과', 2,'010-1212-3434')
]
sql = """
    insert into students
    values (
    ?,?,?,?,?,?,?
)
"""
mycursor.executemany(sql, studentList)


print('# id로 조회')
findId = 'kang'
sql = "select * from students where id = '%s'"
mycursor.execute(sql % findId)
result = mycursor.fetchone()
if result == None:
    print('존재하지 않는 회원입니다.')
else:
    print('#'.join([str(item) for item in result]))

print('# 데이터 정렬')
sql = "select * from students order by name desc"
for row in mycursor.execute(sql):
    print(row)

print('# 컬럼별 출력하기')
for(id, name, birth, gender, major, grade, phone) in mycursor.execute(sql):
    print(f'{id},{name},{birth},{gender},{major},{grade},{phone}')
print('# like 검색')
findWord = '이'
sql = f"select * from students where name like '%{findWord}%'"
print(f'이름에 "{findWord}"라는 글자가 포함된 사람')
mycursor.execute(sql)
result = mycursor.fetchall()
print(result)

print('# update 구문')
pid, newName = 'lee', '이순철'
sql = "update students set name = ? where id = ?"
mycursor.execute(sql ,(newName, pid))

print('# delete 구문')
pid= 'sim'
sql = "delete from students where id = ?"
mycursor.execute(sql ,(pid,))

print('# 최종 출력')
sql = "select * from students order by id asc"
mycursor.execute(sql)
result = mycursor.fetchall()
print(result)

conn.commit()

mycursor.close()
conn.close()