import axios from 'axios';

export default axios.create({
  baseURL: 'http://j3a201.p.ssafy.io:8000/',
  headers: {
    'Content-Type': 'multipart/form-data',
  },
});
