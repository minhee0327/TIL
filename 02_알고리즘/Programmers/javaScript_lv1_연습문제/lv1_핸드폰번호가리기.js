function solution(phone_number) {
  var answer = "";
  for (var i = 0; i < phone_number.length - 4; i++) answer += "*";
  answer += phone_number.slice(phone_number.length - 4);
  return answer;
}

// repear()함수!!으어.. 생각도 못해따리..
// slice에서 음수도 먹힌다는 사실...(소름...ㅠㅠ)

function solution2(phone_number) {
  return "*".repeat(phone_number.length - 4) + phone_number.slice(-4);
}

console.log(solution2("01012348888"));
