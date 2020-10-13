<template>
  <div class="middle">
    <div class="profile">
      <div style="float: left; width: 40%;">
        <img class="fir-circle" :src="userInfo.profilePic">
      </div>
      <div class="info">
        <div>{{ userInfo.nickname }}</div>
        <div style="font-family: 'KyoboHand'">{{ getFormatDate(userInfo.birthdate) }}</div>
      </div>
    </div>
    <div style="clear: both;">
      <div class="group">
        <div style="font-family: 'GmarketSansMedium';">자기소개</div>
        <div class="sketchy">{{ userInfo.intro }}</div>
      </div>
      <div class="group">
        <div style="font-family: 'GmarketSansMedium';">감정리스트</div>
        <div class="sketchy">
          <img class="emotion" :src="emotionList[0]"/> : {{happy}}
          <img class="emotion" :src="emotionList[1]"/> : {{sad}}
          <img class="emotion" :src="emotionList[2]"/> : {{angry}}
          <img class="emotion" :src="emotionList[3]"/> : {{soso}}
        </div>
      </div>
    </div>
    <div style="text-align:center;">
      <button class="button--tertiary" @click="editProfile">프로필 수정</button>
      <button class="button--tertiary" @click="logout">로그아웃</button>
      <button class="button--tertiary" @click="deleteAccount">탈퇴</button>
    </div>
  </div>
</template>

<script>
import api from '@/utils/api';
import store from '@/store/index';
import moment from 'moment';

export default {
  data() {
    return {
      userInfo: {},
      happy: 0,
      sad: 0,
      angry: 0,
      soso: 0,
      emotionList: [
        'imgs/emotion/happy.png',
        'imgs/emotion/sad.png',
        'imgs/emotion/angry.png',
        'imgs/emotion/soso.png',
      ],
    };
  },
  created() {
    api.get(`account/${this.$session.get('user_id')}/`)
      .then(({ data }) => {
        // console.log(data);
        this.userInfo = data;
        if (data.profilePic == null) {
          this.userInfo.profilePic = 'https://lab.ssafy.com/s03-ai-sub3/s03p23a201/uploads/94342b2dc983157f5b3169b765af3da7/3F212117-1473-47F6-AD9F-531326117EAB-95867-00005C1428239F3C_file.jpg';
        } else {
          this.userInfo.profilePic = `http://j3a201.p.ssafy.io:8000${data.profilePic}`;
        }
      }).catch((err) => {
        console.log(err);
        this.$toast.errer('유저 정보 불러오기 실패');
      });
  },
  computed: {
    diaries: () => store.getters['diaryStore/GET_DIARIES'],
  },
  watch: {
    diaries(diarylist) {
      diarylist.forEach((diary) => {
        if (diary.emotion === 0) {
          this.happy += 1;
        } else if (diary.emotion === 1) {
          this.sad += 1;
        } else if (diary.emotion === 2) {
          this.angry += 1;
        } else if (diary.emotion === 3) {
          this.soso += 1;
        }
      });
    },
  },
  methods: {
    editProfile() {
      store.dispatch('userStore/ACT_EDITFLAG', true);
    },
    logout() {
      this.$session.destroy();
      window.location.reload();
    },
    deleteAccount() {
      // if (!confirm('정말 탈퇴하시겠습니까?')) {
      //   return;
      // }
      // if (!result) {
      //   return;
      // }
      api.delete(`account/${this.$session.get('user_id')}`).then(() => {
        this.logout();
      }).catch((err) => {
        console.log(err);
        this.$toast.errer('회원 탈퇴 실패');
      });
    },
    getFormatDate(date) {
      return moment(new Date(date)).format('LL');
      // return moment(new Date(date)).format('YYYY-MM-DD');
    },
  },
};
</script>

<style lang="scss" scoped>
@import '../style/profile.scss';

.middle {
  width: 80%;
  height: 50%;
  margin: 25% 10%;
}

.profile {
  margin: 20px;
  padding: 10px;
  overflow: auto;
  justify-content: center;
  align-items: center;
}

.info {
  float: left;
  padding: 30px;
  width: 40%;
  font-family: 'GmarketSansMedium';
  font-size: 1.5rem;
  line-height: 2rem;
}
</style>>
