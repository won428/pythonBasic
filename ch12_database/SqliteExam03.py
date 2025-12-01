import sqlite3

class SqliteDB:
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def getJoindata(self):
        sql = ' select st.id, st.name, st.birth, sg.subject, sg.jumsu'
        sql += ' from students st join sungjuk sg'
        sql += ' on st.id = sg.id '

        result = self.cursor.execute(sql)
        return result
    # end def getJoindata

    def getSubQuery(self, name):
        sql = " select * from sungjuk "
        sql += " where id = (select id from students where name = '%s')"

        result = self.cursor.execute(sql % (name))
        return result

    def getJumsu(self, name):
        sql = " select jumsu from sungjuk "
        sql += " where id = (select id from students where name = '%s')"

        mydata = self.cursor.execute(sql % (name))
        total = 0 # 총합
        cnt = 0 # 행수

        for row in mydata:
            total += row[0]
            cnt += 1

        if cnt == 0:
            return None

        average = total/cnt
        return (total, average)

# end class SqliteDB

dbname = 'student.db'
mydb = SqliteDB(dbname)

dataset = mydb.getJoindata()
for row in dataset:
    print('아이디 : ', row[0], end='', sep='')
    print(', 이름 : ', row[1], end='', sep='')
    print(', 생일 : ', row[2], end='', sep='')
    print(', 과목 : ', row[3], end='', sep='')
    print(', 점수 : ', row[4], end='', sep='')
    print()
print('-'*20)

who = '조용원'
dataset = mydb.getSubQuery(who)
for id, subject, jumsu in dataset :
    print('아이디 : ', id, end='', sep='')
    print(', 과목 : ', subject, end='', sep='')
    print(', 점수 : ', jumsu, end='', sep='')
    print()
print('-'*20)

who = '고두식'
mytuple = mydb.getJumsu(who)
if mytuple != None :
    print('학생 이름 :', who)
    print('총점 :', mytuple[0])
    print('평균 :', mytuple[1])
else:
    print('존재하지 않는 회원입니다.')

print('-'*20)

print('finished')