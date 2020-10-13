<template>
    <canvas ref="canvas" width="443" height="307" @mousemove="draw" @mousedown="beginDrawing" @mouseup="stopDrawing"></canvas>
</template>

<script>
export default {
  data() {
    return {
      canvas: null,
      ctx: undefined,
      x: 0,
      y: 0,
      isDrawing: false,
    };
  },
  mounted() {
    this.canvas = this.$refs.canvas;
    this.ctx = this.canvas.getContext("2d");
    // context.lineWidth = 2; // 선 굵기를 2로 설정
    this.ctx.strokeStyle = "blue";
    // 마우스 리스너 등록. e는 MouseEvent 객체
    // this.canvas.addEventListener("mousemove", function (e) { move(e) }, false);
    // this.canvas.addEventListener("mousedown", function (e) { down(e) }, false);
    // this.canvas.addEventListener("mouseup", function (e) { up(e) }, false);
    // this.canvas.addEventListener("mouseout", function (e) { out(e) }, false);
  },
  methods: {
    drawLine(x1, y1, x2, y2) {
      this.ctx.beginPath();
      this.ctx.strokeStyle = 'black';
      this.ctx.lineWidth = 1;
      this.ctx.moveTo(x1, y1);
      this.ctx.lineTo(x2, y2);
      this.ctx.stroke();
      this.ctx.closePath();
    },
    draw(e) {
      if (this.isDrawing) {
        this.drawLine(this.x, this.y, e.offsetX, e.offsetY);
        this.x = e.offsetX;
        this.y = e.offsetY;
      }
    },
    beginDrawing(e) {
      this.x = e.offsetX;
      this.y = e.offsetY;
      this.isDrawing = true;
    },
    stopDrawing(e) {
      if (this.isDrawing) {
        this.drawLine(this.x, this.y, e.offsetX, e.offsetY);
        this.x = 0;
        this.y = 0;
        this.isDrawing = false;
      }
    },
    // down(e) {
    //     startX = e.offsetX; startY = e.offsetY;
    //     drawing = true;
    // },
    // up(e) { drawing = false; },
    // move(e) {
    //     if(!drawing) return; // 마우스가 눌러지지 않았으면 리턴
    //     var curX = e.offsetX, curY = e.offsetY;
    //     draw(curX, curY);
    //     startX = curX; startY = curY;
    // },
    // out(e) { drawing = false; },
  },
};
</script>

<style>

</style>
