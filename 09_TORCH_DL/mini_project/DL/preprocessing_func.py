

import pandas as pd






def preprocess_and_encode(df):
    '''
    BMI 8그룹
    저체중: BMI < 18.5
    정상 체중: 18.5 ≤ BMI < 24.9
    과체중: 25 ≤ BMI < 29.9
    비만 (1단계): 30 ≤ BMI < 34.9
    비만 (2단계): 35 ≤ BMI < 39.9
    비만 (3단계, 고도비만): 40 ≤ BMI < 49.9
    초고도비만: 50 ≤ BMI < 59.9
    극단적 비만: BMI ≥ 60
    '''
    
    bmi_bins = [0, 18.5, 24.9, 29.9, 34.9, 39.9, 49.9, 59.9, float('inf')]
    bmi_labels = ['저체중', '정상 체중', '과체중', '비만 1단계', '비만 2단계', '비만 3단계', '초고도비만', '극단적 비만']
    df['BMI_Group'] = pd.cut(df['BMI'], bins=bmi_bins, labels=bmi_labels)
    df = pd.get_dummies(df, columns=['BMI_Group'], prefix='BMI')
    df.drop(columns=['BMI'], inplace=True)  


    '''
    건강상태 2그룹
    적당하다
    좋다
    '''
    genhlth_bins = [0, 3, 5]
    genhlth_labels = ['1-3', '4-5']
    df['GenHlth_Group'] = pd.cut(df['GenHlth'], bins=genhlth_bins, labels=genhlth_labels)
    df = pd.get_dummies(df, columns=['GenHlth_Group'], prefix='GenHlth')
    df.drop(columns=['GenHlth'], inplace=True)  


    
    '''
    나이별 그룹 2 
    청장년층
    노년층
    '''
    age_bins = [0, 8, 13]
    age_labels = ['1-8', '9-13']
    df['Age_Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)
    df = pd.get_dummies(df, columns=['Age_Group'], prefix='Age')
    df.drop(columns=['Age'], inplace=True)  

    '''
    소득수준
    저소득층
    중위층
    고소득층
    '''
    income_bins = [0, 5, 8, 11]
    income_labels = ['1-5', '6-8', '9-11']
    df['Income_Group'] = pd.cut(df['Income'], bins=income_bins, labels=income_labels)
    df = pd.get_dummies(df, columns=['Income_Group'], prefix='Income')
    df.drop(columns=['Income'], inplace=True) 

    '''
    어떻게 그룹화 분류값이 너무 극단적인 친구들은 drop
    '''
    df.drop(columns=['MentHlth'], inplace=True)  
    df.drop(columns=['PhysHlth'], inplace=True) 
    df.drop(columns=['Education'], inplace=True)

    # True/False 값 변환
    df = df.replace({True: 1, False: 0})

    return df