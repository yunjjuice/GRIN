import os
import sys
import urllib.request
import pandas as pd

client_id = "2mm3c1Mi83sCmC_qVpVt" # 개발자센터에서 발급받은 Client ID 값
client_secret = "Xel2UWDy9m" # 개발자센터에서 발급받은 Client Secret 값
# client_id = "J11vvgAknwYK88vOdUa1" # 개발자센터에서 발급받은 Client ID 값
# client_secret = "Miimjr1UnY" # 개발자센터에서 발급받은 Client Secret 값
# client_id = "4hbP936tL3JQ19sm80zX" # 개발자센터에서 발급받은 Client ID 값
# client_secret = "bXQnyI0gZ2" # 개발자센터에서 발급받은 Client Secret 값
# client_id = "ZQxIOH43tkBBPx5iKBn3" # 개발자센터에서 발급받은 Client ID 값
# client_secret = "wjkBMsLROr" # 개발자센터에서 발급받은 Client Secret 값
# client_id = "ZyZ1A7BQrheKDb8F3MTR" # 개발자센터에서 발급받은 Client ID 값
# client_secret = "t2sNZxS5K8" # 개발자센터에서 발급받은 Client Secret 값
# client_id = "0NDGyaB6PCRrmzXvBggQ" # 개발자센터에서 발급받은 Client ID 값
# client_secret = "rkap9K7f6h" # 개발자센터에서 발급받은 Client Secret 값
# client_id = "xCuzI5mRb9U_OikWA1Is" # 개발자센터에서 발급받은 Client ID 값
# client_secret = "c2R5MnfSTg" # 개발자센터에서 발급받은 Client Secret 값
# encText = urllib.parse.quote("반갑습니다")
# data = "source=en&target=ko&text=" + encText
# url = "https://openapi.naver.com/v1/papago/n2mt"
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request, data=data.encode("utf-8"))
# rescode = response.getcode()

fd = open("C:/Users/multicampus/PycharmProjects/s03p23a201/backend/ML/data/anger.txt",
          'r',encoding='UTF8' )
f = open("translate_anger.txt", 'w', encoding='UTF-8')
lines = fd.readlines()
# for t in lines:
#     print("t  ",t)
#
#     print("tasdasd ",t)
#     if t.__contains__('@'):
#         sp = t.split(' ')
#         sp = sp[1:]
#         for spp in sp:
#             if spp.__contains__('@'):
#                 sp.remove(spp)
#
#         sp = " ".join(sp)
#     print("ss  ",sp)
#     encText = urllib.parse.quote(t)
#     print(encText)
cnt = 0
for t in lines:
    if cnt < 943:
        cnt+=1
        print(cnt)
        continue
    if t.__contains__('@'):
        sp = t.split(' ')
        if sp[0].__contains__('@'):
            sp = sp[1:]

        t = " ".join(sp)
    encText = urllib.parse.quote(t)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
        f.write(response_body.decode('utf-8')+"\n")
    else:
        print("Error Code:" + rescode)


