<template>
  <div class="decoration">
    <div class="decoration__book-cover">
      <h1>책 커버</h1>
      <div class="grid">
        <template v-for="index in bookCoverNum">
          <div @click="changeBookCover" :key="index" class="cell">
            <img :src="bookCoverBasePath + index + '.gif'" :alt="index" />
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/utils/api';

export default {
  data() {
    return {
      bookCoverBasePath: "/imgs/bookcovers/",
      bookCoverRibbonColors: ["#EEADDA", "#EEDFE0", "#fff5fc"],
      bookCoverColors: ["white", "#9E6B6D", "#FFF2FC", "#727272", "#c3fffc", "#FDF5D3", "#808e97", "#FEF5C6", "#FE9C70", "#bfa8f8"],
      bookCoverNum: 11,
    };
  },
  methods: {
    changeBookCover(e) {
      const cur = e.currentTarget;
      const paperbackFront = document.querySelector(".paperback_front");
      const selectedCover = cur.querySelector("img").getAttribute("alt");
      const coverImgPath = `${this.bookCoverBasePath}${selectedCover}.gif`;

      if (this.$session.has('user_id')) {
        api.put(`account/${this.$session.get('user_id')}/`, {
          theme: selectedCover,
        }).catch((err) => {
          console.log(err);
          this.$toast.error('커버 업데이트 실패');
        });
      }

      // 커버 이미지
      paperbackFront.querySelector("img").src = coverImgPath;

      // 리본색
      const ribbon = paperbackFront.querySelector(".ribbon");
      for (let i = 1; i <= this.bookCoverNum; i += 1) {
        ribbon.classList.remove(`ribbon--color${i}`);
      }
      ribbon.classList.add(`ribbon--color${selectedCover}`);

      // 뒷쪽색 왼쪽
      const backSpace = paperbackFront.querySelector(".back-space");
      backSpace.style.backgroundColor = this.bookCoverColors[selectedCover - 1];

      // 뒷쪽색 오른쪽
      const paperbackBack = document.querySelector(".paperback_back");
      const li = paperbackBack.querySelectorAll("li");
      li[1].style.backgroundColor = this.bookCoverColors[selectedCover - 1];
    },
  },
};
</script>

<style lang="scss" scoped>
@import "@/style/decoration.scss";
</style>
