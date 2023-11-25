import sqlite3
con=sqlite3.connect('D:\company.db')
cur=con.cursor()
# 建表
cur.execute('create table employee(id primary key,name,sex,birthday,hiredate)')
# 插入一行
cur.execute("insert into employee (id,name,sex,birthday,hiredate) values \
('202131100101','张三','男','20010101','20211010')")
# 带参数插入一行
cur.execute("insert into employee (id,name,sex,birthday,hiredate) values \
(?,?,?,?,?)",('202131100102','李四','男','20010102','20211010'))
# 插入多行
employees={('202131100139','王五','女','20030101','20211012'),\
    ('202131100140','赵六','女','20030102','20210316'),\
    ('202131100110','孙七','男','20030101','20211016')}
cur.executemany("insert into employee (id,name,sex,birthday,hiredate) values \
    (?,?,?,?,?)",employees)
con.commit()
cur.close()
con.close()
