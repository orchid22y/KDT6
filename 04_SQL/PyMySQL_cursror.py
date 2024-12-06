#cursor.description 속성
#   -전체 컬럼의 이름이 description의 각 인덱스[0]에 저장되어있음

import pymysql
import pandas as pd
import csv

conn = pymysql.connect(host='localhost',	user='root',	password='0506',
db='sakila',	charset='utf8')
cur	= conn.cursor()
cur.execute('select	*	from	language')

desc = cur.description #	헤더 정보를 가져옴 
for	i in range(len(desc)):
    print(desc[i][0], end=' ')
print()

rows = cur.fetchall()	#	모든 데이터를 가져옴
for	data in	rows:
    print(data)
print()

cur.close()
conn.close()	#	데이터베이스 연결 종료

