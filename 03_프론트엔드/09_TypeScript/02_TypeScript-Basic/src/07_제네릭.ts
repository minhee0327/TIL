/*
- 제네릭
    - 타입을 파라미터화 할 수 있고
    - 한가지 타입 뿐만 아니라 다양한 타입 지원한다.
    - 다양한 유형에 대해 작동할 수 있는 구성요소.
    - any랑은 뭐가 다를까 고민해봤는데,
        - any를 사용하면 실제로 함수가 반환할 때 어떤 타입인지에 대한 정보를 잃게 된다고 함.
    - 반환되는 타입을 캡쳐하는 방법이라고 생각하면 좋을 것 같다. 
    - user가 준 타입을 캡쳐해서 이정보를 나중에 사용할 수 있도록함.
*/

function createPromise<T>(x: T, timeout: number) {
    return new Promise((resolve: (v: T) => void, reject) => {
        //return new Promise<T>((resolve, reject)=>{
        setTimeout(() => {
            resolve(x);
        }, timeout);
    });
}

createPromise(1, 100).then((v) => console.log(v));
createPromise<string>('asdf', 100).then((v) => console.log(v));

/* 
- 함수의 파라미터를 여러가지 정의할 수 있는것 처럼
- 타입파라미터(제네릭) 또한 여러번 정의할 수 있다.
*/

function createTuple2<T, U>(v1: T, v2: U): [T, U] {
    return [v1, v2];
}

//t1의 0번째 인덱스에 대한 메서드는 string과 관련된것만,
//1번째 인덱스에서는 number와 관련된 것만 뜨는것 확인가능
const t1 = createTuple2('user1', 10000);

function createTuple3<T, U, D>(v1: T, v2: U, v3: D): [T, U, D] {
    return [v1, v2, v3];
}

const t2 = createTuple3(true, 'user1', 10000);
