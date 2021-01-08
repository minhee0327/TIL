const SYM = Symbol();
const o = { a: 1, b: 2, c: 3, [SYM]: 4 };

//배열에 사용하는 것은 비추.
console.log("---------For in--------");
for (let prop in o) {
  if (!o.hasOwnProperty(prop)) continue;
  console.log(`${prop} : ${o[prop]}`);
}

console.log("---------Object.keys()--------");
Object.keys(o).forEach((prop) => console.log(`${prop} : ${o[prop]}`));
