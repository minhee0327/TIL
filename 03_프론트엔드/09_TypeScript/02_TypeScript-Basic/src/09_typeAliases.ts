/*
- Type Aliases(타입별칭)
    - 인터페이스와 비슷하다.
    - 작성한 타입에 이름을 붙일 수 있다.
    - 키워드 'type'
    - 다양한 타입들에 대해서 별칭을 줄 수 있다.
*/
interface User {
    name: string;
}
interface Action {
    do(): void;
}
// intersection, union한 것을 type aliases로 별칭을 만들어서 사용가능
type UserAction = User & Action;
function createUserAction2(): UserAction {
    return {
        do() {},
        name: '',
    };
}

type StringOrNumber = string | number;
type Arr<T> = T[]; //T를 캡쳐에서 T배열 반환
type P<T> = Promise<T>;

//interface처럼 사용되기도 함
type User2 = {
    name: string;
    login(): boolean;
};
class UserImpl implements User2 {
    name: string;
    login(): boolean {
        throw new Error('Method not implemented.');
    }
}

type UserState = 'PENDING' | 'APPROVED' | 'REJECTED';

function checkUSer(user: User2): UserState {
    if (user.login()) {
        return 'APPROVED';
    } else {
        return 'REJECTED';
    }
}
