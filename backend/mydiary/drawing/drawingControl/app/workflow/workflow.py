#-*- coding:utf-8 -*-
# 이미지 프로세서, 그림 데이터 저장 및 앱 실행 제어
from __future__ import division
import numpy as np
from pathlib import Path
import logging
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from app.sketch import SketchGizeh
import subprocess
from csv import writer
import asyncio
class Workflow:
    def __init__ (self, dataset, imageprocessor):
        self._path = Path('') # 저장된 이미지 경로 (없어도 될듯)
        self._image_path = Path('') # 
        self._dataset = dataset # 그림 데이터 세트
        self._image_processor = imageprocessor # 이미지 처리 객체
        self._sketcher = None # 스케치 객체
        self._logger = logging.getLogger(self.__class__.__name__)
        self._image = None
        #self._annotated_image = None
        self._image_labels = []
        self._boxes = None
        self._classes = None
        self._scores = None
        self.count = 0
    
    async def setup(self):
        self._logger.info('퀵드로우 dataset 로딩 중...')
        await self._dataset.setup()
        self._logger.info('완료')
        self._sketcher = SketchGizeh()
        await self._sketcher.setup()
        self._logger.info('tensorflow model 로딩 중...')
        await self._image_processor.setup()
        self._logger.info('완료')
        self._path = Path(__file__).parent / '..' / '..' / 'images' 
        if not self._path.exists():
            self._path.mkdir()
        self.count = len(list(self._path.glob('image*.jpg')))
        self._logger.info('초기 설치 완료.')

    async def label_to_image(self,keyword,path):
        await self._sketcher.draw_object_label(keyword,self._dataset)
        cartoon_path = str(keyword) + '.png'
        print(cartoon_path)
        await self._sketcher.save_png(path+'/'+cartoon_path)
        return cartoon_path


    # 이미지 가져와서 captioning 후 라벨가져와서 데이터세트와 매핑
    async def process(self, image_path,imagename, threshold=0.3,top_x=None):
        """
         top_x : none이 아니면 상위 일치율이 좋은 X 개의 결과 만 그려집니다 (임계 값 무시).
         threshold : 객체 감지 임계 값 (0.0 ~ 1.0) 임계값 이하의 확률로 매칭된 이미지는 무시
         path : 결과를 저장할 디렉토리
         image_path : 처리 할 이미지
        """
        self._logger.info('이미지 처리 중')
        try : 
            self._image_path = Path(image_path)
            img = await self._image_processor.load_image_into_numpy_array(image_path)  # image 가져와서 n*n*3 numpy 배열로 반환
            # 이미지의 크기가 조정 된 버전을 메모리에 로드
            scaled_img = await self._image_processor.load_image_into_numpy_array(image_path, scale = 300 / max(img.shape)) # 크기 300으로 맞추려고
            self._boxes, self._scores, self._classes, num = await self._image_processor.detect(scaled_img)
            self._logger.info('score: {}'.format(str(self._scores)))
             # 원래 이미지에 테두리 따기
            #self._annotated_image = self._image_processor.annotate_image(img, self._boxes, self._classes, self._scores, threshold=threshold)
            self._sketcher = SketchGizeh()
            await self._sketcher.setup(img.shape[1], img.shape[0])
            if top_x is not None:
                sorted_scores = sorted(self._scores.flatten())
                threshold = sorted_scores[-min([top_x, self._scores.size])]   
            self._image_labels = await self._sketcher.draw_object_recognition_results(np.squeeze(self._boxes),
                                   np.squeeze(self._classes).astype(np.int32),
                                   np.squeeze(self._scores),
                                   self._image_processor.labels,
                                   self._dataset,
                                   threshold=threshold)
            debug = True                   
            self._logger.info('결과 저장 중...')
            annotated_path = self._image_path
            cartoon_path = self._image_path.with_name('cartoon_' + imagename + '.png')
            labels_path = self._image_path.with_name('labels_' + imagename+ '.txt')
            with open(str(labels_path), 'w') as f:
                f.writelines(self.image_labels)
            if debug:
                scores_path = self._image_path.with_name('scores_' + imagename + '.txt')
                with open(str(scores_path), 'w', newline='') as f:
                    fcsv = writer(f)
                    fcsv.writerow(map(str, self._scores.flatten()))
            # self._save_3d_numpy_array_as_png(self._annotated_image, annotated_path)
            await self._sketcher.save_png(cartoon_path)
            return 'cartoon_' + imagename + '.png'
            
        except (ValueError, IOError) as e:
            self._logger.exception(e)
            print(e)
        

    async def save_results(self, debug=False):
        """
        결과 이미지를 png로 저장하고 감지 된 개체 목록을 txt로 저장
        debug가 true이면 감지 된 모든 개체와 해당 점수 목록을 저장합니다.
        :return tuple: (경계 딴 이미지 경로, 그림화한 이미지 경로)
        """
        self._logger.info('결과 저장 중...')
        self._logger.info('score: {}'.format(str(self._scores)))
        annotated_path = self._image_path
        cartoon_path = self._image_path.with_name('cartoon' + str(self.count) + '.png')
        labels_path = self._image_path.with_name('labels' + str(self.count) + '.txt')
        with open(str(labels_path), 'w') as f:
            f.writelines(self.image_labels)
        if debug:
            scores_path = self._image_path.with_name('scores' + str(self.count) + '.txt')
            with open(str(scores_path), 'w', newline='') as f:
                fcsv = writer(f)
                fcsv.writerow(map(str, self._scores.flatten()))
        # self._save_3d_numpy_array_as_png(self._annotated_image, annotated_path)
        await self._sketcher.save_png(cartoon_path)
        return cartoon_path

    
    def close(self):
        self._image_processor.close()
    
    @property
    def image_labels(self):
        return self._image_labels