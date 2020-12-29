function solution(number, k) {
  let stack = [];

  for (let i = 0; i < number.length; i++) {
    let now = number[i];

    while (k > 0 && stack[stack.length - 1] < now) {
      stack.pop();
      k--;
    }
    stack.push(now);
  }
  stack.splice(stack.length - k, k);

  return stack.join("");
}

console.log(solution("1924", 2));
console.log(solution("1231234", 3));
console.log(solution("4177252841", 4));
