/* 전위증가 후위증가 예측(주석), 결과(콘솔) */

let a = 2;
const r1 = a++ + a++; //2 + 3 = 5
console.log("r1:", r1);
const r2 = ++a + ++a; //5 + 6 = 11
console.log("r2:", r2);
const r3 = a++ + ++a; //6 + 8 = 14
console.log("r3:", r3);
const r4 = ++a + a++; //9+ 9 = 18
console.log("r4:", r4);

let b = 10;
const r5 = b-- + b--; //10 + 9 = 19
console.log("r5:", r5);
const r6 = --b + --b; //7 + 6 = 13
console.log("r6:", r6);
const r7 = b-- + --b; //6 + 4 = 10
console.log("r7:", r7);
const r8 = --b + b--; //3 + 3 = 6
console.log("r8:", r8);
