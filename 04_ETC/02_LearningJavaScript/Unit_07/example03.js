/* 즉시호출 함수 표현식(IIFE) */

const msg = (function () {
  const secret = "I'm a secret";
  return `The secret is ${secret.length} characters long.`;
})();

console.log(msg);

//secret은 스코프 안에서 안전하게 보호
//외부에서 접근 불가
//단, 스코프 밖으로 무언가를 내보낼 수 있음(여기서는 msg 템플릿 문자를 반환)
// 배열, 객체, 함수 도 반환할 수 있음

const time = (function () {
  //이 내부 스코프에서만 cnt에 접근이 가능.(밖에서 변경 불가)
  let cnt = 0;
  return function () {
    return `called Count: ${++cnt}`;
  };
})();

console.log(time()); //1호출한 현재 스코프에서 cnt자체 값을 변경할 수는 없음. 내부에서만 변경가능
console.log(time()); //2
console.log(time()); //3
