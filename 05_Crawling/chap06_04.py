import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html,'html.parser')
# 두 개의 테이블 중에 첫 번째 테이블 사용

table=bs.find_all('table',{'class':'wikitable'})[0]
rows=table.find_all('tr') #row:리스트 형태

csvFile = open('editors.csv','wt',encoding='utf-8') # t:text mode
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = [] # 리스트 초기화
        for cell in row.find_all(['th','td']):
            print(cell.text.strip())
            csvRow.append(cell.text.strip()) # 1행의 정보를 리스트에 추가
        writer.writerow(csvRow) # 한 행 씩 csv 파일에 저장

finally:
    csvFile.close()