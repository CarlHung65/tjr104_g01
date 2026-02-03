import pymysql

host = 'localhost'
port = 3306
user = 'root'
passwd = '123456'
db = 'TESTDB'
charset = 'utf8mb4'

conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)