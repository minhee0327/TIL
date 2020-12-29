function solution(d, budget) {
  var cnt = 0;

  var sort_budget = d.sort((a, b) => a - b);

  for (var i of sort_budget) {
    if (i <= budget) {
      budget -= i;
      cnt += 1;
    } else {
      break;
    }
  }

  return cnt;
}

console.log(solution([1, 3, 2, 5, 4], 9));
console.log(solution([2, 2, 3, 3], 10));

var solution2 = (d, b) =>
  d.sort((a, b) => a - b).filter((x) => (b - x >= 0 ? ((b = b - x), 1) : 0))
    .length;
console.log(solution2([1, 3, 2, 5, 4], 9));
console.log(solution2([2, 2, 3, 3], 10));
