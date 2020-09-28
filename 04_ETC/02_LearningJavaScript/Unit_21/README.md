# 객체 프로퍼티와 프록시

-   ### 접근자 프로퍼티(setter, getter)

    -   기존에 아래처럼 사용했었음.

    ```js
    class User {
        setEmail(value) {
            if (!/@/.test(value)) throw new Error(`invalid email: ${value}`);
            this[USER_EMAIL] = value;
        }
        getEmail() {
            return this[USER_EMAIL];
        }
    }
    const u = new User();
    u.setEmail('bla@gmail.com');
    cosole.log(u.getEmail());
    ```

    -   단 프로퍼티를 설정하고 읽을때, setEmail(), getEmail()이런식으로 가져와야했음
    -   그래서 접근자 프로퍼티를 사용해서 좀더 사용성 간편하게, 그리고 부주의한 접근을 차단할 수 있도록 할 수 있음.

    ```js
    class User {
        set email(value) {
            if (!/@/.test(value)) throw new Error(`invalid email: ${value}`);
            this[USER_EMAIL] = value;
        }
        get email() {
            return this[USER_EMAIL];
        }
    }
    const u = new User();
    u.email = 'bla@gmail.com';
    cosole.log(u.email);
    ```

    -   함수두개(setter, getter)를 사용하지만, email 프로퍼티 하나에 묶을 수 있다.
    -   setter 없이, getter만 만들수도 있음.(contructor이용해서 읽기전용으로 data를 결정)
    -   getter 없이 setter만 만들수도 있지만, 잘 쓰이지는 않음

-   ### 객체 프로퍼티 속성
    -   `Object.getOwnPropertyDescriptor(객체, 객체의 키값)`
        -   결과: `{value: 해당값 , writable: boolean, enumerable: boolean, configurable: boolean `
        -   writable: 프로퍼티 값 바꾸는 것 가능한지
        -   enumerable: for...in, spread 연산자, objects.keys에서 객체 프로퍼티를 나열할때 해당 프로퍼티 포함유무
        -   configuration: 수정, 삭제 판단
    -   `Object.defineProperty`: configuration이 가능한 경우 새 프로퍼티를 만들 수 있다.
