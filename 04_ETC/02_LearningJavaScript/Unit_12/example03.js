class Fibo {
  [Symbol.iterator]() {
    let a = 0,
      b = 1;
    return {
      next() {
        let temp = { value: b, done: false };
        b += a;
        a = temp.value;
        return temp;
      },
    };
  }
}

const fibo = new Fibo();
let i = 0;
for (let n of fibo) {
  console.log(n);
  if (++i > 9) break;
}
