# UNIT22] 리스트와 튜플 응용하기-----------------------------------------------------------------
## 22.1.1 리스트에 요소 추가하기
#   append:요소 하나를 추가
#   extend:리스트를 연결하여 확장
#   insert: 특정 인덱스에 요소 추가

## 22.1.2 리스트에 요소 하나 추가하기
a=[10,20,30]
a.append(500)
print(a,len(a),'개')

a=[]
a.append(10)
print(a,len(a),'개')

## 22.1.3 리스트 안에 리스트 추가하기
a= [10,20,30]
a.append([500,600])
print(a,len(a),'개')

## 22.1.4 리스트 확장하기
a=[10,20,30]
a.extend([500,600])
print(a,len(a),'개')

##22.1.5 리스트의 특정 인덱스에 요소 추가하기
##  insert(0,요소) : 리스트의 맨 처음에 요소를 추가
##  insert(len(리스트),요소) : 리스트 끝에 요소추가
a=[10,20,30]
a.insert(2,500)
print(a,len(a),'개')

a.insert(0,500)
print(a,len(a),'개')

a.insert(len(a),500)
print(a,len(a),'개')

a.insert(1,[500,600])
print(a,len(a),'개')

## 슬라이싱 사용하여 리스트 중간에 여러 개 추가하기(덮어쓰기)
a=[10,20,30]
a[1:1]=[500,600]    # 시작 인덱스와 끝 인덱스를 같게 지장하면 해당 인덱스 덮어 쓰지 않고 추가 가능
print(a,len(a),'개')

## 21.1.6 리스트에서 요소 삭제하기
##  pop:마지막 요소 또는 특정 인덱스의 요소를 삭제
##  remone:특정 값을 찾아내서 삭제

## 22.1.7 리스트에서 특정 인덱스의 요소를 삭제하기
a=[10,20,30]
a.pop()
print(a,len(a),'개')

a=[10,20,30]
x=[a.pop(1)] #해당 인덱스의 요소를 삭제한 뒤 삭제한 요소를 반환
print(a,len(a),'개')
print(x,len(x),'개')

###  del 사용 가능
a=[10,20,30]
del a[1]
print(a,len(a),'개')

## 22.1.8 리스트에서 특정 값을 찾아서 삭제하기
a=[10,20,30]
a.remove(20)
print(a,len(a),'개')

a=[10,20,30,20]
print(a,len(a),'개')
a.remove(20)
print(a,len(a),'개')
'''
[10, 20, 30, 20] 4 개
[10, 30, 20] 3 개  # 같은 값이 여러 개일 경우 처음 찾은 값을 삭제
'''

## 22.1.9 리스트에서 특정 값의 인덱스 구하기
a=[10,20,30,40,15,20,40]
print(a.index(20))

## 22.1.10 특정 값의 개수 구하기
print(a.count(20))

## 22.1.11 리스트의 순서 뒤집기
a.reverse()
print(a)

## 22.1.12 리스트의 요소를 정렬하기
##  sort() : 오름차순 /sort(reverse=True) : 내림차순
a.sort()
print(a)
a.sort(reverse=True)
print(a)

## 22.1.13 리스트의 모든 요소를 삭제하기
a=[10,20,30]
a.clear()
print(a)

### del
a=[10,20,30]
del a[:]
print(a)

## 22.1.14 리스트를 슬라이스로 조작하기
a=[10,20,30]
a[len(a):]=[500]
print(a)

a=[10,20,30]
a[len(a):]=[500,600] # == a.extend([500,600])과 같음
print(a)

## 22.2 리스트의 할당과 복사 알아보기
a=[0,0,0,0,0]
b=a
print(a is b)
b[2]=99
print(a,'\n',b)

### 리스트 a,b를 완전히 두 개로 만들려면 copy 메서드로 모든 요소를 복사
a=[0,0,0,0,0]
b=a.copy()

print(a is b) ## 다른 객체
print(a==b) ## 복사된 요소는 같음
b[2]=99
print(a)
print(b) ##b만 수정됨


