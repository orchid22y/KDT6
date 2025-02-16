# 분석에 사용되는 라이브러리 호출
import os
import time
import pickle
import datetime
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

pd.set_option('display.max_columns', None)
import warnings
warnings.filterwarnings('ignore') 

def save_model(TARGET, MODEL, gdf, coords, model):
    # 디렉토리 생성 
    os.makedirs(f'./results/{TARGET}/', exist_ok=True)

    # 엑셀 저장
    gdf.to_excel(f'./results/{TARGET}/{TARGET}_{MODEL}.xlsx', index=False)

    # 좌표와 예측값을 포함한 GeoDataFrame 생성
    geometry = [Point(xy) for xy in coords]
    gdf = gpd.GeoDataFrame(gdf, geometry=geometry)

    # Shapefile 저장
    gdf.to_file(f'./results/{TARGET}/{TARGET}_{MODEL}.shp')

    name_dict = {"교통사고": "Accident", "범죄": "Crime"}

    # 모델 저장
    filename = f'./results/{TARGET}/{name_dict[TARGET]}_{MODEL}.pkl'
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

    print(f"모델이 {filename} 파일에 저장되었습니다.")

def run_model(TARGET, MODEL, PATH_DATA):
    # 데이터 로드
    gdf = gpd.read_file(PATH_DATA)
    
    # 종속변수 전처리
    y = gdf['EPDO'].values.reshape((-1, 1))
    print(f"분석 모델의 종속변수는 'EPDO' 변수입니다.")

    # 독립변수 전처리
    feature_columns = gdf.drop(["ROAD_ID", "x", "y", "EPDO", "geometry"], axis=1).columns
    X = gdf[feature_columns]

    print(f'학습에 활용되는 특징들은 {feature_columns.to_list()}입니다.')
    print()
    
    # 좌표 추출
    u = gdf['x']
    v = gdf['y']
    coords = list(zip(u, v))




    # 데이터 변환
    # 1. 비숫자 데이터를 숫자로 변환 (숫자로 변환 불가능한 경우 NaN)
    X = X.apply(pd.to_numeric, errors='coerce').values
    y = pd.to_numeric(y.flatten(), errors='coerce').astype(float).reshape(y.shape)

    # 2. 결측치(NaN) 및 0 처리
    X = np.nan_to_num(X, nan=0.0)  # NaN을 0으로 변환
    y = np.nan_to_num(y, nan=0.0)  # 동일 처리

    # 랜덤 포레스트 모델 정의 및 학습
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y.flatten())

    # 예측 및 평가
    predictions = model.predict(X)
    n = len(y)
    k = X.shape[1]
    residual_sum_of_squares = np.sum((y.flatten() - predictions) ** 2)
    log_likelihood = -0.5 * n * (np.log(2 * np.pi) + 1 + np.log(residual_sum_of_squares / n))

    aic = 2 * k - 2 * log_likelihood
    aicc = aic + (2 * k * (k + 1)) / (n - k - 1)

    r2 = r2_score(y.flatten(), predictions)
    mse = mean_squared_error(y.flatten(), predictions)

    gdf['Predictions'] = predictions

    print(f'분석 모델의 R2는 {r2:.4f}입니다.')
    print(f'분석 모델의 MSE는 {mse:.4f}입니다.')

    # 분석 모델의 성능 확인
    print(f'분석 모델의 Mean R2는 {r2:.4f}입니다.')
    print(f'분석 모델의 AIC는 {aic:.4f}입니다.')
    print(f'분석 모델의 AICc는 {aicc:.4f}입니다.')
    print()

    # 모델 저장
    save_model(TARGET, MODEL, gdf, coords, model)

if __name__ == "__main__":
    # 분석을 수행할 데이터
    TARGET = "교통사고"

    # 분석을 진행할 모델 (Random Forest)
    MODEL = "RandomForest"

    # 분석할 데이터가 저장된 경로
    PATH_DATA = f'data/{TARGET}_분석_데이터.shp'
    
    # 코드 동작 시간 확인
    start_time = time.time()

    # 모델 구동
    run_model(TARGET, MODEL, PATH_DATA)
    
    print(f"코드가 동작하는데 걸린 시간은 {str(datetime.timedelta(seconds=int(time.time() - start_time)))}입니다.")
