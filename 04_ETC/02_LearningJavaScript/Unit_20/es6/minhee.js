module.exports = {
    geometricsum(a, x, n) {
        if (x === 1) return a * n
        return a * (1 - Math.pow(x, n)) / (1 - x)
    },
    arithemticSum(n) {
        return (n + 1) * n / 2
    },
    quadraticFormula(a, b, c) {
        const D = Math.sqrt(b * b - 4 * a * c)
        return [(-b + D) / (2 * a), (-b - D) / (2 * a)]
    },
}

/*
//단축문법 (객체를 내보낼때만 가능. 다른 경우에는 위와같이 module.exports 형태로 내보낸다.)
exports.geometricSum = function (a,x,n){
    if (x === 1) return a * n
    return a * (1 - Math.pow(x, n)) / (1 - x)
}

*/