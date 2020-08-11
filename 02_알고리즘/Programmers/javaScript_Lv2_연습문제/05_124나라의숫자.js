function solution(n) {
  let ans = "";
  while (n) {
    if (n % 3 === 1) {
      ans = 1 + ans;
      n = Math.floor(n / 3);
    } else if (n % 3 === 2) {
      ans = 2 + ans;
      n = Math.floor(n / 3);
    } else if (n % 3 === 0) {
      ans = 4 + ans;
      n = n / 3 - 1;
    }
  }
  return ans;
}
