/* 통과안됨: 효율성 테스트 떨어짐. */
/* 대부분 코드 작성한 것들이 효율성 테스트에서 시간을 넘겨서 참고함. */
function solution(n) {
  var answer = 0;

  for (var i = 2; i <= n; i++) {
    findPrime(i) ? answer++ : null;
  }
  return answer;
}

function findPrime(n) {
  if (n == 1) {
    return false;
  }
  if (n == 2) {
    return true;
  }
  for (let i = 2; i <= Math.ceil(Math.sqrt(n)); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}

console.log(solution(10));

/* 아래 코드는 통과한 코드, 에리스토스테네스의 채를 이해해햐하는데, 잘 이해가 안됨 */
/* 
1.들어온 숫자의 크기만큼 배열의 크기를 만들고, 처음에는 각 자리의 수들을 담음
2. 2부터 돌면서 0일경우는 넘어가기
3. 0이 아닌경우에는 해당값만큼씩 증가시키면서 배열의 원소들은 0으로 만들어줌 
예: 2만 살려두고 2의 배수들은 다 지워가는 과정.
4. 반복문을 돌면서, 0이 아닌 값들이 있을 때는 ans증가 시켜서 출력 
*/
function solution1(n) {
  let answer = 0;
  let arr = [];

  for (let i = 2; i <= n; i++) {
    arr[i] = i;
  }

  for (let i = 2; i <= n; i++) {
    if (arr[i] === 0) continue;

    for (let j = i + i; j <= n; j += i) {
      arr[j] = 0;
    }
  }

  for (let i = 2; i <= n; i++) {
    if (arr[i] !== 0) answer++;
  }

  return answer;
}

console.log(solution1(10));
