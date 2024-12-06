from torch import nn

class reviewClassifierModel(nn.Module):
    def __init__(self, n_vocab, hidden_dim, embedding_dim, n_classes,
                 n_layers, dropout=0.5, bidirectional=True) -> None:
        super().__init__()
        self.embedding = nn.Embedding(
            num_embeddings=n_vocab,         # num_embeddings = vocab이 들어감
            embedding_dim=embedding_dim,
            padding_idx=0
        )
        self.model = nn.LSTM(
            input_size = embedding_dim,         # Input의 사이즈에 해당하는 수
            hidden_size=hidden_dim,             # 은닉층의 사이즈에 해당하는 수
            num_layers=n_layers,                # RNN의 은닉층 레이어 개수, default = 1
            bidirectional=bidirectional,        # bidrectional True일시 양방향 RNN, default = False
            dropout=dropout,                    # dropout 비율설정 기본값 0
            batch_first=True,                   # True일 경우 Output 사이즈는 (batch, seq, feature) 기본값 False
        )
        if bidirectional:
            self.classifier1 = nn.Linear(hidden_dim*2,n_classes)
            self.classifier2 = nn.Linear(hidden_dim*2,1)
        else:
            self.classifier1 = nn.Linear(hidden_dim,n_classes)
            self.classifier2 = nn.Linear(hidden_dim,1)
        self.dropout = nn.Dropout(dropout)

    def forward(self,inputs):
        embeddings = self.embedding(inputs)
        output, _ = self.model(embeddings)
        last_output = output[:, -1, :]  # 마지막 시간 스텝의 출력
        last_output = self.dropout(last_output)

        classesd = self.classifier1(last_output)
        logits = self.classifier2(last_output)

        # LogSoftmax 적용
        classesd = nn.LogSoftmax(dim=1)(classesd)  # 다중 클래스 출력에 LogSoftmax 적용

        return classesd, logits
    
# 순환 신경망(RNN)
# 구조: RNN은 시퀀스 데이터를 처리할 수 있도록 설계된 신경망으로, 이전 시간 단계의 정보를 현재 시간 단계로 전달하여 순서가 있는 데이터를 처리하는 신경망
# 문제점: RNN은 긴 시퀀스에서 장기 의존성 문제(long-term dependency)를 겪음. 이는 시간이 지나면 초기 입력 정보가 점차 소실되어 과거 정보의 영향력이 약해지는 현상으로, "기울기 소실 문제"(vanishing gradient problem)로 인해 학습이 어려워짐.
# 적용: RNN은 주로 단기적인 의존성이 필요한 경우(예: 간단한 시계열 예측)에 적합한 신경망.
# 장단기 메모리(LSTM)
# 구조: LSTM은 RNN의 확장형으로, RNN의 장기 의존성 문제를 해결하기 위해 설계됨. LSTM은 특별한 게이트 구조(입력 게이트, 출력 게이트, 망각 게이트)를 통해 중요한 정보를 더 오랫동안 유지하거나 불필요한 정보를 버리는 방식으로 처리.
# 장점: LSTM은 장기 기억을 유지하면서도 중요한 정보만 남기고 불필요한 정보를 잊는 능력이 뛰어나, 기울기 소실 문제를 완화하여 긴 시퀀스 데이터에서도 효과적인 학습이 가능.
# 적용: 긴 문장 처리, 긴 시계열 데이터, 자연어 처리(NLP), 음성 인식 등 장기적인 의존성이 중요한 작업에서 주로 사용.
# 요약
# RNN은 기본적으로 순차적인 데이터를 처리할 수 있지만, 장기 기억이 어려워 기울기 소실 문제를 겪음.
# LSTM은 RNN의 확장형으로, 장기 의존성 문제를 해결하고 중요한 정보를 더 오래 기억할 수 있도록 설계됨.
# 이 차이점으로 인해 LSTM은 긴 시퀀스를 다루는 작업에 보다 효과적.