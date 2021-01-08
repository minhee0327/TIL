function solution(n, arr1, arr2) {
  var newArr = Array(n);
  for (var i = 0; i < n; i++) {
    var temp = arr1[i];
    arr1[i] = Lpad(n, temp.toString(2));
    temp = arr2[i];
    arr2[i] = Lpad(n, temp.toString(2));

    temp = "";
    for (var j = 0; j < n; j++) {
      if (arr1[i][j] === "1" || arr2[i][j] === "1") {
        temp += "#";
      } else if (arr1[i][j] === "0" && arr2[i][j] === "0") {
        temp += " ";
      }
    }
    newArr[i] = temp;
  }
  return newArr;
}

function Lpad(n, str) {
  while (str.length < n) {
    str = "0" + str;
  }
  return str;
}

console.log(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]));
console.log(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]));
