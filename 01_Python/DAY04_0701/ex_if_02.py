#--------------------------------------------------------------------------------------------------
# [실습] 숫자를 입력 바당서 음이 아닌 정수와 음수 구분하기
##  - 출력 : 숫자 -5는 음수입니다.
#--------------------------------------------------------------------------------------------------

num=int(input("숫자를입력하에요:"))

if num>=0:
    print(f'숫자 {num}은 음이 아닌 정수 입니다.')
else:
    print(f'숫자 {num}은 음수 입니다.')


#--------------------------------------------------------------------------------------------------
# [실습] 점수를 입력 받아서 합격과 불합격 출력
#   -합격 : 60점 이상
#--------------------------------------------------------------------------------------------------

jumsu=int("점수를 입력하세요.: ")

if jumsu>=60:
    print("합격입니다.")
else:
    print("불합격입니다.")


#--------------------------------------------------------------------------------------------------
# [실습] 점수를 입력 받아서 학점 출력
#   - 학점 : A, B, C, D, F
#--------------------------------------------------------------------------------------------------

jumsu=int("점수를 입력하세요.: ")

if jumsu>=90:
    print('A 학점입니다.')
elif jumsu>=80:
    print('B 학점입니다.')
elif jumsu>=70:
    print('C 학점입니다.')
elif jumsu>=60:
    print('D 학점입니다.')
else :
    print('F 학점입니다.')