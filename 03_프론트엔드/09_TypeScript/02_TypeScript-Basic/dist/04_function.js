function add(x, y) {
    return x + y;
}
const res = add(1, 2);
function buildUserInfo(name, email) {
    return { name, email };
}
const user = buildUserInfo();
function MakeUserInfo(name = '-', email = '-') {
    return { name, email };
}
const user2 = MakeUserInfo();
const add2 = (a, b) => a + b;
function store(type) {
    if (type === '통조림') {
        return { a: '통조림' };
    }
    else if (type === '아이스크림') {
        return { b: '아이스크림' };
    }
    else {
        throw new Error('지원되지 않는 저장매체');
    }
}
const i = store('아이스크림');
i.b;
//# sourceMappingURL=04_function.js.map