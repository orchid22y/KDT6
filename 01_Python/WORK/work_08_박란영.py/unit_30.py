#[UNIT 30] 함수에서 위치 인수와 키워드 인수 사용하기
#30.1.1 위치 인수를 사용하는 함수를 만들고 호출하기
def print_numbers(a,b,c):
    print(a)
    print(b)
    print(c)

print_numbers(10,20,30)
print()
#30.1.2 언패킹 사용하기
x=[10,20,30]
print_numbers(*x)
print()
#30.1.3 가변 인수 함수 만들기
# def 함수이름(*매개변수):
#     코드

def print_numbers(*args):
    for arg in args:
        print(arg)

print_numbers(10)
print()
print_numbers(10,20,30,40)

# 고정 인수와 가변 인수를 함께 사용하기
#   고정 인수와 가변 인수를 밤께 사용할 때는 다음과 갗이 고정 매개변수를 먼저 지정하고, 그 다음매개변수에 *를 붙여주면 됩니다.

def print_numbers(a, *args):
    print(a)
    print(args)
    print()
print_numbers(1)
print_numbers(1,10,20)
print_numbers(*[10,20,30])

# 30.2 키워드 인수 사용하기

def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ',address)
    print()

# 함수(키워드=값)
personal_info(age=30, address='서울시 용산구 이촌동',name='홍길동')
'''
이름:  홍길동
나이:  30
주소:  서울시 용산구 이촌동 # 인수의 순서 맞추지 않아도 키워드에 해당하는 값이 들어감
'''

#30.3 키워드 인수와 딕셔너리 언패킹 사용하기
# 함수(**딕셔너리)
def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ',address)
    print()

## 딕셔너리에 '키워드':값 형식으로 인수를 저장하고 앞에 **를 붙여서 함수에 넣어 줍니다.
x={'name':'홍길동','age':30, 'address':'서울시 용산구 이촌동'}
personal_info(**x)
'''
이름:  홍길동
나이:  30
주소:  서울시 용산구 이촌동
'''

#30.3.1 **를 두 번 사용하는 이유
## 딕셔너리는 키-값 쌍 형태로 값이 저장되어 있기 때문
x={'name':'홍길동','age':30, 'address':'서울시 용산구 이촌동'}
personal_info(*x)
'''
이름:  name
나이:  age
주소:  address  # *x를 넣으면 x의 키가 출력
'''

# 30.3.2 키워드 인수를 사용하는 가변 인수 함수 만들기
# def 함수이름(**매개변수):
#   코드

def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ':', arg, sep='')
        print()

personal_info(name='홍길동')
personal_info(name='홍길동',age=30, address='서울시 용산구 이촌동')

# **를 사용한 가변 인수 함수는 다음과 같이 함수 안에서 특정 키가 있는지 확인한 뒤 해당 기능을 만듭니다.
def personal_info(**kwargs):
    if 'name' in kwargs:
        print('이름: ',kwargs['name'])
    if 'age' in kwargs:
        print('나이: ',kwargs['age'])
    if 'address' in kwargs:
        print('주소: ',kwargs['address'])

# 위치 인수와 키워드 인수를 함께 사용하기
def custom_print(*args,**kwargs):
    print(*args,**kwargs)

custom_print(1,2,3, sep=':', end='')
print()
# 30.4 매개변수에 초기값 지정하기
# def 함수이름(매개변수=값):
#   코드

def personal_info(name,age,address='비공개'):
    print('이름: ',name)
    print('나이: ',age)
    print('주소: ',address)
    print()

personal_info('홍길동',30)
'''
이름:  홍길동
나이:  30
주소:  비공개  # 초기값 출력
'''

personal_info('홍길동',30,'서울시 용산구 이촌동')
'''
이름:  홍길동
나이:  30
주소:  서울시 용산구 이촌동 # 초기값이 지정되어 있더라도 값을 넣으면 해당 값이 전달 됨
'''

#30.4.1 초기값이 지정된 매개변수의 위치
#초기값이 지정된 매개변수 다음에는 초기값이 없는 매개변수가 올 수 없음
## 초기값이 지정된 매개변수는 뒤쪽에 몰아주기

# 30.6 연습문제:가장 높은 점수를 구하는 함수 만들기
korean, english, mathematics, science=100,86,81,91

def get_max_score(*args):
    return max(args)

max_score=get_max_score(korean,english, mathematics,science)
print('높은 점수 :', max_score)

max_score=get_max_score(english, science)
print('높은 점수 :', max_score)

'''
높은 점수 : 100
높은 점수 : 91
'''

#30.7 심사문제:가장 낮은 점수, 높은 점수와 평균 점수를 구하는 함수 만들기

korean,english,mathematics,science=map(int, input().split())
def get_min_max_score (*args):
    return min(args), max(args)

def get_average(**kwargs):
    return sum(kwargs.values())/len(kwargs)

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
 
min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
 