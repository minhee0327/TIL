function solution(n) {
  let temp = [0, 1];
  for (let i = 2; i <= n; i++) {
    temp[i] = (temp[i - 2] + temp[i - 1]) % 1234567;
  }
  return temp[n] % 1234567;
}

// 재귀로 했는데, 시간초과 떠서
// 변수로 a,b를 두고 풀었는데 또 시간초과 떠서
// 배열로 담아서 마지막 값 구했음.
