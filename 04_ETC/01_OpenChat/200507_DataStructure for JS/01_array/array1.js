// 배열에서 모든 짝수를 제거하는 함수 만들기

function removeEven(arr) {
    var odds = []
    for (let number of arr) {
        if (number % 2 != 0) {
            odds.push(number)
        }
    }
    return odds
}

console.log(removeEven([1, 2, 4, 5, 10, 6, 3]))