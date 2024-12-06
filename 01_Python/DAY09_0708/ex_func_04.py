def add(num1,num2):
    return num1+num2

def minus(num1,num2):
    return num1-num2

def multi(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2
## 계산기 프로그램--------------------------------------------------------------------------
#   - 사용자 종료를 원할 때 종료 => 'X','x' 입력 시
#   - 연산방식과 숫자 데이터 입력 받기
##-----------------------------------------------------------------------------------------

# while True:
#     #(1) 입력 받기
#     req=input("연산(+,-,*,/) 방식과 정수 2개 입력(예:+ 10 2) :")
#     #(2) 종료 조건 검사
#     if req=='x' or req=='X':
#         print("계산기를 종료합니다.")
#         break
#     #(3) 입력에 연산방식과 데이터 추출 '+ 10 2'
#     op, num1,num2 =req.split() #['+','10','2']
#     #str 정수 ==> int 변환
#     num1=int(num1)
#     num2=int(num2)
#     #연산방식에따라서 계산 진행
#     if op=='+':result=num1+num2
#     elif op=='-' :result=num1-num2
#     elif op=='*':result=num1+num2
#     elif op=='/':
#         result=num1/num2 if num2 else '0으로 나눌 수 없습니다.'
#     else:
#         result=f'{op}는 지원되지 않는 연산 입니다.'
#     print(f'{num1} {op} {num2} = {result}')

##-----------------------------------------------------------------------------------------
# 함수기능 : 계산기 메뉴를 출력하는 함수
# 함수이름 : print_menu
# 매개변수 : 없음
# 함수결과 :없음
##-----------------------------------------------------------------------------------------    
def print_menu():
    print(f'{"*":*<19}')
    print(f'{"*   계   산   기  *":<19}')
    print(f'{"*":*<19}')
    print(f'{"*   1. 덧    셈   *":<19}')
    print(f'{"*   2. 뻴    셈   *":<19}')
    print(f'{"*   3. 곱    셈   *":<19}')
    print(f'{"*   4. 나 눗 셈   *":<19}')
    print(f'{"*   5. 종    료   *":<19}')
    print(f'{"*":*<19}')


##-----------------------------------------------------------------------------------------
# 함수기능 : 입력 받은 데이터가 유효한 데이터인지 검사하는 함수
# 함수이름 : check_data
# 매개변수 : str 데이터, 데이터 수
# 함수결과 : True 또는 False
##-----------------------------------------------------------------------------------------

def check_data(data,count):
    # 입력된 str 데이터를 리스트로 형변환 : split()
    data=data.split()
    #갯수 체크
    if len(data)==count:
        # 0~9로 구성된 str인지 체크
        isOk=True
        for d in data:
            if not d.isdecimal():
                isOk=False
                break
        return isOk
    else:
        return False    
##-----------------------------------------------------------------------------------------
# 함수기능 : 연산 수행 후 결과를 반환하는 함수
# 함수이름 : calc
# 매개변수 : 함수명, str숫자 2개, str 연산자 기호
# 함수결과 :
##-----------------------------------------------------------------------------------------
def calc(func,num1,num2,op):
    #num1=int(num1)
    #num2=int(num2)
    data=input("정수 2개(예: 10 2):")
    if check_data(data,2):
        data=data.split()
        print(f'결과 : {data[0]} {op} {data[1]} = {func(int(data[0]),int(data[1]))}')
    print(f'결과 : {data}는 잘못된 데이터 입니다.')
   

## 계산기 프로그램--------------------------------------------------------------------------
#   - 사용자에게 원하는 계산을 선택하는 메뉴 출력
#   - 종료 메뉴 선택 시 프로그램 종료
#   => 반복 ----> 무한반복 : while
##-----------------------------------------------------------------------------------------
while True:
    # 메뉴 출력
    print_menu()

    # 메뉴 선택 요청
    #choice=int(input("메뉴 선택: "))
    choice=input("메뉴 선택")
    if choice.isdecimal():
        choice=int(choice)
    else:
        print("0~9사이 숫자만 입력하세요")
        continue


    # 종료 조건(5번 메뉴 선택) 처리
    if choice==5:
        print("프로그램을 종료 합니다.")
        break
    elif choice==1 :    #덧셈
        print("덧셈")
        num1,num2=input("정수 2개(예:10 2)").split()
        calc(add,num1,num2,'+')
    elif choice==2 :    #뺄셈
        print("뺄셈")
        num1,num2=input("정수 2개(예:10 2)").split()
        calc(minus,num1,num2,'-')
    elif choice==3 :    #곱셈
        print("곱셈")
        num1,num2=input("정수 2개(예:10 2)").split()
        calc(multi,num1,num2,'*')
    elif choice==4 :    #나눗셈
        print("나눗셈")
        num1,num2=input("정수 2개(예:10 2)").split()
        calc(div,num1,num2,'/')
    else:
        print("선택된 메뉴가 없습니다.")

    