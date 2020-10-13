<template>
  <div class="writing" ref="capture">
    <div class="writing__day-info">
      <div class="day-info__date">{{year}}년 {{month}}월 {{date}}일 ({{day}})</div>
      <div class="day-info__weather">
        <span>날씨</span>
        <div ></div>
        <svg
          class="weather__icon-sunny"
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
        >
          <path
            d="M4.069 13h-4.069v-2h4.069c-.041.328-.069.661-.069 1s.028.672.069
            1zm3.034-7.312l-2.881-2.881-1.414 1.414 2.881 2.881c.411-.529.885-1.003
            1.414-1.414zm11.209 1.414l2.881-2.881-1.414-1.414-2.881 2.881c.528.411
            1.002.886 1.414 1.414zm-6.312-3.102c.339 0
            .672.028 1 .069v-4.069h-2v4.069c.328-.041.661-.069
            1-.069zm0 16c-.339 0-.672-.028-1-.069v4.069h2v-4.069c-.328.041-.661.069-1
            .069zm7.931-9c.041.328.069.661.069 1s-.028.672-.069 1h4.069v-2h-4.069zm-3.033
            7.312l2.88 2.88 1.415-1.414-2.88-2.88c-.412.528-.886
            1.002-1.415 1.414zm-11.21-1.415l-2.88 2.88 1.414
            1.414 2.88-2.88c-.528-.411-1.003-.885-1.414-1.414zm2.312-4.897c0 2.206
            1.794 4 4 4s4-1.794 4-4-1.794-4-4-4-4 1.794-4 4zm10 0c0 3.314-2.686 6-6
            6s-6-2.686-6-6 2.686-6 6-6 6 2.686 6 6z"
          />
        </svg>
        <div></div>
        <svg
          class="weather__icon-rainy"
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
        >
          <path
            d="M12.011 3.981c3.005 0 6.033 1.069 8.21 3.974-1.605-.054-3.101.402-4.301
            1.229-1.131-.785-2.508-1.223-3.955-1.223-1.451 0-2.833.438-3.965
            1.221-1.264-.875-2.783-1.281-4.239-1.227 2.14-2.888 5.156-3.997
            8.25-3.974zm-.011-3.981c-.552 0-1 .448-1 1v1.052c-6.916.522-10.372 5.594-11
            9.906 1.865-2.677 6.136-2.677 8 0 1.836-2.637 6.044-2.689 7.917 0 1.865-2.677
            6.219-2.677 8.083 0-.625-4.292-4.125-9.333-11-9.902v-1.056c0-.552-.448-1-1-1zm1
            12.157v8.843c0 1.657-1.343 3-3 3s-3-1.343-3-3v-1h2v1c0
            .551.449 1 1 1s1-.449 1-1v-8.866c.68-.226 1.27-.242 2 .023z"
          />
        </svg>
        <div></div>
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="24" height="24"
          viewBox="0 0 511.878 511.878" style="enable-background:new 0 0 511.878 511.878;" xml:space="preserve" class="weather__icon-thunder">
          <g>
            <g>
              <path d="M499.15,232.533C486.35,170.667,435.15,128,373.283,128c-6.4,0-14.933,0-21.333,2.133V128c0-70.4-57.6-128-128-128
                c-70.4,0-128,57.6-128,128c0,2.133,0,4.267,0,6.4c-66.133,23.467-102.4,98.133-78.933,164.267
                C27.683,326.4,46.883,352,72.483,366.933l21.333-36.267c-40.533-23.467-53.333-76.8-29.867-117.333
                C76.75,192,98.083,177.067,123.683,172.8c12.8-2.133,19.2-14.933,17.067-25.6c-10.667-44.8,17.067-91.733,64-102.4
                c46.933-10.667,91.733,17.067,102.4,64c4.267,14.933,2.133,32-2.133,46.933c-6.4,17.067,12.8,34.133,29.867,25.6
                c10.667-6.4,25.6-10.667,38.4-10.667c46.933,0,85.333,38.4,85.333,85.333c0,40.533-29.867,76.8-68.267,83.2l8.533,42.667
                C469.283,369.067,514.083,300.8,499.15,232.533z"/>
            </g>
          </g>
          <g>
            <g>
              <path d="M330.617,320h-32l32-76.8c4.267-12.8-4.267-29.867-19.2-29.867H181.283c-8.533,0-17.067,4.267-19.2,12.8L119.417,332.8
                c-6.4,14.933,4.267,29.867,19.2,29.867h32l-51.2,119.467c-8.533,19.2,14.933,38.4,32,25.6l192-149.333
                C358.35,345.6,349.817,320,330.617,320z M249.55,354.133c4.267,6.4,10.667,8.533,17.067,8.533h2.133l-76.8,59.733l32-72.533
                c4.267-10.667,0-23.467-10.667-27.733C209.017,320,204.75,320,202.617,320h-32l25.6-64h81.067l-32,76.8
                C243.15,339.2,245.283,347.733,249.55,354.133z"/>
            </g>
          </g>
        </svg>
        <div></div>
        <svg
          class="weather__icon-cloudy"
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
        >
          <path
            d="M2.396
            12h-2.396v-2h2.396v2zm7.604-6.458v-3.542h-2v3.542h2zm-4.793.876l-2.156-2.156-1.414
            1.414 2.156 2.156 1.414-1.414zm9.461-2.396l-2.115 2.114 1.414
            1.414 2.115-2.114-1.414-1.414zm-11.7 10.907l-2.198 1.919 1.303
            1.517 2.198-1.919-1.303-1.517zm21.032 2.793c0 2.362-1.95 4.278-4.354
            4.278h-10.292c-2.404
            0-4.354-1.916-4.354-4.278 0-.77.211-1.49.574-2.113-.964-.907-1.574-2.18-1.574-3.609
            0-2.762 2.238-5 5-5 1.329 0 2.523.528 3.414 1.376.649-.24 1.35-.376 2.086-.376
            3.171 0 5.753 2.443 5.921 5.516 2.034.359 3.579 2.105 3.579 4.206zm-18-5.722c0
            .86.37 1.628.955 2.172.485-.316 1.029-.551 1.624-.656.088-1.61.843-3.042
            1.994-4.046-.46-.288-.991-.47-1.573-.47-1.654 0-3 1.346-3 3zm16
            5.722c0-2.076-1.979-2.618-3.489-2.512.218-1.439-.24-5.21-4.011-5.21-3.875
            0-4.062 3.854-4.011 5.209-1.385-.084-3.489.395-3.489 2.513 0 1.256 1.056 2.278
            2.354 2.278h10.291c1.299 0 2.355-1.022 2.355-2.278z"
          />
        </svg>
      </div>
    </div>
    <div class="writing__drawing">
      <drawing-canvas ref="canvas" v-if="refresh" v-bind:grimMode="isGrimMode" />
    </div>
    <div class="writing__font-selector">
      <span>글꼴</span>
      <div class="font-selector__font-list">
        <button @click="selectFont" class="font__se-han selected">세한</button>
        <button @click="selectFont" class="font__gom-sin">곰신</button>
        <button @click="selectFont" class="font__min-gyeong">민경</button>
      </div>
      <div class="btn-group">
        <div id="btn-send" @click="showModal">
          <svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
            viewBox="0 0 434.958 434.958" style="enable-background:new 0 0 434.958 434.958;" xml:space="preserve" width="22" height="22">
            <g>
              <g>
                <polygon points="129.777,0.278 104.598,227.593 118.168,229.096 141.844,15.351 419.884,46.147 389.871,317.16 295.825,391.13
                  147.828,374.736 146.324,388.308 299.875,405.316 402.811,324.352 434.958,34.08" />
              </g>
            </g>
            <g>
              <g>
                <path d="M343.66,116.673c-9.866-10.197-34.156-7.016-72.967-0.98c-19.511,3.034-60.109,9.347-63.191,2.572
                  c-1.63-3.586-1.456-6.729,0.544-9.89c7.325-11.575,38.996-24.318,105.919-25.371c3.77-0.058,6.777-3.162,6.719-6.932
                  c-0.058-3.77-3.169-6.76-6.932-6.719c-63.29,0.997-104.928,12.262-117.243,31.722c-4.499,7.11-4.995,15.007-1.435,22.842
                  c7.016,15.425,34.104,12.051,77.718,5.268c22.144-3.444,55.608-8.648,61.056-3.017c0.473,0.49,1.254,1.381,1.171,1.857
                  c-0.21,1.183-2.693,7.767-30.99,21.417c-54.429,26.259-59.45,32.519-57.933,40.544c1.57,8.301,11.273,9.037,25.958,10.151
                  c15.674,1.19,39.363,2.988,40.974,14.78c0.468,3.422,3.395,5.903,6.755,5.903c0.309,0,0.62-0.022,0.934-0.065
                  c3.736-0.51,6.351-3.953,5.84-7.689c-3.104-22.721-33.413-25.021-53.468-26.544c-2.656-0.201-5.769-0.437-8.527-0.729
                  c6.243-4.139,19.14-11.387,45.399-24.055c25.247-12.177,36.76-21.543,38.501-31.321
                  C349.338,125.495,347.721,120.87,343.66,116.673z"/>
              </g>
            </g>
            <g>
              <g>
                <polygon points="300.22,295.159 289.937,396.421 303.52,397.8 312.416,310.207 394.674,319.075 396.136,305.5" />
              </g>
            </g>
            <g>
              <g>
                <path d="M239.659,194.623c-1.442-1.439-3.451-2.156-5.48-1.958l-102.41,9.999c-1.574,0.154-3.046,0.85-4.164,1.968L2,330.237
                  c-1.282,1.28-2,3.017-2,4.826c0,1.809,0.72,3.546,2,4.826l92.79,92.79c1.28,1.282,3.016,2,4.826,2c1.811,0,3.548-0.72,4.828-1.998
                  l125.604-125.604c1.125-1.125,1.821-2.608,1.969-4.192l9.62-102.789C241.828,198.067,241.102,196.06,239.659,194.623z
                  M218.653,299.162L99.616,418.198l-83.135-83.135l119.047-119.049l91.745-8.958L218.653,299.162z"/>
              </g>
            </g>
            <g>
              <g>
                <rect x="170.301" y="192.201" transform="matrix(0.7071 -0.7071 0.7071 0.7071 -130.235 200.6826)" width="13.653" height="130.695"/>
              </g>
            </g>
            <g>
              <g>
                <rect x="198.824" y="197.163" transform="matrix(0.7071 -0.7071 0.7071 0.7071 -101.7181 212.4996)" width="13.653" height="63.743"/>
              </g>
            </g>
            <g>
              <g>
                <rect x="8.936" y="292.55" transform="matrix(0.7071 -0.7071 0.7071 0.7071 -183.001 156.9498)" width="178.038" height="13.653"/>
              </g>
            </g>
            <g>
              <g>
                <rect x="46.274" y="329.899" transform="matrix(0.7071 -0.7071 0.7071 0.7071 -198.4723 194.2968)" width="178.055" height="13.653"/>
              </g>
            </g>
          </svg>
          <span>{{ msg }}</span>
        </div>
        <!-- 다운로드 버튼 -->
        <div id="btn-download" @click="saveDiary">
          <svg width="22px" height="16px" viewBox="0 0 22 16">
            <path d="M2,10 L6,13 L12.8760559,4.5959317 C14.1180021,3.0779974 16.2457925,2.62289624 18,3.5 L18,3.5 C19.8385982,4.4192991 21,6.29848669 21,8.35410197 L21,10 C21,12.7614237 18.7614237,15 16,15 L1,15" id="check"></path>
            <polyline points="4.5 8.5 8 11 11.5 8.5" class="svg-out"></polyline>
            <path d="M8,1 L8,11" class="svg-out"></path>
          </svg>
          <span>일기 저장하기</span>
        </div>
        <button id="btn-drawing" @click="isGrimMode = !isGrimMode" > 그리기 모드 </button>
      </div>
    </div>
    <div class="writing__grid">
      <template v-for="index in gridRow*gridColumn">
        <div :key="index" class="cell"></div>
      </template>
      <textarea ref="content" maxlength="51" class="grid__content font__se-han" v-model="content"
        placeholder="오늘은 무슨 일이 있었나요?"></textarea>
    </div>
  </div>
