#--------------------------------------------------------------------------------------------------
# Iterator 객체 ---> 즉, 반복자를 가지고 있는 객체 : iterable 객체
# - 커스텀 클래스 생성 확인
# - 이미 Iterator객체를 가지고 있는 객체들 살펴보기
#--------------------------------------------------------------------------------------------------
## 내장함수 dir(): 객체가 가지는 변수와 메서드를 리스트로 알려줌
nums=[11,33,55]

# _ 변수 : 저장되는 데이터에 따라서 변수명 지정하는데 이 변수명은 특별한 의미는 없고 문법상 필요한 경우 사용
for _ in dir(nums):
    print(_)

'''
__add__
__class__
__class_getitem__
__contains__
__delattr__
__delitem__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getitem__
__gt__
__hash__
__iadd__
__imul__
__init__
__init_subclass__
__iter__
__le__
__len__
__lt__
__mul__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__reversed__
__rmul__
__setattr__
__setitem__
__sizeof__
__str__
__subclasshook__
append
clear
copy
count
extend
index
insert
pop
remove
reverse
sor
'''
print()
# 리스트에서 반복자(Iterator)추출 : __iter__() 메서드
#nums=[11,33,55]
iterator=nums.__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
'''
11
33
55
'''
print()
## 내장함수 iter(반복이 가능한 객체) : 객체에 존재하는 반복자를 추출
iterator=iter(nums)
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
'''
11
33
55
'''
print()
for _ in dir(10):
    print(_)