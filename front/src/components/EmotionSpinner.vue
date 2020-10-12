<template>
<div class="overlay">

<div v-if="this.showEmotion" >
  <div class="emotion-string">
<span class = "font__se-han">당신의 감정은 <strong>{{emotion}}</strong>입니다</span>
</div>
<img :src="iconUrl" />
</div>
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
  background-color: white;
  border-radius: 5px;
  height : 50px;
}

span{
  padding-left: 100px;
  text-align: center;
  font-size: 40px;
  size : 20px;
}
</style>
