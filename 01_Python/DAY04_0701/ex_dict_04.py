#---------------------------------------------------------------------------------------------------
# Dict 자료형 살펴보기
#   - Dict 자료형 전용의 함수 즉, 메서드(Method) 사용
#   - 사용법 : 변수명.함수명
#---------------------------------------------------------------------------------------------------
person={'name':'홍길동', 'age':20, 'job':'학생'}
dog={'kind':'mix','weight':3,'color':'white','gender':'M','age':5}
jumsu={'국어':90,'수학':178,'체육':100}

##[연산자]-----------------------------------------------------------------------------------------
# 산술 연산 X
# person+dog

# 멤버 연산자 : in, not in
#       key : 
print('name'in dog)
print('name'in person)
'''
False
True
'''
print()
#       value: dict 타입에서는 key만 멤버 연산자로 확인
#print('허스키'in dog)
#print('20'in person)

#value추출
print('허스키' in dog.values())
print('20'in person.values())
'''
False
False
'''

print()
##[내장함수]--------------------------------------------------------------------------------------
##  -원소/요소 개수 확인 : len()
print(f'dog의 요소 개수 : {len(dog)}개')
print(f'person의 요소 개수 : {len(person)}개')
'''
dog의 요소 개수 : 5개
person의 요소 개수 : 3개
'''
print()

##  -요소/원소 정렬 : sorted()
##  -키만 정렬
print(f' dog 오름차순정렬 : {sorted(dog)}')
print(f' dog 내림차순정렬 : {sorted(dog,reverse=True)}')
'''
 dog 오름차순정렬 : ['age', 'color', 'gender', 'kind', 'weight']
 dog 내림차순정렬 : ['weight', 'kind', 'gender', 'color', 'age']
'''
print()


'''
print(f' dog 오름차순정렬 : {sorted(dog.values())}')
>> TypeError: '<' not supported between instances of 'int' and 'str' #값 데이터 타입이 달라 정렬 불가능
'''

print(f'jumsu 값 오름차순 정렬 : {sorted(jumsu.values())}')
print(f'jumsu 키 오름차순 정렬 : {sorted(jumsu)}')

'''
jumsu 값 오름차순 정렬 : [90, 100, 178]
jumsu 키 오름차순 정렬 : ['국어', '수학', '체육']
'''

print()
print(f'jumsu 키 오름차순 정렬 : {sorted(jumsu.items())}')
'''
jumsu 키 오름차순 정렬 : [('국어', 90), ('수학', 178), ('체육', 100)]
'''
print()

print(f'jumsu 값 오름차순 정렬 : {sorted(jumsu.items(),key=lambda x:x[1])}')
'''
jumsu 값 오름차순 정렬 : [('국어', 90), ('체육', 100), ('수학', 178)]
'''
print()

##  - 동일한 타입에서 정렬 가능함-------------------------------------------------------------------------
n1=[1,4,9,-2]
n2=['a','z','f']
n3=[1,'A',-4,9,'f']
#print(sorted(n3))