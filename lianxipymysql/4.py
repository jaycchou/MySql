import pymysql
db=pymysql.connect('localhost','root','123456','python')
cur=db.cursor()
#cur.execute('start transaction')

sqlin="insert into t1 values(10,'liudehua',50,'boy');update t1  age=88 where id =3;"

try:
	cur.execute(sqlin)
	#cur.execute(sqlin2)
except:

	db.rollback()
	





db.commit()
cur.close()
db.close()

