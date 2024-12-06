from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://www.pythonscraping.com/pages/page1.html')
bs=BeautifulSoup(html.read(),'html.parser') # 클러ㅐ스의 생성자 객체 생성
print(bs)
print(bs.h1) # 웹사이트에서 첫 번째 <h1>태그만 반환
print(bs.h1.string) #.string:태그 내부의 문자열만 가져옴
print(bs.div)#<div>텍스트.....</div>
print(bs.div.text)