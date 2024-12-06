#-------------------------------------------------------------------------------------------------------------
# - 파일명 : main_view.py
#-------------------------------------------------------------------------------------------------------------
# 모듈로딩
from flask import Blueprint, render_template

# Blueprint 인스턴스 생성
mainBP = Blueprint('MAIN',
                   import_name=__name__,
                   url_prefix='/',
                   template_folder='templates')

# http://localhost:8080/ URL 처리 라우팅 함수 정의
@mainBP.route('/')
def index():
    return render_template('index.html')
    