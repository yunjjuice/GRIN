<template>
  <div class="middle">
    <div>
      <div class="profile" style="width: 50%;">
        <img class="fir-circle" :src="profilePic">
        <label for="profilePic" class="file-select">
          <fa icon="camera" class="icon"></fa>
        </label>
        <input type="file" id="profilePic" ref="profilePic"
          @change="previewFile" accept=".jpg, .jpeg, .png">
      </div>
      <div class="group">
        <div style="font-family: 'GmarketSansMedium';">닉네임</div>
        <div class="sketchy">
          <input type="text" v-model="userInfo.nickname" class="input-edit">
        </div>
      </div>
      <div class="group">
        <div style="font-family: 'GmarketSansMedium';">생일</div>
        <div class="sketchy">
          <input type="date" v-model="birthdate" class="input-edit">
        </div>
      </div>
      <div class="group">
        <div style="font-family: 'GmarketSansMedium';">자기소개</div>
        <div class="sketchy">
          <input type="text" v-model="userInfo.intro" class="input-edit">
        </div>
      </div>
    </div>
    <div style="text-align:center;">
      <button class="button--tertiary" @click="updateProfile">수정 완료</button>
      <button class="button--tertiary" @click="cancelEdit">취소</button>
    </div>
  </div>
</template>

<script>
import api from '@/utils/api';
import multipart from '@/utils/multipart';
import store from '@/store/index';
import moment from 'moment';

export default {
  data() {
    return {
      profilePic: '',
      uploadImg: null,
      birthdate: '',
      userInfo: {},
    };
  },
  created() {
    api.get(`account/${this.$session.get('user_id')}/`)
      .then(({ data }) => {
        // console.log(data);
        this.userInfo = data;
        if (data.profilePic == null) {
          this.profilePic = 'https://lab.ssafy.com/s03-ai-sub3/s03p23a201/uploads/94342b2dc983157f5b3169b765af3da7/3F212117-1473-47F6-AD9F-531326117EAB-95867-00005C1428239F3C_file.jpg';
        } else {
          this.profilePic = `http://j3a201.p.ssafy.io:8000${data.profilePic}`;
        }
        this.birthdate = this.getFormatDate(data.birthdate);
      });
  },
  methods: {
    previewFile() {
      this.path = "";
      const [files] = this.$refs.profilePic.files;
      this.uploadImg = files;
      this.profilePic = URL.createObjectURL(files);
    },
    updateProfile() {
      const formData = new FormData();

      if (this.uploadImg !== null) {
        formData.append('profilePic', this.uploadImg);
      }
      formData.append('nickname', this.userInfo.nickname);
      formData.append('intro', this.userInfo.intro);
      const birth = moment(this.birthdate, 'YYYY-MM-DD').format();
      formData.append('birthdate', birth);

      multipart.put(`account/${this.$session.get('user_id')}/`, formData).then(() => {
        this.closeEditProfile();
      }).catch((err) => {
        console.log(err);
        this.$toast.error('프로필 업데이트 실패');
      });
    },
    cancelEdit() {
      this.closeEditProfile();
    },
    closeEditProfile() {
      store.dispatch('userStore/ACT_EDITFLAG', false);
    },
    getFormatDate(date) {
      return moment(new Date(date)).format('YYYY-MM-DD');
    },
  },
};
</script>

<style lang="scss" scoped>
@import '../style/profile.scss';

.middle {
  width: 80%;
  height: 80%;
  margin: 5% 10% 15% 10%;
}

.profile {
  width: 50%;
  padding: 10px 25%;
  margin: 20px;
  overflow: auto;
  justify-content: center;
  align-items: center;
}
</style>
