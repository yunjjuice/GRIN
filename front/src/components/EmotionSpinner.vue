<template>
<div class="overlay">

<div v-if="this.showEmotion" >
  <div class="emotion-string">
<span class = "font__se-han" >당신의 감정은 <strong>{{emotion}}</strong>입니다</span>
</div>
</div>
<img :src="iconUrl" class="box" v-if="tf"/>
<div id="steps" v-if="!this.showEmotion" v-bind:class="className"></div>
<!-- <div id="transition"></div> -->
</div>
</template>

<script>
import store from '@/store/index';

const emolist = ["기쁨", "슬픔", "화남", "중립"];
const emourllist = ["happy", "sad", "angry", "soso"];
export default {
  data() {
    return {
      //   class: 'test 0.5s infinite',
      tf: false,
      tf1: false,
      tf2: false,
      tf3: false,
      tf4: false,
      className: 'animation1',
      showEmotion: false,
      emotion: "",
      iconUrl: "",
    };
  },
  watch: {
    isExistEmotion: {
      async handler() {
        if (this.isExistEmotion) { // 감정분석이 끝났으면
          this.className = 'animation2'; // 속도 느리게
          await setTimeout(async () => { await this.setEmotion(); }, 3000);
          await setInterval(async () => { this.updateTransition(); }, 4000);
          await setTimeout(async () => { store.dispatch('windowStore/ACT_EXIST_EMOTION', false); store.dispatch('windowStore/ACT_EMOTION_SPIN', false); }, 8000);
        }
      },
    },
  },
  computed: {
    isExistEmotion: () => store.getters['windowStore/GET_EXIST_EMOTION'],
    getEmotion: () => store.getters['diaryStore/GET_EMO'],
  },
  methods: {
    setEmotion() {
      this.showEmotion = true;
      console.log(this.getEmotion);
      this.emotion = emolist[this.getEmotion]; // 감정 언어로 정해줌
      console.log(this.emotion);
      this.iconUrl = `/imgs/emotion/${emourllist[this.getEmotion]}.png`;
      this.tf = true;
      if (emourllist[this.getEmotion] === "happy") {
        this.tf1 = true;
      } else if (emourllist[this.getEmotion] === "sad") {
        this.tf2 = true;
      } else if (emourllist[this.getEmotion] === "angry") {
        this.tf3 = true;
      } else if (emourllist[this.getEmotion] === "soso") {
        this.tf4 = true;
      }
      // window.setTimeout(this.updateTransition(), 3000);
      // let el = document.querySelector("div.box");
      // if (el) {
      //   el.className = "box1";
      // } else {
      //   el = document.querySelector("div.box1");
      //   el.className = "box";
      // }
    },
    updateTransition() {
      let el = document.querySelector("img.box");
      if (el) {
        if (this.tf1) {
          el.className = "box1";
        } else if (this.tf2) {
          el.className = "box2";
        } else if (this.tf3) {
          el.className = "box3";
        } else if (this.tf4) {
          el.className = "box4";
        }
      } else if (!el) {
        if (this.tf1) {
          el = document.querySelector("img.box1");
          el.className = "box";
          this.tf1 = false;
        } else if (this.tf2) {
          el = document.querySelector("img.box2");
          el.className = "box";
          this.tf2 = false;
        } else if (this.tf3) {
          el = document.querySelector("img.box3");
          el.className = "box";
          this.tf3 = false;
        } else if (this.tf4) {
          el = document.querySelector("img.box4");
          el.className = "box";
          this.tf4 = false;
        }
      }
    },
  },
};
</script>

<style scoped>
@import url(http://fonts.googleapis.com/css?family=Indie+Flower);
@keyframes test{
    0%{
        background-image: url('/imgs/emotion/sad.png');
    }
    20%{
        background-image: url('/imgs/emotion/happy.png');
    }
    40%{
        background-image: url('/imgs/emotion/soso.png');
    }
    60%{
        background-image: url('/imgs/emotion/suprise.png');
    }
    80%{
        background-image: url('/imgs/emotion/angry.png');
    }
    100%{
        background-image: url('/imgs/emotion/sad.png');
    }
}

.animation1 {
    width: 350px;
    height: 250px;
    float: left;
    background-size: contain;
    background-position: 50% 50%;
    background-repeat: no-repeat;
    -webkit-animation: test 0.5s infinite;
            animation: test 0.5s infinite;
}
.animation2{
    width: 350px;
    height: 250px;
    float: left;
    background-size: contain;
    background-position: 50% 50%;
    background-repeat: no-repeat;
    -webkit-animation: test 1s infinite;
            animation: test 1s infinite;
}

#steps{
    -webkit-animation-timing-function: steps(1, end);
            animation-timing-function: steps(1, end);
}

.overlay {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  z-index: 30;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5);
}
.emotion-string{
  text-align: center;
  background-color: white;
  border-radius: 5px;
  height : 50px;
  left: 50%;
  top: 80%;
  /* position:absolute; */
}
.box {
    text-align: center;
    display: block; margin: 0px auto;
    width: 500px;
    height: 500px;
    /* background-color: red; */
    font-size: 20px;
    left: 37%;
    top: 25%;
    position:absolute;
    background-size: contain;
    background-position: 50% 50%;
    background-repeat: no-repeat;
    -webkit-transition-property: width height background-color font-size left top color;
    -webkit-transition-duration:2s;
    -webkit-transition-timing-function: ease;
    transition-property: width height background-color font-size left top color;
    transition-duration:2s;
    transition-timing-function: ease;
}
.box1{
    width: 50px;
    height: 50px;
    /* background-color: blue;
    color: yellow; */
    font-size: 18px;
    left: 59.9%;
    top: 13%;
    position:absolute;
    -webkit-transition-property: width height background-color font-size left top color;
    -webkit-transition-duration:2s;
    -webkit-transition-timing-function: ease;
    transition-property: width height background-color font-size left top color;
    transition-duration:2s;
    transition-timing-function: ease;
}
.box2{
    width: 50px;
    height: 50px;
    /* background-color: blue;
    color: yellow; */
    font-size: 18px;
    left: 62.2%;
    top: 13%;
    position:absolute;
    -webkit-transition-property: width height background-color font-size left top color;
    -webkit-transition-duration:2s;
    -webkit-transition-timing-function: ease;
    transition-property: width height background-color font-size left top color;
    transition-duration:2s;
    transition-timing-function: ease;
}
.box3{
    width: 50px;
    height: 50px;
    /* background-color: blue;
    color: yellow; */
    font-size: 18px;
    left: 64.5%;
    top: 13%;
    position:absolute;
    -webkit-transition-property: width height background-color font-size left top color;
    -webkit-transition-duration:2s;
    -webkit-transition-timing-function: ease;
    transition-property: width height background-color font-size left top color;
    transition-duration:2s;
    transition-timing-function: ease;
}
.box4{
    width: 50px;
    height: 50px;
    /* background-color: blue;
    color: yellow; */
    font-size: 18px;
    left: 67%;
    top: 13%;
    position:absolute;
    -webkit-transition-property: width height background-color font-size left top color;
    -webkit-transition-duration:2s;
    -webkit-transition-timing-function: ease;
    transition-property: width height background-color font-size left top color;
    transition-duration:2s;
    transition-timing-function: ease;
}
span{
  padding-left: 100px;
  text-align: center;
  font-size: 40px;
  size : 20px;
}
</style>
