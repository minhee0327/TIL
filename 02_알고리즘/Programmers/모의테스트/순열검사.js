function solution(arr) {
    let max_val = Math.max(...arr)
    console.log(arr.length, max_val)
    return arr.length === max_val? true: false
}