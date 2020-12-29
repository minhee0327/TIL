function solution(n) {
  let ans = 0;
  let pivot = n;
  let one = pivot
    .toString(2)
    .split("")
    .filter((x) => x === "1").length;

  while (true) {
    n++;
    let n_one = n
      .toString(2)
      .split("")
      .filter((i) => i === "1").length;

    if (one === n_one) {
      ans = n;
      break;
    }
  }
  return ans;
}

console.log(solution(78));
console.log(solution(15));

/* 정규식을 많이 써본편은 아니라서 잘 안썼는데, 간단하기때문에 연습해봅니다. */
function solution1(n) {
  let size = n.toString(2).match(/1/g).length;
  while (n++) {
    if (size === n.toString(2).match(/1/g).length) return n;
  }
}
