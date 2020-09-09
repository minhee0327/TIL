/*
- indexType
    - 속성의 이름이 정해져있지 않고, 동적으로 처리해야할 때 사용
*/

interface Props {
    //index signature의 타입은 string | number만 가능
    [key: string]: string;
    //속성을 고정시키고 싶을 때
    name: string;
}

const p: Props = {
    a: 'd',
    b: '2',
    // c: 3, //error: 숫자니까
    0: 'd',
    2: 'b',
    name: 'mini',
};

p[0];
p.name;
p.a;

let keys: keyof Props; // string |number

interface User3 {
    name: string;
    age: number;
    hello(msg: string): void;
}

let keys2: keyof User; //"name"|'age"|"hello"

let helloMethod: User3['hello'];
helloMethod = function (msg: string) {};
