<template>
  <div @click="closeBook" ref="home" class="home">
    <div class="audio">
      <audio autoplay controls loop> <source src="강아지같아.mp3" type="audio/mp3"> </audio>
    </div>
    <div class="container">
      <div class="component">
        <figure @click="openBook" ref="book" class="book first-page">
          <!-- Front -->

          <ul class="paperback_front">
            <li>
              <div class="back-space"></div>
              <span class="ribbon ribbon--color1"></span>
              <div class="front-wrap">
                <img :src="`/imgs/bookcovers/${theme}.gif`" width="100%" height="100%" />
                <div class="front-title"><img src="front-title.png" /></div>
              </div>
            </li>
            <li></li>
          </ul>

          <!-- Pages -->

          <ul class="ruled_paper">
            <li>
              <!-- 안 쓰는 페이지 임, 근데 지우면 안 댐  -->
            </li>
            <li>
              <bookmark
                pageNumber="3"
                text="꾸미기"
                color="white"
                backgroundColor="#7aa3e6"
                top="170px"
              />
              <decoration-background />
            </li>
            <li>
              <div class="back-space">
                <decoration-cover />
              </div>
              <bookmark
                pageNumber="2"
                text="달력"
                color="white"
                backgroundColor="#77c9c2"
                top="120px"
              />
              <calendar />
            </li>
            <li>
              <div class="back-space">
                <diary-detail />
              </div>
              <bookmark
                pageNumber="1"
                text="일기 쓰기"
                color="white"
                backgroundColor="pink"
                top="70px"
              />
               <writing />
            </li>
            <li v-if="this.$session.has('user_id')">
              <div class="back-space">
                <word-extract />
              </div>
              <bookmark
                pageNumber="0"
                text="내 정보"
                color="white"
                backgroundColor="#e0a951"
                top="20px"
              />
              <profile v-if="!editProfileFlag" />
              <profile-edit v-else />
            </li>
            <li v-else>
              <div class="back-space">
                <word-extract />
              </div>
              <bookmark
                pageNumber="0"
                text="로그인"
                color="white"
                backgroundColor="#e0a951"
                top="20px"
              />
              <sign-up v-if="signupFlag" />
              <login v-else />
            </li>
            <li>
              <!-- 안 쓰는 페이지 임, 근데 지우면 안 댐 -->
            </li>
          </ul>

          <!-- Back -->

          <ul class="paperback_back">
            <li style="background-color:white"></li>
            <li style="background-color:white"></li>
          </ul>
        </figure>
      </div>
    </div>

    <!-- 선택 모달 -->
    <select-modal v-if="showModal" />

    <!-- 이미지 선택 모달 -->
    <file-modal v-if="fileModal" />
  </div>
</template>

<script>
import Bookmark from "@/components/Bookmark.vue";
import Writing from "@/components/Writing.vue";
import Calendar from "@/components/Calendar.vue";
import DiaryDetail from "@/components/DiaryDetail.vue";
import Login from '@/components/Login.vue';
import SignUp from '@/components/Signup.vue';
import Profile from "@/components/Profile.vue";
import ProfileEdit from '@/components/ProfileEdit.vue';
import DecorationBackground from '@/components/DecorationBackground.vue';
import DecorationCover from '@/components/DecorationCover.vue';
import SelectModal from '@/components/modals/SelectModal.vue';
import FileModal from '@/components/modals/FileModal.vue';
import WordExtract from '@/components/WordExtract.vue';
import store from '@/store/index';
import api from '@/utils/api';

export default {
  name: "Home",
  data() {
    return {
      theme: '1',
    };
  },
  components: {
    Bookmark,
    Writing,
    Calendar,
    DiaryDetail,
    Login,
    SignUp,
    Profile,
    ProfileEdit,
    DecorationBackground,
    DecorationCover,
    SelectModal,
    FileModal,
    WordExtract,
  },
  computed: {
    showModal: () => store.getters['windowStore/GET_SM'],
    fileModal: () => store.getters['windowStore/GET_FM'],
    signupFlag: () => store.getters['userStore/GET_FLAG'],
    editProfileFlag: () => store.getters['userStore/GET_EDITFLAG'],
    words: () => store.getters['diaryStore/GET_WORDS'],
  },
  created() {
    if (this.$session.has('user_id')) {
      api.get(`account/${this.$session.get('user_id')}/`)
        .then(({ data }) => {
          this.theme = data.theme;
        });
    }
  },
  methods: {
    moveTo() {
      this.$router.push("/diary");
    },
    openBook() {
      this.$refs.book.classList.add("book--opened");
    },
    closeBook(e) {
      if (e.target !== this.$refs.home) return;

      this.$refs.book.classList.remove("book--opened");
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../style/book.scss";

.home {
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 100vw;
  min-height: 100vh;
}

 .audio{
      position: absolute;
      top: 5%;
      left: 80%;
    }
</style>
