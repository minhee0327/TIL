function solution(array, commands) {
  let answer = [];

  for (let i = 0; i < commands.length; i++) {
    let temp = [];
    temp = array.slice(commands[i][0] - 1, commands[i][1]);
    temp.sort(function (a, b) {
      return a - b;
    });
    answer.push(temp[commands[i][2] - 1]);
  }
  return answer;
}

/*
 * javaScript로 풀려니까 내장함수들이 다 생소하다..ㅠㅠ
 * 그나마 이건 내가 아는대로 풀었는데,
 * 다른사람풀이를 보니까, 비구조화 할당, filter, sort를 한번에 사용했다.
 * 연습차원에서 다시 풀어보기!(다른코드로)
 */
