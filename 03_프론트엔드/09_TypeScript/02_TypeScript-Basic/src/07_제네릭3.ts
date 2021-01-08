// 앞장 복습 및 추가사항
interface DB<T> {
    add(v: T): void;
    get(): T;
}
interface User {
    name: string;
}
interface JSONSerializer {
    serialize(): string;
}

class D<T> implements DB<T> {
    add(v: T): void {
        throw new Error('Method not implemented.');
    }
    get(): T {
        throw new Error('Method not implemented.');
    }
}

//generic상속, 특정타입(JSONSerializer)의 하위타입(T)
class localDB<T extends JSONSerializer> implements DB<T> {
    constructor(private localKeys: string) {}
    add(v: T) {
        if (typeof window != 'undefined') localStorage.setItem(this.localKeys, v.serialize());
    }
    get(): T {
        if (typeof window != 'undefined') {
            const v = localStorage.getItem(this.localKeys);
            return v ? JSON.parse(v) : null;
        }
    }
}

//조건부 타입 generic
interface Vegitable {
    v: string;
}
interface Meat {
    m: string;
}
interface Cart2<T> {
    getItem(): T extends Vegitable ? Vegitable : Meat;
}

const cart4: Cart2<Meat> = {
    getItem() {
        return {
            m: '',
        };
    },
};

cart4.getItem();
