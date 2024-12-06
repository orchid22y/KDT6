#UNIT16 for반복문으로 Hello, World! 100번 출력하기
## 16.1 for와 range 사용하기
for n in range(101):
    print('Hello, world!')

print()

## 16.1.1 반복문에서 변수의 변화 알아보기

for n in range(101):
    print('Hello, world!',n)
print()
## 16.2.1 시작하는 숫자와 끝나는 숫자 지정하기
##  for 변수 in range(시작, 끝):

for n in range(5,12):
    print('Hello, world!',n)
print()
## 16.2.2 증가폭 사용하기
##  for 변수 in range(시작, 끝, 증가폭):
for n in range(0,10,2):
    print('Hello, world!',n)
print()

## 16.2.3 숫자를 감소시키기
for n in range(10,0,-1):
    print('Hello, world!',n)
print()

for n in reversed(range(0,10)):
    print('Hello, world!',n)
print()

## 16.2.4 입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count):
    print('Hello, world!',i)
print()

## 16.3 시퀀스 객체로 반복하기
a=[10,20,30,40,50]
for i in a:
    print(i)
print()

fruits=('apple','orange','grape')
for f in fruits:
    print(f)
print()

for l in 'Python':
    print(l,end=" ")
print()

for l in reversed('Python'):
    print(l,end=" ")
print()

## 16.5] 연습문제 : 리스트의 요소에 10을 곱해서 출력하기
x=[49,-17,25,102,8,62,21]
for i in x:
    print(i*10,end=' ')
print()

## 16.6 심사문제: 구구단 출력하기
dan=int(input())
for d in range(1,10):
    print(f'{dan} * {d} = {dan*d}')