import sqlite3
con=sqlite3.connect("D:/company.db")
cur=con.cursor()
cur.execute("delete from employee where id='202131100102'")
con.commit()
cur.close()
con.close()