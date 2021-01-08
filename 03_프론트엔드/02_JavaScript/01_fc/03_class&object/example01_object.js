//생성자 함수로 객체 만들기
// function 틀 () {} => new 틀()
function A() {
}
const a = new A();
console.log(a, typeof a);
console.log(A()); //return 값 없으니까, undefined

console.log('--------------------------------')
// 생성하면서 데이터 넣기
function B(name, age) {
    console.log(name, age);
}
const b1 = new B();
const b2 = new B('Mark', 37);
//(name, age), return 값이 없어서 => undefined undefined \n undefined 
console.log(B())

console.log('--------------------------------')
//객체에 속성 추가하기 (property)
//값을 속성으로 넣기
function C() {
    this.name = 'Minhee'
}
const c = new C();
console.log(c);

// 함수를 속성으로 넣기
function D() {
    this.hello = () => {
        console.log('hello')
    }
}
new D().hello();

console.log('--------------------------------')
//new Object() 
//object로 객체 만들기
//권장되는 방법은 X

const e = new Object();
console.log(e, typeof e);

const f = new Object(true);
console.log(f, typeof f);

const g = new Object({ name: 'Minhee' });
console.log(g, typeof g);

console.log('--------------------------------')
//프로토타입 체인
//.prototype
function Person(name, age) {
    this.name = name;
    this.age = age;
    // this.hello = function () {
    //     console.log('hello', this.name, this.age);
    // }
}
//prototype의 프로퍼티도, 객체의 프로퍼티로 쓰일수있는 공간에 있다.
Person.prototype.hello = function () {
    console.log('hello', this.name, this.age);
}

const p = new Person('Minhee', 30)
p.hello();
console.log(1, p.toString());

console.log(2, Person.prototype);
console.log(3, Person.prototype.toString);
console.log(4, Person.prototype.constructor);
console.log(5, Person.prototype.hello)

console.log(6, Object.prototype)
console.log(7, Object.prototype.toString)
console.log(8, Object.prototype.constructor)

console.log(p instanceof Person);
console.log(p instanceof Object);

console.log('--------------------------------')

//prototype을 이용한 객체 확장
function Person() {

}
Person.prototype.hello = function () {
    console.log('hello');
}

function Korean(region) {
    this.region = region;
    this.where = function () {
        console.log('where', this.region);
    }
}

Korean.prototype = Person.prototype;
const k = new Korean('Seoul');

k.hello();
k.where();

console.log(k instanceof Korean);
console.log(k instanceof Person);
console.log(k instanceof Object);


console.log('--------------------------------')
//객체 리터럴
const h = {};
console.log(h, typeof h)
const i = {
    name: 'Minhee',
    hello1() {
        console.log('hello1', this)
    },
    hello2: function () {
        console.log('hello2', this)
    },
    hello3: () => {
        console.log('hello3', this);
    }
}

i.hello1();
i.hello2();
i.hello3(); //arrow function 에서는 this가 bind되지 않기 때문에 결과가 다름.


console.log('--------------------------------');
//표준 내장 객체: array

const j = new Array('red', 'black', 'white');
console.log(j, typeof j);
console.log(a instanceof Array); //false Array 객체를 생성한 것이기 때문에 
console.log(a instanceof Object); // true

const l = ['red', 'green', 'yellow'];
console.log(l, typeof l);
console.log(l instanceof Array); //true 
console.log(l instanceof Object); //true

console.log(l.slice(0, 1));
console.log(Array.prototype.slice, Object.prototype.slice); //Array에는 slice 내장 함수가 있지만, Object에는 없음


