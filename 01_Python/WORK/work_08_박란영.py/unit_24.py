#[UNIT 24] 문자열 응용하기
#24.1.1 문자열 바꾸기
print('Hello, World!'.replace('world','python'))

#24.1.2 문자 바꾸기
#translate는 문자열 안의 문자를 다른 문자로 바꿉니다. 
#먼저 str.maketrans('바꿀문자','새문자')로 변환테이블 생성 -> translate(테이블)을 사용하면 문자를 바꾼 뒤 결과를 반환 
table=str.maketrans('aeiou','12345')
print(table)
'''
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
'''
print('apple'.translate(table))
'''
1ppl2
'''

#24.1.3 문자열 분리하기
print('apple pear grape pineapple orange'.split())
##split(기준문자열)
print('apple, pear, grape, pineapple orange'.split(','))

#24.1.4 구분자 문자열과 문자열 리스트 연결하기
#join(리스트)
print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
print('-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
'''
apple pear grape pineapple orange
apple-pear-grape-pineapple-orange
'''

# 24.1.5 소문자를 대문자로 바꾸기
#upper()
print('python'.upper())
# 24.1.6 대문자를 소문자로 바꾸기
#lower()
print('python'.lower())

# 24.1.7~9공백 삭제하기
print('   Pythin   '.lstrip())
print('   Pythin   '.rstrip())
print('   Pythin   '.strip())
'''
Pythin
   Pythin
Pythin
'''

#24.1.10 왼쪽의 특정 문자 삭제하기
print(', python.'.lstrip(',.'))
#24.1.11 오른쪽의 특정 문자 삭제하기
print(', python .'.rstrip(',.'))
#24.1.12 양쪽의 특정 문자 삭제하기
print(', python .'.strip(',.'))
'''
 python.
, python
 python
'''

#24.1.13-15 문자열 정렬하기
print('python'.ljust(10))
print('python'.rjust(10))
print('python'.center(10))
'''
python
    python
  python
'''

print()
# 24.1.16 메서드 체이닝
## 문자열 메서드는 처리한 결과를 반환하도록 만들어져있음. 따라서 메서드를 계속 연결해서 호출 가능
print('python'.rjust(10).upper())
'''
    PYTHON
'''

# 24.1.17 문자열 왼쪽에 0 채우기
#zfill(길이) :지정된 길에에 맞춰서 문자열의 왼쪽에 0을 채움(zero fill)
#               단, 문자열의 길이보다 지정된 길이가 짧다면 아무것도 채우지 않음

print('35'.zfill(4))
print('3.5'.zfill(6))
print('hello'.zfill(10))
'''
0035
0003.5
00000hello
'''

#24.1.18 문자열 위치 찾기
print("apple pineapple".find('pl'))
print("apple pineapple".find('xy'))

'''
2
-1   ## 찾는 문자열이 없으면 -1 반환
'''

#24.1.19 오른쪽에서 부터 문자열 위치 찾기
#rfind('찾을문자열')
print("apple pineapple".rfind('pl'))
print("apple pineapple".rfind('xy'))
'''
12
-1
'''

#24.1.20 문자열 위치 찾기
print("apple pineapple".index('pl'))
#24.1.21 오른쪽에서부터 문자열 위치 찾기
print("apple pineapple".rindex('pl'))

#24.1.22 문자열 개수 세기
print("apple pineapple".count('pl'))
'''
2
'''

#24.2 문자열 서식 지정자와 포매팅 사용하기
#24.2.1 서식 지정자로 문자열 넣기
#'%s' %'문자열'

print('I am %s.'%'jamse')
'''
I am jamse.
'''
name='maria'
print('I am %s.'%'name')

# 24.2.2 서식 지정자로 숫자 넣기
#'%d' % 숫자
print('I am %d years old'%20)
'''
I am 20 years old
'''
#24.2.3 서식 지정자로 소수점 표현하기
#'%f' %숫자
print('%f'%2.3)
#'%.자리수f'%숫자
print('%.2f'%2.3)
print('%.3f'%2.3)
'''
2.300000
2.30
2.300
'''
#24.2.4 서식 지정자로 문자열 정열하기
#%길이s
print("%10s"%'python')
'''
    python
'''
#%-길이s
print('%-10s'%'python')

#24.2.5 서식 지정자로 문자열 안에 값 여러 개 넣기
#'%d %s'%(숫자,'문자열')
print("Today is %d %s"%(3,'April'))
print("Today is %d%s"%(3,'April'))
'''
Today is 3 April
Today is 3April
'''
# 24.2.6 format 메서드 사용하기
#'{인덱스}'.format(값)
print('Hello,{0}'.format('world!'))
print('Hello,{0}'.format('100'))
'''
Hello,world!
Hello,100
'''

# 24.2.7 format메스드로 값을 여러개 넣기
print('Hello,{0}, {2}, {1}'.format('Python','Script',3.6))
'''
Hello,Python, 3.6, Script
'''

#24.2.8 format메서드로 같은 값을 여러 개 넣기
print('{0} {0} {1} {1}'.format('python','Script'))
'''
python python Script Script
'''

#24.2.9 format 메서드에서 인덱스 생략하기
# 만약 {}에서 인덱스를 생략하면 format에 지정한 순서대로 값이 들어갑니다.

# 24.2.10 format 메서드에서 인덱스 대신 이름 지정하기
print('Hello,{language} {version}'.format(language='Python',version=3.6))
'''
Hello,Python 3.6
'''

#24.2.12 format 메서드로 문자열 정렬하기
#'{인덱스:<길이}'.format(값)
print('{0:<10}'.format('python')) # 왼쪽정렬
print('{0:>10}'.format('python')) # 오른쪽 정렬
print('{0:^10}'.format('python')) # 가운데 정렬
'''
python
    python
  python
'''

#24.2.13 숫자 개수 맞추기
#'%0개수d'%숫자
print('%03d'%1)
print('{0:03d}'.format(35))
'''
001
035
'''

# '%0개수.자리수f'%숫자
print('%08.2f'%3.6)
print('{0:08.2f}'.format(150.37))

# 24.2.14 채우기와 정렬을 조합해서 사용하기
# '{인덱스:[[채우기]정렬][길이][.자릿수][자료형]}'
print('{0:0<10}'.format(15)) # 길이 10, 왼쪽으로 정렬하고 남는 공간은 0으로 채움
print('{0:0>10}'.format(15)) # 길이 10, 오른쪽으로 정렬하고 남는 공간은 0으로 채움
print('{0:0>10.2f}'.format(15)) # 길이 10, 오른쪽으로 정렬하고 소수점 자릿수는 2자리
'''
1500000000
0000000015
0000015.00
'''
print('{0: >10}'.format(15))    # 남는 공간을 공백으로 채움
print('{0:>10}'.format(15))     # 채우기 부분을 생략하면 공백이 들어감
print('{0:x>10}'.format(15))    # 남는 공간을 문자 x로 채움
'''
        15
        15
xxxxxxxx15
'''
# 24.4 연습문제:파일 경로에서 파일명만 가져오기
path = 'C:\\Users\\dojang\\Appdata\\Local\\Programs\\Python\\Python36-32\\python.exe'
a=path.rfind('\\')
print(path[a+1:])
'''
python.exe
'''
# raw 문자열 사용하기
# 문자열 앞에 r 또는 R을 붙이면 row 문자열이 됩니다. 이 raw 문자열은 이스케이프 시퀀스를 그대로 저장할 때 사용
print(r'C:\Users\dojang\Appdata\Local\Programs\Python\Python36-32\python.exe')

#C:\Users\dojang\Appdata\Local\Programs\Python\Python36-32\python.exe

# 24.5 심사문제 : 특정 단어 개수 세기
'''
#표준입력
the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the
'''

msg=input("").split()

cnt=0
for m in msg:
    m2=m.strip(',.')
    if m2=='the':
        cnt+=1
print(cnt)

# 24.6 심사문제:높은 가격순으로 출력하기
#표준입력 51900;83000;158000;367500;250000;59200;128500;1304000
cost=list(map(int,input("가격").split(';')))
cost=sorted(cost,reverse=True)

for c in cost:
    print('{c:>9,}')