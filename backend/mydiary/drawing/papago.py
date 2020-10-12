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

def papa(text):
    encText = urllib.parse.quote(text)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
  
    if (rescode == 200):
        response_body = response.read()
        
        # print(response_body.decode('utf-8'))

    tran  = response_body.decode('utf-8')
    sp = tran.split('"')[27]

    return sp