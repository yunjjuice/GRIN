#-*- coding:utf-8 -*-
import time
import logging
from .app.workflow import Workflow
from .app.drawing_data import DrawingData
from .app.image_processor import ImageProcessor
from .app.sketch import SketchGizeh
from .app.painting import cgi_exe
from pathlib import Path
import tarfile
import datetime
import asyncio
import sys
sys.path.append('./app/painting')

root = Path(__file__).parent

#tensorflow_model_name = 'ssd_mobilenet_v2_320x320_coco17_tpu-8'
tensorflow_model_name ='ssd_mobilenet_v1_coco_2018_01_28'
model_path = root / 'downloads' / 'detection_models' / tensorflow_model_name / 'frozen_inference_graph.pb'#'saved_model' / 'saved_model.pb'

# parameter(이미지 카테고리 적은 텍스트파일, 재 mapping할 jsonl파일)
dataset = DrawingData(str(root / 'downloads/drawing_dataset'), str(root / 'label_mapping.jsonl'))
# 이미지 검출 위한 이미지 프로세서 객체
imageprocessor = ImageProcessor(str(model_path),
                                 str(root / 'app' / 'object_detection' / 'data' / 'mscoco_label_map.pbtxt'),
                                 tensorflow_model_name)

# configure logging 로그 남기기
logging_filename = datetime.datetime.now().strftime('%Y%m%d-%H%M.log')
logging_path = Path(__file__).parent / 'logs' # 현 폴더 위치에 logs 파일 
if not logging_path.exists():
    logging_path.mkdir()
logging.basicConfig(format=u'%(levelname)s:%(message)s',
                    level=logging.DEBUG, filename=str(Path(__file__).parent / 'logs' / logging_filename))
# 이미지 처리 하고 매핑, 매핑만 할 것인지
async def run(drawtype,path,imagename=None,keyword=None):
    app = Workflow(dataset, imageprocessor)
    await app.setup()
    if drawtype == 'image_captioning': # 이미지 올리고 captioning 할 때
        
        cartoon_path = await app.process(str(path),imagename) # top_x : none이 아니면 상위 일치율이 높은 X 개의 결과 만 그려집니다
        #cartoon_path = await app.save_results(debug=True)
        
        app.count += 1 #필요 없을 거 같긴함
        print('finished processing files, closing app.')
        app.close()
        return cartoon_path
           
    elif drawtype == 'keyword_drawing': # 주어진 키워드로 mapping 할때 (둘다 할 수 있도록?)
        drawing_path = await app.label_to_image(keyword,path)
        app.close()
        return drawing_path

    elif drawtype == 'painting':
        painter = cgi_exe.Painter(0)
        painter.colorize('testImage',"C", blur=0)
    # if str(path) != '.' or 'exit':
    #     app.process(str(path), top_x=3)
    #     app.save_results()
    else:
        app.close()
        sys.exit()


if __name__=='__main__':
    #run('painting','testImage')
    # app = Workflow(dataset, imageprocessor)
    # app.setup()
    ap = tarfile.open('./downloads/detection_models/ssd_mobilenet_v1_coco_2018_01_28.tar.gz')
    ap.extractall('./downloads/detection_models/ssd_mobilenet_v1_coco_2018_01_28') 
    ap.close()
    #imageprocessor.load_model('./downloads/detection_models/ssd_mobilenet_v1_coco_2018_01_28')