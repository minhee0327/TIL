function solution(s) {
  return s[0] + s[1] + "*".repeat(s.length - 2);
}

console.log(solution("강민희"));
console.log(solution("미니미짱"));
console.log(solution("코딩사랑해요"));
console.log(solution("Hello_World_!!!"));
console.log(solution("abcdefghijklmnopqrstuv"));
