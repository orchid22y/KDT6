#----------------------------------------------------------------------------------------------------------------------
# 내장함수 input() 사용법
#   - 키보드로 부터 입력한 데이터 받아오는 내장함수
#   - 문법 : input('요청문자열')
#   - 특징 : 입력 후 Enter키 입력이 되어야지만 데이터 전달 됨
#            즉, 입력이 완료될때까지 멈춤
#----------------------------------------------------------------------------------------------------------------------
# 이름 입력 받기

name = input("이름?")

# 000님 맛점!
print(f"{name}님 맛점!")
print("%s님 맛점!" %name)
print(name,"님 맛점!")
'''
이름?베트맨
베트맨님 맛점!
베트맨님 맛점!
베트맨 님 맛점!
'''