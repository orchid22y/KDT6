#-----------------------------------------------------------------------------------
# [실습] 10번 숫자 데이터를 입력 받습니다.
#   - 숫자 데이터를 모두 더해서 합계가 30 이상이 되면
#    10번 입력 안 받았더라도 종료해 주세요.
#-----------------------------------------------------------------------------------

total=0
for i in range(0,10):
    nums=int(input("숫자를 입력하세요: "))
    total=total+nums
    if total>=30: break
print(f"합계 : {total}")