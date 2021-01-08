const d = new Date();
console.log(d); //2020-09-01T08:28:58.189Z //타임존이 들어간 그레고리력 날짜
console.log(d.valueOf()); //1598948938189 //유닉스 타임스탬프

const moment = require('moment-timezone');

const m = new Date(Date.UTC(2016, 4, 27)); // May 27, 2016 UTC
const s = moment.tz([1991, 2, 27, 9, 19], 'Asia/Seoul').toDate();

console.log(m);
console.log(s);