function solution(x, n) {
  var answer = [];
  for (let i = 1; i <= n; i++) {
    answer.push(x * i);
  }
  return answer;
}

/* 이건 정말 자바스크립트 스러워 */
function solution2(x, n) {
  return Array(n)
    .fill(x)
    .map((v, idx) => v * (idx + 1));
}
