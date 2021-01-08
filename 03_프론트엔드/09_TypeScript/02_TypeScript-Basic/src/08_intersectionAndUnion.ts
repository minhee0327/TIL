interface User {
    name: string;
}
interface Action {
    do(): void;
}

//1. intersection: 기존타입을 합친 타입이 필요할때 사용하면 좋다.
function createUserAction(u: User, a: Action): User & Action {
    return { ...u, ...a };
}
const u = createUserAction({ name: 'mini' }, { do() {} });

//4.runtime error 방지 위해서 overloading
//참고) 함수의 반환형식이 지정되어있지 않아서 추론가능한 number로 명시해주었다.
function compare(x: string, y: string): number;
function compare(x: number, y: number): number;

//2.union type: 둘 중 하나의 타입을 사용할 수 있도록함.(or)
//단, 사용가능한 method는 두 타입에 모두 존재하는 메서드만 사용가능.
function compare(x: string | number, y: string | number) {
    //number끼리 계산하고 싶다 => type guard 해야함
    //이렇게하면, number에서 사용가능한 모든 method 사용할 수 있음.
    if (typeof x === 'number' && typeof y === 'number') {
        return x === y ? 0 : x > y ? 1 : -1;
    }
    //마찬가지로 string끼리 계산하고싶다 => 타입가드
    //이렇게하면 string타입에서 사용가능한 모든 method를 사용할 수 있다.
    if (typeof x === 'string' && typeof y === 'string') {
        return x.localeCompare(y);
    }
    //두 타입이 같지 않으면 error 발생시켜보기
    throw Error('not supported type');
}

// 3. compile error는 피할 수 있지만 같은 타입이 아니기 때문에 런타임시 error
// const v = compare('a', 1);

// 4. 런타임 에러 방지를 위해서, 함수 overloading(위4.확인) 을 하게 되면, 컴파일단에서 error를 확인할 수 있음
const v1 = compare(2, 1);
const v2 = compare('a', 'b');

console.log([3, 2, 1].sort(compare)); //[1,2,3]
console.log(['d', 'c', 'b', 'a'].sort(compare)); //[ 'a', 'b', 'c', 'd' ]
