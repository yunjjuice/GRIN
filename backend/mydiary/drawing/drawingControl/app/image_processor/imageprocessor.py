#-*- coding:utf-8 -*-
from pathlib import Path
from PIL import Image
import numpy as np
import tensorflow as tf
import logging
import os
import tarfile
import six.moves.urllib as urllib
from app.object_detection import label_map_util

root = Path(__file__).parent

class ImageProcessor(object):

    def __init__(self, path_to_model, path_to_labels, model_name):
        self._model_name = model_name
        # Path to frozen detection graph. This is the actual model that is used for the object detection.
        self._path_to_model =  path_to_model
        # strings used to add correct label for each box.
        self._path_to_labels = path_to_labels
        self._download_url = 'http://download.tensorflow.org/models/object_detection/'
        self._num_classes = 90
        self._detection_graph = None
        self._labels = dict()
        self._image = None
        self._boxes = None
        self._classes = None
        self._scores = None
        self._num = None
        self._logger = None
        self._session = None
        self.image_tensor = None
        self.detection_boxes = None
        self.detection_scores = None
        self.detection_classes = None
        self.num_detections = None

    async def setup(self):
        self._logger = logging.getLogger(self.__class__.__name__)
        if not Path(self._path_to_model).exists():
            self._logger.info('모델 다운로드중..')
            self.download_model(self._download_url, self._model_name + '.tar.gz')
        #self.download_model(self._download_url, self._model_name + '.tar.gz')
        await self.load_model(self._path_to_model)
        self._labels = await self.load_labels(self._path_to_labels)
        # run a detection once, because first model run is always slow
        await self.detect(np.ones((150, 150, 3), dtype=np.uint8))


    def unzip(self,path):
        ap = tarfile.open(path + '.tar.gz')
        ap.extractall(path) 
        ap.close()

    def download_model(self, url, filename):
        """URL에서 모델 파일을 다운로드하고 압축을 풉니다.
        """
        self._logger.info('downloading model: {}'.format(filename))
        opener = urllib.request.URLopener()
        opener.retrieve(url + filename, filename)
        tar_file = tarfile.open(filename)
        for file in tar_file.getmembers():
            file_name = os.path.basename(file.name)
            if 'saved_model' in file_name:
                tar_file.extract(file, path=str(Path(self._path_to_model).parents[1]))

    async def load_model(self, path):
        """
        파일에서 저장된 모델로드
        """
        self._logger.info('model 로드 중...')
        if not Path(path).exists():
            raise IOError('model file missing: {}'.format(str(path)))
        with tf.io.gfile.GFile(path, 'rb') as fid:
            graph_def = tf.compat.v1.GraphDef()
            graph_def.ParseFromString(fid.read())
        with tf.Graph().as_default() as graph:
            tf.import_graph_def(graph_def, name='')
        self._detection_graph = graph
        self._session = tf.compat.v1.Session(graph=self._detection_graph)
        # detection_graph에 대한 명확한 입력 및 출력 텐서
        self.image_tensor = self._detection_graph.get_tensor_by_name('image_tensor:0')
        # Each box represents a part of the image where a particular object was detected.
        self.detection_boxes = self._detection_graph.get_tensor_by_name('detection_boxes:0')
        # Each score represent how level of confidence for each of the objects.
        # Score is shown on the result image, together with the class label.
        self.detection_scores = self._detection_graph.get_tensor_by_name('detection_scores:0')
        self.detection_classes = self._detection_graph.get_tensor_by_name('detection_classes:0')
        self.num_detections = self._detection_graph.get_tensor_by_name('num_detections:0')
        self._logger.info('model 로드 완료...')

    async def load_labels(self, path):
        """ 
        원래 tensorflow api pb 파일에서 레이블을 로드하고 정수를 사용하여 dict에 매핑합니다 (예 : 1 = aeroplane).
        """
        label_map = label_map_util.load_labelmap(path) # tensor의 레이블
        categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=self._num_classes,
                                                                    use_display_name=True) 
        category_index = label_map_util.create_category_index(categories)
        return category_index

    # image 가져와서 n*n*3 numpy 배열로 반환
    async def load_image_into_numpy_array(self, path, scale = 1.0):
        image = Image.open(path) #PIL 라이브러리로 이미지 올림
        image = image.resize(tuple(int(scale * dim) for dim in image.size)) # 이미지 사이즈에 디멘션을 scale곱해서 늘려주거나 줄여줌
        (im_width, im_height) = image.size
        return np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8) #왜 3차원 배열? RGB값이 들어가니까
    
    # image에서 객체 검출
    async def detect(self,image):
        # 모델이 이미지의 모양을 예상하므로 치수 확장 : [1, None, None, 3]
        image_np_expanded = np.expand_dims(image, axis=0)
        # 검출
        (self._boxes, self._scores, self._classes, num) = self._session.run(
            [self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],
            feed_dict={self.image_tensor: image_np_expanded})
        return self._boxes, self._scores, self._classes, self._num

    @property
    def labels(self):
        return self._labels

    def close(self):
        self._session.close()   

if __name__=='__main__':
    ip = ImageProcessor()
    ip.unzip(r'C:\Users\multicampus\git\s03p23a201\backend\mydiary\drawing\drawingControl\downloads\detection_models\ssd_mobilenet_v1_coco_2018_01_28')