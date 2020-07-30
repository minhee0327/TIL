function solution(n) {
  return (n + "")
    .split("")
    .map((i) => i * 1)
    .reverse();
}
