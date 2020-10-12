<template>
  <div class="writing" ref="capture" v-show="diary.id > 0">
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
        <!-- <svg
          class="weather__icon-snowy"
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
        >
          <path
            d="M14 19.25c0 .689-.559 1.25-1.25 1.25s-1.25-.561-1.25-1.25.559-1.25 1.25-1.25 1.25.561 1.25 1.25zm-3.75 1.25c-.691 0-1.25.561-1.25 1.25s.559 1.25 1.25 1.25 1.25-.561 1.25-1.25-.559-1.25-1.25-1.25zm8.75-1.25c0 .689-.559 1.25-1.25 1.25s-1.25-.561-1.25-1.25.559-1.25 1.25-1.25 1.25.561 1.25 1.25zm-3.75 1.25c-.691 0-1.25.561-1.25 1.25s.559 1.25 1.25 1.25 1.25-.561 1.25-1.25-.559-1.25-1.25-1.25zm-6.25-1.25c0 .689-.559 1.25-1.25 1.25s-1.25-.561-1.25-1.25.559-1.25 1.25-1.25 1.25.561 1.25 1.25zm-3.75 1.25c-.691 0-1.25.561-1.25 1.25s.559 1.25 1.25 1.25 1.25-.561 1.25-1.25-.559-1.25-1.25-1.25zm15.172-11.984c-.178-3.232-3.031-5.777-6.432-5.491-1.087-1.24-2.693-2.025-4.49-2.025-3.172 0-5.754 2.443-5.922 5.516-2.033.359-3.578 2.105-3.578 4.206 0 2.362 1.949 4.278 4.354 4.278h1.326c.771 1.198 2.124 2 3.674 2h10.291c2.406 0 4.355-1.916 4.355-4.278 0-2.101-1.545-3.847-3.578-4.206zm-15.395 4.484h-.673c-1.297 0-2.354-1.021-2.354-2.278 0-2.118 2.104-2.597 3.488-2.513-.05-1.355.137-5.209 4.012-5.209.967 0 1.714.25 2.29.645-1.823.921-3.096 2.745-3.212 4.871-2.022.357-3.697 2.127-3.551 4.484zm14.618 2h-10.291c-1.297 0-2.354-1.021-2.354-2.278 0-2.118 2.104-2.597 3.488-2.513-.05-1.355.137-5.209 4.012-5.209 3.771 0 4.229 3.771 4.012 5.209 1.509-.105 3.488.437 3.488 2.513 0 1.257-1.057 2.278-2.355 2.278z"
          />
        </svg> -->
        <svg id="Capa_1" class="weather__icon-snowy" enable-background="new 0 0 512.002 512.002" height="512" viewBox="0 0 512.002 512.002" width="512" xmlns="http://www.w3.org/2000/svg"><g><path d="m121.001 331h16.973l-44.453 66.68c-2.387 3.58-3.121 8.012-2.017 12.17 1.104 4.159 3.94 7.643 7.789 9.566l51.708 25.854v51.73c0 6.624 4.345 12.464 10.689 14.367 6.411 1.923 13.226-.638 16.833-6.11l60-91c2.361-3.581 3.076-8.001 1.965-12.144s-3.942-7.611-7.779-9.529l-51.708-25.854v-35.73h136.973l-44.453 66.68c-2.387 3.58-3.121 8.012-2.017 12.17 1.104 4.159 3.94 7.643 7.789 9.566l51.708 25.854v51.73c0 6.624 4.345 12.464 10.689 14.367 6.411 1.923 13.226-.638 16.833-6.11l60-91c2.361-3.581 3.076-8.001 1.965-12.144s-3.942-7.611-7.779-9.529l-51.708-25.854v-35.73h60c49.922 0 91-40.431 91-90 0-49.52-41.033-90-91-90-.501 0-1.003.004-1.504.013-6.248-30.683-31.289-54.618-62.534-59.214-13.244-53.118-61.092-91.799-115.962-91.799-54.894 0-102.314 38.259-115.749 91.118-1.397-.076-2.812-.118-4.251-.118-66.72 0-121 53.832-121 120s54.28 120 121 120zm83.172 80.856-23.172 35.144v-11c0-5.682-3.21-10.876-8.292-13.416l-44.802-22.401 23.094-34.641v10.458c0 5.682 3.21 10.876 8.292 13.416zm180 0-23.172 35.144v-11c0-5.682-3.21-10.876-8.292-13.416l-44.802-22.401 23.094-34.641v10.458c0 5.682 3.21 10.876 8.292 13.416zm-263.172-290.856c4.362 0 8.74.635 14.011 1.466 8.396 1.318 16.143-4.57 17.213-12.908 5.82-45.356 43.985-79.558 88.776-79.558 44.168 0 82.281 33.649 88.654 78.271 1.101 7.713 8.089 13.845 17.082 12.734 24.229.39 43.863 20.024 44.258 44.251-1.385 11.15 8.215 18.96 17.867 16.973 3.975-.815 8.059-1.229 12.139-1.229 33.636 0 61 26.916 61 60s-27.364 60-61 60h-300c-50.178 0-91-40.374-91-90s40.822-90 91-90z"/></g></svg>
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
      const options = {
        type: 'dataURL',
      };
      const output = await this.$html2canvas(el, options);
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
