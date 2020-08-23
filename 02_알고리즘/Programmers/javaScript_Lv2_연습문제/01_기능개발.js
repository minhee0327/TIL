function solution(progresses, speeds) {
  var bapo = progresses.map((v, i) =>
    (100 - v) % speeds[i]
      ? parseInt((100 - v) / speeds[i]) + 1
      : parseInt((100 - v) / speeds[i])
  );
  var answer = [];
  let pivot = bapo[0];
  let cnt = 1;
  bapo.push(101);

  for (let i = 1; i < bapo.length; i++) {
    if (pivot >= bapo[i]) {
      cnt += 1;
    } else {
      answer.push(cnt);
      pivot = bapo[i];
      cnt = 1;
    }
  }
  console.log(answer);
  return answer;
}
/*
[내코드 리뷰(위)]
- bapo 가 가능한 날짜를 먼저 계산하기 (map을 돌면서 계산결과에 해당하는 경우 값을 넣어줌)
- 마지막에 임의로 끝날수 없는 임의값(101)을 넣어주고 반복해서 체크.
- pivot(기준값) 기준으로 더 작을때는 카운드를 높여주고, 아닐경우엔 해당 위치부터 다시 탐색하기 위해 초기화함
- 위 코드 개선 코드 (하단에 추가)
*/

function solution(progresses, speeds) {
  var bapo = progresses.map((v, i) => Math.Ceil((100 - v) / speeds[i]));

  var answer = [0];
  let pivot = bapo[0];

  for (let i = 0, j = 0; i < bapo.length; i++) {
    if (pivot >= bapo[i]) {
      answer[j] += 1;
    } else {
      pivot = bapo[i];
      answer[++j] = 1;
    }
  }
  console.log(answer);
  return answer;
}
