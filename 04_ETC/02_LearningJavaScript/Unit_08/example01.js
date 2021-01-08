/* concat */
const arr = [1, 2, 3];
arr.concat(4, 5, 6);
console.log(arr); //기존 배열 유지([1,2,3])

/* splice: 요소 제거 혹은 추가 */
console.log("-----splice----");
const arr1 = [1, 5, 7];
arr1.splice(1, 0, 2, 3, 4);
console.log(arr1);
arr1.splice(5, 0, 6);
console.log(arr1);
arr1.splice(1, 2);
console.log(arr1);
arr1.splice(2, 1, "a", "b");
console.log(arr1);

/*copyWith: 배열요소 복사해서 다른위치에 붙여넣기(기존 요소 덮어씌움) */
//첫번째 매개변수: 복사한 요소를 붙여넣을 위치
//두번째 매개변수: 복사 시작위치
//세번째 변수: 복사를 끝낼위치
console.log("------- copyWith ------");
const arr2 = [1, 2, 3, 4];
arr2.copyWithin(1, 2); //1 3 4 4
console.log(arr2);
arr2.copyWithin(2, 0, 2); //1,3,1,3
arr2.copyWithin(0, -3, -1); //3,1,1,3

/*Array.fill()*/
// fill첫번째 매개변수: 채울 값
// 두번째 매개변수: 넣고자하는 시작점
// 세번째 매개변수: 넣고자하는 끝점
console.log("---------Array.fill------");
const arr3 = new Array(5).fill(1);
arr3.fill("c", 2, 4);
console.log(arr3);
