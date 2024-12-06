from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import platform
import numpy as np
from PIL import Image

text=open('test.txt', encoding='utf-8').read()
okt=Okt()

sentences_tag=[]
sentences_tag=okt.pos(text)

noun_adj_list=[]

for word, tag in sentences_tag:
    if tag in ['Noun', 'Adjective']:
        noun_adj_list.append(word)

print(noun_adj_list)

counts=Counter(noun_adj_list)
tags=counts.most_common(50)
print(tags)

if platform.system()=='Windows':
    path=r"C:\Users\KDP-27\anaconda3\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\온글잎 언즈체.ttf"
elif platform.system()=='Darwin':
    path=r'/System/Library/Fonts/AppleGothic'
else:
    font=r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

img_mask=np.array(Image.open('cloud.png'))
wc=WordCloud(font_path=path, width=400, height=400,
             background_color='white', max_font_size=200,
             repeat=True,
            colormap='inferno', mask=img_mask)
cloud=wc.generate_from_frequencies(dict(tags))

plt.figure(figsize=(10,8))
plt.axis('off')
plt.imshow(cloud)
plt.show()