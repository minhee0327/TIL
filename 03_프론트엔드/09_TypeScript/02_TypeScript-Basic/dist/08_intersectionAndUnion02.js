function isAction(v) {
    return v.do !== undefined;
}
function process(v) {
    if (isAction(v)) {
        v.do();
    }
    else {
        console.log(v.name);
    }
}
//# sourceMappingURL=08_intersectionAndUnion02.js.map