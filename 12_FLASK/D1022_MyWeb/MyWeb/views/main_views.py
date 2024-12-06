# ------------------------------------------------------------------------
# Flask Framework 에서 '/'URL 에 대한 라우팅 처리 파일
# # - 파일명 : main_views.py
# ------------------------------------------------------------------------
# 모듈로딩
from flask import Blueprint, render_template

# Blueprint 인스턴스 생성 -------------------------------------------------
main_bp = Blueprint('main', 
                        __name__, 
                        url_prefix='/',
                        template_folder='templates')

# 라우팅 기능 함수 정의 ----------------------------------------------------
@main_bp.route('/', endpoint='hello') # endpoint 지정해주면 그거대로, 안해주면 함수명이 endpoint가 됨
def index():
    return render_template('index.html')