//유클리드 호제법 참조
function solution(n, m) {
  return [gcd(n, m), lcm(n, m)];
}

function gcd(n, m) {
  return n % m ? gcd(m, n % m) : m;
}
function lcm(n, m) {
  return Number((n * m) / gcd(n, m));
}
console.log("-----solution1:유클리드 호제법------");
console.log(solution(3, 12));
console.log(solution(2, 5));

// 반복문으로 풀어낸 코드
function solution2(n, m) {
  var min = n > m ? m : n,
    max = n > m ? n : m;
  var answer = [];

  //최대공약수
  for (var i = min; i > 0; i--) {
    if (min % i === 0 && max % i === 0) {
      answer.push(i);
      break;
    }
  }
  //최소공배수
  for (var i = max; i <= max * min; i++) {
    if (i % min === 0 && i % max === 0) {
      answer.push(i);
      break;
    }
  }
  return answer;
}
console.log("-----solution2: 반복문-----");
console.log(solution2(3, 12));
console.log(solution2(2, 5));
