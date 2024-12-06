# -------------------------------------------------------------------
# Flask Framework 에서 WebServer 구동 파일
# - 파일명 : app.py
# -------------------------------------------------------------------
# 모듈로딩-----------------------------------------------------------
## 터미널 명령어 mkdir (makedirectory)
# mkdir static
# mkdir templates / views
# 

from flask import Flask

# 전역변수 ----------------------------------------------------------
# Flask Web Server 인스턴스 생성

APP = Flask(__name__)

# 라우팅 기능 함수 --------------------------------------------------
# @Flask Web Server 인스턴스변수명.route("URL")
# http://127.0.0.1:5000/
@APP.route("/")
def index():
    return """<body style='background-color:yellow'>
                 <h1> HELLO </h1>



                 .
                 </body>"""

# http://127.0.0.1:5000/info
@APP.route("/info")
@APP.route("/info/")

def info():
    return """<body style='background-color:skyblue; text-align:center'>
                 <h1> INFORMATION </h1>
                 </body>"""     

# http://127.0.0.1:5000/info/문자열변수
# name에 문자열 변수 저장, 즉, name=문자열변수
# http://127.0.0.1:5000/info/홍길동

@APP.route("/info/<name>")
@APP.route("/info/<name>/")

def printInfo(name):
    return f"""<body style='background-color:pink; text-align:center'>
                 <h1> {name}'s INFORMATION </h1>
                 HELLO~
                 </body>"""     

# 조건부 실행
if __name__ =='__main__': #즉 import 된 상태가 아니라면
    # Flask Web Server 구동
    APP.run()


