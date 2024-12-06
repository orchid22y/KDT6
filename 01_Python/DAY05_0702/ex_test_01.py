#-----------------------------------------------------------------------------------------------
# [실습1] 글자를 입력 받습니다.
#        입력 받은 글자의 (a~z, A~Z) 코드값을 출력합니다.
# #-----------------------------------------------------------------------------------------------

msg=input("글자를 입력하세요. (a~z, A~Z):")

# 문자 ==> 코드값 변환 내장함수 : ord(문자 1개)

if len(msg)==1 and ('a'<= msg <='z' or 'A'<= msg <='Z'):
        print(f'{msg}의 코드값 : {ord(msg)}')
else:
    print("1개의 알파벳 문자만 입력해야 합니다. \n입력된 데이터를 확인하세요.")


# ord(data[0]) # ord(data[1])
print(list(map(ord,msg)))


#-----------------------------------------------------------------------------------------------
# [실습2] 점수를 입력 받은 후 학점을 출력합니다.
#   - 학점 : A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F
#           A+ : 96~100
#           A  : 95
#           A- : 90~94
# #-----------------------------------------------------------------------------------------------

jumsu=int(input("점수를 입력하세요. :"))
grade=''
if jumsu<0 or jumsu>100:
    print("{jumsu}sms 잘못 입력된 점수 입니다.")
else:
    if 95<jumsu<=100: grade='A+'
    elif jumsu==95: grade="A"
    elif jumsu>=90: grade="A-"
    elif jumsu>85: grade='B+'
    elif jumsu==85: grade="B"
    elif jumsu>=80: grade="B-"
    elif jumsu>75: grade='C+'
    elif jumsu==75: grade="C"
    elif jumsu>=70: grade="C-"
    elif jumsu>65: grade='D+'
    elif jumsu==65: grade="D"
    elif jumsu>=60: grade="D-"
    else:grade='F'



