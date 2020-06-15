//var는 함수스코프를 따르기때문에 블록 내부에 선언된 d를 밖에서 사용해도 문제없음
var c = 0;

{
    c++;
    console.log(c);
}

{
    var d = 0;
    console.log(d);
}

console.log(d);