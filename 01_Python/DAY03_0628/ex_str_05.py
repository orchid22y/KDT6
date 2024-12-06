#----------------------------------------------------------------------------------------
# 문자열 str 데이터 다루기
#   - 이스케이프문자 : 특수한 의미를 가지는 문자
#   * 형식 : \문자 1개
#   * '\n' - 줄바꿈 문자
#   * '\t' - 탭간격 문자
#   * '\'' - 홑따옴표 문자
#   * '\"' - 쌍따옴표 문자
#   * '\\' - \백슬러시 문자, 경로(path), URL관련
#   * '\U' - 유니코드
#   * '\a' - 알람소리 문자
#----------------------------------------------------------------------------------------

msg="오늘은 좋은날\n내일은 주말이라 행복해"
print(f'msg 줄바꿈 : {msg}')
'''
msg 줄바꿈 : 오늘은 좋은날
내일은 주말이라 행복해
'''
print()


msg='오늘은 나의 \'생일\'이야'
print(msg)
'''
오늘은 나의 '생일'이야
'''

print()

# file='C:\Users\KDP-27\test.txt'
# print(file)

r'''
  File "c:\Users\KDP-27\Desktop\EX_PY06\DAY03_0628\ex_str_05.py", line 31
    file='C:\Users\KDP-27\test.txt'
                                   ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
'''

file='C:\\Users\\KDP-27\\test.txt'
print(file)
r'''
C:\Users\KDP-27\test.txt
'''
print()


#r'   ' 또는 R'   ' : 문자열 내 이스케이프 문자는 무시됨!
file=r'C:\Users\KDP-27\test.txt'
print(file)
r'''
C:\Users\KDP-27\test.txt
'''
print()


msg="Happy\tNew\tYear"
msg2=R"Happy\tnew\tyear"
print(msg,msg2)
r'''
C:\Users\KDP-27\test.txt
'''