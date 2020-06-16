console.log('------------1. function 선언: 선언적 function -----------')
//function hello(){}
function hello1() {
    console.log('hello1');
}
hello1();
console.log(hello1, typeof hello1); //함수도 객체의 한 종류


// 함수의 매개변수
// 함수 호출할 때 값을 지정
function hello2(name) {
    console.log('hello2 ' + name);
}
hello2('minhee')
console.log(hello2, typeof hello2)


//함수의 리턴
//함수를 실행하면 얻어지는 값
function hello3(name) {
    return `hello3 ${name}`;
}
console.log(hello3('Minhee'))
console.log(hello3, typeof hello3)



console.log('\n------------2. function 선언: 익명함수 만들어 변수에 선언-----------')
//기본
const hello4 = function () {
    console.log('hello4');
};
hello4()
console.log(hello4, typeof hello4)

//매개변수
const hello5 = function (name) {
    console.log('hello5', name);
}
hello5('Mini');
console.log(hello5, typeof hello5);

//return
const hello6 = function (name) {
    return `hello6 ${name}`;
}
console.log(hello6('Min'));
console.log(hello6, typeof hello6);


console.log('\n ------------선언적 방식 과 익명함수 방식의 차이점 --------------');
hello7();
//hello8(); //error: is not a function
console.log(hello8); //undefined

// hello9(); //error : before initialization

function hello7() {
    console.log('hello7');
}

var hello8 = function () {
    console.log('hello8');
}

const hello9 = function () {
    console.log('hello9');
}


console.log('\n------------3. function선언: 생성자 함수로 함수를 만드는 방법-----------')
// const hello = new Function();
// 선언적
const sum = new Function('a', 'b', 'c', 'return a+b+c');
console.log(sum(1, 2, 3));

console.log('\n -------------선연적 방식과 생성자 함수 차이점-----------');
//생성자 함수 방식의 내부 변수는 global변수만 접근 가능
global.a = 0;
{
    const a = 1;
    const test = new Function('return a');
    console.log(test()) //error: a is not defined
}

//선언적 방식은 block scope에서 정의한 변수를 사용한다.
{
    const a = 2;
    const test = function () {
        return a;
    }
    console.log(test());
}



console.log('\n------------4. function선언: arrow function (es6), () => {} -----------');
//arrow 함수를 만들어 이름이 hello1인 변수에 할당
const hello10 = () => {
    console.log('hello1')
}
//매개변수, 함수 호출할 때 값을 지정
// 매개 변수 하나 일때, 괄호 생략 가능
const hello11 = name => {
    console.log('hello11', name);
}
const hello12 = (name, age) => {
    console.log('hello12', name, age);
}

//함수의 리턴 (return 생략 가능)
const hello13 = name => {
    return `hello13 ${name}`;
}
const hello14 = name => `hello14${name}`;

hello10()
hello11('Minhee arrow')
hello12('Minhee arrow', 30)
console.log(hello13('Minhee template'));
console.log(hello14('Minhee template'));



console.log('\n---------생성자 함수를 이용하여 새로운 객체를 만들어 내는 방법-----');
function Person(name, age) {
    this.name = name;
    this.age = age;
}

const p = new Person('Minhee', 30);
console.log(p, p.name, p.age);
const p2 = new Person('Lee', 33);
console.log(p2, p2.name, p2.age);

//arrow function으로는 생성자 함수 생성 안된다.
//arrow function은 this 나오지 않음.
/*
//error: Cat is not a constructor;
const Cat = (name, age) => {
    this.name = name;
    this.age = age;
}
const cat = new Cat('야옹', 3);
console.log(cat);
*/

console.log('\n------------함수 안에서 함수를 만들어 리턴 ---------------');
function plus(base) {
    return function (num) {
        return base + num;
    }
}
const plus5 = plus(5);
console.log(plus5(10));


console.log('\n-----------함수 호출할 때, 인자로 함수 사용--------------');
function hello15(c) {
    console.log('hello15');
    c();
}

hello15(function () {
    console.log('콜백')
})