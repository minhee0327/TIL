// filter() 및 람다 사용하여 짝수 함수 구하기
// 시간복잡도는 array1.js와 동일하다.

function removeEven(arr) {
    return arr.filter(v => v % 2 != 0)
}

console.log(removeEven([1, 2, 4, 5, 10, 6, 3]))