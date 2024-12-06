# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import torch
import os
import pickle
import re
import numpy as np
from konlpy.tag import Okt
import string
from konlpy.tag import Kkma



# reviewclassifiermodel 모듈에서 ReviewClassifierModel 클래스 임포트
from reviewclassifiermodel import *


app = Flask(__name__)

# 모델 경로 설정
category_name = ["화장품"]
model_files = ["cosmetic"]
Acepts_list = [
    ['유통기한', '제품구성', '보습력/수분감', '용량', '자극성', '가격', '흡수력', '제형', '향', '발림성', '품질', '기능/효과', '사용감', '피부타입', '윤기/피부(톤)', '용기', '성분', '탄력', '편의성/활용성', '지속력', '디자인', '색상', '밀착력/접착력', '커버력', '탈모개선', '청량감/쿨링감', '세정력', '지속력/유지력', '두피보호', '머릿결관리', '향/냄새', '용량/사이즈', '거품력', '스타일링효과', '세팅력/고정력', '염색력', '발색력', '클렌징/제거력', '이염', '분사력', '그립감', '보습력/수분감/쿨링감', '사이즈/두께', '용량/개수'],
]

MODEL_PATH = r'C:\Users\KDP-27\Desktop\KDT6\pj\WEB\model\cosmetic_model.pth'
DATA_PATH = r'C:\Users\KDP-27\Desktop\KDT6\pj\WEB\data\stopwords.txt'
MAX_LENGTH = [38]   

# 모델 불러오기 함수
def load_model(model, model_path):

    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()  # 평가 모드로 전환
    return model

def load_vocab(vocab_path):

    with open(vocab_path, 'rb') as f:
        vocab = pickle.load(f)
    return {token: idx for idx, token in enumerate(vocab)}

def split_sentences(text):
    kkma = Kkma()
    sentences = kkma.sentences(text)
    return sentences

def load_stopwords():
    STOP_WORD = os.path.join(DATA_PATH, 'stopwords.txt')
    with open(STOP_WORD, 'r', encoding='utf-8') as f:
        stop_words = set([line.strip() for line in f])
    return stop_words

# 전처리 함수
def preprocess_text(text, punc):
    for p in punc:
        text = text.replace(p, '')
    text = re.sub('[^ ㄱ-ㅣ가-힣]+', ' ', text)
    return text.strip()

# 토큰화 및 불용어 제거 함수
def tokenize_and_remove_stopwords(tokenizer, texts, stop_words):
    tokens = [tokenizer.morphs(text) for text in texts]
    tokens = [[token for token in doc if token not in stop_words] for doc in tokens]
    return tokens

# 인코딩 함수
def encoding_ids(token_to_id, tokens, unk_id):
    return [[token_to_id.get(token, unk_id) for token in doc] for doc in tokens]

# 패딩 함수
def pad_sequences(sequences, max_length, pad_value):
    padded_seqs = []
    for seq in sequences:
        seq = seq[:max_length]  # 최대 길이에 맞춤
        pad_len = max_length - len(seq)
        padded_seq = seq + [pad_value] * pad_len
        padded_seqs.append(padded_seq)
    return np.array(padded_seqs)

def analyze_review(model, sentence_tensor):
    classesd, logits = model(sentence_tensor)
    return classesd, logits

@app.route('/', methods=['GET', 'POST'])
def index():
    outputdata=[]
    review=''
    selected_model = 0
    if request.method == 'POST':
        tokenizer = Okt()
        selected_model = int(request.form.get('model'))
        review = request.form.get('review')
        vocab = load_vocab(selected_model)
        stop_words = load_stopwords()
        punc = string.punctuation

        n_vocab = len(vocab)
        hidden_dim = 64
        embedding_dim = 128
        n_layers = 2

        # 모델 로드
        if selected_model == 3:
            model = ReviewClassifierModel(
            n_vocab=n_vocab,
            hidden_dim=hidden_dim,
            embedding_dim=embedding_dim,
            n_classes=len(Acepts_list[selected_model]),
            n_layers=n_layers,
            dropout=0.3
            ).to('cpu')
        else:
            from models.reviewclassifiermodel import reviewClassifierModel
            model = reviewClassifierModel(
                n_vocab=n_vocab, hidden_dim=hidden_dim, embedding_dim=embedding_dim, n_classes=len(Acepts_list[selected_model]), n_layers=n_layers
            ).to('cpu')
        model = load_model(selected_model, model)

        # 리뷰 처리
        sentences = split_sentences(review)
        pre_sentences = [preprocess_text(sentence, punc) for sentence in sentences]
        sentence_tokens = tokenize_and_remove_stopwords(tokenizer, pre_sentences, stop_words)
        sentence_ids = encoding_ids(vocab, sentence_tokens, vocab.get('<unk>'))

        # 입력 데이터 패딩
        input_data = pad_sequences(sentence_ids, MAX_LENGTH[selected_model], vocab.get('<pad>'))
        sentence_tensor = torch.tensor(input_data, dtype=torch.long)

        # 분석
        classesd, logits = analyze_review(model, sentence_tensor)
        classesd = torch.argmax(classesd, dim=1)
        logits = torch.sigmoid(logits)
        classesd = classesd.tolist()
        logits = logits.tolist()

        for i in range(len(classesd)):
            outputdata.append([Acepts_list[selected_model][classesd[i]], '긍정' if logits[i][0] > 0.5 else '부정'])
        outputdata = outputdata

    return render_template('index.html', category_name=category_name,selected_model=selected_model, review = review, outputdata=outputdata)

if __name__ == '__main__':
    app.run(debug=True)
