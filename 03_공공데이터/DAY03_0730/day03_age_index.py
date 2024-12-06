import csv

f=open('age.csv',encoding='euc_kr')
data= csv.reader(f)
header=next(data)



print('-'*80)
print('age.csv index')
print('-'*80)

for i in range(len(header)):
    print(f'[{i:3}]:{header[i]}') #{1:3} :3자리의 공간에 i값 출력

f.close()