function solution(s) {
  if (s.length % 2) {
    return s[parseInt(s.length / 2)];
  } else {
    return s[parseInt(s.length / 2) - 1] + s[parseInt(s.length / 2)];
  }
}

console.log(solution("abcde"));
console.log(solution("qwer"));

/* 다른풀이 */
/* 자바스크립트는 삼항연산자를 많이 활용하는 것 같다.*/
/* substr 내장함수로 원하는문자열 길이를 반환할 수 있다. 짝수일 경우 1개만, 홀수일경우 2개만 반환하는 코드로 짬. */

function solution2(s) {
  return s.substr(Math.ceil(s.length / 2) - 1, s.length % 2 ? 1 : 2);
}

console.log(solution2("abcde"));
console.log(solution2("qwer"));
