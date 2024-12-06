
## 계산기 프로그램--------------------------------------------------------------------------
#   - 사용자 종료를 원할 때 종료 => 'X','x' 입력 시
#   - 연산방식과 숫자 데이터 입력 받기

while True:
    #(1) 입력 받기
    req=input("연산(+,-,*,/) 방식과 정수 2개 입력(예:+ 10 2) :")
    #(2) 종료 조건 검사
    if req=='x' or req=='X':
        print("계산기를 종료합니다.")
        break
    #(3) 입력에 연산방식과 데이터 추출 '+ 10 2'
    op, num1,num2 =req.split() #['+','10','2']
    #str 정수 ==> int 변환
    num1=int(num1)
    num2=int(num2)
    #연산방식에따라서 계산 진행
    if op=='+':result=num1+num2
    elif op=='-' :result=num1-num2
    elif op=='*':result=num1+num2
    elif op=='/':
        result=num1/num2 if num2 else '0으로 나눌 수 없습니다.'
    else:
        result=f'{op}는 지원되지 않는 연산 입니다.'
    print(f'{num1} {op} {num2} = {result}')