function solution(s, n) {
  var answer = "";
  for (let i = 0; i < s.length; i++) {
    if (s[i] == " ") {
      answer += " ";
    } else {
      if (s.charCodeAt(i) > 90) {
        answer += String.fromCharCode(((s.charCodeAt(i) + n - 97) % 26) + 97);
      } else {
        answer += String.fromCharCode(((s.charCodeAt(i) + n - 65) % 26) + 65);
      }
    }
  }
  return answer;
}

/*
 * ASCII CODE로 풀어보기
 */
