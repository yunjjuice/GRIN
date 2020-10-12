/**
 * 일기 관련 store
 * 일기 내용 저장
 */
import api from '@/utils/api';

const diaryStore = {
  namespaced: true,
  state: {
    content: '', // 일기 텍스트
    diary: {}, // 캘린더에서 선택한 다이어리 정보
    //   id: "",
    //   content: "",
    //   image: "",
    //   createdate: "",
    // },
    words: {}, // 추출된 단어
    emotion: 30, // 감정분석결과
  },
  getters: {
    GET_CONTENT: (state) => state.content,
    GET_DIARY: (state) => state.diary,
    GET_WORDS: (state) => state.words,
    GET_EMO: (state) => state.emotion,
  },
  mutations: {
    MUT_CONTENT: (state, payload) => {
      state.content = payload;
    },
    MUT_DIARY(state, diary) {
      state.diary = diary;
    },
    MUT_WORDS: (state, payload) => {
      state.words = payload;
    },
    MUT_EMO: (state, payload) => {
      state.emotion = payload;
    },
  },
  actions: {
    ACT_CONTENT: ({ commit }, payload) => {
      commit('MUT_CONTENT', payload);
    },
    async fetchDiary(context, id) {
      try {
        const res = await api.get(`diary/${id}/`);
        context.commit("MUT_DIARY", res.data);
      } catch (error) {
        console.log(error);
      }
    },
    ACT_WORDS: ({ commit }, payload) => {
      commit('MUT_WORDS', payload);
    },
    ACT_EMO: ({ commit }, payload) => {
      commit('MUT_EMO', payload);
    },
  },
};

export default diaryStore;
