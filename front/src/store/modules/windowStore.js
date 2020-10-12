/**
 * 컴포넌트 표시를 위한 store
 * 모달창 관리 등
 */

const windowStore = {
  namespaced: true,
  state: {
    selectModal: false, // 선택 모달창
    fileModal: false, // 파일 선택 모달창
    showSpinner: false, // 스피너
    showEmotionSpinner: false, // 감정 스피너
    existEmotion: false,
  },
  getters: {
    GET_SM: (state) => state.selectModal,
    GET_FM: (state) => state.fileModal,
    GET_SPIN: (state) => state.showSpinner,
    GET_EMOTION_SPIN: (state) => state.showEmotionSpinner,
    GET_EXIST_EMOTION: (state) => state.existEmotion,
  },
  mutations: {
    MUT_SM: (state, payload) => {
      state.selectModal = payload;
    },
    MUT_FM: (state, payload) => {
      state.fileModal = payload;
    },
    MUT_SPIN: (state, payload) => {
      state.showSpinner = payload;
    },
    MUT_EMOTION_SPIN: (state, payload) => {
      state.showEmotionSpinner = payload;
    },
    MUT_EXIST_EMOTION: (state, payload) => {
      state.existEmotion = payload;
    },
  },
  actions: {
    ACT_SM: ({ commit }, payload) => {
      commit('MUT_SM', payload);
    },
    ACT_FM: ({ commit }, payload) => {
      commit('MUT_FM', payload);
    },
    ACT_SPIN: ({ commit }, payload) => {
      commit('MUT_SPIN', payload);
    },
    ACT_EMOTION_SPIN: ({ commit }, payload) => {
      commit('MUT_EMOTION_SPIN', payload);
    },
    ACT_EXIST_EMOTION: ({ commit }, payload) => {
      commit('MUT_EXIST_EMOTION', payload);
    },
  },
};

export default windowStore;
