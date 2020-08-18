function solution(s) {
  let ans = "";
  let temp = s.split(" ").map((i) => i * 1);
  let max_val = temp.reduce((a, c) => (c > a ? c : a));
  let min_val = temp.reduce((a, c) => (c > a ? a : c));
  ans = min_val + " " + max_val;
  return ans;
}

console.log(solution("1 2 3 4"));
console.log(solution("-1 -2 -3 -4"));
console.log(solution("-1 -1"));

/* Math.max, Math.min쓰면서 NaN이 나와서 reduce로 최대최소값을 구했는데 스프레드 연산자를 활용하면 쉬웠을 문제!!ㅠㅠ*/

function solution1(s) {
  const arr = s.split(" ");
  return Math.min(...arr) + " " + Math.max(...arr);
}

/* 문자열로 정렬해서 맨 앞, 맨뒤 값을 출력하는 방법! */
function solution2(s) {
  return (
    s.split(" ").sort((a, b) => a - b)[0] +
    " " +
    s.split(" ").sort((a, b) => b - a)[0]
  );
}

/* JS의 apply, call, bind를 다시 한번 보고싶어진 문제였음.. */
