class D {
    add(v) {
        throw new Error('Method not implemented.');
    }
    get() {
        throw new Error('Method not implemented.');
    }
}
class localDB {
    constructor(localKeys) {
        this.localKeys = localKeys;
    }
    add(v) {
        if (typeof window != 'undefined')
            localStorage.setItem(this.localKeys, v.serialize());
    }
    get() {
        if (typeof window != 'undefined') {
            const v = localStorage.getItem(this.localKeys);
            return v ? JSON.parse(v) : null;
        }
    }
}
const cart4 = {
    getItem() {
        return {
            m: '',
        };
    },
};
cart4.getItem();
//# sourceMappingURL=07_제네릭3.js.map