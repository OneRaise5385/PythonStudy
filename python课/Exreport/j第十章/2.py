import sqlite3
con=sqlite3.connect('D:/company.db')
cur=con.cursor()
cur.execute("select * from employee")
for i in cur:
    print(i)
cur.close()
con.close()