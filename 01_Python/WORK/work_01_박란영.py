#3.7 연습문제 : 문자열 출력하기

print('Hello, world!')
print('Python Programming')

print()

#3.8 심사문제:문자열 출력하기
#   'Hello, World!' 두 개를 각 줄에 출력하는 프로그램을 만드세요
#       (대소문자 구분과 띄어쓰기가 정확해야 합니다.)
print('Hello, world!')
print('Hello, world!')

print()

#5.1.1 사칙연산

print(f'1 + 1 = {1+1} ')
print(f'1 - 2 = {1-2} ')
print(f'2 * 2 = {2*2} ')
print(f'5 / 2 = {5/2} ')
print(f'4 / 2 = {4/2} ')

print()

#5.1.2 나눗셈 후 소수점 이하를 버리는 // 연산자
print(f'5 // 2 = {5//2} ')
print(f'4 // 2 = {4//2} ')

print()

#실수에 // 연산자를 사용하면 결과는 실수가 나오며 소수점 이하는 버림. 따라서 결과는 항상 .0으로 끝남
print(f'5.5 // 2 = {5//2} ') 
print(f'4 // 2.0 = {4 // 2.0} ') 
print(f'4.1 // 2.1 = {4.1 // 2.1} ')

print()

#5.1.3 나눗셈 후 나머지를 구하는 % 연산자
print(f'5 % 2= {5%2} ') 
print()


#5.1.4 거듭제곱을 구하는 ** 연산자
print(f'2 ** 10 = {2**10}')
print()


#5.1.5 값을 정수로 만들기
print(int(3.2)) # 숫자
print(int(5/2)) # 계산식
print(int('10')) # 문자열
print()

#5.1.6 객체의 자료형 알아내기
print(type(10))
print()

#   [참고] 몫과 나머지 함께 구하기
print(divmod(5,2)) # 튜플 형태로 결과 도출

quotient, remainder = divmod(5,2) # 변수 두개로 저장 가능
print(quotient, remainder)

print()

#   [참고] 2진수, 8진수, 16진수
#       2진수 : 숫자 앞에 0b를 붙이며 0과 1사용
#       8진수 : 숫자 앞에 0o(숫자0과 소문자 o)를 붙이며 0부터 7까지 사용
#       16진수 : 숫자 앞에 0x 또는 0X를 붙이며 0부터 9, A부터 F까지 사용(소문자 a부터 f도 가능)
print('0b110 =>',0b110)
print('0o10 =>',0o10)
print('0xf =>',0xf)
print()

#5.2 실수 계산하기
print(f'3.5 + 2.1 = {3.5+2.1}')
print(f'4.3 - 2.7 = {4.3 - 2.7}')
print(f'1.5 * 3.1 = {1.5*3.1}')
print(f'5.5 / 3.1 = { 5.5/3.1}')
print()

#5.2.1 실수와 정수 함께 계산
print(f'4.2 + 5 = {4.2+5}')
print()
#5.2.2 값을 실수로 만들기

print(f'float(5) => {float(5)}') #숫자
print(f'float(1+2) => {float(1+2)}') #계산식
print(f"float('5.3') => {float('5.3')} ") # 문자열
print(f' type(3.5) => {type(3.5)}')
print()
#   [참고] 복소수
#       허수부는 숫자 뒤에 j를 붙임
print(f'1.2+1.3j => {1.2+1.3j}')
# 두 실수를 복소수로 만들 때는 complex를 사용
print(f'complex(1.2, 1.3) => {complex(1.2, 1.3)}')
print()

#5.5 연습문제
M=12
print(int(0.2467*M+4.159))

#5.6 심사문제 
ap=102
print(ap*0.6+255)
print()

#6.6 연습문제:정수 세 개를 입력받고 합계 출력하기
a,b,c=map(int,input("정수를 3개 입력하세요. : ").split())
print(f'a+b+c=> {a+b+c}')
print()

#6.7 심사문제 : 변수 만들기
a,b,c=50,100,'None'
print(a)
print(b)
print(c)
print()

#6.8 심사문제 : 평균점수 구하기

kor,eng,math,sci=map(int, input("국어, 영어, 수학, 과학 점수를 입력하세요 : ").split())
print(int((kor+eng+math+sci)/4))
print()
#7.4 연습문제 : 날짜와 시간 출력하기
year=2000
month = 10
day = 27
hour=11
minute=43
second=59

print(year, month, day, sep='/',end=" ")
print(hour, minute, second,sep=':')
print()
#7.5 심사문제 : 날짜와 시간 출력하기
year,month,day,hour,minute,second=input("년, 월, 일, 시, 분, 초 입력 ").split()
print(year,month,day,sep='-',end="T")
print(hour,minute,second,sep=':')
print()
#8.4 연습문제:합격 여부 출력하기
korean=92
english=47
mathematics=86
science=81

print(korean>=50 and english>=50 and mathematics>=50 and science>=50)
print()

#8.5 심사문제 : 합격 여부 출력하기

kor,eng,mat,sci=map(int, input("국어, 영어, 수학, 과학 점수 입력 ").split())
print(kor>=90 and eng>80 and mat>85 and sci>=80)
print()


#9.3 연습문제 : 여러 줄로 된 문자열 사용하기
s='''Python is a programming language that lets you work quickly
and
integrate systems more effectively.'''
print(s)
print()
#9.4 심사문제 : 여러 줄로 된 문자열 사용하기

s="""'Python' is a \"programming langeuage\"
that lets you work quickly
and
integrate systems more effectively."""
print(s)
print()