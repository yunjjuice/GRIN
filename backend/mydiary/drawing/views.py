from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response

from .models import Picture
from .serializers import *
from .drawingControl.processing import run
from pathlib import Path
import os
import time
from .papago import papa
import asyncio
import jsonlines
parentPath = Path(__file__).parent
rootPath = os.path.dirname((os.path.abspath(os.path.dirname(__file__)))) +'/media/images/'
drawingPath = rootPath+ time.strftime('%Y/%m/%d', time.localtime(time.time()))
returnPath = '/media/images/'+ time.strftime('%Y/%m/%d', time.localtime(time.time()))
class UploadAPIView(generics.CreateAPIView):
    serializer_class = PictureSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        print(drawingPath)
        imagename = str(request.data["image"]).split(".")[0]
        filename = drawingPath +'/'+  str(request.data["image"])
        # image_path =sync_to_async(run,thread_sensitive=True)('image_captioning',filename)
        image_path = asyncio.run(run('image_captioning',filename,imagename=imagename))
        print(image_path)
        
        return Response({
            'trans_image' : returnPath+'/'+str(image_path)
        })
    
    # get_blog = (post, thread_sensitive=True)

class KeywordAPIView(APIView):
    def get(self, request):
        
        keyword = self.request.query_params.get('keyword')
        #번역
        print(keyword)
        keyword = papa(keyword).lower()
        keyword = keyword.rstrip(".")
        print(keyword)
        firstword = keyword.split(" ")[0]
        deletelist = ["the","an","a"]
        if firstword in deletelist:
            keyword = keyword[2:]



        categoryfile = parentPath / 'drawingControl' / 'downloads' / 'drawing_dataset' / 'categories.txt'
        # keyword 매핑
        categorylist = ["person"]
        with open(categoryfile, "r") as file:
            for line in file:
                categorylist.append(line.rstrip("\n"))

        if keyword not in categorylist :
            with jsonlines.open(str(parentPath)+"/label_matching.jsonl", mode='r') as reader:
                category_mapping = reader.read()
            if keyword in category_mapping.keys(): # 대체할 단어가 있을 때
                keyword = category_mapping[keyword]
                print("대체 키워드", keyword)
            else : #keyword가 아예 존재하지 않을 때
                return Response(status=status.HTTP_404_NOT_FOUND)

        if not os.path.isdir(Path(drawingPath)) :
            os.makedirs(drawingPath)

        image_path = asyncio.run(run('keyword_drawing',drawingPath,keyword=keyword))

        return Response({
            'image_path' : returnPath+'/'+image_path
        })
    


            
