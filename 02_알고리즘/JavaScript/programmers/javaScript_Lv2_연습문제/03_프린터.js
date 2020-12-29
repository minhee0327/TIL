function solution(priorities, location) {
  let cnt = 0;
  let idx_arr = new Array(priorities.length).fill(0);
  idx_arr = idx_arr.map((v, i) => i);

  while (true) {
    if (priorities[0] === Math.max(...priorities)) {
      cnt++;
      if (idx_arr[0] === location) {
        return cnt;
      } else {
        priorities.shift();
        idx_arr.shift();
      }
    } else {
      idx_arr.push(idx_arr.shift());
      priorities.push(priorities.shift());
    }
  }
}
