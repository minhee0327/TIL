const arr = [1, 17, 16, 5, 4, 16, 10, 3, 49];
console.log(arr.find((x, i) => i > 2 && Number.isInteger(Math.sqrt(x))));

//some : 조건에 맞는 요소를 찾으면 즉시 검색 멈추고 true반환
const arr1 = [5, 7, 12, 15, 17];
arr1.some((x) => x % 2 === 0); //true , 12에서 true반환
arr1.some((x) => Number.isInteger(Math.sqrt(x))); // false, 제곱수 없기때문

//every: 모든 요소가 조건에 맞아야 true
//하나라도 조건 충족이 안되면 false
const arr2 = [4, 6, 16, 36];
arr2.every((x) => x % 2 === 0); // true 모두 나눠 떨어짐
arr2.every((x) => Number.isInteger(Math.sqrt(x))); //false (6)
