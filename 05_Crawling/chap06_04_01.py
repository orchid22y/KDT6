import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parse
import pandas as pd
import	collections
if	not	hasattr(collections,'Callable'):
    collections.Callable =	collections.abc.Callable

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')

table=bs.find('table',{'class':'wikitable'})
table_data=parse.make2d(table)#2차원 리스트 형태로 변환

# 테이블의 2행을 출력
print('[0]:', table_data[0])
print('[1]:', table_data[1])