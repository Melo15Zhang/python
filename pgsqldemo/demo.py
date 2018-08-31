# -*- coding:utf-8 -*-
# python2 method
# 具体配置要根据自己的pg库进行修改
import psycopg2


conn = psycopg2.connect(database='test01',
                        user='test',
                        password='test',
                        host='127.0.0.1',
                        port='3601')
cur = conn.cursor()
cur.execute("select id,type from test limit 10")
rows = cur.fetchall()

print(rows)
conn.commit()
cur.close()
conn.close()
