function solution(arr, divisor) {
  var answer = [];
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] % divisor === 0) {
      answer.push(arr[i]);
    }
  }
  if (answer.length === 0) {
    answer.push(-1);
  }
  // console.log(answer.sort(function(a,b){return a-b}))
  console.log(answer.sort((a, b) => a - b));
  return answer;
}

/*
- sort()의 기준은 문자열이라는점. 숫자비교를할때는 위와같이 해야한다.(내림차순은 b-a)

- 나는 반복문 돌면서 풀어가는 과정으로 했는데, filter나 map함수로 구현한 코드가 좀더 자바스크립트스러운 느낌이든다.
- 연습삼아 아래 solution2, solution3등으로 연습함.
*/

// map 함수 사용
function solution2(arr, divisor) {
  var answer = [];
  arr.map((i) => i % divisor === 0 && answer.push(i));
  return answer.length ? answer.sort((a, b) => a - b) : [-1];
}

console.log(solution2([5, 9, 7, 10], 5));

//filter 함수 사용
function solution3(arr, divisor) {
  var answer = arr.filter((i) => i % divisor === 0);
  return answer.length ? answer.sort((a, b) => a - b) : [-1];
}
console.log(solution3([5, 9, 7, 10], 5));
