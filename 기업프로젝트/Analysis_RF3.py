# 분석에 사용되는 라이브러리 호출
import os
import time
import pickle
import datetime
import numpy as np
import geopandas as gpd
from shapely.geometry import Point

import pandas as pd
pd.set_option('display.max_columns', None)

import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 72

import seaborn as sns
sns.set_style("darkgrid")
sns.set_context(context="paper", font_scale=1.5, rc=None)
sns.set(font="serif")

import warnings
warnings.filterwarnings('ignore') 

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

from sklearn.neighbors import KernelDensity

def save_model(TARGET, MODEL, gdf, coords, rf_results):
    # 디렉토리 생성 
    os.makedirs(f'./results/{TARGET}/', exist_ok=True)

    # 엑셀
    gdf.to_excel(f'./results/{TARGET}/{TARGET}_{MODEL}3.xlsx', index=False)

    # 좌표와 예측값을 포함한 GeoDataFrame 생성
    geometry = [Point(xy) for xy in coords]
    gdf = gpd.GeoDataFrame(gdf, geometry=geometry)

    # Shapefile
    gdf.to_file(f'./results/{TARGET}/{TARGET}_{MODEL}3.shp')

    name_dict = {"교통사고": "Accident", "범죄": "Crime"}

    # 모델을 저장할 파일 이름
    filename = f'./results/{TARGET}/{name_dict[TARGET]}_{MODEL}3.pkl'
    # 학습된 모델을 pickle로 저장
    with open(filename, 'wb') as file:
        pickle.dump(rf_results, file)

    print(f"모델이 {filename} 파일에 저장되었습니다.")

def calculate_bandwidth(X):
    # 대역폭 계산 (커널 밀도 추정 사용)
    kde = KernelDensity(kernel='gaussian', bandwidth=1.0).fit(X)
    scores = kde.score_samples(X)
    print(f"대역폭 계산 결과 (일부): {scores[:10]}")
    return scores


# 모델 실행 함수
def run_model(TARGET, MODEL, PATH_DATA):
    print("데이터를 로드 중입니다...")
    # GQIS를 통해 전처리한 데이터를 로드
    gdf = gpd.read_file(PATH_DATA)
    
    print("종속변수와 독립변수 전처리를 시작합니다...")
    # 종속변수 전처리
    y = gdf['EPDO'].values.reshape((-1,1))
    print(f"분석 모델의 종속변수는 'EPDO' 변수입니다.")

    # 독립변수 전처리
    X = gdf.drop(["ROAD_ID", "x", "y", "EPDO", "geometry"], axis=1).values
    print(f'학습에 활용되는 특징들은 {gdf.drop(["ROAD_ID", "x", "y", "EPDO", "geometry"], axis=1).columns.to_list()}입니다.')
    print()
    
    # 좌표 데이터 추출
    u = gdf['x']
    v = gdf['y']
    coords = list(zip(u, v))
    
    print("데이터 스케일링을 진행합니다...")
    # 데이터의 스케일링 (특이 행렬 방지 및 결측값 처리)
    X = pd.to_numeric(X.flatten(), errors='coerce').astype(float).reshape(X.shape)
    X[X == 0] = np.random.uniform(0, 0.5, size=np.count_nonzero(X == 0))
    X[np.isnan(X)] = np.random.uniform(0, 0.5, size=np.count_nonzero(np.isnan(X)))
    X = np.round(X, 2)

    y = pd.to_numeric(y.flatten(), errors='coerce').astype(float).reshape(y.shape)
    y[y == 0] = np.random.uniform(0, 0.5, size=np.count_nonzero(y == 0))
    y[np.isnan(y)] = np.random.uniform(0, 0.5, size=np.count_nonzero(np.isnan(y)))
    y = np.round(y, 2)

    print("대역폭 계산을 시작합니다...")
    # 대역폭 계산 (Kernel Density 사용)
    gdf['Bandwidth'] = calculate_bandwidth(X)

    # 랜덤 포레스트 모델 실행
    if MODEL == "RandomForest":
        print("랜덤 포레스트 모델 학습을 시작합니다...")
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X, y.ravel())  # 모델 학습
        pred_results = model.predict(X)  # 예측값 생성
        gdf['RF_Predict'] = pred_results

        # R2 점수 계산
        r2 = r2_score(y, pred_results)

        # AIC와 AICc 계산
        residuals = y.ravel() - pred_results
        n = len(y)
        rss = np.sum(residuals**2)
        sigma2 = rss / n
        log_likelihood = -0.5 * n * (np.log(2 * np.pi * sigma2) + 1)

        k = model.n_estimators  # 트리 개수를 자유도로 사용
        aic = 2 * k - 2 * log_likelihood
        aicc = aic + (2 * k * (k + 1)) / (n - k - 1)

        # 모델 성능 출력
        print(f'랜덤 포레스트 모델의 R2 점수는 {r2}입니다.')
        print(f'랜덤 포레스트 모델의 AIC는 {aic}입니다.')
        print(f'랜덤 포레스트 모델의 AICc는 {aicc}입니다.')
        print()

        print("결과를 저장합니다...")
        # 결과 저장
        save_model(TARGET, MODEL, gdf, coords, model)
    else:
        # 지원되지 않는 모델 유형일 경우 예외 발생
        raise ValueError(f"지원되지 않는 모델 유형입니다: {MODEL}")



if __name__ == "__main__":
    # 분석을 수행할 데이터
    TARGET = "교통사고"

    # 분석을 진행할 모델 (RandomForest)
    MODEL = "RandomForest"

    # 분석할 데이터가 저장된 경로
    PATH_DATA = r"C:\Users\KDP-27\Desktop\KDT6\mini_project\제이솔루션\data2\최적지 선정 분석 코드(교통사고)\data\교통사고_분석_데이터.shp"
    
    # 코드 동작 시간 확인
    start_time = time.time()

    # 대역폭 찾고 모델 구동
    run_model(TARGET, MODEL, PATH_DATA)
    
    print(f"코드가 동작하는데 걸린 시간은 {str(datetime.timedelta(seconds=int(time.time() - start_time)))}입니다.")
