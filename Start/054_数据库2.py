# 查询数据库的内容
import sqlite3
con=sqlite3.connect('D:\school.db')
cur=con.cursor()
cur.execute("select * from student")
for row in cur:
    print(row)
cur.execute("select count (id) as 男同学个数 from student where sex='男'")
for row in cur:
    print(row)
cur.close()
con.close()