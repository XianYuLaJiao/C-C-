# 数据库操作
# 1，连接数据库 2，拿到游标 3，执行sql 4,关闭游标 5，关闭数据库的连接
import sqlite3

# 连接
conn =sqlite3.connect('test.db')

# 拿到游标
cursor = conn.cursor()

# 执行sql
sql ='create table user (id int(11) primary0)'
cursor.execute(sql)