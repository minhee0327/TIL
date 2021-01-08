function solution(answers) {
  let p1 = [1, 2, 3, 4, 5],
    p2 = [2, 1, 2, 3, 2, 4, 2, 5],
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let cnt = [0, 0, 0];
  let answer = [];

  //정답 체크
  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === p1[i % p1.length]) {
      cnt[0]++;
    }
    if (answers[i] === p2[i % p2.length]) {
      cnt[1]++;
    }
    if (answers[i] === p3[i % p3.length]) {
      cnt[2]++;
    }
  }
  //cnt의 최대값
  let max_cnt = cnt.reduce((a, c) => (a > c ? a : c));

  for (let i = 0; i < 3; i++) {
    if (max_cnt === cnt[i]) {
      answer.push(i + 1);
    }
  }

  return answer;
}

console.log(solution([1, 2, 3, 4, 5]));
console.log(solution([1, 3, 2, 4, 2]));

//filter 사용해보기

function solution2(answers) {
  let answer = [];
  let p1 = [1, 2, 3, 4, 5],
    p2 = [2, 1, 2, 3, 2, 4, 2, 5],
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  p1 = answers.filter((v, i) => v === p1[i % p1.length]).length;
  p2 = answers.filter((v, i) => v === p2[i % p2.length]).length;
  p3 = answers.filter((v, i) => v === p3[i % p3.length]).length;

  var max = Math.max(p1, p2, p3);

  if (max === p1) answer.push(1);
  if (max === p2) answer.push(2);
  if (max === p3) answer.push(3);

  return answer;
}

console.log(solution2([1, 2, 3, 4, 5]));
console.log(solution2([1, 3, 2, 4, 2]));

/*
- 문제풀면서 실수
- 1. i % arr.length : 배열길이로 나눈 나머지값으로 배열을 돌기때문에 반복해서 값을 알수있다.
  2. filter를 사용해서 원하는 값만 추출하기
  3. if else 와 if 헷갈리지 말기@@
   - if else는 if문 이 아닐 경우, if문을 계속쓰는건 해당 경우에는 무조건 체크.
*/
