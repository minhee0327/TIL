function showPrime(n) {
    nextPrime: for (let i = 2; i < n; i++) {
        for (let j = 2; j < i; j++) {
            if (i % j == 0) continue nextPrime
        }
        alert(i)
    }
}

// showPrime(10);

// js label : 반복문 제어
// i % j인 경우 nextPrime으로 돌아감.
// 그게 아니고 i == j가 된 경우 alert출력하고 nextPrime쪽으로.
// label사용한 부분을 함수로 구현(아래)

function showPrime2(n) {
    for (let i = 2; i < n; i++) {
        if (!isPrime(i)) continue
        alert(i)
    }
}

function isPrime(n) {
    for (let i = 2; i < n; i++) {
        if (n % i == 0) return false
    }
    return true
}

showPrime2(10);