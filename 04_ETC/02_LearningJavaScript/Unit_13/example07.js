//함수를 반환하는 함수
function sum(arr, f) {
  if (typeof f !== "function") f = (x) => x;
  return arr.reduce((a, x) => (a += f(x)), 0);
}
/*
function sumOfsuares(arr) {
  return sum(arr, (x) => x * x);
}
*/
function newSummer(f) {
  return (arr) => sum(arr, f);
}

const sumOfsuares = newSummer((x) => x * x);
console.log(sumOfsuares([1, 2, 3])); //14

const sumOfCubes = newSummer((x) => Math.pow(x, 3));
console.log(sumOfCubes([1, 2, 3])); //36
