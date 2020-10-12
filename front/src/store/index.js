import Vue from "vue";
import Vuex from "vuex";
import diaryStore from '@/store/modules/diaryStore';
import userStore from '@/store/modules/userStore';
import windowStore from '@/store/modules/windowStore';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    diaryStore,
    userStore,
    windowStore,
  },
});
