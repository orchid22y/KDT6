# 모듈 로딩
# -Model 관련
import torch
import torch.nn as nn
import torch.nn.functional as F # 변수명과 헷갈릴까봐 소문자는 사용 X

from torch.utils.data import Dataset, DataLoader
import torch.optim as optim

from torchmetrics.classification import F1Score, BinaryF1Score
from torchmetrics.classification import BinaryConfusionMatrix

from torchinfo import summary


# - Data 및 시각화 관련

import pandas as pd
import matplotlib.pyplot as plt



from sklearn.preprocessing import *
from sklearn.model_selection import train_test_split 



class SmokingBCFModel(nn.Module):

    '''
    [2] 모델 클래스 설계 및 정의 <hr>

- 클래스 목적 : Smoking 데이터를 학습 및 추론 목적
- 클래스 이름 : SmokingModel
- 부모 클래스 : nn.Module
- 매 개 변 수 : 층별 입/출력 개수 고정이므로 필요 없음!
- 속 성 필 드 : 
- 기능 / 역할 
    * _ _ _init_ _ _() : 모델 구조 설정
    * forward() : 순방향 학습 <= 오버라이딩(overriding, 상속관계에서만 가능)
- 클래스 구조 
    * 입력층 : 입력  21개(피쳐 수)  출력 10개(퍼셉트론/뉴런 10개 존재)
    * 은닉층 : 입력 10개           출력  5개(퍼셉트론/뉴런 5개 존재)   
    * 출력층 : 입력  5개           출력  1개(퍼셉트론/뉴런 1개 존재 : 2진분류)

- 활성화함수
    * 클래스 형태 ==> nn.MESLoss, nn.ReLU ==> _ _ _init_ _ _() 메서드에서 사용
    * 함수 형태 ==> torch.nn.functional 아래에 ==> forward() 메서드에서 사용
    '''


    # 모델 구조 구성 및 인스턴스 생성 메서드
    def __init__(self):
        super().__init__()

        self.in_layer=nn.Linear(21,10)
        self.hd_layer1=nn.Linear(10,30)
        self.hd_layer2=nn.Linear(30,60)
        self.hd_layer3=nn.Linear(60,30)
        self.hd_layer4=nn.Linear(30,10)
        self.hd_layer5=nn.Linear(10,5)
        self.out_layer=nn.Linear(5,1)


    # 순방향 학습 진행 메서드
    def forward(self, input_data):
        # - 입력층
        y = self.in_layer(input_data)  # f11w11+f12w12+f13w13+b, ... , f101w101+f102w102+f103w103+b
        y = F.relu(y)                  # relu => y값의 범위 : 0 <= y (sigmoid면 y값은 0에서 1사이가 됨)

        # - 은닉층 : 10개의 숫자 값 (>=0)
        y = self.hd_layer1(y)            # f21w21+f22w22+...+f210w210+b, ... , f230w101...+f230w210+b
        y = F.relu(y)                   # relu => y값의 범위 : 0 <= y

        # 두번째 은닉층
        y = self.hd_layer2(y)            # f21w21+f22w22+...+f210w210+b, ... , f230w101...+f230w210+b
        y = F.relu(y)   

        # 세번째 은닉층
        y = self.hd_layer3(y)            # f21w21+f22w22+...+f210w210+b, ... , f230w101...+f230w210+b
        y = F.relu(y)  

        # 네번째 은닉층
        y = self.hd_layer4(y)            # f21w21+f22w22+...+f210w210+b, ... , f230w101...+f230w210+b
        y = F.relu(y)  

        # 다섯번째 은닉층

        y = self.hd_layer5(y)            # f21w21+f22w22+...+f210w210+b, ... , f230w101...+f230w210+b
        y = F.relu(y)  

        # - 출력층 : 5개의 숫자 값 (>=0) => 회귀이므로 바로 반환(return)
        return F.sigmoid(self.out_layer(y))  
    

class SmokingDataset(Dataset):

    '''
    [3] 데이터셋 클래스 설계 및 정의 <hr>
- 데이터_셋 : iris.csv
- 피쳐_개수 : 21개
- 타겟_개수 : 1개
- 클래스이름 : SmokingDataset
- 부모클래스 : utils.data.Dataset
- 속성__필드 : featureDF, targetDF, n_rows, n_features
- 필수메서드 : 
    - _ _init_ _(self) : 데이터셋 저장 및 전처리, 개발자가 필요한 속성 설정
    - _ _len_ _(self) : 데이터의 개수 반환
    - _ _getitem_ _(self, index) : 특정 인덱스의 피쳐와 타겟 반환
    '''

    def __init__(self, featureDF, targetDF):
        super().__init__()

        self.featureDF=featureDF
        self.targetDF=targetDF
        self.n_rows=featureDF.shape[0]
        self.n_features=featureDF.shape[1]

    def __len__(self):
        return self.n_rows

    def __getitem__(self, index):
        # 텐서화
        featureTS = torch.FloatTensor(self.featureDF.iloc[index].values) # 시리즈를 array로 만들기위해 values함 
        targetTS = torch.FloatTensor(self.targetDF.iloc[index].values)

        # 피쳐와 타겟 반환
        return featureTS, targetTS
    


class DynamicModel(nn.Module):
    '''
    # -----------------------------------------------------------------------
# 모델 이름 : DynamicModel
# 부모클래스: nn.Module
# 매개 변수 : in_in, out_out, h_ins=[], n_outs=[] 
# -----------------------------------------------------------------------  
# 입력층과 출력층 개수 동적 => 입력층의 입력값, 출력층의 출력값
은닉층의 개수 동적 + 퍼셉트론 개수 동적 => 은닉층의 개수, 은닉층 마다 퍼셉트론 수 
    
    '''
    # 모델 구조 설계 함수 즉, 생성자 메서드
    def __init__(self, in_in, in_out, out_out, h_ins=[], h_outs=[]):
        super().__init__()
        
        self.in_layer=nn.Linear(in_in, h_ins[0] if len(h_ins) else in_out )
        
        self.h_layers=nn.ModuleList()
        for idx  in range(len(h_ins)):
            self.h_layers.append( nn.Linear(h_ins[idx], h_outs[idx])  )
        
        self.out_layer=nn.Linear(h_outs[-1]  if len(h_outs) else in_out, out_out)
        
        
    # 학습 진행 콜백 메서드
    def forward(self, x): 
        # 입력층
        y=self.in_layer(x)                  # y=x1w1+x2w2+x3w3+b
        y=F.relu(y)                         # 0 <= y
        #y=F.relu(self.in_layer(x) )

        # 은닉층
        for linear in self.h_layers:
            y=linear(y)
            y=F.relu(y) 
            #y=F.relu( linear(y) )
            
        # 출력층
        return F.sigmoid(self.out_layer(y)) 