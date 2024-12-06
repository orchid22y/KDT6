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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

subject=['웹에이젼시','포털_인터넷_콘텐츠','쇼핑몰_오픈마켓','네트워크_통신_모바일','하드웨어_장비','보안_백신','솔루션_SI_ERP_CRM','IT컨설팅','게임','기타_IT웹_통신']


driver = webdriver.Chrome()
result=[]
for idx,sub in enumerate(subject):

    # #마지막 페이지 찾기
    # xpath_company ='//*[@id="listInterviews"]/div/div[2]/article/a[8]'
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_company)))
    # company=driver.find_element(By.XPATH, xpath_company).get_attribute('href')
    # num =int(re.search(r'(\d+)(?!.*\d)', company).group(1))


    try:
        for page in range(30):
            url=f'https://www.jobplanet.co.kr/interviews/by_industry/{idx+701}?page={page+1}'
            
            driver.get(url)
            try:
                for i in range(10):

                    xpath_company = f'//*[@id="listInterviews"]/div/div[1]/section[{i+1}]/div[1]/div[1]/h2/a'
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_company)))
                    company=driver.find_element(By.XPATH, xpath_company).text
                    # print(company_text)
                        
                    xpath_job = f'//*[@id="listInterviews"]/div/div[1]/section[{i+1}]/div[1]/div[1]/p/span[1]'
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_job)))
                    job= driver.find_element(By.XPATH, xpath_job).text
                    # print(job_text)

                    xpath_title = f'//*[@id="listInterviews"]/div/div[1]/section[{i+1}]/div[1]/div[2]/a/h2'
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_title)))
                    title=driver.find_element(By.XPATH, xpath_title).text
                    # print(title_text)

                    xpath_question=f'//*[@id="listInterviews"]/div/div[1]/section[{i+1}]/div[1]/div[2]/dl/dd[1]'
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_question)))
                    question=driver.find_element(By.XPATH, xpath_question).text
                    #print(question_text)

                    
                    xpath_answer=f'//*[@id="listInterviews"]/div/div[1]/section[{i+1}]/div[1]/div[2]/dl/dd[2]'
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_answer)))
                    answer=driver.find_element(By.XPATH, xpath_answer).text
                    # print(answer_text)
                    result.append([company,job,title,question,answer])
                    
            except:
                print(f'{page+1}에러')
            finally:
                print(page+1)    
    except:
        print()
    finally:
        column=['company','job','title','question','answer']
        resultdf=pd.DataFrame(result,columns=column)
        resultdf.to_csv(f'{idx+1}jobplanet-{sub}.csv',index=True,encoding='utf-8')
        print(f'{sub}저장')
        result=[]
driver.quit()