			create table ccb(name char(20),money int); insert into ccb
values('zhangsan',10000);
		icbc 
			create table icbc(name char(20),money int); insert into icbc values('lisi',4000);


start transaction;#开始转账
update ccb set money=5000 where name='zhangsan';# 赚钱
update icbc set money=9000 where 工行断电了;#宕机
rollback;#回滚
commit;# 转账成功
