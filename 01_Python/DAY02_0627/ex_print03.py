#------------------------------------------------------------------------------------------------------
# 내장함수 print() 사용법
#   - print함수의 매개변수 알아보기
#       -file 매개변수 : 데이터를 파일에 기록
#------------------------------------------------------------------------------------------------------
# 파일 읽기 & 쓰기
#   - 파일열기 open()
#   - 파일 읽기 또는 쓰기
#   - 파일 닫기 close()
FILENAME='result.txt'

#파일을 쓰기모드(w) 열기
f = open(FILENAME, mode='w')
f.write("Hello\n")

#파일에 데이터 출력하기
print("Good Luck", file=f)

#파일 닫기
f.close()
