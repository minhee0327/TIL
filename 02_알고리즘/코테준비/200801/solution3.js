//내장함수
function solution3(num) {
  return num.toLocaleString();
}

console.log(solution3(1));
console.log(solution3(1234));
console.log(solution3(1234567));

//제출
function solution3_1(num) {
  let len, idx, str;

  num += "";
  idx = num.length % 3;
  len = num.length;

  str = num.substring(0, idx);
  while (idx < len) {
    if (str != "") str += ",";
    str += num.substring(idx, idx + 3);
    idx += 3;
  }

  return str;
}
