function solution(numbers, hand) {
  var ans = "";
  var h_idx = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
    "*": [3, 0],
    0: [3, 1],
    "#": [3, 2],
  };
  var l_idx = h_idx["*"],
    r_idx = h_idx["#"];

  for (var i of numbers) {
    if (i === 1 || i === 4 || i === 7) {
      l_idx = h_idx[i];
      ans += "L";
    } else if (i === 3 || i === 6 || i === 9) {
      r_idx = h_idx[i];
      ans += "R";
    } else if (i === 2 || i === 5 || i === 8 || i === 0) {
      var l_diff =
        Math.abs(h_idx[i][0] - l_idx[0]) + Math.abs(h_idx[i][1] - l_idx[1]);
      var r_diff =
        Math.abs(h_idx[i][0] - r_idx[0]) + Math.abs(h_idx[i][1] - r_idx[1]);

      if (l_diff === r_diff) {
        if (hand === "right") {
          ans += "R";
          r_idx = h_idx[i];
        } else if (hand === "left") {
          ans += "L";
          l_idx = h_idx[i];
        }
      } else if (l_diff < r_diff) {
        ans += "L";
        l_idx = h_idx[i];
      } else if (l_diff > r_diff) {
        ans += "R";
        r_idx = h_idx[i];
      }
    }
  }

  return ans;
}

console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"));
console.log(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"));
console.log(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"));
