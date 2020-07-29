let count = 10; //숫자리터럴
const blue = 0x0000ff; //16진수 ff => 10진수 255
const umask = 0o0022; //8진수 22 => 10진주 18
const roomTemp = 21.5;
const c = 3.0e6; //지수
const e = -1.6e-19; //지수
const inf = Infinity;
const ninf = -Infinity;
const nan = NaN; //숫자아님

console.log(count, typeof count);
console.log(blue, typeof blue);
console.log(umask, typeof umask);
console.log(roomTemp, typeof roomTemp);
console.log(c, typeof c);
console.log(e, typeof e);
console.log(inf, typeof inf);
console.log(ninf, typeof ninf);
console.log(nan, typeof nan);

console.log("----------------------------");

const small = Number.EPSILON;
console.log(small);
//표현 가능한 가장 큰 정수
const bigInt = Number.MAX_SAFE_INTEGER;
console.log(bigInt, typeof bigInt);
//표현 가능한 가장 큰 수
const max = Number.MAX_VALUE;
console.log(max, typeof max);
//표현가능한 가장 작은 정수
const minInt = Number.MIN_SAFE_INTEGER;
console.log(minInt, typeof minInt);
// 표현 가능한 가장 작은 수
const min = Number.MIN_VALUE;
console.log(min, typeof min);
// -Infinity
const nInf = Number.NEGATIVE_INFINITY;
//NaN
const nan = Number.NaN;
// +Infininty
const inf = Number.POSITIVE_INFINITY;
