class localDB {
    constructor(localKeys) {
        this.localKeys = localKeys;
    }
    add(v) {
        if (typeof window != 'undefined')
            localStorage.setItem(this.localKeys, JSON.stringify(v));
    }
    get() {
        if (typeof window != 'undefined') {
            const v = localStorage.getItem(this.localKeys);
            return v ? JSON.parse(v) : null;
        }
    }
}
const testDB = new localDB('user1');
testDB.add({ name: 'mini' });
console.log(testDB.get());
console.log(testDB.get().name);
//# sourceMappingURL=07_제네릭3.js.map