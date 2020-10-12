<template>
  <transition name="modal" appear>
    <div class="modal modal-overlay" @click.self="close">
      <div class="modal-window">
        <div class="modal-content">
          <div class="button">
            <div style="float:left;"></div>
            <div class="close" style="float:right;">
              <a @click="close"><fa icon="times"></fa></a>
            </div>
          </div>
          <div style="clear:both;">
            <a class="open-button" @click="wordExtract">
              <fa icon="font"></fa><br>
              <span class="btn-text">단어에 맞는<br>그림 가져오기</span>
            </a>
            <a class="open-button" @click="choosePic">
              <fa icon="images"></fa><br>
              <span class="btn-text">사진에 맞는<br>그림 가져오기</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import api from '@/utils/api';
import store from '@/store/index';

export default {
  methods: {
    close() {
      store.dispatch('windowStore/ACT_SM', false);
    },
    async wordExtract() {
      store.dispatch('windowStore/ACT_SPIN', true);
      await api.post('word/extract/', {
        content: store.getters['diaryStore/GET_CONTENT'],
      }).then(({ data }) => {
        store.dispatch('diaryStore/ACT_WORDS', data);
        this.close();
      }).catch((err) => {
        console.log(err);
        this.$toast.error('단어 추출 실패');
      });
      store.dispatch('windowStore/ACT_SPIN', false);
      // store.dispatch('diaryStore/ACT_EMO', 1);
      this.getEmotion();
    },
    choosePic() {
      store.dispatch('windowStore/ACT_FM', true);
    },
    async getEmotion() {
      store.dispatch('windowStore/ACT_EMOTION_SPIN', true);
      await api.post('word/emo/', {
        content: store.getters['diaryStore/GET_CONTENT'],
      }).then(({ data }) => {
        store.dispatch('diaryStore/ACT_EMO', data);
        store.dispatch('windowStore/ACT_EXIST_EMOTION', true);
      }).catch((err) => {
        console.log(err);
        this.$toast.error('감정 분석 실패');
        store.dispatch('windowStore/ACT_EMOTION_SPIN', false);
      });
    },
  },
};
</script>

<style lang="scss" scoped>
@import '../../style/modal.scss';
</style>
