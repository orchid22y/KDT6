#-----------------------------------------------------------------------------------------
# list 데이터 자료형 살펴보기
#   - 여러 개의 데이터를 저장하는 타입
#   - 다른 종류의 데이터도 함께 저장 가능
#   - 형식 : [데1, 데2,...,데n]
#-----------------------------------------------------------------------------------------
# 나이, 키, 몸무게를 저장
age=16
height=170
weight=70

# 여러 개 데이터를 하나의 변수명으로 저장
# 리스트
my=[16,170,70]

# 리스트 내의 원소/요소 접금 ==> 인덱싱
# 0번원소 출력
print(my[0])
'''
16
'''
print()
#마지막원소 출력
print(my[2],my[-1])
'''
70 70
'''
print()

# 리스트 내의 원소/요소 여러개 접근 ==> 슬라이싱
# 0번, 1번 원소 출력
print(my[0:2],my[:2],my[:-1])
'''
[16, 170] [16, 170] [16, 170]
'''
print()

#[차이점]----------------------------------------------------------------------------------------
# 0번, 1번 원소 출력
print(f'인덱싱 : {my[0]},{my[1]}, {type(my[0])}')
print(f'슬라이싱 : {my[0:2]}, {type(my[0:2])}')

'''
인덱싱 : 16,170, <class 'int'>          # 개별 원소의 타입
슬라이싱 : [16, 170], <class 'list'>    # 리스트로 출력      >>필요한 타입에 따라 다르게 사용
'''