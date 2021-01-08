function solution(dartResult) {
  var ans = [0, 0, 0];
  var idx = -1;
  var Num = "0";

  for (var i = 0; i < dartResult.length; i++) {
    if (
      dartResult[i].charCodeAt(0) >= "0".charCodeAt(0) &&
      dartResult[i].charCodeAt(0) <= "9".charCodeAt(0)
    ) {
      Num += dartResult[i];
    } else if (
      dartResult[i] === "S" ||
      dartResult[i] === "D" ||
      dartResult[i] === "T"
    ) {
      idx++;
      var bonus = 1;
      if (dartResult[i] === "D") {
        bonus = 2;
      } else if (dartResult[i] === "T") {
        bonus = 3;
      }

      ans[idx] += Number(Num) ** bonus;
      Num = "0";
    } else if (dartResult[i] === "*" || dartResult[i] === "#") {
      var option = -1;
      if (dartResult[i] === "*") {
        option = 2;
        if (idx >= 1) {
          ans[idx - 1] *= option;
        }
      }
      ans[idx] *= option;
    }
  }
  return ans.reduce((a, c) => a + c);
}

console.log(solution("1S2D*3T"));
// console.log(solution("1D2S#10S"));
// console.log(solution("1D2S0T"));

/*
[문제요약]
- 3번의 기회, (0<=score<=10)
- S, D, T => 각각 1제곱, 2제곱, 3제곱
- * => 해당점수 및 전 점수 각 2배, 첫번째 경우엔 해당 점수만 2배 , 중첩가능
- # => 해당점수 마이너스
- *, # 도 중첩 가능
[입력]
- 점수 (0~10)|보너스(S|D|T)|옵션(*|#|없음)
*/
