'''
1. 대구 기온 데이터에서 시작 연도, 마지막 연도를 입력하고 특정 월의 최고 기온 및 최저
기온의 평균값을 구하고 그래프로 표현
n daegu-utf8.csv 또는 daegu-utf8-df.csv 파일 이용
n 데이터 구조
 ['날짜', '지점', '평균기온', '최저기온', '최고기온’]
 [0] [1] [2] [3] [4]
n 화면에서 측정할 달을 입력 받아서 진행
n 해당 기간 동안 최고기온 평균값 및 최저기온 평균값 계산
- 최고기온 및 최저기온 데이터를 이용하여 입력된 달의 각각 평균값을 구함
- 문자열 형태의 ‘날짜’ 열의 데이터는 datetime 으로 변경함:
n 하나의 그래프 안에 2개의 꺾은선 그래프로 결과를 출력
- 마이너스 기호 출력 깨짐 방지
- 입력된 월을 이용하여 그래프의 타이틀 내용 변경
- 최고 온도는 빨간색, 최저 온도는 파란색으로 표시하고 각각 마커 및 legend를 표시
'''

#[1]모듈 로드
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

#[2] 파일
daeguDF=pd.read_csv('daegu-utf8.csv',encoding='utf-8-sig')

# 측정할 달 입력 받기
month=input('측정할 달을 입력하세요. : ')

# 해당 기간 동안 최고기온 평균값 및 최저기온 평균값 계산
daeguDF[(month in deaguDF[0])][4].mean()


print(high_avg)

deaguDF.append