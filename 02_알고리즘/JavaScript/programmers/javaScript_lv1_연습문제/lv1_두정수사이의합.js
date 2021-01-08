function solution(a, b) {
  var answer = 0;
  var min = Math.min(a, b);
  var max = Math.max(a, b);
  for (let i = min; i <= max; i++) {
    answer += i;
  }
  return answer;
}
console.log(solution(3, 5));
console.log(solution(3, 3));
console.log(solution(5, 3));

/* 위는 내 풀이고.. 가우스의 법칙을 쓴 코드가 인상깊었다. */
console.log("------------가우스법칙-------------");
function solution2(a, b) {
  return ((a + b) * (Math.abs(b - a) + 1)) / 2;
}
console.log(solution2(3, 5));
console.log(solution2(3, 3));
console.log(solution2(5, 3));

//두 수 사이의 총합 = (최소값 + 최댓값) * (최대 최소 gap)/2
