interface User {
    name: string;
}
interface Action {
    do(): void;
}

//3.사용자 정의 타입가드
function isAction(v: User | Action): v is Action {
    // do라는 속성이 있으면 true반환 (Action 이다.)
    return (<Action>v).do !== undefined;
}

//1.v의 타입을 가지고 타입가드를 하고싶은데, interface는 JS에 존재하지 않음
//typeof 연산자도 JS만 있음
//User, Action은 class도 아님(instanceof로 접근 불가)

//2.Type Assertion(타입 단언): 특정 변수에 대해 타입에 대해 개발자가 확정지어준다.(힌트를준다)
//그리고나서 v라는 값 안에 member를 체크하면 된다!
//그런데 매번 타입단언을 하는것은 코드의 량이 어마무시하게 늘어나는일! ㅠㅠ 안되..!!!
// => 타입가드 사용자 정의를 할 수 있다!!(isAction함수 참조)
function process(v: User | Action) {
    // if((<Action>v).do){
    //     (<Action>v).do
    // }

    if (isAction(v)) {
        v.do();
    } else {
        console.log(v.name);
    }
}
