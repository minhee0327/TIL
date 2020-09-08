class LocalDB {
    constructor(localStorageKey) {
        this.localStorageKey = localStorageKey;
    }
    add(v) {
        if (typeof window != 'undefined')
            localStorage.setItem(this.localStorageKey, JSON.stringify(v));
    }
    get() {
        if (typeof window != 'undefined') {
            const v = localStorage.getItem(this.localStorageKey);
            return v ? JSON.parse(v) : null;
        }
    }
}
const userDB = new LocalDB('user');
userDB.add({ name: 'jay' });
const userA = userDB.get();
console.log(userDB);
console.log(userA);
console.log(userA.name);
//# sourceMappingURL=07_제네릭2.js.map