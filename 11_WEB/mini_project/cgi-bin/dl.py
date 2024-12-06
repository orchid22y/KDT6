#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cgi
import cgitb
import sys
import codecs
import torch
import torch.nn as nn
from sklearn.preprocessing import StandardScaler
import numpy as np

# 동작관련 전역 변수
cgitb.enable()  # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능

# WEB 인코딩 설정
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

class DiabetesModel(nn.Module):
    def __init__(self, input_dim):
        super(DiabetesModel, self).__init__()
        self.layer1 = nn.Linear(input_dim, 64)
        self.layer2 = nn.Linear(64, 32)
        self.layer3 = nn.Linear(32, 1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        x = self.sigmoid(self.layer3(x))
        return x

# 모델 로딩
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), './model/model_best_dict.pt')
checkpoint = torch.load(model_path, map_location=torch.device('cpu'))
input_dim = checkpoint['input_dim']
model = DiabetesModel(input_dim)
model.load_state_dict(checkpoint['model_state_dict'])
scaler = checkpoint['scaler']
model.eval()

def showHTML(inputs, result):
    print("Content-Type: text/html; charset=utf-8")
    print()
    print(f"""
    <!DOCTYPE html>
    <html lang="en">
     <head>
      <meta charset="UTF-8">
      <title>---흡연여부예측모델---</title>
      <style>
        body {{ 
            font-family: Arial, sans-serif; 
            background-size: cover; /* 이미지 크기 조정 */
            background-position: left; /* 이미지 위치 조정 */
        }}
        form {{ max-width: 500px; margin: 0 auto; }}
        input {{ margin-bottom: 10px; width: 100%; padding: 5px; }}
        input[type="submit"] {{ width: auto; }}
      </style>
     </head>
     <body>
      <form>
        <h2>건강 정보 입력</h2>
        <p>각 항목에 해당하는 값을 입력하세요:</p>
        당뇨병여부<input type="number" step="0.01" name="Diabetes_binary" placeholder="당뇨병 여부 (0 또는 1)" value="{inputs.get('Diabetes_binary', '')}">
        고혈압 여부<input type="number" name="HighBP" placeholder="고혈압 여부 (0 또는 1)" value="{inputs.get('HighBP', '')}">
        고콜레스테롤<input type="number" step="0.01" name="HighChol" placeholder="고콜레스테롤 (0 또는 1)" value="{inputs.get('HighChol', '')}">
        콜레스테롤 검사 여부<input type="number" name="CholCheck" placeholder="콜레스테롤 검사 여부 (0 또는 1)" value="{inputs.get('CholCheck', '')}">
        BMI<input type="number" step="0.1" name="BMI" placeholder="BMI" value="{inputs.get('BMI', '')}">
        뇌졸중 경험<input type="number" step="0.01" name="Stroke" placeholder="뇌졸중 경험 (0 또는 1)" value="{inputs.get('Stroke', '')}">
        심장병<input type="number" step="0.01" name="HeartDiseaseorAttack" placeholder="심장병 또는 심장마비 (0 또는 1)" value="{inputs.get('HeartDiseaseorAttack', '')}">
        신체 활동<input type="number" name="PhysActivity" placeholder="신체 활동 (0 또는 1)" value="{inputs.get('PhysActivity', '')}">
        과일 섭취<input type="number" name="Fruits" placeholder="과일 섭취 (0 또는 1)" value="{inputs.get('Fruits', '')}">
        채소 섭취<input type="number" name="Veggies" placeholder="채소 섭취 (0 또는 1)" value="{inputs.get('Veggies', '')}">
        과도한 알코올 섭취<input type="number" name="HvyAlcoholConsump" placeholder="과도한 알코올 섭취 (0 또는 1)" value="{inputs.get('HvyAlcoholConsump', '')}">
        의료 보험 여부<input type="number" name="AnyHealthcare" placeholder="의료 보험 여부 (0 또는 1)" value="{inputs.get('AnyHealthcare', '')}">
        비용으로 인한 의사 방문 불가<input type="number" step="0.01" name="NoDocbcCost" placeholder="비용으로 인한 의사 방문 불가 (0 또는 1)" value="{inputs.get('NoDocbcCost', '')}">
        일반 건강 상태<input type="number" step="0.01" name="GenHlth" placeholder="일반 건강 상태 (1-5)" value="{inputs.get('GenHlth', '')}">
        정신 건강 일수<input type="number" step="0.01" name="MentHlth" placeholder="정신 건강 일수 (0-30)" value="{inputs.get('MentHlth', '')}">
        신체 건강 일수<input type="number" step="0.01" name="PhysHlth" placeholder="신체 건강 일수 (0-30)" value="{inputs.get('PhysHlth', '')}">
        걷기 어려움<input type="number" step="0.01" name="DiffWalk" placeholder="걷기 어려움 (0 또는 1)" value="{inputs.get('DiffWalk', '')}">
        성별<input type="number" name="Sex" placeholder="성별 (0: 여성, 1: 남성)" value="{inputs.get('Sex', '')}">
        나이<input type="number" name="Age" placeholder="나이" value="{inputs.get('Age', '')}">
        교육 수준<input type="number" step="0.01" name="Education" placeholder="교육 수준 (1-6)" value="{inputs.get('Education', '')}">
        소득 수준<input type="number" step="0.01" name="Income" placeholder="소득 수준(1~10)" value="{inputs.get('Income', '')}">
        <p><input type="submit" value="예측"><br>
            <font size="18" color="#f3c262">결과: {result}</font>
      </form>
     </body>
    </html>""")

def predictHighChol(inputs):
    # 입력값을 numpy 배열로 변환
    input_array = np.array([[float(inputs[key]) for key in inputs]])
    
    # 스케일링 적용
    input_scaled = scaler.transform(input_array)
    
    # 텐서로 변환
    input_tensor = torch.FloatTensor(input_scaled)
    
    # 예측
    with torch.no_grad():
        output = model(input_tensor)
        prediction = output.item()
    
    return "흡연자🚬" if prediction > 0.5 else "💕비흡연자💕"

# 메인 실행 부분
form = cgi.FieldStorage()
inputs = {
    'Diabetes_binary': form.getvalue('Diabetes_binary', ''),
    'HighBP': form.getvalue('HighBP', ''),
    'HighChol': form.getvalue('HighChol', ''),
    'CholCheck': form.getvalue('CholCheck', ''),
    'BMI': form.getvalue('BMI', ''),    
    'Stroke': form.getvalue('Stroke', ''),
    'HeartDiseaseorAttack': form.getvalue('HeartDiseaseorAttack', ''),
    'PhysActivity': form.getvalue('PhysActivity', ''),
    'Fruits': form.getvalue('Fruits', ''),
    'Veggies': form.getvalue('Veggies', ''),
    'HvyAlcoholConsump': form.getvalue('HvyAlcoholConsump', ''),
    'AnyHealthcare': form.getvalue('AnyHealthcare', ''),
    'NoDocbcCost': form.getvalue('NoDocbcCost', ''),
    'GenHlth': form.getvalue('GenHlth', ''),
    'MentHlth': form.getvalue('MentHlth', ''),
    'PhysHlth': form.getvalue('PhysHlth', ''),
    'DiffWalk': form.getvalue('DiffWalk', ''),
    'Sex': form.getvalue('Sex', ''),
    'Age': form.getvalue('Age', ''),
    'Education': form.getvalue('Education', ''),
    'Income': form.getvalue('Income', '')
}

result = ""
if all(inputs.values()):  # 모든 필드가 채워졌는지 확인
    result = predictHighChol(inputs)

showHTML(inputs, result)