
#[UNIT 29] 함수 사용하기
# 29.1.1 함수 만들기
def hello():
    print('Hello, World!')

# 29.1.2 함수 호출하기
hello()    
'''
Hello, World!
'''

##  빈 함수 만들기
def hello():
    pass        #내용이 없는 빈 함수를 만들 때는 코드 부분에 pass를 넣는다.

# 29.2 덧셈 함수 만들기
def add(num1,num2):
    print(num1+num2)

# 29.3 함수의 결과를 반환하기
def add(num1, num2):
    return num1+num2
x=add(10,20)
print(x)
print()
## 함수 중간에 빠져나오기
def not_ten(a):
    if a==10:
        return
    print(a,'입니다.',sep='')

not_ten(5) #5입니다.
not_ten(10) # 출력 X

# 29.4 함수에서 값을 여러개 반환하기
# def 함수이름()

def add_sub(a,b):
    return a+b, a-b #return에 값이나 변수를 ,(콤마)로 구분해서 지정

x,y=add_sub(10,20)
print('x,y')

# 29.7 연습문제 : 몫과 나머지를 구하는 함수 만들기
x=10
y=3

def get_quotient_remainder(a,b):
    return a//b, a%b
quotient, remainder= get_quotient_remainder(x,y)
print('목 : {0}')

#29.8 심사문제:사칙 연산 함수 만들기

def calc():
    a,b=map(int,input( "정수 두개 입력하세요.").split())
    print(f'덧셈 : {a+b}, 뺄셈 : {a-b}, 곱셈 : {a*b},나눗셈 : {float(a/b)}')

#calc()