## 22.3.1 for 반복문으로 요소 출력
a=[38,21,53,62,19]
for i in a:
    print(i)

## 22.3.2 인덱스와 요소를 함께 출력
for index, value in enumerate(a): 
    print(index, value)
print()
### for 인덱스, 요소 in enumerate(리스트,start=시작숫자)
a=[38,21,53,62,19]
for index, value in enumerate(a,start=1): 
    print(index, value)

## 22.3.3 while 반복문으로 요소 출력하기
a=[38,21,53,62,19]
i=0
while i<len(a):
    print(a[i])
    i+=1
print()

## 22.4 리스트의 가장 작은 수, 가장 큰 수, 합계 구하기
a=[38,21,53,62,19]
smallest=a[0]

for i in a:
    if smallest>i:
        smallest=i
print(smallest)

largest=a[0]
for i in a:
    if largest<i:
        largest=i
print(largest)

print()
a.sort()
result=a[0]+a[len(a)-1]
print(result)

print()
##22.4.2 요소의 합계 구하기
a=[10,10,10,10,10]
x=0
for i in a:
    x+=i
print(x)

print(sum(a))
print()

## 22.5 리스트 표현식 사용하기
### [식 for 변수 in 리스트]
### list(식 for 변수 in 리스트)

a= [i for i in range(10)]   # 0부터 9까지 숫자를 생성하여 리스트 생성
print(a)

b=list(i for i in range(10)) # 0부터 9까지 숫자를 생성하여 리스트 생성
print(b)

print()

## 22.5.1 리스트 표현식에서 if 조건문 사용하기
### [식 for 변수 in 리스트 if 조건식]
### list(식 for 변수 in 리스트 if 조건식)

# 0~9숫자 중 2의 배수인 숫자(짝수)로 리스트 생성
a=[i for i in range(10) if i%2==0] 
print(a,'\n')

# 0~9 숫자 중 홀수에 5를 더하여 리스트 생성
b=[i+5 for i in range(10)if i%2]
print(b,'\n')

## 22.5.2 for반복문과 if조건문을 여러 번 사용하기
# 2단부터 9단까지 구구단을 리스트로 생성
a=[i*j for i in range(2,10) for j in range(1,10)]
print(a)

## 22.6 리스트에 map 사용하기
### list(map(함수,리스트))
### tuple(map(함수,튜플))


# >>리스트의 모든 요소 정수 변환하기 - for 사용
a=[1.2,2.5,3.7,4.6]
for i in range(len(a)):
    a[i]=int(a[i])
print(a)
# >>리스트의 모든 요소 정수 변환하기 - map 사용
a=[1.2,2.5,3.7,4.6]
a=list(map(int,a))
print(a)

## 22.61 input().split()과 map
#a=map(int,input().split()) 

## 22.7 튜플 응용하기
## 22.7.1 튜플에서 특정 값의 인덱스 구하기

a=(38,21,53,62,19,53)
print(a.index(53))

## 22.7.2 특정 값의 개수 구하기
a=(10,20,30,15,20,40)
print(a.count(10))

## 22.7.3 for 반복문으로 요소 출력하기
a=(37,21,53,62,19)
for i in a:
    print(i,end=" ")
print()

## 22.7.4 튜플 표현식 사용하기
### tuple(식 for 변수 in 리스트 if 조건식)
a=tuple(i for i in range(10) if i %2 ==0)
print(a)
## 22.7.5 tuple에 map사용하기
a=(1.2,2.5,3.7,4.6)
a=map(int,a)
print(a)

## 22.7.6 튜플에서 가장 작은 수, 가장 큰 수, 합계 구하기
a=(38,21,53,62,19)
print(f'최소값 : {min(a)}, 최대값 : {max(a)},총 합계 = {sum(a)}')

