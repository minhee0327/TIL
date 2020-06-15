// 값에 따라 변수의 타입이 바뀜 => Dynamic Type Language.
// 런타임에 실행되다가, 다른값이 들어와서 문제될 수 있음. 주의
// 변수가 가지는 고정타입이 없다.(타입이 없는 것은 아니다.)
let whatever = 'Mark';
whatever = 37;
whatever = true;

console.log('--------- example01: boolean ----------');
//Boolean (true, false)
const isTrue = true;
const isFalse = false;
console.log(isTrue, typeof (isTrue)); //true boolean
console.log(isFalse, typeof (isFalse)); //false boolean

// a는 primitive boolean이 아닌, object
const a = new Boolean(false);
console.log(a, typeof (a)); //[Boolean:false] object
//따라서 true로 판단이 됨
if (a) {
    console.log('false?')
}
//Primitive boolen 형태
const b = Boolean(false);
console.log(b, typeof (b)); //false boolean
//false로 인식해서 출력 안된다.
if (b) {
    console.log('fasle?')
}


console.log('--------- example02: null & undefined ----------');
//NULL 
const c = null;
console.log(c, typeof c);

//undefined
let d;
console.log(d, typeof d);
d = undefined;
console.log(d, typeof d);

//null undefined compare
if (c == d) {
    console.log('출력됨', c == d);
}
if (c === d) { //js에서는 타입까지 비교할 때 === 사용
    console.log('출력안됨', c === d);
}


console.log('--------- example03: number ----------');
const e = 37;
console.log(e, typeof e);
const f = 96.7;
console.log(f, typeof f);
const g = NaN; //Not a Number
console.log(g, typeof g);
const h = Number('Minhee');
console.log(h, typeof h);
const i = Number('37'); //string to number
console.log(i, typeof i); //37 number


console.log('--------- example04: String ----------');
const j = 'Minhee';
console.log(j, typeof j);
const k = 'Minhee' + 'Kang'; //문자열끼리 합
console.log(k, typeof k);
const l = `${j} Kang`; //template string
console.log(l, typeof l);


console.log('--------- example05: Symbol(ES6) ----------');
// new keyword 사용X
// 고유한 값을 만들고 싶을때 사용
const m = Symbol();
const n = Symbol(37);
const o = Symbol('Minhee');
const p = Symbol('Minhee');

console.log(m, typeof m);
console.log(o === p);

//new Symbol() //error: Symbol is not a constructor