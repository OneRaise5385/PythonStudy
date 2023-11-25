import sqlite3
con=sqlite3.connect('D:\school.db')
cur=con.cursor()
# 建表
cur.execute('create table student(id primary key,name,sex,birthday)')
# 插入一行
cur.execute("insert into student (id,name,sex,birthday) values ('202131100137','张义举','男','20030118')")
# 带参数插入一行
cur.execute("insert into student (id,name,sex,birthday) values (?,?,?,?)",('202131100138','赵钢','男','20040328'))
# 插入多行
students={('202131100139','张三','女','20030101'),('202131100140','李四','女','20030102')}
cur.executemany("insert into student (id,name,sex,birthday) values (?,?,?,?)",students)
con.commit()
cur.close()
con.close()




