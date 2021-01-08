/*
var i;
for (i = 5; i >= 0; i--) {
    setTimeout(function () {
        console.log(i === 0 ? "go!" : i);
    }, (5 - i) * 1000);
}
*/

//위 결과 1초마다 -1이 6번 출력됨

/* 
setTimeout에 전달된 함수가 루프안에서 실행되지 않고, 루프가 다 종료된 뒤 실행됐기 때문 
루프가 모두 종료된 시점에 i는 -1이고 그 시점에 콜백함수가 호출이 됨 
 
let을 사용해서 블록수준의 스코프를 만들면 해결할 수 있음  
블록스코프변수가 도입되기 전에는 이 문제를 해결하기 위해 함수를 하나 더 사용했었음
함수를 하나 더 사용하면, 스코프가 새로 만들어지고 각 단계에서 i값이 클로저에 캡쳐되기 때문
*/

//예시
// 변수 j를 전달하는게 아니라, j의 값을 전달
/*
function loopBody(j) {
  setTimeout(function () {
    console.log(j === 0 ? "go!" : j);
  }, (5 - j) * 1000);
}
var j;
for (j = 5; j >= 0; j--) {
  loopBody(j);
}
*/

// 루프를 위한 변수를 하나 사용하는 것보다, 익명함수를 만들어 즉시호출하는 IIFE를 쓰는게 효율적
/*
var i;
for (i = 5; i >= 0; i--) {
  (function (i) {
    setTimeout(function () {
      console.log(i === 0 ? "go!" : i);
    }, (5 - i) * 1000);
  })(i);
}
*/

//블록스코프 let을 사용하면, 스코프 하나때문에 함수를 만드는 일을 할 필요가 없어짐
for (let i = 5; i >= 0; i--) {
  setTimeout(function () {
    console.log(i === 0 ? "go!" : i);
  }, (5 - i) * 1000);
}
