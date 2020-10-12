import Vue from "vue";
import VueSession from 'vue-session';
import VueCookies from 'vue-cookies';
import { library } from '@fortawesome/fontawesome-svg-core';
import {
  faPaperPlane, faFileDownload, faFont, faImages, faTimes, faCamera, faShare,
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import Toast from 'vue-toastification';
import VueHtml2Canvas from 'vue-html2canvas';
import App from "./App.vue";
import router from "./router";
import store from "./store";
import 'vue-toastification/dist/index.css';

// fontawesome
library.add(faPaperPlane);
library.add(faFileDownload);
library.add(faFont);
library.add(faImages);
library.add(faTimes);
library.add(faCamera);
library.add(faShare);
Vue.component('fa', FontAwesomeIcon);

Vue.use(VueSession);
Vue.use(VueCookies);
Vue.use(VueHtml2Canvas);

Vue.use(Toast, {
  timeout: 2000,
  transition: "Vue-Toastification__fade",
  maxToasts: 5,
  newestOnTop: true,
  hideProgressBar: true,
  position: "bottom-center",
});

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
