# -------------------------------------------------------------------------------------------------
# 제어문 - 반복문과 break
#   - 중첩 반복문일 경우의 break는 가장 가까이 있는 반복문만 종료
# -------------------------------------------------------------------------------------------------
## [실습] 단의 숫자만큼만 구구단을 출력하세요.
## 2 * 1 = 2  2 * 2 = 4
## 3 * 1 = 3  3 * 2 = 6  3 * 3 = 9
## 4 * 1 = 4  4 * 2 = 8  4 * 3 = 12 4 * 4 = 16
## [중첩 반복문] 내부 반복문 종료 시 외부 반복문 종료-------------------------------------------------
##  -내부 반복문 종료여부를 변수 저장
##  - 외부 반복문에서는 내부 반복문이 종료되면 함께 종료
for d in range(2,10):
    for n in range(1,10):
        if n==d+1:break
        print(f'{d} * {n} = {d*n}',end=" ")
    print()
print()

dan=int(input("출력 원하는 단 입력 : "))
isBreak=False

for d in range(2,10):
    print(f'\n[{d}단]',end=" ")
    for n in range(1,10):
        print(f'{d} * {n} = {d*n:<3}',end=' ')
        if n==d:
            isBreak=True
            break
    print('outer for')
    if isBreak:break

for d in range(2,10):
    print(f'\n[{d}단]',end=" ")
    for n in range(1,10):
        print(f'{d} * {n} = {d*n:<3}',end=' ')
        if n==d:break
    if d == dan: break

for d in range(2, dan+1):
    print(f'\n[{d}단]', end=" ")
    for n in range(1,d+1):
        print(f'{d}*{n}={d*n:<2}',end='  ')
