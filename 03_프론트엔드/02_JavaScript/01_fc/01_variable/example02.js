// var 함수 스코프
// 따라서 함수 내부에서 선언한 b의 경우 밖에서 console.log 찍으면 error남
var a = 0;

(function () {
    a++;
    console.log(a);
})();

console.log(a);


(function () {
    var b = 0;
    console.log(b);
})();

console.log(b); //error: b is not defined
