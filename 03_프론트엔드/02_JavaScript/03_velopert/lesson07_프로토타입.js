// 그동안 다른 언어들의 class 를 사용하는 것에 익숙해 져서,
// prototype은 유사하면서도 조금 혼란스럽다.
// 심지어 class키워드도, 처음에는 비슷하다고 생각했는데 쓸수록 조금 다르더라~~
// 그래서 정리

// 객체 생성자
// 객체 생성자는 함수를 통해 새로운 객체를 만들고 그안에 넣고싶은 값 또는 함수 구현
// 보통 함수의 이름 대문자, new키워드로 새로운 객체 만듬

// 프로토타입
// 같은 객체 생성자를 사용하는 경우, 특정 함수 또는 값을 재사용할 수 있음.
// 설정방법
// 객체 생성자 함수 아래에 
//.prototype.[원하는키] = 코드 
//를 입력하여 설정할 수 있음
function Animal(type, name, sound) {
    this.typoe = type;
    this.name = name;
    this.sound = sound;
}

Animal.prototype.say = function () {
    console.log(this.sound);
}
Animal.prototype.sharedValue = 1

const dog = new Animal('강아지', '멍멍이', '왈왈!');
const cat = new Animal('고양이', '냐옹이', '야옹야옹');

dog.say();
cat.say();

console.log(dog.sharedValue);
console.log(cat.sharedValue);


// 객체 생성자 상속받기
// 각 객체는 prototype이라는 은닉(private)속성을 가짐
// 자신의 프로토타입이 되는 다른 객체를 가리킴
// 그 객체의 프로토 타입 또한 프로토 타입을 가지고 있고, null을 프로토 타입으로 가진 객체에서 끝이남.
// null 은 프로토타입이 없다고 정의, 프로토 타입의 체인 종점역할
console.log('--------------prototype 상속: ECMA 5-------------')
var a = { a: 1 };
// a => Object.prototype => null
var b = Object.create(a);
// b => a => Object.prototype => null
console.log(b.a);
var c = Object.create(b);
// c => b=> a => Object.prototype => null
console.log(c.a);
var d = Object.create(null);
// d=> null
// undefined, d는 바로 null을 가리키기 때문에 Object.prototype 의 속성을 가질 수 없음
console.log(d.hasOwnProperty)

// 프로토 타입 체인을 모두 검사하면서, 성능 저하의 원인을 발생시킬 수 있음
// 이때 .hasOwnProperty 메소드를 이용하여 프로토타입 체인상 어딘가에 존재하는지 확인이 가능함.
