<template>
  <canvas id = "background" ref="canvas" width="443" height="307"></canvas>
  <canvas id = "newcan" ref="canvas" width="443" height="307"></canvas>
</template>

<script>
import EventBus from '@/utils/EventBus';

class ImageInfo {
  constructor(x, y, width, height, img) {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    this.img = img;
  }
}
const STATE = {
  NONE: 0, IMAGE: 1, CIRCLE_LT: 2, CIRCLE_RT: 3, CIRCLE_RB: 4, CIRCLE_LB: 5, DELETE_IMG: 6,
};
const PIVOT_CIRCLE_RADIUS = 5;
export default {
  data() {
    return {
      cursorPos: STATE.NONE,
      hoveredImg: undefined,
      selectedImg: undefined,
      prevMouseX: undefined,
      prevMouseY: undefined,
      isMouseDown: false,
      imgs: [],
      imageInfos: [],
      canvas: undefined,
      canvasD: undefined,
      ctx: undefined,
      loadCount: 0,
      x: 0,
      y: 0,
      isDrawing: false,
      drawingImage: {
        sx: Number.MAX_VALUE,
        sy: Number.MAX_VALUE,
        dx: 0,
        dy: 0,
      },
    };
  },
  created() {
    EventBus.$on('addImg', (payload) => {
      // console.log('event on', payload);
      this.imgs[this.loadCount] = new Image();
      this.imgs[this.loadCount].src = payload;
      // console.log('src', this.imgs[this.loadCount].src);
      this.imgs[this.loadCount].crossOrigin = "Anonymous";
      this.imgs[this.loadCount].onload = () => {
        this.draw(this.imgs);
        this.loadCount += 1;
      };
    });
  },
  props: {
    grimMode: {
      default: false,
    },
  },
  watch: {
    grimMode() {
      console.log(this.grimMode);
      this.canvas = this.$refs.canvas;
      this.ctx = this.canvas.getContext("2d");
      if (this.grimMode) {
        this.canvas.removeEventListener("mousedown", this.handleMouseDown);
        this.canvas.removeEventListener("mousemove", this.handleMouseMove);
        document.removeEventListener("mouseup", this.handleMouseUp);
        this.canvas.addEventListener("mousedown", this.beginDrawing);
        this.canvas.addEventListener("mousemove", this.drawing);
        document.addEventListener("mouseup", this.stopDrawing);
      } else {
        this.canvas.removeEventListener("mousedown", this.beginDrawing);
        this.canvas.removeEventListener("mousemove", this.drawing);
        document.removeEventListener("mouseup", this.stopDrawing);
        this.canvas.addEventListener("mousedown", this.handleMouseDown);
        this.canvas.addEventListener("mousemove", this.handleMouseMove);
        document.addEventListener("mouseup", this.handleMouseUp);
      }
    },
  },
  methods: {
    handleMouseMove(e) {
      const canvasRect = this.canvas.getBoundingClientRect();
      const x = e.clientX - canvasRect.left;
      const y = e.clientY - canvasRect.top;
      this.updateCursorState(x, y);
      this.updateCursorIcon();
      this.dragImage(x, y);
      this.scaleImage(x, y);
    },
    handleMouseDown() {
      this.isMouseDown = true;
      this.selectedImg = this.hoveredImg;
      this.deleteImage();
      this.updateCursorIcon();
      this.render();
    },
    handleMouseUp() {
      this.isMouseDown = false;
      this.selectedImg = undefined;
      this.prevMouseX = undefined;
      this.prevMouseY = undefined;
      this.updateCursorIcon();
    },
    scaleImage(x, y) {
      if (this.selectedImg === undefined || this.cursorPos < STATE.CIRCLE_LT || this.cursorPos > STATE.CIRCLE_LB) {
        return;
      }
      if (this.prevMouseX === undefined || this.prevMouseY === undefined) {
        this.prevMouseX = x;
        this.prevMouseY = y;
      } else {
        const dx = x - this.prevMouseX;
        const dy = y - this.prevMouseY;
        this.prevMouseX = x;
        this.prevMouseY = y;

        const imgInfo = this.selectedImg;
        switch (this.cursorPos) {
          case STATE.CIRCLE_LT:
            this.resizeImage(imgInfo, x, y, -dx, -dy);
            break;
          case STATE.CIRCLE_RT:
            this.resizeImage(imgInfo, imgInfo.x, y, dx, -dy);
            break;
          case STATE.CIRCLE_RB:
            this.resizeImage(imgInfo, imgInfo.x, imgInfo.y, dx, dy);
            break;
          case STATE.CIRCLE_LB:
            this.resizeImage(imgInfo, x, imgInfo.y, -dx, dy);
            break;
          case STATE.DELETE_IMG:
            this.deleteImage(imgInfo);
            break;
          default:
        }
      }
      this.render();
    },
    dragImage(x, y) {
      if (this.selectedImg === undefined || this.cursorPos !== STATE.IMAGE) {
        return;
      }
      if (this.prevMouseX === undefined || this.prevMouseY === undefined) {
        this.prevMouseX = x;
        this.prevMouseY = y;
      } else {
        const dx = x - this.prevMouseX;
        const dy = y - this.prevMouseY;
        this.prevMouseX = x;
        this.prevMouseY = y;

        this.moveImage(this.selectedImg, dx, dy);
      }
      this.render();
    },
    updateCursorIcon() {
      switch (this.cursorPos) {
        case STATE.CIRCLE_LT:
        case STATE.CIRCLE_RB:
        case STATE.CIRCLE_RT:
        case STATE.CIRCLE_LB:
        case STATE.DELETE_IMG:
          this.canvas.style.cursor = "all-scroll";
          break;
        case STATE.IMAGE:
          this.canvas.style.cursor = "grab";
          if (this.selectedImg !== undefined) {
            this.canvas.style.cursor = "grabbing";
          }
          break;
        // case STATE.DELETE_IMG:
        //   this.deleteImage();
        //   break;
        default:
          this.canvas.style.cursor = "default";
          break;
      }
    },
    updateCursorState(x, y) {
      if (this.isMouseDown) {
        return;
      }
      this.cursorPos = STATE.NONE;
      this.hoveredImg = undefined;
      for (let i = 0; i < this.imageInfos.length; i += 1) {
        const img = this.imageInfos[i];
        let left = img.x;
        let right = img.x + img.width;
        let top = img.y;
        let bottom = img.y + img.height;

        if (left > right) {
          const temp = left;
          left = right;
          right = temp;
        }
        if (top > bottom) {
          const temp = top;
          top = bottom;
          bottom = temp;
        }

        if (
          x >= left
          && x < right
          && y >= top
          && y < bottom
        ) {
          this.hoveredImg = img;
          this.cursorPos = STATE.IMAGE;
        }

        let circleX = img.x - PIVOT_CIRCLE_RADIUS * 1.5;
        let circleY = img.y - PIVOT_CIRCLE_RADIUS * 1.5;
        const PIVOT_CIRCLE_RADIUS2 = PIVOT_CIRCLE_RADIUS * 3;
        // 좌상
        if (x >= circleX && x < circleX + PIVOT_CIRCLE_RADIUS2
        && y >= circleY && y < circleY + PIVOT_CIRCLE_RADIUS2) {
          this.hoveredImg = img;
          this.cursorPos = STATE.CIRCLE_LT;
          break;
        }
        // 우상
        circleX += img.width;
        if (x >= circleX && x < circleX + PIVOT_CIRCLE_RADIUS2
        && y >= circleY && y < circleY + PIVOT_CIRCLE_RADIUS2) {
          this.hoveredImg = img;
          this.cursorPos = STATE.CIRCLE_RT;
          break;
        }
        // 우하
        circleY += img.height;
        if (x >= circleX && x < circleX + PIVOT_CIRCLE_RADIUS2
        && y >= circleY && y < circleY + PIVOT_CIRCLE_RADIUS2) {
          this.hoveredImg = img;
          this.cursorPos = STATE.CIRCLE_RB;
          break;
        }
        // 좌하
        circleX -= img.width;
        if (x >= circleX && x < circleX + PIVOT_CIRCLE_RADIUS2
        && y >= circleY && y < circleY + PIVOT_CIRCLE_RADIUS2) {
          this.hoveredImg = img;
          this.cursorPos = STATE.CIRCLE_LB;
          break;
        }
        circleX += img.width / 2;
        if (x >= circleX && x < circleX + PIVOT_CIRCLE_RADIUS2
        && y >= circleY && y < circleY + PIVOT_CIRCLE_RADIUS2) {
          this.hoveredImg = img;
          this.cursorPos = STATE.DELETE_IMG;
          break;
        }
      }
    },
    render() {
      this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
      for (let i = 0; i < this.imageInfos.length; i += 1) {
        const info = this.imageInfos[i];

        if (info !== this.selectedImg) {
          this.ctx.drawImage(info.img, info.x, info.y, info.width, info.height);
        }
      }
      const sel = this.selectedImg;
      if (sel !== undefined) {
        this.ctx.drawImage(sel.img, sel.x, sel.y, sel.width, sel.height);

        this.ctx.strokeRect(sel.x, sel.y, sel.width, sel.height);

        const PI2 = 2 * Math.PI;
        this.ctx.beginPath();
        this.ctx.arc(sel.x, sel.y, PIVOT_CIRCLE_RADIUS, 0, PI2);
        this.ctx.moveTo(sel.x + sel.width, sel.y);
        this.ctx.arc(sel.x + sel.width, sel.y, PIVOT_CIRCLE_RADIUS, 0, PI2);
        this.ctx.moveTo(sel.x, sel.y + sel.height);
        this.ctx.arc(sel.x, sel.y + sel.height, PIVOT_CIRCLE_RADIUS, 0, PI2);
        this.ctx.moveTo(sel.x + sel.width, sel.y + sel.height);
        this.ctx.arc(sel.x + sel.width, sel.y + sel.height, PIVOT_CIRCLE_RADIUS, 0, PI2);
        this.ctx.fill();
        this.ctx.beginPath();
        this.ctx.moveTo((sel.x + sel.width / 2) + PIVOT_CIRCLE_RADIUS, sel.y + sel.height + PIVOT_CIRCLE_RADIUS);
        this.ctx.lineTo((sel.x + sel.width / 2) - PIVOT_CIRCLE_RADIUS, sel.y + sel.height - PIVOT_CIRCLE_RADIUS);
        this.ctx.moveTo((sel.x + sel.width / 2) - PIVOT_CIRCLE_RADIUS, sel.y + sel.height + PIVOT_CIRCLE_RADIUS);
        this.ctx.lineTo((sel.x + sel.width / 2) + PIVOT_CIRCLE_RADIUS, sel.y + sel.height - PIVOT_CIRCLE_RADIUS);
        this.ctx.closePath();
        this.ctx.stroke();
      }
    },
    imageLoad() {
      // let loadCount = 0;
      this.imgs[0] = new Image();
      this.imgs[0].src = "https://avatars0.githubusercontent.com/u/33210021?s=60&v=4";
      this.imgs[0].crossOrigin = "Anonymous";
      this.imgs[0].onload = () => {
        this.loadCount += 1;
        if (this.loadCount >= 2) {
          this.draw(this.imgs);
        }
      };

      this.imgs[1] = new Image();
      this.imgs[1].src = "https://yt3.ggpht.com/a-/AOh14GgCvbN3uY2qTNLziC8WwXyazvhSHsJV0312Fw=s68-c-k-c0x00ffffff-no-rj-mo";
      this.imgs[1].crossOrigin = "Anonymous";
      this.imgs[1].onload = () => {
        this.loadCount += 1;
        if (this.loadCount >= 2) {
          this.draw(this.imgs);
        }
      };
    },
    addImage(src) {
      this.imgs[this.loadCount] = new Image();
      this.images[this.loadCount].src = src;
      this.imgs[this.loadCount].crossOrigin = "Anonymous";
      this.imgs[this.loadCount].onload = () => {
        this.loadCount += 1;
        if (this.loadCount >= 2) {
          this.draw(this.imgs);
        }
      };
      this.loadCount += 1;
      this.draw(this.imgs);
    },
    draw(imgs) {
      const prevX = 0;
      const prevY = 0;
      this.canvas = this.$refs.canvas;
      this.ctx = this.canvas.getContext("2d");
      // for (let i = 0; i < imgs.length; i += 1) {
      //   this.ctx.drawImage(imgs[i], prevX, prevY, imgs[i].width, imgs[i].height);
      //   this.imageInfos[i] = new ImageInfo(
      //     prevX,
      //     prevY,
      //     imgs[i].width,
      //     imgs[i].height,
      //     imgs[i],
      //   );
      //   // prevX += imgs[i].width;
      //   imgs[i].style.display = "none";
      // }
      const index = this.loadCount;
      // console.log('index', index);
      // console.log('imgs', imgs[index]);
      this.ctx.drawImage(imgs[index], prevX, prevY, imgs[index].width, imgs[index].height);
      this.imageInfos[index] = new ImageInfo(
        prevX,
        prevY,
        imgs[index].width,
        imgs[index].height,
        imgs[index],
      );
      imgs[index].style.display = 'none';

      this.canvas.addEventListener("mousedown", this.handleMouseDown);
      this.canvas.addEventListener("mousemove", this.handleMouseMove);
      document.addEventListener("mouseup", this.handleMouseUp);
      this.render();
    },
    resizeImage(imageInfo, x, y, dx, dy) {
      imageInfo.x = x;
      imageInfo.y = y;
      imageInfo.width += dx;
      imageInfo.height += dy;
    },
    moveImage(imageInfo, dx, dy) {
      imageInfo.x += dx;
      imageInfo.y += dy;
      this.render();
    },
    deleteImage() {
      if (this.cursorPos !== STATE.DELETE_IMG) {
        return;
      }
      for (let i = 0; i < this.imageInfos.length; i += 1) {
        if (this.imageInfos[i] === this.selectedImg) {
          this.imageInfos.splice(i, 1);
          this.imgs.splice(i, 1);
          this.loadCount -= 1;
          break;
        }
      }
      this.render();
    },
    drawLine(x1, y1, x2, y2) {
      this.ctx.beginPath();
      this.ctx.strokeStyle = 'black';
      this.ctx.lineWidth = 1;
      this.ctx.moveTo(x1, y1);
      this.ctx.lineTo(x2, y2);
      this.ctx.closePath();
      this.ctx.stroke();
    },
    drawing(e) {
      if (this.isDrawing) {
        this.drawLine(this.x, this.y, e.offsetX, e.offsetY);
        console.log("xx ", e.offsetX);
        console.log("this.drawingImage.s ", this.drawingImage.sx);
        this.drawingImage.sx = Math.min(e.offsetX, this.drawingImage.sx);
        this.drawingImage.sy = Math.min(e.offsetY, this.drawingImage.sy);
        this.drawingImage.dx = Math.max(e.offsetX, this.drawingImage.dx);
        this.drawingImage.dy = Math.max(e.offsetY, this.drawingImage.dy);
        this.x = e.offsetX;
        this.y = e.offsetY;
      }
    },
    beginDrawing(e) {
      this.canvasD = document.createElement('canvas');
      this.canvasD.Zindex = 10;
      this.ctx = this.canvasD.getContext("2d");
      this.x = e.offsetX;
      this.y = e.offsetY;
      this.isDrawing = true;
    },
    stopDrawing(e) {
      const img = new Image();
      // const newImage = new Image();
      if (this.isDrawing) {
        this.drawLine(this.x, this.y, e.offsetX, e.offsetY);
        this.x = 0;
        this.y = 0;
        this.isDrawing = false;
        img.src = this.canvasD.toDataURL();
        img.onload = () => {
          const oCanvas = document.createElement('canvas');
          oCanvas.width = this.drawingImage.dx - this.drawingImage.sx;
          oCanvas.height = this.drawingImage.dy - this.drawingImage.sy;
          const oCtx = oCanvas.getContext('2d');
          oCtx.drawImage(img, this.drawingImage.sx, this.drawingImage.sy, oCanvas.width, oCanvas.height, 0, 0, oCanvas.width, oCanvas.height);
          console.log(oCanvas.toDataURL());
          console.log(this.loadCount);
          this.imgs[this.loadCount] = new Image();
          this.imgs[this.loadCount].src = oCanvas.toDataURL();
          this.imgs[this.loadCount].crossOrigin = "Anonymous";
          this.imageInfos[this.loadCount] = new ImageInfo(
            this.drawingImage.sx,
            this.drawingImage.sy,
            oCanvas.width,
            oCanvas.height,
            this.imgs[this.loadCount],
          );
          this.imgs[this.loadCount].style.display = 'none';
          this.loadCount += 1;
          this.drawingImage.sx = Number.MAX_VALUE;
          this.drawingImage.sy = Number.MAX_VALUE;
          this.drawingImage.dy = 0;
          this.drawingImage.dy = 0;
        };
        this.canvasD = undefined;
        console.log("ASD ", this.canvasD);
      }
      console.log(this.imgs);
      this.ctx = this.canvas.getContext("2d");
      img.src = this.canvas.toDataURL();
    },
  },
  // mounted() {
  //   this.imageLoad();
  // },
};
</script>

<style lang="scss" scoped>

</style>
