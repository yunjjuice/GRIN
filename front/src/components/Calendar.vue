<template>
  <section>
    <div class="main">
      <div class="custom-calendar-wrap">
        <div id="custom-inner" class="custom-inner">
          <div class="custom-header clearfix">
            <nav>
              <span @click="mvPrevMonth" id="custom-prev" class="custom-prev"></span>
              <span @click="mvNextMonth" id="custom-next" class="custom-next"></span>
            </nav>
            <h2 id="custom-month" class="custom-month">{{month+1}}월</h2>
            <h3 id="custom-year" class="custom-year">{{year}}년</h3>
          </div>
          <div id="calendar" class="fc-calendar-container">
            <div class="fc-calendar fc-five-rows">
              <div class="fc-head">
                <div>SUN</div>
                <div>MON</div>
                <div>TUE</div>
                <div>WED</div>
                <div>THU</div>
                <div>FRI</div>
                <div>SAT</div>
              </div>
              <div class="fc-body">
                <div class="calendar__grid">
                  <div :key="index" v-for="index in 42">
                    <div class="date" v-if="index >startDay && index-startDay<=endDate" style="float:left;">
                      {{ index - startDay}}
                    </div>
                    <div style="float:right;" v-if="diaryData.filter((it) => it.createdate == year+'-'+(month+1)+'-'+(index-startDay)) != false">
                      <img class="emotion" :src="emotionList[diaryData.filter((it) => it.createdate.includes(year+'-'+(month+1)+'-'+(index-startDay)))[0].emotion]" />
                    </div>
                    <div class="picture" style="clear:both;" @click="getDiaryDetail(diaryData.filter((it) => it.createdate.includes(year+'-'+(month+1)+'-'+(index-startDay)))[0].id)" v-if="diaryData.filter((it) => it.createdate == year+'-'+(month+1)+'-'+(index-startDay)) != false">
                      <img :src="diaryData.filter((it) => it.createdate.includes(year+'-'+(month+1)+'-'+(index-startDay)))[0].image" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import api from '@/utils/api';
import store from '@/store/index';
import { mapGetters } from 'vuex';
import moment from 'moment';

export default {
  data() {
    return {
      year: 0,
      month: 0,
      date: 0,
      day: 0,
      endDate: 0,
      startDay: 0,
      tempDate: 1,
      diaryData: [],
      emotionList: [
        'imgs/emotion/happy.png',
        'imgs/emotion/sad.png',
        'imgs/emotion/angry.png',
        'imgs/emotion/soso.png',
      ],
    };
  },
  created() {
    const dateObj = new Date();
    this.year = dateObj.getFullYear();
    this.month = dateObj.getMonth();
    this.startDay = new Date(this.year, this.month).getDay();
    this.endDate = new Date(this.year, this.month + 1, 0).getDate();
    if (this.$session.has('user_id')) {
      this.getdiaries();
    }
  },
  // updated() {
  //   if (this.$session.has('user_id')) {
  //     this.getdiaries();
  //   }
  // },
  methods: {
    ...mapGetters({
      getDiary: "diaryStore/GET_DIARY",
    }),
    mvPrevMonth() {
      this.month -= 1;
      if (this.month < 0) {
        this.year -= 1;
        this.month = 11;
      }
      this.calculateDateOfMonth();
    },
    mvNextMonth() {
      this.month += 1;
      if (this.month > 11) {
        this.month = 0;
        this.year += 1;
      }
      this.calculateDateOfMonth();
    },
    calculateDateOfMonth() {
      this.startDay = new Date(this.year, this.month).getDay();
      this.endDate = new Date(this.year, this.month + 1, 0).getDate();
    },
    async getdiaries() {
      await api.get(`diary/?user=${this.$session.get('user_id')}`)
        .then(({ data }) => {
          this.diaryData = data;
          this.diaryData.forEach((item) => {
            item.createdate = moment(new Date(item.createdate)).format('yyyy-M-D');
          });
          console.log('get diary', data);
        })
        .catch((err) => console.log(err));
    },
    getDiaryDetail(id) {
      store.dispatch('diaryStore/fetchDiary', id);
    },
    getEmotion(index) {
      return this.emotionList[index];
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../style/calendar.scss";
</style>
