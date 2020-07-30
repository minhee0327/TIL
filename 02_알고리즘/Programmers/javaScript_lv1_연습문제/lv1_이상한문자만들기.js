function solution(s) {
  var answer = s.split(" ");
  for (var i = 0; i < answer.length; i++) {
    temp = "";
    for (var j = 0; j < answer[i].length; j++) {
      if (j % 2) {
        temp += answer[i][j].toLowerCase();
      } else {
        temp += answer[i][j].toUpperCase();
      }
    }
    answer[i] = temp;
  }
  return answer.join(" ");
}

console.log(solution("try hello world"));

//map 함수로 도전
function solution2(s) {
  return s
    .split(" ")
    .map((item) =>
      item
        .split("")
        .map((c, idx) => (idx % 2 === 0 ? c.toUpperCase() : c.toLowerCase()))
        .join("")
    )
    .join(" ");
}

console.log(solution2("try hello world"));
