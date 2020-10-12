<template>
  <div class="middle">
    <div class="container-login100">
      <div class="wrap-login100">
        <form @submit.prevent="login" class="login100-form validate-form">
          <span class="login100-form-title">
            Login
          </span>
          <div class="wrap-input100 validate-input" data-validate = "Username is required">
            <label class="input">
              <input class="input100" type="username" ref="username" v-model="username"
                :class="{ white: username.length > 0 }"
                required placeholder="ID">
              <span class="focus-input100"></span>
            </label>
          </div>
          <div class="wrap-input100 validate-input" data-validate = "Password is required">
            <label class="input">
              <input class="input100" type="password" ref="pwd" v-model="pwd"
                :class="{ white: pwd.length > 0 }"
                required placeholder="Password">
              <span class="focus-input100"></span>
            </label>
          </div>
          <div class="container-pwd-form-btn">
            <a href="#" class="txt1">
              Forgot password?
            </a>
          </div>
          <div class="container-login100-form-btn">
            <input type="submit" class="login100-form-btn" value="Login"
                style="margin: 15px 0;">
          </div>
        </form>
        <div class="container-signup-form-btn">
          <button class="txt2" @click="changeSignup">Sign Up</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/utils/api';
import store from '@/store/index';

export default {
  components: {
  },
  data() {
    return {
      username: '',
      pwd: '',
    };
  },
  methods: {
    login() {
      console.log('로그인');
      api.post('account/login/', {
        username: this.username,
        password: this.pwd,
      }).then(({ data }) => {
        console.log(data);
        this.$session.set('user_id', data.user.id);
        this.$session.set('user_token', data.token);
        window.location.reload();
      }).catch((res) => {
        console.log(res);
        this.$toast.error('로그인 실패');
      });
    },
    changeSignup() {
      store.dispatch('userStore/ACT_FLAG', true);
    },
  },
};
</script>

<style lang="scss" scoped>
@import '../style/login.scss';
</style>
