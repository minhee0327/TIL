function solution(n) {
  var answer = 0;

  while (n) {
    answer += n % 10;
    n = parseInt(n / 10);
  }

  return answer;
}

/* 위 코드는 그동안 자릿수 합할때 사용하던 코드 */
/* 아래코드는 좀 더 javaScript 스럽게 푼 코드들*/

// 1. 문자열로 바꿔준다음, split()으로 쪼개서, reduce로 누적합을 구하는 방법!
function solution2(n) {
  return (n + "").split("").reduce((a, b) => a + parseInt(b), 0);
}

console.log(solution2(123));
