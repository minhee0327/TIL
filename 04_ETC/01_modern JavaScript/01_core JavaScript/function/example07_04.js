function min(a, b) {
    return a >= b ? b : a
}

// alert(min(2, 5))
// alert(min(3, -1))
// alert(min(1, 1))

// js도 let, const, var 키워드 없이 동작하기는 하지만, strict한 상황에서는 오류나니까.주의
function pow(x, n) {
    let ret = 1
    for (let i = 0; i < +n; i++) {
        ret *= x
    }
    return ret
}
let x = prompt("x?", "0");
let n = prompt("n?", "0");
alert(pow(x, n))