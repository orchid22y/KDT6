import csv

f=open('subwayfee.csv',encoding='utf-8-sig')
data=csv.reader(f)
header = next(data)# 한 줄을 읽고 다음 줄로 이동
print(header)
i=1
for row in data:
    print(row)
    if i> 5:
        break
    i+=1
f.close()