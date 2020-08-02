function count3(num) {
  return num.toLocaleString();
}

function solution4(num) {
  let words = ["", "만", "억"];
  let splitUnit = 10000;
  let cnt = words.length;
  let ans = [];
  let str = "";

  for (let i = 0; i < cnt; i++) {
    //예 1234565789이면
    // 6789, 2345, 1로 쪼개짐 (뒤에서부터 4개씩 우와...)
    let unit = (num % Math.pow(splitUnit, i + 1)) / Math.pow(splitUnit, i);
    unit = Math.floor(unit);
    // 이걸함으로써, 10000 단위로 쪼갠값이 0이면 그 값은 제외시킬 수 있음!!
    if (unit > 0) {
      ans[i] = unit;
    }
  }

  for (let i = 0; i < ans.length; i++) {
    // 0인값은 단위를 붙여줄 필요가 없으니까.. continue
    if (!ans[i]) continue;
    str = String(count3(ans[i])) + words[i] + str;
  }

  return str;
}

console.log(solution4(10000));
console.log(solution4(123));
console.log(solution4(123456541230));
console.log(solution4(9876543210));
