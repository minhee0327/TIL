function solution(arr) {
  return sum(arr) / arr.length;
}

function sum(arr) {
  return arr.reduce((a, c) => a + c);
}

console.log(solution([1, 2, 3, 4]));
