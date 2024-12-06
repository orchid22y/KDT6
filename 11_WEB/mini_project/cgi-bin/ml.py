# 모듈 로딩--------------------------------------------
import os.path     # 파일 및 폴더 관련
import cgi, cgitb  # cgi 프로그래밍 관련
import joblib      # AI 모델 관련
import sys, codecs # 인코딩 관련
import torch

# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()         # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능


# 사용자 정의 함수-----------------------------------------------------------
# WEB에서 사용자에게 보여주고 입력받는 함수 ---------------------------------
def showHTML(data, msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    <!DOCTYPE html>
    <html lang="en">
     <head>
      <meta charset="UTF-8">
      <title>---건강 점수 측정---</title>
      <style>
          body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh; /* 화면 전체 높이 */
                margin: 0;
                font-family: Arial, sans-serif; /* 기본 글꼴 */
                text-align: center; /* 가운데 정렬 */
            }}
          </style>
     </head>
     <body>
      <form>
        주당 공부 시간: <input type='text' name='q0' placeholder='20' value='{data[0]}'><br/>
        출석률: <input type='text' name='q1' placeholder='80' value='{data[1]}'><br/>
        이전 학기 성적: <input type='text' name='q2' placeholder='75' value='{data[2]}'><br/>
        부모 학력: <input type='text' name='q3' placeholder='8 부모 학력 (단위: 년)' value='{data[3]}'><br/>
        사교육 여부: <input type='text' name='q4' placeholder='사교육 여부(예=1,아니요=0)' value='{data[4]}'><br/>
        <p><input type="submit" value="결과보기"></p>
        <p>{msg}</p>
      </form>
     </body>
    </html>""")

    
# 사용자 입력 텍스트 판별하는 함수---------------------------------------------------------------------------

# ['Study Hours per Week', 'Attendance Rate', 'Previous Grades', 'Parent Education Level',
                        #   'Participation in Extracurricular Activities']

def detectLang(data_input):
    result=""
    if data_input == [""]*5:  # 여기를 5로 변경 (입력 필드 수에 맞추기)
        result="입력 대기" 
    elif len(data_input) != 5:  # 5개의 필드가 모두 입력되었는지 확인
        result ="다시 입력하세요."
        return result
    
    model=joblib.load(r'C:\Users\KDP-27\Desktop\KDT6\pj\WEB\model\decision_tree_model.pkl')

    data_input = list(map(float, data_input))  # 문자열을 float로 변환
    sample = [data_input]

    # test data 예측-----------------------------------------
    result_num = model.predict(sample)

    # 예측 결과에 따른 출력
    result=['Not Passed', 'Pass']
    return result[int(result_num)]

# 기능 구현 ------------------------------------------------
# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# (2) 모델 로딩
pklfile = r"C:\Users\KDP-27\Desktop\KDT6\pj\WEB\model\decision_tree_model.pkl"  # 모델 경로를 변경

if os.path.exists(pklfile):
    model = joblib.load(pklfile)
else:
    print(f'{pklfile} 파일이 존재하지 않습니다. 다시 확인하세요.')

# (3) WEB 사용자 입력 데이터 처리
form = cgi.FieldStorage()

# 사용자 입력 필드를 리스트로 가져오기
data = [
    form.getvalue("q0", default=""),  # 주당 공부 시간
    form.getvalue("q1", default=""),  # 출석률
    form.getvalue("q2", default=""),  # 이전 학기 성적
    form.getvalue("q3", default=""),   # 부모 학력 (단위: 년)
    form.getvalue("q4", default="")    # 사교육 여부 (예=1, 아니요=0)
]

# 판별하기
result_input = ""
# 기본값이 아닌 실제 입력이 있을 때만 판별
if any(value != default for value, default in zip(data, ["", "", "", "", ""])):
    result_input = detectLang(data)

# data 초기화
# (4) 사용자에게 WEB 화면 제공
showHTML(data, result_input)  # 입력한 데이터와 결과를 보여줌