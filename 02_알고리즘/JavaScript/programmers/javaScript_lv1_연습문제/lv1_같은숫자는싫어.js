function solution(arr) {
  var idx = 0;

  while (idx !== arr.length) {
    if (arr[idx] === arr[idx + 1]) {
      arr.splice(idx, 1);
    } else {
      idx += 1;
    }
  }

  return arr;
}

console.log(solution([1, 1, 3, 3, 0, 1, 1]));
console.log(solution([4, 4, 4, 3, 3]));

/*효율성 체크에서 떨어진 코드.. splice를 쓰면서 시간이 많이 잡힌건가..*/

function solution2(arr) {
  var answer = [];
  var now = arr[0];
  answer.push(now);

  for (var i = 1; i < arr.length; i++) {
    if (now !== arr[i]) {
      now = arr[i];
      answer.push(arr[i]);
    }
  }
  return answer;
}

console.log(solution2([1, 1, 3, 3, 0, 1, 1]));
console.log(solution2([4, 4, 4, 3, 3]));

/*fliter함수*/
function solution3(arr) {
  return arr.filter((v, idx) => v != arr[idx + 1]);
}
console.log(solution3([1, 1, 3, 3, 0, 1, 1]));
console.log(solution3([4, 4, 4, 3, 3]));
