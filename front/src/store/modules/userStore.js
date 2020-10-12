/**
 * 로그인창, 회원가입창 관리 store
 */

const userStore = {
  namespaced: true,
  state: {
    flag: false, // signup 창을 띄울 건지 체크
    editFlag: false, // 프로필 수정 창을 띄울건지
  },
  getters: {
    GET_FLAG: (state) => state.flag,
    GET_EDITFLAG: (state) => state.editFlag,
  },
  mutations: {
    MUT_FLAG: (state, payload) => {
      state.flag = payload;
    },
    MUT_EDITFLAG: (state, payload) => {
      state.editFlag = payload;
    },
  },
  actions: {
    ACT_FLAG: ({ commit }, payload) => {
      commit('MUT_FLAG', payload);
    },
    ACT_EDITFLAG: ({ commit }, payload) => {
      commit('MUT_EDITFLAG', payload);
    },
  },
};

export default userStore;
