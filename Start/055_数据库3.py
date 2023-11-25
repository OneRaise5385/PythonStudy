# 更新和删除数据
import sqlite3
con=sqlite3.connect('D:\school.db')
cur=con.cursor()

cur.execute("update student set birthday='20021216' where id='202131100137'")
cur.execute("select * from student")
print('更新后')
for row in cur:
    print(row)
con.commit()
cur.close()
con.close()
