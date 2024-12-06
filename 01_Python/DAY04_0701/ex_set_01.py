# -----------------------------------------------------------------------------------------
# Set 자료형 살펴보기
#   - 여러가지 종류의 여러 개 데이터를 저장
#   - 단! 중복 안됨!!
#   - 컬렉션 타입의 데이터 저장 시 Tuple 가능
#   - 형태 : {데이터1, 데이터2,...,데이터n}
# -----------------------------------------------------------------------------------------
##  [Set 생성]------------------------------------------------------------------------------
data=[] # 비어있는 리스트
data=() # 비어있는 튜플
data={} # 비어있는 딕셔너리
data=set() 

print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')
'''
data의 타입 : <class 'set'>, 원소/요소 개수 : 0개, 데이터 : set()
'''
print()

# 여러개 데이터 저장한 set
data={10,30,20,-9,10,0,10,30,10,10}
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')
'''
data의 타입 : <class 'set'>, 원소/요소 개수 : 5개, 데이터 : {0, 20, -9, 10, 30} ## 자동으로 중복 값 삭제
'''
print()

data={9.34,"Apple",10,True,'10'}
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')
'''
data의 타입 : <class 'set'>, 원소/요소 개수 : 5개, 데이터 : {True, '10', 'Apple', 9.34, 10}
'''
print()
'''
data={1,2,3,[1,2,3]}
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')
>> TypeError: unhashable type: 'list'
'''

data={1,2,3,(1,2,3)}
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')
'''
data의 타입 : <class 'set'>, 원소/요소 개수 : 4개, 데이터 : {1, 2, 3, (1, 2, 3)}
'''
print()

data={1,2,3,(1)}
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')
'''
data의 타입 : <class 'set'>, 원소/요소 개수 : 3개, 데이터 : {1, 2, 3}
'''
print()

data={1,2,3,(1,)}
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')
'''
data의 타입 : <class 'set'>, 원소/요소 개수 : 4개, 데이터 : {1, 2, 3, (1,)}
'''
print()

data={1,2,3,(1,)[0]}
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')
'''
data의 타입 : <class 'set'>, 원소/요소 개수 : 3개, 데이터 : {1, 2, 3}
'''
print()
'''
# data2={1,2,3,data}
print(f'data2의 타입 : {type(data2)}, 원소/요소 개수 : {len(data2)}개, 데이터 : {data2}')
>> TypeError: unhashable type: 'set'

# data={1,2,3,{1:100}}
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')
>> TypeError: unhashable type: 'dict'

'''

# set() 내장함수
data={1,2,3}    # ===> set([1,2,3])
data=set()      # Empty set
data=set({1,2,3})
# 다양한 타입 ===>set 벼환
data=set([1,2,3,2,3])

data=set("good")
print(data)
data=list("good")
print(data)
data=({'name':'홍길동','age':12,'name':'베트맨'})
print(data)

'''
{'o', 'd', 'g'}
['g', 'o', 'o', 'd']

'''
