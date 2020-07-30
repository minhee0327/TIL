function solution(s) {
  if (s.length === 4 || s.length === 6) {
    if (!isNaN(s * 1) && s.length === (s * 1 + "").length) {
      return true;
    } else {
      return false;
    }
  } else {
    return false;
  }
}

console.log(solution("a234"));
console.log(solution("1234"));

/*
- 문제를 잘 읽어봐야했던 문제 + 조건을 잘 체크할 문제
- 문자열 길이 4 혹은 6일때 
- 숫자인 경우 (+빈공백이 안주어졌을 경우에만 숫자임) 만 true
- 나머지는 false
*/
