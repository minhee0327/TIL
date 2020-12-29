function solution(numbers) {
  let filter_zero = numbers.filter((x) => x === 0);
  if (filter_zero.length === numbers.length) {
    return "0";
  }
  return numbers
    .map((x) => x + "")
    .sort((a, b) => b + a - (a + b))
    .join("");
}
