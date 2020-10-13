<template>
   <canvas ref="canvas" width="443" height="307"></canvas>
</template>

<script>
export default {
  created() {
    var canvas = document.getElementById("myCanvas");
    var context = canvas.getContext("2d");

    context.lineWidth = 2; // 선 굵기를 2로 설정
    context.strokeStyle = "blue";

    // 마우스 리스너 등록. e는 MouseEvent 객체
    canvas.addEventListener("mousemove", function (e) { move(e) }, false);
    canvas.addEventListener("mousedown", function (e) { down(e) }, false);
    canvas.addEventListener("mouseup", function (e) { up(e) }, false);
    canvas.addEventListener("mouseout", function (e) { out(e) }, false);
  },
  methods: {
    draw(curX, curY) {
      context.beginPath();
      context.moveTo(startX, startY);
      context.lineTo(curX, curY);
      context.stroke();
    },
    down(e) {
        startX = e.offsetX; startY = e.offsetY;
        drawing = true;
    },
    up(e) { drawing = false; },
    move(e) {
        if(!drawing) return; // 마우스가 눌러지지 않았으면 리턴
        var curX = e.offsetX, curY = e.offsetY;
        draw(curX, curY);
        startX = curX; startY = curY;
    },
    out(e) { drawing = false; },
  },
}
</script>

<style>

</style>
