import pymysql
db=pymysql.connect('localhost','root','123456')
cur=db.cursor()
cur.execute("create database python;")
cur.execute("use python")
cur.execute("create table t1(id int,name char(20),age tinyint unsigned,sex enum('boy','girl'));")
cur.execute("insert into t1 values(1,'zhangsanfeng',30,'boy'),(2,'wuji.zhang',25,'boy'),(3,'panjielian',25,'girl'),(4,'ximenqing',40,'boy'),(5,'wudalang',33,'boy');")
cur.execute('select*from t1;')
data=cur.fetchone()
print('fetchone的结果是',data)
db.commit()
cur.close()
db.close()
