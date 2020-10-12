<template>
  <div class="decoration">
    <div class="decoration__background">
      <h1>배경</h1>
      <div class="grid">
        <template v-for="index in backgroundNum">
          <div @click="changeBackground" :key="index" class="cell">
            <img :src="backgroundBasePath + index + '.png'" :alt="index" />
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      backgroundBasePath: "/imgs/backgrounds/",
      backgroundNum: 7,
    };
  },
  methods: {
    changeBackground(e) {
      const img = e.currentTarget.querySelector("img");
      const cur = img.getAttribute("alt");
      const app = document.querySelector("#app");
      const imgPath = `url("${this.backgroundBasePath}${cur}.png")`;
      this.$cookies.set('bgImg', cur);
      app.style.backgroundImage = imgPath;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "@/style/decoration.scss";
</style>
