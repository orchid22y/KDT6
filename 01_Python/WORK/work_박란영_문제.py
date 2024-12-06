#---------------------------------------------------------------------------------
# 초보자를 위한 파이썬 300제 
#---------------------------------------------------------------------------------
print('01 파이썬 시작하기','-'*30)

#001
print("Hello World")

#002
print("Mary's cosmetics")

#003
print('신씨가 소리질렀다. "도둑이야".')

#004
print('C:\Windows')

#005
# \n : 줄바꿈
# \t : 탭

#006
#오늘은 일요일

#007
print('naver','kakao','sk','samsung',sep=';')

#008
print('naver','kakao','sk','samsung',sep='/')

#009
print("first",end="");print("second")

#010
print(5/3)

print('\n02 파이썬 변수','-'*30)
#011
삼성=50000
총평가금액 = 삼성*10
print(총평가금액)

#012
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

#013
s = "hello"
t = "python"
print(f'{s}! {t}')


#014
print(2+2*3) #8

#015
a="132"
print(type(a)) 

#016
num_str='720'
num_int=int(num_str)
print(num_int,type(num_int))

#017
num=100
num_1=str(num)
print(num_1,type(num_1))

#018
data='15.79'
data = float(data)
print(data, type(data))

#019
year = "2020"
year2=int(year)

print(year2-3)
print(year2-2)
print(year2-1)

#020
월=48584
할부=36
print(월*할부)
print('\n03. 파이썬 문자열','-'*30)

#021
letters = 'python'
print(letters[0],letters[2])

#022
license_plate = "24가 2210"
print(license_plate[-4:])

#023
string = "홀짝홀짝홀짝"
print(string[::2])

#024
string = "PYTHON"
print(string[::-1])

#025
phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))

#026
print(phone_number.replace("-",""))

#027
url = "http://sharebook.kr"
print(url[url.index('.')+1:])

#028
#문자열 수정 X -> ERROR

#029
string = 'abcdfe2a354a32a'
print(string.replace('a','A'))

#030
string = 'abcd'
string.replace('b', 'B')#변수X->수정사항 저장X
print(string)
# 그대로 출력

#031
a = "3"
b = "4" 
print(a + b) ## 34

#032
print("Hi" * 3) ## HiHiHi

#033
print('-'*80)

#034
t1 = 'python'
t2 = 'java'
t3= t1+' '+t2+' '
print(t3*4)

#035
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: %s 나이: %d" %(name1, age1))
print("이름: %s 나이: %d" %(name2, age2))

#036
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

#037
print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')

#038
상장주식수 = "5,969,782,550"
상장주식수=int(상장주식수.replace(",",""))
print(상장주식수,type(상장주식수))

#039
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

#040
data = "   삼성전자    "
data=data.strip()
print(data)

#041
ticker = "btc_krw"
print(ticker.upper())

#042
ticker = "BTC_KRW"
print(ticker.lower())

#043
msg='hello'
print(msg.capitalize())

print('\n04. 파이썬 리스트','-'*30)

#051
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

#052
movie_rank.append("배트맨")
print(movie_rank)

#053
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)

#054
del movie_rank[3]
print(movie_rank)

#055
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

#056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang3=lang1+lang2
print(lang3)

#057
nums = [1, 2, 3, 4, 5, 6, 7]

print(f'max: {max(nums)}')
print(f'min: {min(nums)}')

#058
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

print(len(cook))

#060
nums = [1, 2, 3, 4, 5]
average=sum(nums)/len(nums)
print(average)

#061
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#063
print(nums[1::2])

#064
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])

#066
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

#070
data = [2, 4, 3, 1, 5, 10, 9]
data2 = sorted(data) 
print(data2)

print('\n05. 파이썬 튜플','-'*30)

#071
my_variable=()
print(type(my_variable))

#072
movie_rank=("닥터 스트레인지","	스플릿","럭키")
print(movie_rank)

#073
data=1,
print(data,type(data))

#074
#튜플은 원소값 변경 불가

#075
t = 1, 2, 3, 4
print(type(t)) #튜플

#076
t = ('a', 'b', 'c')
t = ('A', 'b', 'c') #튜플 값 변경 X -> 변수 업데이트

#077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest=list(interest)
print(interest,type(interest))

#078
interest=tuple(interest)
print(interest,type(interest))

#079
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c) #apple banana cake

#080
num=tuple(range(2,100,2))
print(num)

