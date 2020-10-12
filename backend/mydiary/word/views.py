
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from konlpy.tag import Okt
from .predic_emo import predic
from .apps import WordConfig




import json
# Create your views here.

class ExtractAPIView(APIView):
    def post(self, request):
        json_data = json.dumps(request.data)
        dict_json = json.loads(json_data)

        nlpy = Okt()
        nonus = nlpy.nouns(dict_json['content'])
        return Response(nonus)


class EmoAPIView(APIView):
    def post(self, request):
        json_data = json.dumps(request.data)
        dict_json = json.loads(json_data)
        print("dict_json  ", dict_json)
        model = WordConfig.model
        pred = predic(model, dict_json['content'])   
        return Response(pred)
