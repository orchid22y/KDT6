#UNIT 12 딕셔너리 사용하기------------------------------------------------------------
## 12.1 딕셔너리 사용하기 - 딕셔너리={키1:값1, 키2:값2}
lux={'health':490, 'mana':334, 'melee':550,'armor':18.72}
print(lux,'\n')

## 12.1 키 이름이 중복 되면?
lux={'health':490,'health':890, 'mana':334, 'melee':550,'armor':18.72}
print(lux,'\n') # 키가 중복되면 가장 뒤에 있는 값만 사용함

## 12.1.2 딕셔너리 키의 자료형
x={100:'hundred',False:0,3.5:[3.5,3.5]}
print(x,'\n') #키는 문자열, 정수, 실수, 불도 사용 가능 리스트와, 딕셔너리는 사용X

## 12.1.3 빈 딕셔너리 만들기
x={}
y=dict()
print(x,y,'\n')

## 12.1.4 dict로 딕셔너리 만들기
##  dict는 키와 값을 연결하거나, 리스트, 튜플, 딕셔너리로 딕셔너리를 만들 때 사용
##  - 딕셔너리=dict(키1=값1,키2=값2)
##  - 딕셔너리=dict([(키1,값1),(키2,값2)]
##  - 딕셔너리=dict(zip([키1,키2],[값1,값2])
##  - 딕셔너리=dict({키1:값1,키2:값2}

lux1=dict(health=490, mana=334,melee=550,armor= 18.72)
print(lux1,'\n')

lux2=dict(zip(['health','mana','melee','armor'],[490,334,550,18.72]))
print(lux2,'\n')

lux3=dict([('health',490),('mana',334),('melee',550),('armor', 18.72)])
print(lux3,'\n')

lux4=dict({'health':490, 'mana':334, 'melee':550,'armor':18.72})
print(lux4,'\n')

## 12.2 딕셔너리의 키에 접근하고 값 할당하기
##  -딕셔너리[키]
##  -키를 지정하지 않은 상태는 해당 딕셔너리 전체를 뜻함
print(lux['health'],lux['armor'],'\n')

## 12.2.1 딕셔너리의 키에 값 할당하기
##  -딕셔너리[키]=값
print(lux)
lux['health']=2037
lux['mana']=1184
print(lux)
lux['mana_regen']=3.28 # 없는 키에 값을 할당하면 해당 키가 추가되고 값이 할당 됨
print(lux,'\n')
## 없는 키에선 값을 가져올 수 없음

## 12.2.2 딕셔너리에 키가 있는지 확인하기
##  - 키 in 딕셔너리
print('health' in lux)
print('attack_speed' in lux)
##  - 키 not in 딕셔너리
print('health' not in lux)
print('attack_speed' not in lux)
print()

## 12.2.3 딕셔너리의 키 개수 구하기
##  - len(딕셔너리)
lux={'health':490, 'mana':334, 'melee':550,'armor':18.72}
print(len(lux),'\n')

## 12.4 연습문제 : 딕셔너리에 게임 캐릭터 능력치 저장하기
cmaille={
    'health':575.6,
    'health_regen':1.7,
    'mana':338.8,
    'mana_regen':1.63,
    'melee':125,
    'attack_damage':60,
    'attack_speed':0.625,
    'armor':26,
    'magic_resistance':32.1,
    'monement_speed':340
}

print(cmaille['health'])
print(cmaille['monement_speed'],'\n')

## 12.5 심사문제 : 딕셔너리에 게임 캐릭터 능력치 저장하기
d1=input().split()
d2=input().split()

d3=dict(zip(d1,d2))
print(d3,'\n')

# UNIT if조건문으로 특정 조건일 때 코드 실행하기------------------------------------------
## 13.1.3 if 조건문에서 코드를 생략하기
x=10
if x==10:
    pass

## 13.6 연습문제 : if 조건문 사용하기
x = 5
if x != 10:
    print('ok')

