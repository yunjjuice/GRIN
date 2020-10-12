<template>
  <div ref="bookmark" class="bookmark" @click="movePage">
    <div class="bookmark--start"></div>
    <div ref="bookmarkEnd" class="bookmark--end">{{text}}</div>
  </div>
</template>

<script>
export default {
  props: ["pageNumber", "text", "color", "backgroundColor", "top"],
  data() {
    return {
      classList: ["first-page", "second-page", "third-page", "fourth-page"],
    };
  },
  mounted() {
    const bookmarkEnd = this.$refs.bookmarkEnd.style;
    const bookmark = this.$refs.bookmark.style;
    bookmarkEnd.color = this.color;
    bookmarkEnd.backgroundColor = this.backgroundColor;
    bookmark.top = this.top;
  },
  methods: {
    movePage() {
      const curPageClass = this.classList[this.pageNumber];
      const book = document.querySelector(".book");
      this.classList.forEach((elem) => {
        book.classList.remove(elem);
      });
      book.classList.add(curPageClass);
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../style/bookmark.scss";
</style>
