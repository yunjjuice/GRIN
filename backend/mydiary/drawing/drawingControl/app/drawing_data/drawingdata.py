import six.moves.urllib as urllib
import struct
from struct import unpack
from pathlib import Path
import jsonlines
import random
import logging
root = Path(__file__).parent
# 그림 데이터 set에 대한 인터페이스

# run.py 에서 객체 초기화
# dataset = DrawingDataset(str(root / 'downloads/drawing_dataset'),
#  str(root / 'app/label_mapping.jsonl'))
class DrawingData(object):
    def __init__(self, path_to_drawing_dataset, path_to_label_mapping):
        self._path = Path(path_to_drawing_dataset)
        self._categories_filepath = self._path / 'categories.txt' # 카테고리 저장시킬 경로
        self._category_mapping_filepath = path_to_label_mapping # 매핑시킬 정보들이 들어있는 jsonl
        self._quickdraw_dataset_url = 'https://storage.googleapis.com/quickdraw_dataset/full/binary/' # 이미지 가져올 url
        self._categories = [] # 카테고리들 가져올 배열
        self._category_mapping = dict() # 카테고리와 매핑 값들
        self._logger = logging.getLogger(self.__class__.__name__) # 자기 클래스 이름의 logger갖고옴
    
    async def setup(self):
        # 이미 download.py에 구현되어 있는 카테고리와 이름 매칭
        try :
            with jsonlines.open(self._category_mapping_filepath, mode = 'r') as reader:
                self._category_mapping = reader.read() 
        except IOError as e:
            self._logger.exception(e)
            print('label_mapping.jsonl not found')
            raise e
        self.categories = self.load_categories(self._path)
        if not self._categories: # 다운이 안되어서 bin이 없을 때 다운 받기
            self.download_recurse(self._quickdraw_dataset_url, self._path)
            self._categories = self.load_categories(self._path)


    # dataset의 바이너리 파일들 목록 가져와서 카테고리목록 만듬
    def load_categories(self, path): 
        files = Path(path).glob('*.bin')
        categories = [f.stem for f in files] # bin 빼고 카테고리화 만들게
        return categories
    
    def download(self, url, filename, path):
        """download file @ specified url and save it to path
        """
        # if not Path(path).exists():
        #     Path(path).mkdir()
        # fpath = Path(path) / filename
        # opener = urllib.request.URLopener()
        # opener.retrieve(url, str(fpath))
        # return fpath

    # url에서 quick dataset에서 이미지 바이너리 파일 다운 받기
    def download_recurse(self, url, path):
        path = Path(path)
        # with open(str(self._categories_filepath)) as f:
        #     categories = f.readlines()
        # categories = [cat.strip() for cat in categories] #strip 앞뒤 공백 \n 없애준다.
        # for cat in categories:
        #     site = url + cat.replace(' ', '%20') + '.bin'
        #     fpath = self.download(site, cat + '.bin', path)
        #     print('downloaded: {} from {}'.format(fpath, site))

    def _unpack_drawing(self, file_handle):
        """GOOGLE 그림 데이터셋 바이러니 파일들에서 한개의 이미지만 압축 품
        """
        key_id, = unpack('Q', file_handle.read(8))
        countrycode, = unpack('2s', file_handle.read(2))
        recognized, = unpack('b', file_handle.read(1))
        timestamp, = unpack('I', file_handle.read(4))
        n_strokes, = unpack('H', file_handle.read(2))
        image = []
        for i in range(n_strokes):
            n_points, = unpack('H', file_handle.read(2))
            fmt = str(n_points) + 'B'
            x = unpack(fmt, file_handle.read(n_points))
            y = unpack(fmt, file_handle.read(n_points))
            image.append((x, y))

        return {
            'key_id': key_id,
            'countrycode': countrycode,
            'recognized': recognized,
            'timestamp': timestamp,
            'image': image
        }

    def unpack_drawings(self, path):
        """바이너리 파일로부터 모든 그림 읽어오고 생성자 retrun
        """
        with open(path, 'rb') as f:
            while True:
                try:
                    yield self._unpack_drawing(f)
                except struct.error:
                    break

    def get_drawing(self, name, index): # 이름, 랜덤
        """이름과 색인으로 그림 가져 오기 (예 : 100 번째 'pelican')
        """
        try:
            if name not in self._categories:
                # try and get the closest matching drawing. If nothing suitable foumd then return a scorpion
                name = self._category_mapping.get(name, 'scorpion')
            if index < 1 or not isinstance(index, int):
                raise ValueError('index must be integer > 0')
            itr = self.unpack_drawings(str(self._path / Path(name).with_suffix('.bin')))
            for i in range(index):
                drawing = next(itr)
            return drawing['image']
        except ValueError as e:
            self.log.exception(e)
            raise e

if __name__=='__main__':
    print(root)
    dataset = DrawingData(str('backend/mydiary/drawing/downloads/drawing_dataset'), str('backend/mydiary/drawing/label_mapping.jsonl'))
    dataset.setup()
    drawing = dataset.get_drawing('cat',random.randint(1, 1000))
    with open('./drawingTest', 'w') as f :
        for item in drawing:
            f.write(str(item))
        