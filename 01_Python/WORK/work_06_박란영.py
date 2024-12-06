# UNIT17] while 반복문
## 17.1.1 초기값을 1부터 시작하기
i=1
while i <= 100:
    print('Hello, World!',i)
    i+=1

print()

## 17.1.2 초기값을 감소시키기
i=100
while i>0:
    print('Hello, World!',i)
    i-=1

## 17.1.3] 입력한 횟수대로 반복하기
count=int(input("반복할 횟수를 입력하세요: "))
i=0
while i<count:
    print('Hello, World!')
    i+=1
print()
count=int(input("반복할 횟수를 입력하세요: "))
while count>0:
    print('Hello, World!')
    count-=1
print()
## 17.2 반복 횟수가 정해지지 않은 경우
### import모듈
import random # random 모듈을 가져옴 (난수생성)
print(random.random())
### random.randint(a,b) ->a와 b 사이의 난수
print(random.randint(1,6))
### random.choice(시퀀스객체)
dice=[1,2,3,4,5,6]
print(random.choice(dice))

print()

## 17.3 while 반복문으로 무한 루프 만들기
# while True: # while에 True를 지정하면 무한루프
#     print('Hello, world!')

## 17.5 연습문제:변수 두 개를 다르게 반복하기
i=2
j=5

while i<=32 or j>=1:
    print(i,j)
    i*=2
    j-=1

print()

##17.3 심사문제 : 교통카드 잔액 출력하기
cost=int(input(""))

while cost>0:
    cost-=1350
    if cost>0 :
        print(cost)
    
#UNIT18] break,continue로 반복문 제어하기
## 18.1.1 While에서 break로 반복문 끝내기
i=0
while True:             # 무한루프
    print(i)    
    i+=1                # i를 1씩 증가시킴
    if i == 100:break   # i가 100일때 반복문을 끝냄
## 18.1.2 for에서 break로 반복문 끝내기
for i in range(10000):
    print(i)
    if i==100:break
##18.2.1 for에서 condinue로 코드 실행 건너뛰기
for i in range(100):
    if i%2 ==0:
        continue
    print(i)

## 18.2.2 while 반복문에서 conrinue로 코드 실행 건너뛰기
i=0
while i<100:
    i+=1
    if i % 2 ==0:
        continue
    print(i)

### 반복문과 pass

for i in range(10):
    pass # 10번 반복, 아무일도 하지 않음
# while True:
#     pass  # 무한루프, 아무일도 하지 않음

## 18.3.1 입력한 숫자까지 홀수 출력하기
count = int(input('반복할 횟수를 입력하세요 : '))
for i in range(count+1):
    if i%2==0:
        continue
    print(i)
print()
## 18.5 연습문제:3으로 끝나는 숫자만 출력하기
i=0
while True:
    if i%10!=3:
        i+=1
        continue
    if i>73:
        break
    print(i, end=' ')
    i+=1
print()
## 18.6 심사문제 : 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
start,stop=map(int,input("시작숫자, 끝 숫자 :").split())
i=start
while True:
    if i==stop+1: break
    print(i,end=' ')
    i+=1
print()

# UNIT19] 계단식으로 별 출력하기
for i in range(6):
    print(i*('*'))
print()
## 19.2 사각형으로 별 출력하기
for i in range(5):
    for j in range(5):
        print('*',end="")
    print()
print()
## 19.2.1 사각형 모양 바꾸기
for i in range(3):
    for j in range(7):
        print('*',end="")
    print()
print()
## 19.3 계단식으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j<=i:
            print('*',end='')
    print()
print()
## 19.3.1 대각선으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j==i:
            print('*',end='')
        else:
            print(' ',end='')
    print()
print()
## 19.5 연습문제 : 역삼각형 모양으로 별 출력하기

for i in range(5):
    for j in range(5):
        if j<i:
            print(' ',end="")
        else:
            print('*',end="")
    print()
print()
## 19.6 심사문제:산 모양으로 별 출력하기
height=int(input("산높이:"))
for i in range(height):
    for j in reversed(range(height)):
        if j > i:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(height-1):
        if j < i:
            print('*', end='')
    print()
print()
# UNIT20] FizzBuzz 문제
## 20.11부터 100까지 숫자 출력하기
for i in range(1,101):
    print(i)
## 20.2 3의 배수일 때와 5의 배수일 때 처리하기
for i in range(1,101):
    if i%3==0:
        print('Fizz')
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
print()
## 20.3 3과 5의 공배수 처리하기
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("Fizz Buzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
print()
## 20.4 논리 연산자를 사용하지 않고 3과 5의 공배수 처리하기

for i in range(1,101):
    if i%15==0:
        print("Fizz Buzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
## 20.5 코드 단축하기
for i in range(1,101):
    print('Fizz'*(i%3==0)+'Buzz'*(i%5==0) or i)

## 20.7 연습문제:2와 11의 배수, 공배수 처리하기
for i in range(1,101):
    if i%2==0 and i%11==0:
        print("Fizz Buzz")
    elif i%2==0:
        print("Fizz")
    elif i%11==0:
        print("Buzz")
    else:
        print(i)

## 20.8 심사문제:5와 7의 배수, 공배수 처리하기
start,last=map(int,input("시작값, 마지막값 : ").split())
for i in range(start,last+1):
    if i%5==0 and i%7==0:
        print("Fizz Buzz")
    elif i%5==0:
        print("Fizz")
    elif i%7==0:
        print("Buzz")
    else:
        print(i)
print()