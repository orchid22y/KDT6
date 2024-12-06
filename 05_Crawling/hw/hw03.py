from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
html=requests.get("https://finance.naver.com/sise/sise_market_sum.naver")
soup=BeautifulSoup(html.text, 'html.parser')

company=soup.find_all('a',{'class':'tltle'})
company10=[]
company10herf=[]
company10code=[]


for idx, c in enumerate(company[:10]):
    company10.append(c.text) # 상위 10개의 기업 이름
    company10herf.append('https://finance.naver.com'+company[idx]['href'])# 상위 10개의 기업 링크
    company10code.append(company10herf[idx][-6:])# 상위 10개의 기업 종목코드
# print(company10herf)

#open시가/high고가/low저가/present현재 /previous전일
openP=[]
highP=[]
lowP=[]
presentP=[]
previousP=[]

for idx,code in enumerate(company10code):
    companyURL='https://finance.naver.com/item/main.naver?code={0}'.format(code)
    # print(code)
    # print(companyURL)
    html=urlopen(companyURL)
    soup=BeautifulSoup(html,'html.parser')
    tag_info=soup.find('dl')
    #print(tag_info)
    for idx, info in enumerate(tag_info.find_all('dd')):
        #print(idx)
        if idx==3:
            #print(idx,info)
            presentP.append(info.text.split()[1])
        elif idx==4:
            #print(idx,info)
            previousP.append(info.text.split()[1])
        elif idx==5:
            #print(idx,info)
            openP.append(info.text.split()[1])
        elif idx==6:
            #print(idx,info)
            highP.append(info.text.split()[1])  
        elif idx==8:
            #print(idx,info)
            lowP.append(info.text.split()[1])  
        
# print(openP)
# print(highP)
# print(lowP)
# print(presentP)
# print(previousP)




#메뉴입력
def printMenu():
    title='[ 네이버 코스피 상위 10대 기업 목록]'
    print('-'*35)
    print(title)
    print('-'*35)
    for idx, c in enumerate(company10):
        print(f'[{idx+1:>2}] {c}')
    num=input('주가를 검색할 기업의 번호를 입력하세요(-1:종료):')
    return num

#입력확인함수
def checknum(num):
    if num.isdecimal and -1<= num <=10:
        return True
    else:
        return False
    
#출력
def printInfo(num):
    print(company10herf[num])
    print(f'종목명: {company10[num]}')
    print(f'종목코드: {company10code[num]}')
    print(f'현재가: {presentP[num]}')
    print(f'전일가: {previousP[num]}')
    print(f'시가: {openP[num]}')
    print(f'고가: {highP[num]}')
    print(f'저가: {lowP[num]}')


#메인실행

def main():
    while True:
        num=printMenu()
        if num=='-1':
            print('프로그램 종료')
            break
        try:
            num=int(num)
            if 1<= num <=10:
                num-=1
                printInfo(num)
            else:
                print('\n🚨 1~10 사이의 숫자를 입력해주세요.🚨\n')
        except:
            print('\n🚨 숫자를 입력해주세요🚨\n')

main()