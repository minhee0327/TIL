function solution(n) {
  var cnt = 0;
  while (n !== 1) {
    if (cnt >= 500) {
      return -1;
    }
    if (n % 2) {
      n = n * 3 + 1;
    } else {
      n = Number(n / 2);
    }
    cnt += 1;
  }
  return cnt;
}
