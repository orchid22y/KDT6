import pymysql

conn = pymysql.connect(host='localhost',
                       user='ranyoung',passwd='0506',db='scraping',charset='utf8')

cur = conn.cursor()
cur.execute('use scraping')
cur.execute("select * from pages where id=2")

print(cur.fetchone())
cur.close()
conn.close()

