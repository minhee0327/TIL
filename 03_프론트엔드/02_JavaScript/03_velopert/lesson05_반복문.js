//for ... of
// 배열에 관한 반복문 돌리기
console.log('--------------for of------------------')
let numbers = [10, 8, 2, 4, 5]
for (let number of numbers) {
    console.log(number);
}

console.log('--------------for in------------------')

// for ... in
// 객체를 위한 반복문
const doggy = {
    'name': '멍멍이',
    'sound': '왈왈!',
    age: 2
}

console.log(Object.entries(doggy)); // [k,v]
console.log(Object.keys(doggy)); // k 값들
console.log(Object.values(doggy)); // v 값들

for (let key in doggy) {
    console.log(`${key}: ${doggy[key]}`)
}