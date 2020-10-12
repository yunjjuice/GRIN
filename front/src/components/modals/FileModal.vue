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

          <div id="file-upload-form" class="uploader">
            <input id="file-upload" type="file" name="fileUpload" ref="imageSelect"
              accept=".jpg, .jpeg, .png" @change="imageSelect" />
            <label for="file-upload" id="file-drag">
              <div id="file-image" class="hidden"></div>
              <div id="start">
                <i class="fa fa-download" aria-hidden="true"></i>
                <div>Select a file</div>
                <span id="file-upload-btn" class="btn btn-primary">Select a file</span>
              </div>
            </label>
            <button class="btn send" @click="picToDraw">그림으로 바꾸기</button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import api from '@/utils/api';
import multipart from '@/utils/multipart';
import store from '@/store/index';
import EventBus from '@/utils/EventBus';

export default {
  data() {
    return {
      extractPic: null,
      previewImg: '',
    };
  },
  methods: {
    close() {
      store.dispatch('windowStore/ACT_FM', false);
    },
    imageSelect() {
      console.log('image select');
      const [files] = this.$refs.imageSelect.files;
      this.extractPic = files;
      const url = URL.createObjectURL(files);
      document.querySelector('#file-image').classList.remove('hidden');
      document.querySelector('#file-image').style.backgroundImage = `url(${url})`;
      document.querySelector('#start').classList.add('hidden');
    },
    async picToDraw() {
      // console.log('pic extract');
      // console.log('pic', this.extractPic);
      if (this.extractPic === null) {
        alert('이미지를 등록해주세요');
        return;
      }

      store.dispatch('windowStore/ACT_SPIN', true);
      const formData = new FormData();
      formData.append('image', this.extractPic);
      await multipart.post('drawing/picture/', formData).then(({ data }) => {
        const imagePath = data.trans_image;
        const src = `http://j3a201.p.ssafy.io:8000${imagePath}`;
        EventBus.$emit('addImg', src);
        this.close();
      }).catch((err) => {
        console.log(err);
        this.$toast.error('이미지 변환 실패');
      });
      store.dispatch('windowStore/ACT_SM', false);
      store.dispatch('windowStore/ACT_SPIN', false);
      this.getEmotion();
    },
    async getEmotion() {
      store.dispatch('windowStore/ACT_EMOTION_SPIN', true);
      await api.post('word/emo/', {
        content: store.getters['diaryStore/GET_CONTENT'],
      }, {
        timeout: 10000,
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
@import '../../style/filemodal.scss';
</style>
