import pymysql
db=pymysql.connect('localhost','root','123456','python')
cur=db.cursor()
a='show tables;'
b='show databases;'
#cur.execute('create table t3 (id int);')
cur.execute('show tables;')
print(cur.fetchall())






db.commit()
cur.close()
db.close()
