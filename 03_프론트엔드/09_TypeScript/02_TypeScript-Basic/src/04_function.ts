//함수의 반환되는 타입을 명시적으로 하지 않더라도 함수의 바디 내용을 가지고 추론한다. (이 경우 생략 가능)
//strict하게 명시적으로 타입 annotation을 붙여서 사용할 수도 있다.
// 매개변수는 반드시 타입을 지정해주어야한다.
function add(x: number, y: number): number {
    return x + y;
}

const res = add(1, 2);

// ? 키워드를 가지고, optional하게 매개변수를 받을 수 있다.
function buildUserInfo(name?: string, email?: string) {
    return { name, email };
}

const user = buildUserInfo();

// default 설정을 할 경우, type을 지정하거나, 옵션을 넣을 필요가 없다.
function MakeUserInfo(name = '-', email = '-') {
    return { name, email };
}
const user2 = MakeUserInfo();

//화살표함수 또한 type annotaion 사용 가능하다.
const add2 = (a: number, b: number): number => a + b;

//함수의 오버로딩
//문자열을 타입 어노테이션으로 사용할 수도 있다.
interface Storage {
    a: string;
}
interface ColdStorage {
    b: string;
}
// 함수시그니처: 함수에 대한 바디 없이 이름, 매개변수타입, 반환되는 값의 타입만 정의한 것을 뜻함.
// 동일한 이름으로 여러번 정의하는 것을 함수 오버로드 시그니처라고한다.
function store(type: '통조림'): Storage;
function store(type: '아이스크림'): ColdStorage;
//위에까지만 선언하면 error: 함수 구현이 없거나 선언 바로 다음에 나오지 않습니다

//union type으로 매개변수 작성 후 body를 구현해주어 error 해결
function store(type: '통조림' | '아이스크림') {
    if (type === '통조림') {
        return { a: '통조림' };
    } else if (type === '아이스크림') {
        return { b: '아이스크림' };
    } else {
        throw new Error('지원되지 않는 저장매체');
    }
}

const i = store('아이스크림');
i.b; //a 속성은 나올수가 없음
