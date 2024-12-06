#----------------------------------------------------------------------------------------------------
# 제어문 - 반복문
#   - 유사하거나 동일한 코드를 1번 작성으로 재사용하기 위한 방법
#   - 종류 : for, while
#----------------------------------------------------------------------------------------------------
## for 반복문
##  - 시퀀스(이터러블) 데이터에서 원소/요소를 하나씩 읽어올때 사용
##  - 형식
##      for 변수명 in 시퀀스/이터러블데이터:
##      ----반복실행 될 코드
#----------------------------------------------------------------------------------------------------
# [실습] 문자열에서 문자를 1줄에 1개 씩 출력하기

msg="Merry Christmas 2025"
print(msg[0])
print(msg[1])
print(msg[2])
print(msg[3])
print(msg[4])
print(msg[5])
print(msg[6])
print(msg[7])
print(msg[8])
print(msg[9])
print(msg[10])
print(msg[11])
print(msg[12])
print(msg[13])
print(msg[14])
print(msg[15])
print(msg[16])
print(msg[17])
print(msg[18])
print(msg[19])
print("*"*30)


for m in range(0,len(msg)):
    print(msg[m],ord(msg[m]),end=" ")

print("\nEnd\n")

# [실습] list에서 원소를 하나씩 읽어오기
# 1~100 범위에서 3의 배수만 저장한 리스트

data=list(range(3,101,3))
print(data,'\n')

for d in data:
    print(d,end=" ")

print("\nEnd\n")

# [실습] str 타입의 원소를 가지는 리스트 입니다.
# 해당 원소를 정수로 형변환 시켜서 저장해 주세요.
# 원래 원소의 값을 변경해야 하는 경우는 인덱스 필요
data=['4','9','1','3','8']
print('전 : ',data)
for d in data:
    d=int(d)
print('후 : ',data)
print()

#리스트의 인덱스
data=['4','9','1','3','8']
print('전 : ',data)
for idx in range(len(data)):
    print(f'idx=>{idx}')
    data[idx]=int(data[idx])
print('후 : ',data)
print()

data=['4','9','1','3','8']
print('전 : ',data)
for d in range(0,len(data)):
    data[d]=int(data[d])

print('후 : ',data)

data=['4','9','1','3','8']
data2=[]
n=0
print('전 : ',data2)

for d in data:
    d=int(d)
    data2=data2.append(d)
    n=n+1

print('후 : ',data2)