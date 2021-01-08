let numValue: number;
let stringValue: string;
let boolValue: boolean;
let nullValue: null;
let undefinedValue: undefined;
let SymbolValue: symbol;

let objValue: object;

let anyValue: any;

//배열
let stringArray: string[];
let numArray: number[];
let anyArray: any[];

//안라인타입(
//객체에 대한 리터럴 형태로, 값이 아니라 type을 지정
let user1: { name: string; score: number };
user1 = {
    name: 'jay',
    score: 30,
};

//튜플
let tuple2: [number, string];
tuple2 = [1, 'hello'];
let tuple3: [number, boolean, string];
tuple3 = [1, true, 'asdf'];

numValue = 3;
numValue = 3.3;

stringValue = 'hello'; //"", '' 다 됨 (prettier설정을 ''로 해두어서 통일되게 쓰려고함.)
stringValue = `
hello
${1 + 1}
hi
`; //개행 가능, multiline표현가능

boolValue = true;
//undefined와 null은 모든 타입의 하위타입
//즉, 어떠한 타입으로 설정을 했더라도, null, undefined는 사용이 가능함
//하위타입은 상위타입으로 적용된 변수에 할당할 수 있다.
undefinedValue = null;
numValue = undefined;
numValue = null;
//모든 타입의 상위타입은 any타입

anyValue = 1;
anyValue = '1';
anyValue = null;
anyValue = undefined;
anyValue = {};

objValue = { name: 'jay' };
objValue = {};
objValue = new String('hello');

SymbolValue = Symbol();

stringArray = ['hello', 'world', '!!!'];
stringArray.push('alright');

numArray = [1, 2, 3, 4, 5];
