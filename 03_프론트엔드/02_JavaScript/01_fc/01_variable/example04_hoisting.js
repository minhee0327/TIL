//함수 먼저
console.log('---------example01--------');
function hello1() {
    console.log('hello1');
}

hello1();

//함수의 호출을 먼저해도 문제 없음
hello2();

function hello2() {
    console.log('hello2');
}

console.log('---------example02--------');
//age를 아래에 선언해도 위에서 사용가능
age = 6;
age++;
console.log(age);

var age;


console.log('---------example03--------');
console.log(name) //undefined
//값을 할당 한 후에야 이름 출력
//단, 선언부만 올라가짐
name = 'MinHee';

console.log(name);

var name;



console.log('---------example04--------');
console.log(name1) //undefined
//값을 할당 한 후에야 이름 출력
//단, 선언부만 올라가짐
name1 = 'Mark';

console.log(name1); //Mark로 찍힘!Jong아님

var name1 = 'Jong';

console.log(name1);


console.log('---------example05--------');
//let 키워드는 hoisting X!
//let name2;

console.log(name2); //cannot access before initaliztion error

name2 = 'Minhee';

console.log(name2);

let name2;
