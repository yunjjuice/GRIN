# -*- encoding: utf-8 -*-
import tweepy
import os

import sys


#트위터의 개인 앱 계정에서 아래 4가지 사항 확인
consumer_key = "coPxdqeKvCZMv8ZQnj1Y4MhrI"
consumer_secret = "qkR04FhcQHiXszD68yNksTwnx7tAkQKYv0dz5vrgJduCrayprw"
access_token = "1309012765911248898-GWU6gRDlA3Xs6ULS7rrYCU94HhOJiY"
access_token_secret = "fHX1SMdjAdgQ0bNohQotjhAWP9nh2PaZlDLC6wNSR9cK8"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



location = "%s,%s,%s" % ("35.95", "128.25", "1000km")  # 검색기준(대한민국 중심) 좌표, 반지름

keyword = "빡치"                                      # OR 로 검색어 묶어줌, 검색어 5개(반드시 OR 대문자로)

wfile = open(os.getcwd()+"/빡치.txt", 'w',-1,'utf-8')        # 텍스트 파일로 출력(쓰기모드)

# twitter 검색 cursor 선언

cursor = tweepy.Cursor(api.search,

                       q=keyword,

                       since='2015-01-01', # 2015-01-01 이후에 작성된 트윗들로 가져옴

                       count=100,  # 페이지당 반환할 트위터 수 최대 100

                       geocode=location,

                       include_entities=True)

for i, tweet in enumerate(cursor.items()):

    print("{}: {}".format(i, tweet.text))

    wfile.write(tweet.text + '\n')

wfile.close()