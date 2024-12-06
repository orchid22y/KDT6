##-----------------------------------------------------------------------------------------------------
## ==> 1줄로 조건식을 축양 : 조건부 표현식
##-----------------------------------------------------------------------------------------------------
## [실습1] 임의의 숫자가  5의 배수인지 여부 결과를 출력하세요.
num=4

result="5의 배수가 아님" if num%5 else "5의 배수"

print(f'{num}은 {result}')


if not num%2 : print("2의 배수")
elif not num%5: print("5의 배수")
else: print("둘다 아님")

## [실습2] 문자열을 입력 받아서 문자열의 원소 개수를 저장
##  - 단 원소 개수가 0이면 None저장
##  -(1) 입력받기 input()
##  -(2) 원소/요소 개수 파악 len()
##  -(3) 원소/요소 개수 저장 단, 0인 경우 None 저장하기
msg=input("문자를 입력하세요")
result= len(msg) if len(msg) else None
print(f'{msg}의 원소/요소 개수 : {result}')


## [실습3] 연산자(4칙 연산자:+,-,*,/)와 숫자 2개 입력 받기
##  - 입력된 연산자에 따라 결과 저장
##  - 입력 예 )+ 10 3 출력 : 13

data=input("4칙연산자 1개와 숫자 2개 입력\n(예: + 10 3)").split()
num1=int(data[1])
num2=int(data[2])

if data[0]=='+': result= {num1 + num2}
elif data[0]=='-': result= {num1 - num2}
elif data[0]=='*': result= {num1 * num2}
elif data[0]=='/': result= {num1 / num2}
else:
    print(f'잘못된 입력입니다.')

    
print(f'{num1} {data[0]} {num2} = {result}')

