const a = { id: 1, title: "sample1" };
const b = { id: 1, title: "sample1" };

console.log(a === b); //false: 객체는 가리키고 있는 것이 다르기 때문에 내부의 값이 같더라도 서로 다르다.

/*NaN : Not a number */
// 표현불가능한 수치형 결과
// 또한 자기 자신과도 일치하지 않는 유일한 값
// 예: 0/0, "문자"*100, Math.sqrt(-9)와 같은 허수
console.log(NaN === NaN); // false
console.log(NaN == NaN); // false

// 숫자 값이긴 한데, 컴퓨터로는 표현 불가능한 숫자값.
console.log(NaN, typeof NaN); //NaN number

//NaN인지 체크하는 함수: isNaN()
