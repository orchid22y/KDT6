#----------------------------------------------------------------------------------------
# 연산자
#----------------------------------------------------------------------------------------
# [1] 산술연산자--------------------------------------------------------------------------
#   - 종류 : +, -, *, /, //, %, **

num1=8
num2=3

# 출력형태 : 8 + 3 = 11
print(f'{num1} + {num2} = {num1+num2}')
print(f'{num1} - {num2} = {num1-num2}')
print(f'{num1} * {num2} = {num1*num2}')
print(f'{num1} / {num2} = {num1/num2}')
print(f'{num1} // {num2} = {num1//num2}')
print(f'{num1} % {num2} = {num1%num2}')
print(f'{num1} ** {num2} = {num1**num2}')

'''
8 + 3 = 11
8 - 3 = 5
8 * 3 = 24
8 / 3 = 2.6666666666666665
8 // 3 = 2
8 % 3 = 2
8 ** 3 = 512
'''
print()

#----------------------------------------------------------------------------------------
# [2] 비교연산자--------------------------------------------------------------------------
#   - 종류 : >, <, >=, <=, ==, !=
print(f'{num1} > {num2} = {num1>num2}')
print(f'{num1} < {num2} = {num1<num2}')
print(f'{num1} >= {num2} = {num1>=num2}')
print(f'{num1} <= {num2} = {num1<=num2}')
print(f'{num1} == {num2} = {num1==num2}')
print(f'{num1} != {num2} = {num1!=num2}')

''''
8 > 3 = True
8 < 3 = False
8 >= 3 = True
8 <= 3 = False
8 == 3 = False
8 != 3 = True
'''
print()

# 문자열도 비교 연산 사용 가능
num1='a' 
num2='f'
print(f'{num1} > {num2} = {num1>num2}')
print(f'{num1} < {num2} = {num1<num2}')
print(f'{num1} >= {num2} = {num1>=num2}')
print(f'{num1} <= {num2} = {num1<=num2}')
print(f'{num1} == {num2} = {num1==num2}')
print(f'{num1} != {num2} = {num1!=num2}')

'''
a > f = False
a < f = True
a >= f = False
a <= f = True
a == f = False
a != f = True
'''
print()

num1='aF'
num2='ac'
print(f'{num1} > {num2} = {num1>num2}')
print(f'{num1} < {num2} = {num1<num2}')
print(f'{num1} >= {num2} = {num1>=num2}')
print(f'{num1} <= {num2} = {num1<=num2}')
print(f'{num1} == {num2} = {num1==num2}')
print(f'{num1} != {num2} = {num1!=num2}')

'''
aF > ac = False
aF < ac = True
aF >= ac = False
aF <= ac = True
aF == ac = False
aF != ac = True
'''