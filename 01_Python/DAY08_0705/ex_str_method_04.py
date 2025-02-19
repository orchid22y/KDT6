#----------------------------------------------------------------------------------------------
# str 데이터 타입 전용 함수 즉, 메서드 살펴보기
#----------------------------------------------------------------------------------------------
## 문자열에서 원소/요소 변경해주는 메서드 => replace()
##---------------------------------------------------------------------------------------------
msg='Pithon'

#인덱스로 요소 변경 ===> ERROR 미지원 기능 : 불변의 시퀀스 타입
# msg[1]='y'

# 전용 메서드로 변경
#변경 적용 위해서는 반드시 저장
m1=msg.replace('i','y')

print(f'msg : {msg} ---> m1 : {m1}')

'''
msg : Pithon ---> m1 : Python
'''

msg="Good Happy"
#   -o ===> O로 변경

print(msg.replace('o','O')) 
'''
>>>
GOOd Happy # 모든 o가 변경
'''

#   -o ==> O로 1개만 변경
print(msg.replace('o','O',1))
'''
GOod Happy
'''