class LocalDB<T> {
    constructor(private localStorageKey: string) {}
    add(v: T) {
        if (typeof window != 'undefined') localStorage.setItem(this.localStorageKey, JSON.stringify(v));
    }
    get(): T {
        //localStrorage is not defind 라는 문구가 계속 떠서, 찾아봄
        //서버에서 렌더링할 때, 브라우저가 없기 때문에 브라우저에서 제공하는 모든 API에 접근 불가.
        // 따라서 서버와 클라이언트 모두에서 실행되는 js코드에는 window를 정의하고 보호되고 있는지 확인하는것이 일반적.
        //window는 브라우저에서 제공되는 모든 API에 대해 브라우저에서 제공하는 루트 개체
        if (typeof window != 'undefined') {
            const v = localStorage.getItem(this.localStorageKey);
            return v ? JSON.parse(v) : null;
        }
    }
}

interface User {
    name: string;
}

const userDB = new LocalDB<User>('user');
userDB.add({ name: 'jay' });
const userA = userDB.get();
console.log(userDB);
console.log(userA); //서버로 실행시 error => 브라우저에서 확인(genericTest.html)
console.log(userA.name);