print()

## 13.7 심사문제:온라인 할인 쿠폰 시스템 만들기
cash=int(input("가격입력:"))
dc=input("할인쿠폰 입력 : ")
if dc=="Cash3000":
    print(cash-3000)
elif dc=="Cash5000":
    print(cash-5000)
else:
    print(cash)

print()
# UNIT14 else를 사용하여 두 방향으로 분기하기
## 14.3 if 조건문의 동작 방식 알아보기
##  - 숫자는 정수(2진수,10진수,16진수), 실수와 관계 없이 0이면 거짓, 0이 아닌 수는 참
if True:
    print('참')
else:
    print('거짓') # True는 참

if False:
    print('참')
else:
    print('거짓') # False 는 거짓

if None:
    print('참')
else:
    print('거짓') # None은 거짓

if 0:
    print('참')
else:
    print('거짓') # 0 은 거짓

if 1:
    print('참')
else:
    print('거짓') # 1은 참

if 0x1f:    # 16진수
    print('참')
else:
    print('거짓') # 0x1f 참
if 0b1000: # 2진수
    print('참')
else:
    print('거짓') # 0b1000은 참

if 13.5: #실수
    print('참')
else:
    print('거짓') # 13.5는 참

print()
## 14.3.2 if 조건문에 문자열 지정하기
##  -문자열은 내용이 있을 때 참, 빈 문자열은 거짓
if 'Hello': # 문자열
    print('참') #문자열은 참
else:
    print('거짓')

if '': # 빈 문자열
    print('참')
else:
    print('거짓') # 빈 문자열은 거짓 (0, None,''=>거짓)
print()
##  - 0, None, 빈 문자열을 not으로 뒤집으면?
if not 0: 
    print('참') 
else:
    print('거짓') #not 0 은 참

if not None:
    print('참')
else:
    print('거짓') # not None은 참

if not '':
    print('참')
else:
    print('거짓') # not 빈 문자열은 참
print()
### False로 취급하는 것들
###     - None
###     - False
###     - 0인 숫자들:0,0.0,0j
###     - 비어 있는 문자열, 리스트, 튜플, 딕셔너리, 세트:'',"",[],(),{},set()
###     - 클래스 인스턴스의 __bool__(),__len() 메서드가 0 또는 False를 반환할 때
### 위에 나열한 것을 제외한 모든 요소는 True로 취급

## 14.6 연습문제:합격 여부 판단하기
written_test=75
coding_test=True

if written_test >=80 and coding_test == True:
    print('합격')
else:
    print('불합격')
print()
## 14.7 심사문제:합격 여부 판단하기

kor,eng,math,sci=map(int,input("점수입력:").split())

if 0<=kor<=100 and 0<=eng<=100 and 0<=math<=100 and 0<=sci<=100 :
    if (kor+eng+math+sci)/4>=80:
        print('합격')
    else:
        print('불합격')
else:
    print("잘못된 점수")
print()

# UNIT15 elif를 사용하여 여러 방향으로 분기하기
# 15.1.2 음료수 자판기 만들기

button=int(input("1.콜라,2.사이다,3,환타"))

if button==1:
    print("콜라")
elif button==2:
    print("사이다")
elif button==3:
    print("환타")
else:
    print("제공하지 않는 메뉴")

print()

## 15.3 연습문제:if, elif, else 모두 사용하기
x=int(input())
if 11<=x<=20:
    print('11~20')
elif  21<=x<=30:
    print('21~30')
else:
    print("아무것도 해당하지 않음")
print()

## 15.4 심사문제 : 교통카드 시스템 만들기
age=int(input('만 나이 입력:'))
balance=9000
if age<7:
    print(balance)
elif 7<=age<=12:
    balance=balance-650
    print(balance)
elif 13<=age<=18:
    balance=balance-1050
    print(balance)
else:
    balance=balance-1250
    print(balance)

print()
