import pandas as pd

import numpy as np
from konlpy.tag import Okt


okt = Okt()

NRC = pd.read_csv("C:/Users/multicampus/PycharmProjects/s03p23a201/backend/ML/data/after_change_csv.csv",
                header=None,)

NRC = NRC[(NRC != 0).all(1)]

# 인덱스 번호 리셋
NRC = NRC.reset_index(drop=True)

ko_stopwords = pd.read_csv("C:/Users/multicampus/PycharmProjects/s03p23a201/backend/ML/data/ko_stopwords.txt",
                  engine="python", header=None, sep="\n")


pos_review = "오늘 아빠와 함께 바다에 갔다. 정말 재미있는 하루였다. 낚시도 하고 라면도 먹었다."



stop_words = ko_stopwords

raw = pos_review.lower()
tokens = okt.morphs(pos_review)
print(raw)
print(tokens)
print(NRC)
stopped_tokens = [i for i in tokens if not i in stop_words] # 불용어 제거
match_words = [x for x in stopped_tokens if x in list(NRC[0])] # 사전과 매칭
print("stop",stopped_tokens)
print(match_words)
#Positive	Negative	Anger	Anticipation	Disgust	Fear	Joy	   Sadness  	Surprise	Trust

#긍정         부정         화남       기대          혐호  두려움     즐거움  슬픔         놀람          믿음

#기쁨  긍정, 기대, 즐거움, 믿음
#슬픔  부정 슬픔 두려움
#화남  부정, 화남, 혐호,
#중립
emotion=[]
for i in match_words:
    temp = list(NRC.iloc[np.where(NRC[0] == i)[0],1])
    for j in temp:
        emotion.append(j)

sentiment_result1 = pd.Series(emotion).value_counts()
print("asdasd  ",sentiment_result1[0])
emo_score = [0,0,0,1/len(emotion)]
for i in emotion:
    if i == 'Positive' or i == 'Anticipation' or i =='Joy' or i =='Trust' or i =='Surprise':
        emo_score[0]+=1
    elif i == 'Negative':
        emo_score[1]+=1
        emo_score[2]+=1
    elif i == 'Sadness' or i =='Fear':
        emo_score[1] += 1
    elif i == 'Anger' or i =='Disgust':
        emo_score[2]+=1

    print("dd ",i)
    print(emo_score)
for i in range(len(emo_score)-1):
    emo_score[i] = emo_score[i]/len(emo_score)
print(emo_score)
print(sentiment_result1, sentiment_result1.plot.bar(), raw)