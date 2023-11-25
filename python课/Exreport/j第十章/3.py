import sqlite3
con=sqlite3.connect("D:/company.db")
cur=con.cursor()
cur.execute("update employee set hiredate='20190101'")
con.commit()
cur.close()
con.close()