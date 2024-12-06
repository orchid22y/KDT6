import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib

def parse_district_name(city):
    '''
    '행정구역' 명칭에서 숫자 부분을 제거함
    - 서울특별시 종로구 (1111000000)
    '''
    city_name=re.split('[()]',city)
    #print(city_name)
    return city_name[0]


def print_population(population):
    '''
    특정 지역의 인구 현황을 화면에 출력함
    '''

    for i in range(len(population)):
        print(f'{i:3d}세: {population[i]:4d}명', end=' ')
        if (i+1)%10==0:
            print()

def draw_population(city_name,popluation_list):
    '''
    특정 지역에 대한 인구 분포를 그래프로 나타냄(plot)
    - city_name:지역이름
    - population_list:0~100세 이상까지 인구수 리스트
    '''

    plt.title(f'{city_name} 인구현황')
    plt.xlabel('나이')
    plt.ylabel('인구수')
    plt.bar(range(101),popluation_list)
    plt.xticks(range(0,101,10)) # 0세 ~ 100세 이상
    plt.show()

def get_population(city):
    f=open('age.csv',encoding='euc_kr')
    data=csv.reader(f)
    next(data) #헤더 정보 건너뜀

    population_list=[]
    full_distrit_name=''
    for row in data:
        if city in row[0]:
            full_distrit_name=parse_district_name(row[0]) #(시 구 동 ) 이름만 분리: 지역 번호 제거
            for data in row[3:]:
                data=data.replace(',','')#천 단위 콤마 제거
                population_list.append(int(data))
            break # 처음으로 일치하는 도시명만 검색하기 위함

    f.close()
    print_population(population_list)
    draw_population(full_distrit_name,population_list)

city = '대구'
get_population(city)