# 10.1 리스트 만들기
a=[38,21,53,62,19]
print(a)
print()

# 10.1.1 리스트에 여러 가지 자료형 저장하기
person=['james',17,175.3,True]
print(person)
print()

# 10.1.2 빈 리스트 만들기
a=[]
b=list()
print(a,b)
print()

# 10.1.3 range를 사용하여 리스트 만들기
a=list(range(10))
print(a)

b=list(range(5,12))
print(b)

c=list(range(-4,10,2))
print(c)

d=list(range(10,0,-1))
print(d)

print()

# 10.2 튜플 사용하기

a=(38,21,53,62,19)
print(a)
a=38,21,53,62,19
print(a)
person=('james',17,175.3,True)
print(person)
print()

# 10.2.1 요소가 한 개 들어있는 튜플 만들기
a=38, #',' 붙여야함
print(a)
print()
# 10.2.2 range를 사용하여 튜플 만들기
#   *튜플 = tuole(range(횟수))
a= tuple(range(10))
print(a)
#   *튜플 = tuole(range(시작,끝))
b=tuple(range(5,12))
print(b)
#   *튜플 = tuole(range(시작,끝,증가폭))
c=tuple(range(-4,10,2))
print(c)

print()

#10.2.3 튜플을 리스트로 만들고 리스트를 튜플로 만들기
a=[1,2,3]
print(f'{a} -> {tuple(a)}')

b=[4,5,6]
print(f'{a} -> {list(b)}')
print()

#   [참고] 리스트와 튜플로 변수 만들기
##   변수 여러 개를 한 번에 만들기
a,b,c=[1,2,3]
print(a,b,c)
d,e,f=(4,5,6)
print(d,e,f)
print()

##   리스트와 튜플 변수로 변수 여러 개 만들기
x=[1,2,3]
a,b,c=x
print(a,b,c)

y=(4,5,6)
d,e,f=y
print(d,e,f)

print()

##    리스트 언패킹 형식으로 입력 값을 변수 여러 개에 저장
x=input().split()
a,b=x
print(a,b)
print()

# 10.4 연습문제 : range로 리스트 만들기
a=list(range(5,-10,-2))
print(a)
print()

# 10.5 심사문제 : range로 튜플 만들기
a=tuple(range(-10,10,int(input())))
print(a)
print()

# 11.1.1 특정 값이 있는지 확인하기
#   값 in 시퀀스객체
a=[0,10,20,30,40,50,60,70,80,90]
print(30 in a)
print(100 in a)

#   값 not in 시퀀스객체
print(30 not in a)
print(100 not in a)
print()

# 11.1.2 시퀀스 객체 연결하기
##  시퀀스객체1 + 시퀀스객체2

a=[0,10,20,30]
b=[9,8,7,6]
c=a+b
print(c)
print()
#   *range는 +연산자로 객체 연결X , range를 리스트 또는 튜플로 만들어서 연결
#   *문자열끼리 +연산자로 연결 가능, 문자열+정수(or 실수) => str로 형변환 후 연결 가능

# 11.1.3 시퀀스 객체 반복하기
#       시퀀스객체*정수
#       정수*시퀀스객체

a=[0,10,20,30]
print(a*3)
#   *range는 불가능(리스트나 튜플로 변환하여 사용),문자열 가능
print()

# 11.2.1 리스트와 튜플의 요소 개수 구하기
a=[0,10,20,30,40,40,50,60,70,80,90]
print(len(a))
b=(38,76,43,62,19)
print(len(b))
print()

# 11.2.2 range의 숫자 생성 개수 구하기
a=range(0,10,2)
print(f'{a},{len(a)}개')
print()

# 11.3 인덱스 사용하기
a=[38,21,53,62,19,"apple"]
print(a[-1][0])
print()
# 11.3.4 요소에 값 할당하기
#   * 시퀀스객체[인덱스]=값

a=[0,0,0,0,0]
a[:]=38,21,53,62,19
print(a)
print()

#   ** 튜플,range,문자열은 읽기 전용, 수정 불가

# 11.3.5 del로 요소 삭제하기
#   * del 시퀀스 객체[인덱스] ## 튜플,range,문자열 불가
a=[38,21,53,62,19]
del a[2]
print(a)
print()

#11.4.5 len 응용하기
a=[0,10,20,30,40,50,60,70,80,90]
print(a[:len(a)])
print()

#11.4.6 튜플,range,문자열에 슬라이스 적용하기
r=range(10)
print(r[4:7])   #range객체 새로 생성됨
print(r[4:])
print(r[:7:2])
print()

print(list(r[4:7]))   #range->list로 변환
print(list(r[4:]))
print(list(r[:7:2]))
print()

# 11.4.7 슬라이스에 요소 할당하기
a=[0,10,20,30,40,50,60,70,80,90]
a[2:5]=['a','b','c'] # 인덱스 2부터 4까지 값 할당
print(a)

a[2:5]=['a'] # 인덱스 2부터 4까지에 값 1개를 할당하여 요소의 개수가 줄어듬
print(a)

a[2:5]=['a',1,5,8,'w'] # 인덱스 2~4까지 값을 5개를 할당하여 요소의 개수가 늘어남
print(a)

a[2:8:2]=['a','b','c'] # 인덱스 2부터 2씩 증가시키면서 인덱스 7까지 할당
# *인덱스 증가폭을 지정했을 때는 슬라이스 범위의 요소 개수와 할당할 요소 개수가 정확히 일치해야 함
# * 튜플,range,문자열은 슬라이스 범위를 지정하더라도 요소 할당 불가
print()


# 11.4.8 del로 슬라이스 삭제하기
a=[0,10,20,30,40,50,60,70,80,90]
del a[2:5]
print(a)
a=[0,10,20,30,40,50,60,70,80,90]
del a[2:8:2]
print(a)
# * 튜플,range,문자열은 슬라이스 삭제 불가
print()

# 11.6 연습문제: 최근 3년간 인구 출력하기
year=[2011,2012,2013,2014,2015,2016,2017,2018]
population=[10249679,10195318,10143645,10103233,10022181,9930616,9857426,9838892]
print(year[-3:])
print(population[-3:])
print()

# 11.7 연습문제 : 인덱스가 홀수인 요소 출력하기
n=-32,75,97,-10,9,32,4,-15,0,76,14,2
print(n[1::2])
print()

# 11.8 심사문제:리스트의 마지막 부분 삭제하기
x=input().split()
del x[-5:]
print(tuple(x))
print()

# 11.9 심사문제 : 문자열에서 인덱스가 홀수인 문자와 짝수인 문자 연결하기
msg=input()
msg2=input()
msg3=msg[1::2]+msg[::2]
print(msg3)
