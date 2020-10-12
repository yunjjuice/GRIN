<template>
  <div id="app">
    <router-view></router-view>
    <spinner class="middle" v-if="spinnerFlag" />
    <emotion-spinner class="middle" v-if="emotionSpinnerFlag" />
  </div>
</template>

<script>
import store from '@/store/index';

export default {
  data() {
    return {
      bgImg: '1',
      backgroundBasePath: "/imgs/backgrounds/",
      load: true,
    };
  },
  components: {
    Spinner: () => import('@/components/Spinner.vue'),
    EmotionSpinner: () => import('@/components/EmotionSpinner.vue'),
  },
  updated() {
    const app = document.querySelector("#app");
    if (this.$cookies.isKey('bgImg')) {
      this.bgImg = this.$cookies.get('bgImg');
    }
    const imgPath = `url("${this.backgroundBasePath}${this.bgImg}.png")`;
    app.style.backgroundImage = imgPath;
  },
  computed: {
    spinnerFlag: () => store.getters['windowStore/GET_SPIN'],
    emotionSpinnerFlag: () => store.getters['windowStore/GET_EMOTION_SPIN'],
  },
};
</script>

<style lang="scss">
@import "./style/app.scss";

#app {
  overflow-y: hidden !important;
}

.middle {
  position: absolute;
  z-index: 300;
}
</style>
