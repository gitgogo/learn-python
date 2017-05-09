#coding=utf-8
import MySQLdb
try:
    conn = MySQLdb.connect(
    host = "127.0.0.1", 
    port = 3306,
    user = "root", 
    passwd = "" 
    )
    cur = conn.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS pythonDBnew DEFAULT CHARSET utf8 COLLATE utf8_general_ci;')
    cur.close()
    conn.close()
    print u"创建数据库pythonDB成功! "
except MySQLdb.Error, e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])



#coding=utf-8
import MySQLdb
try:
    conn = MySQLdb.connect(
    host = "127.0.0.1", 
    port = 3306,
    user = "root", 
    passwd = "gloryroad" 
    )
    conn.select_db('pythondb')# 选择pythonDB数据库
    cur = conn.cursor()# 获取游标
    
    # 如果所建表已存在，删除重建
    cur.execute("drop table if exists User;")
    # 执行建表sql语句
    cur.execute('''CREATE TABLE `User`(
    `id` int(11) DEFAULT NULL,
    `name` varchar(255) DEFAULT NULL,
    `password` varchar(255) DEFAULT NULL,
     `birthday` date DEFAULT NULL
                   )ENGINE=innodb DEFAULT CHARSET=utf8;''')
    cur.close()
    conn.close()
    print u"创建数据表成功"
except MySQLdb.Error, e:
     print "Mysql Error %d: %s" %(e.args[0], e.args[1])