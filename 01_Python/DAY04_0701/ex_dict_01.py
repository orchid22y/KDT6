#---------------------------------------------------------------------------------------------------
# Dict 자료형 살펴보기
#   - 데이터의 의미를 함께 저장하는 자료형
#   - 형태 {키1:값, 키2:값,..., 키n:값}
#   - 키는 중복 X,값은 중복
#   - 데이터 분석 시 파일 데이터 가져올 때 많이 사용
#---------------------------------------------------------------------------------------------------
## [Dict 생성]
data={}
print(f'data => {len(data)}개, {type(data)}, {data}')
'''
data => 0개, <class 'dict'>, {}
'''
print()

# 사람에 대한 정보 : 이름, 나이, 성별
data={'name':'마징가', 'age':100, 'gender':'남'}
print(f'data => {len(data)}개, {type(data)}, {data}')
'''
data => 3개, <class 'dict'>, {'name': '마징가', 'age': 100, 'gender': '남'}
'''
print()

# 강아지에 대한 정보 : 품종, 무게, 색상, 성별, 나이
data={'type':'mix','weight':3,'color':'white','gender':'M','age':2}
print(f'data => {len(data)}개, {type(data)}, {data}')
'''
data => 5개, <class 'dict'>, {'type': 'mix', 'weight': 3, 'color': 'white', 'gender': 'M', 'age': 5}
'''
print()

## [Dict 원소/요소 읽기]----------------------------------------------------------------------
##  - 키를 가지고 값/데이터 읽기
##  - 형식 : 변수명[키]

# 색상 출력
print(f'색상 : {data["color"]}')
'''
색상 : white
'''
print()

# 성별, 품종 출력
print(f'성별 : {data["gender"]}, 품종 : {data["type"]}')
'''
성별 : M, 품종 : mix
'''
print()


## [Dict 원소/요소 변경]----------------------------------------------------------------------
##  -변수명[키]=새로운 값
# 나이 5살 ==> 6살
data['age']=6
print(data)
'''
{'type': 'mix', 'weight': 3, 'color': 'white', 'gender': 'M', 'age': 6}
'''
print()

# 몸무게 ===>8kg
data['weight']=8
print(data)
'''
{'type': 'mix', 'weight': 8, 'color': 'white', 'gender': 'M', 'age': 6}
'''
print()

## [Dict 원소/요소 삭제]----------------------------------------------------------------------
##  - del 변수명[키] 또는 del (변수명[키])
## 성별 데이터 삭제
del data['gender']
print(data)
'''
{'type': 'mix', 'weight': 8, 'color': 'white', 'age': 6}
'''
print()


## [Dict 원소/요소 추가]----------------------------------------------------------------------
##  -변수명[새로운 키]= 값
data["name"]="뽀삐"
print(data)
'''
{'type': 'mix', 'weight': 8, 'color': 'white', 'age': 6, 'name': '뽀삐'}
'''