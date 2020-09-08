/*
- ts에서는 접근제한자가 있음 
    - private, protected, public
    - private: class 내부에서만 접근 가능 상속한 class에서도 사용불가,  인스턴스에서 접근 불가
    - protected: class 내부 접근 가능 및 상속을 한 class에서 사용가능, 인스턴스에서 접근 불가
    - public: 모두 접근 가능
    - 명시하지 않았을 경우에는 public

- 생성자 정의할 때, 매개변수에 접근제한자를 같이 쓰면, 속성 정의와 동시에 할당할 수 있다.
*/

interface User {
    name: string;
}
interface Product {
    id: string;
    price: number;
}

class Cart {
    //클래스 바디 내부에 속성에 대한 정의를 한 후,
    // protected user: User;
    // private store: object;

    constructor(protected user: User = user, private store: Product) {
        // 정의된 속성에 할당을 하거나 (아니면 매개변수에 작성해서 선언과동시에 할당할 수 있다.)
        // this.user = user;
        // this.store = {};
    }
    public put(temp: Product) {
        this.store.id = temp.id;
        // this.store[id] = temp.id; //error
        //error: 처음에 강의안대로 id를 매개변수로받아서 타입을 string으로 설정하고 했는데,
        //빈객체에서는 형식이 string인 것을 읽을 수 없다는 등의 msg가 나왔다.
        //그래서 constructor의 store를 Product interface로 설정하고,
        //매개변수로 받아온temp의 id를 설정하는 방식으로 작성했다.
    }
    get(id: string) {
        return this.store.id;
    }
}

class PromotionCart extends Cart {
    addPromotion() {
        this.user;
    }
}

let cart1 = new Cart({ name: 'john' }, { id: '1', price: 2000 });
let cart2 = new Cart({ name: 'jay' }, { id: '2', price: 3000 });
console.log(cart1);
console.log(cart2);

let cart3 = new PromotionCart({ name: 'mini' }, { id: '3', price: 1000 });
console.log(cart3);

/*
- 강의안 구매시점이 작년이라 그런가 그 사이에 업데이트가 조금 된 것 같다..
- 그래서 입맛에 맞추어 조금 코드를 수정했다..
*/
