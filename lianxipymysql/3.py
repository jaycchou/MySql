import pymysql
db=pymysql.connect('localhost','root','123456','python')
cur = db.cursor()


sel='select*from t1;'
cur.execute(sel)

firstrow=cur.fetchone()
print('第一条记录为：',firstrow)
l=11*'                '
print(l)
manysize=cur.fetchmany(2)
print('第二条记录',manysize)
print(l)
allrow=cur.fetchall()
print('fetchall()的记录是',allrow)
print(l)





db.commit
cur.close()
db.close()
