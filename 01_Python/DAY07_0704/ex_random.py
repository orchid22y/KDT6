#-------------------------------------------------------------------------------------------------
# 모듈 : 변수, 함수, 클래스가 들어있는 파이썬 파일
# 패키지 : 동일한 목적의 모듈들을 모은 것 
#        여러개의 모듈 파일들 존재
# 모듈 사용법 : import 모듈파일명 <----확장자 제외
#-------------------------------------------------------------------------------------------------
import random as rad

# 임의의 숫자를 생성 추출 하기 ---------------------------------------------------------------------
# 임의의 숫자 10개 생성
for c in range(10):
    print(int(rad.random()*10))

print()

# -> randint(a,b)
for cnt in range(10):
    print(rad.randint(0,1))
print('-'*50)
## ----------------------------------------------------------------------------------------------
## [실습] 로또 프로그램을 만들어 주세요.
## - 1 ~ 45 범위에서 중복되지 않는 6개 추출
## ----------------------------------------------------------------------------------------------
## - 반복 횟수 ? 알수 없음
## 무한 반복문
## - 종료조건 ? 중복x 6개 숫자 =>list, set, dic 

idx=0
lotto=[0,0,0,0,0,0]
while True:
    num = rad.randint(1,45)
    if num not in lotto:
        lotto[idx] = num
        idx=idx+1
    if idx==6: break
print(lotto)

lotto={}
key=1
while len(lotto)<=6:
    num = rad.randint(1,45)
    if num not in lotto.values():
        lotto[key]=num
        key=key+1
print(lotto.values())

lotto=set()
key=1
while len(lotto)<6:
    num=rad.randint(1,45)
    num_set=set([num])
    lotto=lotto.union(num_set)
print(lotto)
#----------------------------------------------------------------------------------------------
# set 타입의 add(메서드) : 원소 추가, 중복 시 추가
lotto=set()
while len(lotto)<6:
    num = rad.randint(1,45)
    lotto.add(num)
print(lotto)