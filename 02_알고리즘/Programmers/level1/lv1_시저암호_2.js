function solution(s, n) {
  let answer = "";
  let big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  let small = "abcdefghijklmnopqrstuvwxyz";

  for (let i = 0; i < s.length; i++) {
    if (s[i] == " ") {
      answer += " ";
    } else {
      let text = big.includes(s[i]) ? big : small;
      let index = text.indexOf(s[i]) + n;
      if (index >= text.length) {
        index -= text.length;
      }
      answer += text[index];
    }
  }
  return answer;
}

// console.log(solution("z", 1));

/*
 * 문자열 만들어서 풀어보기
 */
