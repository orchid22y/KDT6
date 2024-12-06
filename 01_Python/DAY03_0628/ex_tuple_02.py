#---------------------------------------------------------------------------------------------
# Tuple 데이터 자료형 살펴보기
#   - 내장함수 : len(), max(), min(), sum()
#   - 연산자 : 덧셈, 곱셈, 멤버연산자
#---------------------------------------------------------------------------------------------

nums=11,22,33,44,55

## 내장함수 ----------------------------------------------------------------------------------
print(f'nums 개수 : {len(nums)}개')
print(f'최대값 : {max(nums)}, 최소값 : {min(nums)}')
print(f'합계 : {sum(nums)}')

print(f'정렬 : {sorted(nums)}, {sorted(nums,reverse=True)}')
'''
nums 개수 : 5개
최대값 : 55, 최소값 : 11
합계 : 165
정렬 : [11, 22, 33, 44, 55], [55, 44, 33, 22, 11]  ## 오름차순, 내림차순
'''

print(max('abc','abC'))
print(sorted(['abc','Zoo']))
'''
abc
['Zoo', 'abc']
'''

'''
print(sum(['abc','Zoo']))
>> TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''
print()
## 연산자 ---------------------------------------------------------------------------
## 덧셈

data1=11,22
data2='A','B','C'
data3=[1,2]

print(data1+data2)  # tuple+tuple
'''
(11, 22, 'A', 'B', 'C')
'''
'''
print(data1+data3)  # tuple+list
>> TypeError: can only concatenate tuple (not "list") to tuple  ## 같은 자료형만 가능, 형변환 해야함
'''
print()


## 곱셈 : tuple*int (tuple*tuple은 불가능)
print(data1*3)
'''
(11, 22, 11, 22, 11, 22)
'''
print()

## 멤버연산자 => in, not in
print(f'11 in data1 => {11 in data1}')
print(f"'A' in data1 => {'A' in data1}")
'''
11 in data1 => True
'A' in data1 => False
'''

