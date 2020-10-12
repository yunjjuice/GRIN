<template>
  <div class="container-login100">
    <div class="wrap-login100">
      <!-- 회원가입 -->
      <span class="login100-form-title">
        SIGN UP
      </span>
      <fieldset>
        <form  @submit.prevent="signUp" class="login100-form validate-form">
          <div class="wrap-input100 validate-input" data-validate="Username is required">
            <label class="input">
              <input class="input100" type="text" ref="username" v-model="username"
                required placeholder="ID">
              <span class="focus-input100"></span>
            </label>
          </div>
          <div class="wrap-input100 validate-input" data-validate="Password is required">
            <label class="input">
              <input class="input100" type="password" ref="pwd" v-model="pwd"
                placeholder="Password"
                pattern=".{0}|.{5,20}" required title="비밀번호는 5~20자 사이로 해주세요">
              <span class="focus-input100"></span>
            </label>
          </div>
          <div class="wrap-input100 validate-input" data-validate="Password is required">
            <label class="input">
              <input class="input100" type="password" ref="pwdConfirm" v-model="pwdConfirm"
                placeholder="Password Confirm"
                pattern=".{0}|.{5,20}" required title="비밀번호는 5~20자 사이로 해주세요">
              <span class="focus-input100"></span>
            </label>
          </div>
          <div class="container-login100-form-btn">
            <input type="submit" class="login100-form-btn" value="Sign Up">
          </div>
          <div class="container-login100-form-btn">
            <input type="submit" class="login100-form-btn" value="Cancel"
              @click="changeLogin">
          </div>
        </form>
      </fieldset>

      <!-- 추가정보 입력 -->
      <fieldset>
        <form @submit.prevent="updateProfile" class="login100-form validate-form">
          <div class="wrap-input100 validate-input">
            <label class="input">
              <input class="input100" type="file" ref="profilePic"
                @change="fileSelect" accept=".jpg, .jpeg, .png"
                placeholder="profile photo">
              <span class="focus-input100"></span>
            </label>
          </div>
          <div class="wrap-input100 validate-input">
            <label class="input">
              <input class="input100" type="text" v-model="nickname"
                placeholder="nickname">
              <span class="focus-input100"></span>
            </label>
          </div>
          <div class="wrap-input100 validate-input">
            <label class="input">
              <input class="input100" type="text" v-model="intro"
                placeholder="intro">
              <span class="focus-input100"></span>
            </label>
          </div>
          <div class="wrap-input100 validate-input">
            <label class="input">
              <input class="input100" type="date" v-model="birthdate"
                placeholder="birthdate">
              <span class="focus-input100"></span>
            </label>
          </div>
          <div class="container-login100-form-btn">
            <input type="submit" class="login100-form-btn" value="Update Profile">
          </div>
        </form>
      </fieldset>

      <!-- 추가 정보 입력 완료 -->
      <fieldset style="text-align:center;">
        <!-- 성공 아이콘 -->
        <div class="screenAlert-icon screenAlert-success animate" style="margin: 50px 38%; ">
          <span class="screenAlert-line screenAlert-tip animateSuccessTip"></span>
          <span class="screenAlert-line screenAlert-long animateSuccessLong"></span>
          <div class="screenAlert-placeholder"></div>
          <div class="screenAlert-fix"></div>
        </div>
        <span class="success">
          회원 가입 완료
        </span>
        <div class="container-login100-form-btn">
          <input type="button" class="login100-form-btn" @click="changeLogin" value="Complete">
        </div>
      </fieldset>
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
      username: '',
      pwd: '',
      pwdConfirm: '',
      confirmFlag: false,
      id: '',
      nickname: '',
      profilePic: '',
      intro: '',
      birthdate: null,
      fieldsetList: [],
    };
  },
  watch: {
    pwdConfirm(val) {
      if (val === this.pwd) {
        this.confirmFlag = true;
      } else {
        this.confirmFlag = false;
      }
    },
  },
  mounted() {
    const fieldList = document.querySelectorAll('fieldset');
    this.fieldsetList = fieldList;
  },
  methods: {
    signUp() {
      if (!this.confirmFlag) {
        alert('비밀번호를 확인해주세요');
        this.$refs.pwdConfirm.focus();
        return;
      }
      api.post('account/', {
        username: this.username,
        password: this.pwd,
      }).then(({ data }) => {
        this.id = data.user.id;
        this.disappearObject(this.fieldsetList[0]);
        this.fieldsetList[0].animate([
          { opacity: 0 },
        ], 500);
        this.appearObject(this.fieldsetList[1]);
      }).catch((res) => {
        console.log(res);
        this.$toast.error('회원가입 실패');
      });
    },
    fileSelect() {
      const [files] = this.$refs.profilePic.files;
      this.profilePic = files;
    },
    updateProfile() {
      const formData = new FormData();

      if (this.profilePic !== null) {
        formData.append('profilePic', this.profilePic);
      }
      if (this.nickname !== '') {
        formData.append('nickname', this.nickname);
      }
      if (this.intro !== '') {
        formData.append('intro', this.intro);
      }
      if (this.birthdate !== null) {
        const birth = moment(this.birthdate, 'YYYY-MM-DD').format();
        formData.append('birthdate', birth);
      }

      multipart.put(`account/${this.id}/`, formData).then(() => {
        this.disappearObject(this.fieldsetList[1]);
        this.fieldsetList[1].animate([
          { opacity: 0 },
        ], 500);
        this.appearObject(this.fieldsetList[2]);
      }).catch((err) => {
        console.log(err);
        this.$toast.error('프로필 업데이트 실패');
      });
    },
    changeLogin() {
      store.dispatch('userStore/ACT_FLAG', false);
    },
    disappearObject(element) {
      setTimeout(() => {
        element.classList.add('invisible');
        element.classList.remove('visible');
      }, 500);
    },
    appearObject(element) {
      setTimeout(() => {
        element.classList.add('visible');
      }, 500);
    },
  },
};
</script>

<style lang="scss" scoped>
@import '../style/fancyinput.scss';
@import '../style/success.css';
@import '../style/login.scss';

fieldset {
  padding: 20px;
  position: relative;
  &:not(:first-of-type) {
    display: none;
  }
}

.invisible {
  display: none !important;
}

.visible {
  display: block !important;
}

.success {
  font-family: 'GmarketSansMedium';
  font-size: 1.5rem;
  text-align: center;
  padding: 10px;
}
</style>
