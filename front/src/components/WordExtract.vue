<template>
  <div class="middle">
    <div v-show="words.length > 0" >
      <div class="word-group">
        <span>단어를 눌러 원하는 그림을 추가해주세요</span>
      </div>
      <button :class='randomButton()' @click="getImg('사람')">사람</button>
      <button v-for="word in words" :key="word" :class="randomButton()" @click="getImg(word)">{{ word }}</button>
    </div>
  </div>
</template>

<script>
import api from '@/utils/api';
import store from '@/store/index';
import EventBus from '@/utils/EventBus';

export default {
  data() {
    return {
      buttonStyle: ['dotted-thin', 'dashed-thin', 'lined-thin'],
    };
  },
  computed: {
    words: () => store.getters['diaryStore/GET_WORDS'],
  },
  methods: {
    async getImg(word) {
      let imagePath;
      store.dispatch('windowStore/ACT_SPIN', true);
      await api.get(`drawing/keyword/?keyword=${word}`)
        .then((res) => {
          console.log(res);
          imagePath = res.data.image_path;
        }).catch((err) => {
          console.log(err);
          this.$toast.error('그림을 가져오지 못했습니다');
        });
      const src = `http://j3a201.p.ssafy.io:8000${imagePath}`;
      store.dispatch('windowStore/ACT_SPIN', false);
      EventBus.$emit('addImg', src);
    },
    randomButton() {
      const num = Math.floor(Math.random() * 3);
      return this.buttonStyle[num];
    },
  },
};
</script>

<style lang="scss" scoped>
.middle {
  width: 90%;
  height: 80%;
  margin: 10% 5%;
  text-align: center;
}

.word-group {
  padding: 20px 0;
  margin: 20px 0;
}

span {
  font-family: 'GmarketSansMedium';
  font-size: 1.5rem;
}

// 버튼 디자인
@import url(https://fonts.googleapis.com/css?family=Patrick+Hand+SC);
*{
  box-sizing:border-box;
}

button {
  align-self: center;
  background: transparent;
  padding: 1rem 1.5rem;
  margin: 1rem;
  transition: all .5s ease;
  color: #41403E;
  font-size: 1.2rem;
  font-family: 'KyoboHand';
  cursor: pointer;
  letter-spacing: 2px;
  outline: none;
  box-shadow: 20px 38px 34px -26px hsla(0,0%,0%,.2);
  border-radius: 255px 15px 225px 15px/15px 225px 15px 255px;
  /*
  Above is shorthand for:
  border-top-left-radius: 255px 15px;
  border-top-right-radius: 15px 225px;
  border-bottom-right-radius: 225px 15px;
  border-bottom-left-radius:15px 255px;
  */
  &:hover{
    box-shadow:2px 8px 4px -6px hsla(0,0%,0%,.3);
  }
  &.lined-thick{
      border:solid 7px #41403E;
  }
  &.dotted-thick{
      border:dotted 5px #41403E;
  }
  &.dashed-thick{
    border:dashed 5px #41403E;
  }
    &.lined-thin{
      border:solid 2px #41403E;
  }
  &.dotted-thin{
      border:dotted 2px #41403E;
  }
  &.dashed-thin{
    border:dashed 2px #41403E;
  }
}

@media (max-width:620px){
  & button{
    align-self:center;
    margin-bottom:2rem;
  }
}
</style>
