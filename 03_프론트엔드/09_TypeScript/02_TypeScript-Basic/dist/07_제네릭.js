function createPromise(x, timeout) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(x);
        }, timeout);
    });
}
createPromise(1, 100).then((v) => console.log(v));
createPromise('asdf', 100).then((v) => console.log(v));
function createTuple2(v1, v2) {
    return [v1, v2];
}
const t1 = createTuple2('user1', 10000);
function createTuple3(v1, v2, v3) {
    return [v1, v2, v3];
}
const t2 = createTuple3(true, 'user1', 10000);
//# sourceMappingURL=07_제네릭.js.map