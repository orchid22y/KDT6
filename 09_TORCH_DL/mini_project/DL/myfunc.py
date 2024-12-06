
# - Data 및 시각화 관련

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def draw_bar(df):
    col = 3
    row = (len(df.columns) + col - 1) // col
    colors = [
    "#AED6F1",  # 옅은 하늘색
    "#A9DFBF",  # 옅은 초록색
    "#F9E79F",  # 옅은 노란색
    "#F5B7B1",  # 옅은 핑크색
    "#D2B4DE",  # 옅은 보라색
    "#FAD7A0",  # 옅은 주황색
    "#D5DBDB",  # 옅은 회색
    "#A3E4D7",  # 옅은 민트색
    "#D7BDE2",  # 옅은 연보라색
    "#F5CBA7",  # 옅은 살구색
]

    plt.figure(figsize=(15, row * 4))
    for i, column in enumerate(df.columns, 1):
        plt.subplot(row, col, i)
        df[column].value_counts().plot(kind='bar', color=colors)
        plt.title(column)
        plt.xticks(rotation=360)
    plt.tight_layout()
    plt.show()


