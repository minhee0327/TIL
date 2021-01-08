//함수에 함수 전달
//비동기적 프로그래밍에서 이런 용도로 전달하는 함수를 콜백(CallBack)이라고함
//자신을 감싼 함수가 실행을 마쳤을 때 호출됨

function sum(arr, f) {
  if (typeof f !== "function") f = (x) => x;
  return arr.reduce((a, x) => (a += f(x)), 0);
}

console.log(sum([1, 2, 3])); //6
console.log(sum([1, 2, 3], (x) => x * x)); //14
console.log(sum([1, 2, 3], (x) => Math.pow(x, 3))); //36
