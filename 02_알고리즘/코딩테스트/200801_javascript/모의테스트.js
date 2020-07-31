console.log("========== Q2 ===========");
//숫자만 숫자타입으로 출력하기.(문자, 쉼표 등 모두 제외)
function getAmount(text) {
  return Number(
    text
      .split("")
      .map((t) => (isNaN(t * 1) ? null : t))
      .join("")
  );
}

console.log(getAmount("$1,250"));
console.log(getAmount("5021USD"));
console.log(getAmount("3000KRW"));

console.log("=========== Q3============");
// 연산자에 따라서 합, 곱 구하기
function calculate(type, operands) {
  if (type === "add") {
    return sum(operands);
  } else if (type === "multiply") {
    return multiply(operands);
  }
}

function sum(lst) {
  return lst.reduce((a, b) => a + b, 0);
}
function multiply(lst) {
  return lst.reduce((a, b) => a * b, 1);
}
console.log(calculate("add", [1, 2]));
console.log(calculate("multiply", [1, 2, 3]));
