//객체를 만들 수 있는 새로운 방법
// 기존의 prototype을 좀 더 명료하게 쓸 수 있다

// class
// 선언적방식
class A { }
console.log(new A());

//class 표현식을 변수에 할당
const B = class { };
console.log(new B());

//선언적 방식이지만 호이스팅은 일어나지 않는다. ES6에서 추가된 방법이기 때문
// new C();
// class C { }; //Error


console.log('--------------------------------');
class D { }
console.log(new D());

class E {
    constructor() {
        console.log('constructor');
    }
}
console.log(new E());

class F {
    constructor(name, age) {
        console.log('constructor', name, age);
    }
}
console.log(new F('Minhee', 30));
console.log(new F()); // 인수를 전달하지 않으면, undefined로 출력이 됨



console.log('--------------------------------');
//멤버 변수: 객체의 프로퍼티
class G {
    constructor(name, age) {
        this.name = name
        this.age = age
    }
}
console.log(new G('Minhee', 30));

//runtime error (node v12 이상에서 사용가능)
//현재 내가 사용중인 node13.1.0 따라서 강의와 같이 error 발생은 하지 않았음.
// 상위 문법을 이해하기 위해 babel을 사용하기는 하지만, 지원하는 상태인지 항상 체크
class H {
    name;
    age;
}
console.log(new H());

class I {
    name = 'no name';
    age = 0;
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

console.log(new I('Minhee', 30));



console.log('--------------------------------');
// 멤버 함수
class J {
    hello1() {
        console.log('hello1', this);
    }
    hello2 = () => {
        console.log('hewllo2', this);
    }
}
new J().hello1();
new J().hello2();

class K {
    name = "Minhee";
    hello() {
        console.log('hello', this.name);
    }
}

new K().hello();

console.log('--------------------------------');
//getter, setter
class L {
    _name = 'no name'; //내부적으로만 쓰는 변수라면, 관례로 _로 시작한다.
    get name() {
        return this._name + '@@@';
    }
    set name(value) {
        this._name = value + "!!!";
    }
}

const l = new L();
console.log(l)
l.name = 'Minhee';
console.log(l);
console.log(l.name);
console.log(l._name);

//readonly
class M {
    _name = 'no name'; //_변수: 외부에서 값을 바꾸지말자. 
    get name() {
        return this._name + '@@@';
    }
}

const m = new M();
console.log(m);
m.name = 'Minhee'; //setter가 없기 때문에 readonly만 된다.
console.log(m);

console.log('--------------------------------');
//static 변수, 함수: 객체가 아니고 클래스의 변수와 함수
class N {
    static age = 30;
    static hello() {
        console.log(N.age);
    }
}
console.log(N, N.age);
N.hello();

class P {
    age = 10;
    static hello() {
        console.log(this.age)
    }
}
console.log(P, P.age); // static age가 없기때문에 undefined가 나오게 됨.
P.hello();
// new P().hello(); //hello is not a function => new (static 함수이기 때문에 객체에 포함된 함수가 아님)
class Q {
    static name = '이 클래스의 이름은 Q가 아니다.'
}
console.log(Q, Q.name);


console.log('--------------------------------');
//상속 (extends)
class Parent {
    name = 'Lee';
    hello() {
        console.log('hello', this.name);
    }
}
class Child extends Parent {

}

const parent = new Parent();
const child = new Child();

console.log(parent, child);
child.hello();
child.name = 'Anna';
child.hello();
parent.hello();

//override: 클래스의 상속 멤버 변수 및 함수 오버라이딩 추가.
class Parent1 {
    name = 'Lee';
    hello() {
        console.log('hello', this.name);
    }
}

class Child1 extends Parent1 {
    age = 30;
    hello() {
        console.log('hello', this.name, this.age);
    }
}

const parent1 = new Parent1();
const child1 = new Child1();

console.log(parent1, child1);
child1.hello();

child1.name = 'Anna';
child1.hello();


