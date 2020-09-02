//날짜 형식

var date = new Date(Date.UTC(2012, 11, 12, 3, 0, 0));
console.log(date.toLocaleDateString()); //2012.12.12
console.log(date.toLocaleString()); //2012.12.12. 오후 12:00:00
console.log(date.toLocaleTimeString()); //오후 12:00:00
console.log(date.toTimeString()); //12:00:00 GMT+9000 (대한민국 표준시)
console.log(date.toUTCString()); //Wed, 12 Dec 2012 03:00:00 GTM


console.log(moment(date).format("YYYY-MM-DD")) //2012-12-12
console.log(moment(date).format("YYYY-MM-DD HH:mm")) //2012-12-12 12:00
console.log(moment(date).format("YYYY-MM-DD HH:mm Z")) //2012-12-12 12:00 +09:00
console.log(moment(date).format("YYYY-MM-DD HH:mm [UTC]Z")) //2012-12-12 12:00 UTC+09:00
console.log(moment(date).format("YYYY년MM월DD일 HH:mm")) //2012년12월12일 12:00

console.log(moment(date).format("dddd, MMMM [the] Do, YYYY")) //Wednesday, December the 12th, 2012

/*
M: 1,2,3,...
MM: 01,02, 03,...
MMM: Jan, Feb, Mar
MMMM: January, Febuary, March, ...

o 를 붙이면 1st, 2nd, 3rd
문자열 사용하고 싶을 때, []로 감싸기
*/