import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def select_features_with_rf(PATH_DATA):
    # 데이터 로드
    data = pd.read_csv(PATH_DATA, sep=',')

    # 독립변수와 종속변수 정의
    X = data.iloc[:, 3:-1].values
    y = data.iloc[:, -1:].values.ravel()
    np.nan_to_num(X, copy=False)
    np.nan_to_num(y, copy=False)

    # 랜덤포레스트를 이용한 모델 생성
    rf = RandomForestClassifier(n_jobs=-1, class_weight='balanced', max_depth=5, random_state=1)
    rf.fit(X, y)

    # 특징 중요도 계산
    feature_importances = rf.feature_importances_
    feat = data.columns[3:-1]
    dic = dict(zip(feat, feature_importances))

    # 중요도를 기준으로 정렬
    sorted_by_importance = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    # DataFrame으로 변환
    tmp_df = pd.DataFrame(sorted_by_importance, columns=['변수', '중요도'])

    # 중요도 상위 10개 특징 선택
    result_list = tmp_df['변수'].tolist()[:10]

    columns = ["ROAD_ID", "x", 'y', 'EPDO']
    columns.extend(result_list)
    
    return data[columns]

if __name__ == "__main__":
    # QGIS로 추출한 원천 데이터 경로
    PATH_DATA = "preAcc.csv"

    # 랜덤포레스트 특징 선택 실행
    postRF = select_features_with_rf(PATH_DATA)

    # 결과 저장
    postRF.to_csv("./postAcc_RF.csv", encoding="cp949", index=False)
