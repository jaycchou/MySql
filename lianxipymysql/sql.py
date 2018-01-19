


import pymysql
# 创建一个库Ｐｙｔｈｏｎ　在库中创建一个表ｔ１

#1创建数据库连接（创建一个ｃｏｎｎｅｃｔ对象，ｄｂ）
db=pymysql.connect('localhost','root','123456')
#2 创建游标对象（用ｄｂ对象的cursor方法创建游标）
cursor =db.cursor()
#3 使用游标方法操作数据库
cursor.execute('create database pythonn;')
cursor.execute('use python;')
cursor.execute('create table t1(id int primary key,name char(20),age tinyint unsigned,sex enum("boy","girl"));')
# 4 提交到数据库
db.commit()
#5 关闭游标对象
cursor.close()
#6 关闭数据连接
db.close()
