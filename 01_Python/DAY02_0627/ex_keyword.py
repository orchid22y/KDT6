#-------------------------------------------------------------------------------------------
# 변수이름과 키워드
#   -키워드 : 프로그래밍 언어에서 미리 사용한다고 즉, 문법에 사용한다고 예약해 놓은 단어들
#-------------------------------------------------------------------------------------------
# 키워드가 들어있는 모듈/파일 로딩하기(가져오기)
# 방법 : import 

import keyword

# 키워드 파일안에 있는 함수, 변수, 클래스 사용하기
# 문법 : 모듈/파일명.함수명, 모듈/파일명.변수, 모듈/파일명.클래스명
# 파이썬 언어의 키워드 리스트

print(keyword.kwlist)

'''
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
