#------------------------------------------------------------------------------------------
# 내장함수 range()
#   - 숫자 범위를 생성하는 내장 함수
#   - 형식 : range(시작숫자, 끝숫자+1, 간격)
#            range(끝숫자+1) : 처음부터, 간격 1
#------------------------------------------------------------------------------------------
# [실습1] 1 ~ 100 숫자를 저장하세요
# nums=[1,2,3,4,5,6,....,100]
nums=range(1,101)

print(f'nums 값 : {nums}\n타입 : {type(nums)}\n개수 : {len(nums)}')
'''
nums 값 : range(1, 101)     ## 개별숫자 X , 범위
타입 : <class 'range'>
개수 : 100
'''
print()
# 원소/요소 읽기 ==>인덱싱

print(nums[0],nums[-1])
'''
1 100
'''
print()


#원소 여러개 읽기 ==> 슬라이싱

print(nums[0:10],nums[30:41])
'''
range(1, 11) range(31, 42)
'''
print()

#원소/요소 하나하나를 보기  ==> list, tuple 형변환

print(list(nums[0:10]),'\n',tuple(nums[30:41]),sep="")
'''
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
(31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41)
'''
print()

# [실습2] 1~100에서 3의 배수만 저장하세요
# => 3,6,9,12,...,99
#three=[3,6,9,12,15,18,21,...,96,99]
three=range(3,101,3)
print(list(three))
'''
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
'''
print()

# [실습3] 1.0~10.0 사이의 숫자 저장
'''
range(1.0,10.1)
>> TypeError: 'float' object cannot be interpreted as an integer
'''

datas=list(range(1,11))
'''
print(float(datas))
>>TypeError: float() argument must be a string or a number, not 'list'
'''

print(datas)
'''
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
print()
# float(datas[0])   ==> map() 내장함수 사용
# float(datas[1])
# float(datas[2])
# float(datas[3])
# float(datas[4])
# float(datas[5])
# float(datas[6])
# float(datas[7])
# float(datas[8])
# float(datas[9])

# map ==> list 형변환
datas=list(map(float,datas))
print(datas)
'''
[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
'''
