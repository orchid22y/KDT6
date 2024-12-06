from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd


# #키워드 및 키워드 링크 리스트
subject=[]
subject_url=[]

url="https://careerly.co.kr/qnas"
html= requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')


tag=soup.find_all('li',{'class':"tw-flex-none"})
tag2=soup.find_all('a',{'class':"tw-flex tw-items-center tw-gap-1.5 tw-py-1.5 tw-px-2.5 tw-border tw-border-solid tw-rounded-full hover:tw-bg-color-background-hover tw-border-color-slate-200"})

sub=[]
for idx, a in enumerate(tag2):
    subject_url.append('https://careerly.co.kr/'+tag2[idx]['href'])
    subject.append(a.find('span',{'class':"tw-text-xs tw-font-bold tw-text-color-text-bold"}).text)
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


cnt=0

for idx, url in enumerate(subject_url):
    driver = webdriver.Chrome()
    driver.get(url)
    result_list=[]
    sub=subject[idx].split()[0]

    print(sub)
    #스크롤을 통해 모든 콘텐츠를 로드
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # 페이지 하단으로 스크롤
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # 페이지 로딩 대기
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    try:
        for i in range(200):
            print(cnt)
            xpath_title =f'//*[@id="__next"]/div/div[2]/div/div/a[{i+1}]/p[1]/span'
            title_text = driver.find_element(By.XPATH, xpath_title).text
            # print(title1_text)

            xpath_content = f'//*[@id="__next"]/div/div[2]/div/div/a[{i+1}]/p[2]'
            content_text = driver.find_element(By.XPATH, xpath_content).text
            # print(content1_text)
            cnt+=1
            result_list.append([sub,title_text,content_text])
    except:
        print('error')
    
    finally:
        driver.quit()
        columns=['subject','title','content']
        resultdf=pd.DataFrame(result_list,columns=columns)
        resultdf.to_csv(f'careerly QnA-{sub}.csv',index=True,encoding='utf-8')
        print(f'{idx+1}.{sub}저장완료')


