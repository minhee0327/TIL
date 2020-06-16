/*
for (초기화; 반복조건; 반복이 된 후 실행되는 코드) {
    반복되는 코드 블럭
}
*/

for (let i = 0, j = 5; i < 5; i++) {
    console.log(i, j)
}

console.log('---------------------------')
for (let i = 0, j = 2; i < 5; i++, j = j * j) {
    console.log(i, j)
}

console.log('---------------------------')
for (let i = 0; i < 5; i++) {
    console.log(i);
    if (i > 2) {
        break;
    }
    console.log('break ', i);
}

console.log('---------------------------')
for (let i = 0; i < 5; i++) {
    console.log(i);
    if (i < 2) {
        continue;
    }
    console.log('continue ', i);
}

/*
무한루프
for(;;){
    d
}

// 예시
for (; ;) {
    console.log('안녕하세요');
    if (Math.random() * 100 > 90) {
        break;
    }
}
*/

console.log('---------------------------');
while (true) {
    console.log('안녕하세요');
    if (Math.random() * 100 > 90) {
        break;
    }
}

console.log('---------------------------');
/*
do{
    조건이 거짓이 될 때까지 반복실행
}while(조건);
*/
do {
    console.log('안녕하세요')
} while (Math.random * 100 <= 90);


console.log('--------- for of ------------------');
for (const i of [1, 2, 3]) {
    console.log(i);
}

console.log('--------- for in ------------------');
//런타임 환경에 때라 다르게 동작할 수 있기 때문에 주의해서 사용.
// object.prototype.test 로 인해서, test가 출력됨...
Object.prototype.test = function () { };

for (const i in { a: 1, b: 2, c: 3 }) {
    console.log(i);
}