## 22.9 연습문제: 리스트에서 특정 요소만 뽑아내기
a=['alpha', 'bravo', 'aharlie','delta','echo','foxtrot','golf','hotel','india']
b=[i for i in a if len(i)==5]
print(b)

## 22.10 심사문제 : 2의 거듭제곱 리스트 생성하기
#a,b=map(int,input("시작,끝 :").split())
# for n in range(a,b+1):
#     print(2**n,end=" ")
# print()

#UNIT25] 딕셔너리 응용하기
## 25.1.1 딕셔너리에 키-값 쌍 추가하기
### setdefault:키-값 쌍 추가
### update:키의 값 수정, 키가 없으면 키-값 쌍 추가

## 25.1.2 딕셔너리에 키와 기본값 저장하기
x={'a':10,'b':20,'c':30,'d':40}
x.setdefault('e')
print(x)
x.setdefault('f',100)
print(x)

##25.1.3 딕셔너리에서 키의 값 수정하기
x.update(a=90)
print(x)
x.update(g=90) # 키가 없을 경우 'g': 9 추가
print(x)
### update(키=값)은 키가 문자열일 때만 사용
### 키가 숫자일 경우 update(딕셔너리) 처럼 딕셔너리를 넣어 값을 수정
y={1:'one', 2:'two'}
y.update({1:'ONE',3:'THREE'})
print(y)

y.update([[2,'TWO'],[4,'FOUR']]) # 리스트나 튜플도 가능
print(y)

y.update(zip([1,2],['one','two'])) # zip 사용
print(y)

## 25.1.4 딕셔너리에서 키-값 쌍 삭제하기
x={'a':10,'b':20,'c':30,'d':40}
d=x.pop('a')
print(d)
print(x)
d=x.pop('z',0) # 키가 없을 경우 지정한 기본값 반환
print(d)

## 25.1.5 딕셔너리에서 임의의 키-값 쌍 삭제하기
x={'a':10, 'b':20, 'c':30,'d':40}
i=x.popitem()
print(i)
print(x)

##25.1.6 딕셔너리의 모든 키-값 쌍을 삭제하기
x={'a':10, 'b':20, 'c':30,'d':40}
x.clear()
print(x)

## 25.1.7 딕셔너리에서 키의 값을 가져오기
### get(키) : 딕셔너리에서 특정 키의 값을 가져옴
x={'a':10, 'b':20, 'c':30,'d':40}
print(x.get('a'))

### get(키, 기본값) : 기본값을 지정하면 딕셔너리에 키가 있을 때는 해당 키의 값 반환, 없을 경우 기본값 반환
print(x.get('t',5))

## 25.1.8 딕셔너리에서 키-값 쌍을 모두 가져오기
### items:키-값 쌍을 모두 가져옴
print(x.items()) 
### keys:키를 모두 가져옴
print(x.keys())
### values : 값을 모두 가져옴
print(x.values())

print()

## 25.1.9 리스트와 튜플로 딕셔너리 만들기
keys=['a','b','c','d']
x=dict.fromkeys(keys)
print(x) ## 리스트로 키를 생성, 값은 모두 None으로 저장

y=dict.fromkeys(keys,100)
print(y) ## 리스트와 값을 지정하면 해당 값이 키의 값으로 저장

### 딕셔러리는 없는 키에 접근 했을 경우 에러발생
## defaultdict(기본값생성함수)



from collections import defaultdict # collections 모듈에서 defaultdic 가져옴
y= defaultdict(int) #int로 기본값 생성
print(y['z']) # 없는키, 기본값 0으로 생성

## 25.2 반복문으로 딕셔너리의 키-값 쌍을 모두 출력하기
x={'a': 10, 'b': 20, 'c': 30,'d':40}

### items:키-값 쌍을 모두 가져옴
for i in x:
    print(i,end=' ')
for key, value in x.items():
        print(key,value)
print()

### keys:키를 모두 가져옴
for key in x.keys():
    print(key,end=' ')
print()

### values: 값을 모두 가져옴

for values in x.values():
    print(values,end=' ')
print()