</template>
<script>
import DrawingCanvas from "@/components/Canvas.vue";
import store from '@/store/index';
import multipart from '@/utils/multipart';
import moment from 'moment';

export default {
  components: {
    DrawingCanvas,
  },
  data() {
    return {
      imgscr: '/imgs/emotion/sad.png',
      gridRow: 5,
      gridColumn: 10,
      weatherIconList: [],
      weatherList: ['sunny', 'cloudy', 'rainy', 'snowy'],
      weather: '', // 선택된 날씨
      fontMapList: {
        세한: "font__se-han",
        곰신: "font__gom-sin",
        민경: "font__min-gyeong",
      },
      fontBtnList: [],
      font: 0, // 선택된 폰트
      year: "",
      month: "",
      date: "",
      day: "",
      content: "",
      refresh: true,
      isGrimMode: false,
      action: [],
      sendBtn: '',
      downloadBtn: '',
      msg: '10글자 이상 작성해주세요',
    };
  },
  computed: {
    emotion: () => store.getters['diaryStore/GET_EMO'],
  },
  watch: {
    emotion(newVal) {
      if (newVal >= 0 && newVal < 4) {
        console.log("durl ", this.action);
        this.changeWeather(this.weatherIconList[newVal]);
      } else {
        this.weatherIconList.forEach((elem) => {
          elem.classList.remove("selected");
        });
      }
      console.log("newVal ", newVal);
      if (newVal === '0') {
        setTimeout(() => { this.action[newVal].classList.add('pulse-loader-sunny'); }, 8000);
        setTimeout(() => { this.action[newVal].classList.remove('pulse-loader-sunny'); }, 11000);
      } else if (newVal === '1') {
        setTimeout(() => { this.action[newVal].classList.add('pulse-loader-cloudy'); }, 8000);
        setTimeout(() => { this.action[newVal].classList.remove('pulse-loader-cloudy'); }, 11000);
      } else if (newVal === '2') {
        setTimeout(() => { this.action[newVal].classList.add('pulse-loader-rainy'); }, 8000);
        setTimeout(() => { this.action[newVal].classList.remove('pulse-loader-rainy'); }, 11000);
      } else if (newVal === '3') {
        setTimeout(() => { this.action[newVal].classList.add('pulse-loader-snowy'); }, 8000);
        setTimeout(() => { this.action[newVal].classList.remove('pulse-loader-snowy'); }, 11000);
      }
      console.log("d액션", this.action);
    },
    content(newVal) {
      if (newVal.length < 10) {
        this.msg = '10글자 이상 작성해주세요';
        this.sendFlag = false;
      } else {
        this.msg = '그림 그리기';
        this.sendFlag = true;
      }
    },
  },
  created() {
    const date = new Date();
    this.year = date.getFullYear();
    this.month = date.getMonth() + 1;
    this.date = date.getDate();
    this.day = ["일", "월", "화", "수", "목", "금", "토"][date.getDay()];
  },
  mounted() {
    const weatherInfo = document.querySelector(".day-info__weather");
    this.weatherIconList = weatherInfo.querySelectorAll("svg");
    this.action = weatherInfo.querySelectorAll("div");
    const fontSelector = document.querySelector(".font-selector__font-list");
    this.fontBtnList = fontSelector.querySelectorAll("button");

    this.downloadBtn = document.querySelector('#btn-download');
    this.sendBtn = document.querySelector('#btn-send');
  },
  methods: {
    init() {
      this.content = '';
      store.dispatch('diaryStore/ACT_EMO', 30);
      store.dispatch('diaryStore/ACT_CONTENT', '');
      store.dispatch('diaryStore/ACT_WORDS', {});
    },
    changeWeather(e) {
      this.weatherIconList.forEach((elem) => {
        elem.classList.remove("selected");
      });
      e.classList.add('selected');
    },
    selectFont(e) {
      this.fontBtnList.forEach((elem, index) => {
        elem.classList.remove("selected");
        if (e.currentTarget === elem) {
          this.font = index;
        }
      });

      e.currentTarget.classList.add("selected");

      Object.values(this.fontMapList).forEach((elem) => {
        this.$refs.content.classList.remove(elem);
      });

      const fontName = e.currentTarget.innerText;
      this.$refs.content.classList.add(this.fontMapList[fontName]);
    },
    showModal() {
      if (this.content.length < 10) return;

      store.dispatch('windowStore/ACT_SM', true);
      store.dispatch('diaryStore/ACT_CONTENT', this.content);
    },
    async saveDiary() {
      if (!this.$session.has('user_id')) {
        this.$toast.error('로그인한 회원만 저장 가능합니다');
        return;
      }

      if (this.content === '' || this.emotion === 30) {
        this.$toast.warning('일기를 작성해주세요');
        return;
      }

      this.downloadBtn.classList.add('downloaded');
      const el = this.$refs.canvas.$el;
      this.refresh = false;
      await el.toBlob((blob) => {
        const formData = new FormData();
        formData.append('user', this.$session.get('user_id'));
        formData.append('content', this.content);
        formData.append('image', blob, 'today.png');
        const createDate = moment(new Date(), 'YYYY-MM-DD').format();
        formData.append('createdate', createDate);
        formData.append('font', this.font);
        formData.append('emotion', this.emotion);

        multipart.post('diary/', formData).then(() => {
          this.$toast.success('그림일기 저장 성공');
          this.init();
        }).catch((err) => {
          console.log(err);
          this.$toast.error('그림일기 저장 실패');
        });
        this.refresh = true;
      });
      setTimeout(() => {
        this.downloadBtn.classList.remove('downloaded');
      }, 3000);
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../style/writing.scss";
@import "../style/downloadbutton.scss";

.btn-group {
  position: absolute;
  right: 30px;
}

.btn {
  border: none;
  background-color:rgba(0,0,0,0);
  font-size: 1.5rem;
  outline: none;
  margin: 5px;
  // color: rgba(0, 0, 0, 0.4);
  font-weight: bold;
  cursor: pointer;
}

.sunny {
  position: absolute;
  width: 60px;
  right: 136px;
}
.cloudy {
  position: absolute;
  width: 60px;
  right: 90px;
}
.rainy {
  position: absolute;
  width: 60px;
  right: 52px;
}
.snowy {
  position: absolute;
  width: 60px;
  right: 10px;
}
</style>
