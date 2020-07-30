function solution(arr1, arr2) {
  var ans = [];
  for (var i = 0; i < arr1.length; i++) {
    var temp = [];
    for (var j = 0; j < arr1[i].length; j++) {
      temp.push(arr1[i][j] + arr2[i][j]);
    }
    ans.push(temp);
  }
  return ans;
}

console.log(solution([[1], [2]], [[3], [4]]));

function solution1(arr1, arr2) {
  return arr1.map((a, i) => a.map((b, j) => b + arr2[i][j]));
}
console.log(solution1([[1], [2]], [[3], [4]]));
