import numpy as np
import sys
import gizeh as gz
import random
from PIL import Image
class SketchGizeh(object):

    def __init__(self):
        self._surface = None

    async def setup(self, width=300, height=300, bg_color=(1, 1, 1)):
        self._width = width
        self._height = height
        self._surface = gz.Surface(width=width, height=height, bg_color=bg_color)

    async def draw(self, pic_to_drawing, strokes, scale=1.0, pos=[0.5, 0.5], stroke_width=6, color=[0, 0, 0]):
        """획 목록을 반복하여 캔버스에 그립니다.
        pos는 (0,1) 범위에서 정규화 된 좌표입니다.
        """
        if scale <= 0:
            return
        try:
            for val in pos:
                if val < 0 or val > 1 or not isinstance(val, float):
                    raise ValueError('위치 좌표는 (0,1) 정수 사이이어야한다')
            scale *= np.mean([self._width, self._height]) / 255 # 전체 성분의 평균 계산하고 / 255
            if pic_to_drawing : 
                pos[0] = pos[0] * self._width - (scale * (255/2 ))
                pos[1] = pos[1] * self._height - (scale * (255/2 ))
            lines = self._convert_quickdraw_strokes_to_gizeh_group(strokes, color, stroke_width=stroke_width / scale)
            lines = lines.scale(scale).translate(xy=pos)
            lines.draw(self._surface)
            
        except ValueError as e:
            print(repr(e))

    async def draw_person(self, dataset, scale=1.0, position=[0.5, 0.5], stroke_width=6):
        body_parts = {'face': [0, 0], 't-shirt': [0, 250], 'pants': [0, 480]}  # dict of parts + translation
        gz_body_parts = []
        for name, pos in body_parts.items():
            strokes = dataset.get_drawing(name, random.randint(1, 1000))
            strokes_gz = self._convert_quickdraw_strokes_to_gizeh_group(strokes, stroke_width=stroke_width / scale)
            strokes_gz = strokes_gz.translate(pos)
            gz_body_parts.append(strokes_gz)
        scale *= np.mean([self._width, self._height]) / 750
        pos[0] = position[0] * self._width - (scale * (255 / 2))
        pos[1] = position[1] * self._height - (scale * (750 / 2))
        gz_body_parts = gz.Group(gz_body_parts).scale(scale).translate(xy=pos)
        gz_body_parts.draw(self._surface)

    async def remove_bg(self, image):
        img = Image.open(image)
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            if item[0] > 200 and item[1] > 200 and item[2] > 200:
                newData.append((item[0], item[1], item[2], 0))
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(image)

    def _convert_quickdraw_strokes_to_gizeh_group(self, strokes, color=[0, 0, 0], stroke_width=5):
        lines_list = []
        for stroke in strokes:
            x, y = stroke
            points = list(zip(x, y))
            line = gz.polyline(points=points, stroke=color, stroke_width=stroke_width)
            lines_list.append(line)
        return gz.Group(lines_list)

    async def draw_object_recognition_results(self, boxes, classes, scores, labels, dataset, threshold=0.5):
        """draw results of object recognition
        :return: list of objects drawn to the canvas
        """
        drawn_objects = []  # list of the objects drawn
        for i in range(boxes.shape[0]):
            if scores is None or scores[i] >= threshold:
                box = tuple(boxes[i].tolist())
                if classes[i] in labels.keys():
                    class_name = labels[classes[i]]['name']
                    drawn_objects.append(class_name)
                else:
                    raise ValueError('no label for index {}'.format(i))
                ymin, xmin, ymax, xmax = box
                centre = [np.mean([xmin, xmax]), np.mean([ymin, ymax])]
                size = np.mean([xmax - xmin, ymax - ymin])
                print('centre: {}, szie : {}'.format(centre,size))
                if size == 0.0 :
                    continue
                if class_name == 'person':
                    await self.draw_person(dataset, scale=ymax - ymin, position=centre)
                else:
                    drawing = dataset.get_drawing(class_name, random.randint(1, 1000))
                    await self.draw(True, drawing, scale=size, pos=centre)
        return drawn_objects

    async def draw_object_label(self, label, dataset) :
        if label == 'person':
            self.setup(100,300)
            await self.draw_person(dataset)
        else:
            drawing = dataset.get_drawing(label,random.randint(1, 1000))
            xlist = []
            ylist = []
            for line in drawing: 
                x,y = line
                xlist+=list(x)
                ylist+=list(y)
            xmin = min(xlist)
            xmax = max(xlist)
            ymin = min(ylist)
            ymax = max(ylist)
            self.setup(xmax+100, ymax+100)
            print(xmax,xmin,ymax,ymin)
            #centre = [np.mean([xmin, xmax])/255, np.mean([ymin, ymax])/255]
            centre = [(xmax/4)/255,(ymax/4)/255]
            await self.draw(False, drawing, 1.0, centre)


    def get_npimage(self):
        return self._surface.get_npimage()

    async def save_png(self, path):
        self._surface.write_to_png(str(path))
        await self.remove_bg(str(path))




