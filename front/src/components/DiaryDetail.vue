<template>
  <div class="writing" id="capture" ref="capture" v-show="diary.id > 0">
    <div class="writing__day-info">
      <div class="day-info__date">{{year}}년 {{month}}월 {{date}}일 ({{day}})</div>
      <div class="day-info__weather2">
        <span>날씨</span>
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
      <img :src="diary.image">
    </div>
    <div class="writing__font-selector">
      <span>공유</span>
      <div class="btn-group">
        <button @click="saveFile" class="btn">
          <fa icon="file-download"></fa>
        </button>
        <button class="btn">
          <fa icon="share"></fa>
        </button>
      </div>
    </div>
    <div class="writing__grid">
      <template v-for="index in gridRow*gridColumn">
        <div :key="index" class="cell"></div>
      </template>
      <textarea ref="content" maxlength="51" :class="getFont()" v-model="diary.content"
        disabled></textarea>
    </div>
  </div>
</template>

<script>
// import html2canvas from 'html2canvas';
const computedStyleToInlineStyle = require("computed-style-to-inline-style");

export default {
  data() {
    return {
      gridRow: 5,
      gridColumn: 10,
      weatherIconList: [],
      weather: '',
      fontMapList: [
        "font__se-han",
        "font__gom-sin",
        "font__min-gyeong",
      ],
      fontBtnList: [],
      font: '',
      year: "",
      month: "",
      date: "",
      day: "",
      diary: [],
    };
  },
  computed: {
    diarydata() {
      return this.$store.getters["diaryStore/GET_DIARY"];
    },
  },
  watch: {
    diarydata(val) {
      this.diary = val;
      const date = new Date(this.diary.createdate);
      this.year = date.getFullYear();
      this.month = date.getMonth() + 1;
      this.date = date.getDate();
      this.day = ["일", "월", "화", "수", "목", "금", "토"][date.getDay()];
      this.font = val.font;
      console.log('font', this.font);
      console.log('emotion', val.emotion);
      this.selectWeather(this.weatherIconList[val.emotion]);
    },
  },
  created() {
  },
  // mounted() {
  //   const weatherInfo = document.querySelector(".day-info__weather2");
  //   this.weatherIconList = weatherInfo.querySelectorAll("svg");
  // },
  mounted() {
    const weatherInfo = document.querySelector(".day-info__weather2");
    this.weatherIconList = weatherInfo.querySelectorAll("svg");
    console.log('info2', weatherInfo);

    const fontSelector = document.querySelector(".font-selector__font-list");
    this.fontBtnList = fontSelector.querySelectorAll("button");
  },
  methods: {
    selectWeather(e) {
      console.log('change', e);
      this.weatherIconList.forEach((elem) => {
        elem.classList.remove("selected");
      });
      e.classList.add('selected');
    },
    getFont() {
      return `grid__content ${this.fontMapList[this.font]}`;
    },
    async saveFile() {
      // console.log(this.$refs.capture);
      // await html2canvas(this.$refs.capture).then((canvas) => {
      //   document.body.appendChild(canvas);
      //   this.saveAs(canvas.toDataURL(), 'capture.png');
      //   // window.open(canvas);
      // });
      const el = this.$refs.capture;
      // const options = {
      //   type: 'dataURL',
      //   async: true,
      //   imageTimeout: 5000,
      // };
      const output = await this.$html2canvas(el, {
        type: 'dataURL',
        useCORS: true,
        imageTimeout: 0,
        onclone: (document) => {
          computedStyleToInlineStyle(document.querySelector("#capture"), {
            recursive: true,
          });
        },
      });
      window.open(output);
      await this.saveAs(output, 'capture.png');
    },
    saveAs(uri, filename) {
      const link = document.createElement('a');
      if (typeof link.download === 'string') {
        link.href = uri;
        link.download = filename;

        // Firefox required the link to be in the body
        document.body.appendChild(link);

        // simulate click
        link.click();

        // remove the link when done
        document.body.removeChild(link);
      } else {
        window.open(uri);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../style/diarydetail.scss";

.writing__drawing{
  img{
    width: 100%;
    height: 100%;
  }
}

.btn-group {
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

</style>
