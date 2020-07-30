function solution(arr) {
  if (arr.length <= 1) {
    return [-1];
  } else {
    var min_v = arr.reduce((a, c) => (a > c ? c : a));
    return arr.filter((i) => i !== min_v);
  }
}
