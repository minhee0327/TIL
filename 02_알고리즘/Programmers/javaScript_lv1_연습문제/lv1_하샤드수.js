function solution(x) {
  if (x % harshad(x)) {
    return false;
  } else {
    return true;
  }
}

function harshad(x) {
  return (x + "").split("").reduce((a, c) => a + Number(c), 0);
}
