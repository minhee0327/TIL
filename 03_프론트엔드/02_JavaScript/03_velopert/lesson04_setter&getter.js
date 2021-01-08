const numbers = {
    _a: 1,
    _b: 2,
    sum: 3,
    caculate() {
        console.log('calculate');
        this.sum = this._a + this._b;
    },
    get a() {
        return this._a
    },
    get b() {
        return this._b
    },
    set a(value) {
        console.log('a가 바뀝니다.');
        this._a = value
        this.caculate();
    },
    set b(value) {
        console.log('b가 바뀝니다.');
        this._b = value
        this.caculate();
    }
}