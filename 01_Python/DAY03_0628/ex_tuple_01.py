#---------------------------------------------------------------------------------------------
# Tuple 데이터 자료형 살펴보기
#   - 다양한 종류의 여러 개 데이터를 저장하는 타입
#   - List와 비슷하지만 추정, 삭제 안됨!!!
#   - 형식 : (데1,..., 데n)
#             데1,..., 데n      //소괄호 생략가능
#             (데,) 또는 데,    //데이터가 1개일 경우 마지막에 ',' 사용하여 다른 자료형과 구분
#---------------------------------------------------------------------------------------------
# 튜플 데이터 생성 ----------------------------------------------------------------------------
datas=()
print(type(datas),datas,len(datas))
datas=(1,5,7)
print(type(datas),datas,len(datas))
'''
<class 'tuple'> () 0
<class 'tuple'> (1, 5, 7) 3
'''
print()
'''
datas=(1)                               ## 튜플X => 정수로 인식
print(type(datas),datas,len(datas))             
>>>TypeError: object of type 'int' has no len()
'''
datas=(1,)                                     
print(type(datas),datas,len(datas))  
datas=1,                                     
print(type(datas),datas,len(datas))     ## ',' 사용하여 다른 자료형과 구분

'''
<class 'tuple'> (1,) 1
<class 'tuple'> (1,) 1
'''
print()

# 튜플 데이터의 원소/요소 읽기 --------------------------------------------------------------------
datas=11,22,33,44,55
#     0  1  2  3  4
#    -5 -4 -3 -2 -1

# 2번 요소 읽기
print(datas[2],datas[-3])
'''
33 33
'''
# 요소/원소 수정 및 삭제 즉, 변경 불가!!!
# datas=11,22,33,44,55
# 마지막 원소를 'A'로 변경 : ERROR
'''
datas[-1]='A'
>> TypeError: 'tuple' object does not support item assignment
'''
# 마지막 원소 삭제 : ERROR
'''
del datas[-1]
>> TypeError: 'tuple' object doesn't support item deletion
'''

# 튜플 데이터의 원소/요소 변경 ==> 형변환 ----------------------------------------------
birthday=(2024,1,1)

# 1월 ===> 3월 변경하기

birthday=list(birthday)
birthday[1] = 3

# List ==> Tuple 형변환
birthday=tuple(birthday)

