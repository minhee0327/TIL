function solution(Pcnt, amonut) {
  let dutch = parseInt(amonut / Pcnt);
  let ans = Array(Pcnt).fill(dutch);
  ans[0] += parseInt(amonut % Pcnt);

  return ans;
}

console.log(solution(2, 2));
console.log(solution(3, 4));
console.log(solution(10, 13500));
console.log(solution(4, 11003));
console.log(solution(3, 9850));
