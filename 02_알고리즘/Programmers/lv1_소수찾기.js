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
/* 별도로 한번 더 찾고 upload합시다. */
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
