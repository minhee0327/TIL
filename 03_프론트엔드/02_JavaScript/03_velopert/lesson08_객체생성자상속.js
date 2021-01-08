// 앞의 예제에서 만들었던 Animal 객체 
// Animal의 기능을 새로운 객체 생성자에서 사용하고 싶다면?
// 예(새로운 객체 생성자: Dog, Cat)

function Animal(type, name, sound) {
    this.typoe = type;
    this.name = name;
    this.sound = sound;
}

Animal.prototype.say = function () {
    console.log(this.sound);
}

function Dog(name, sound) {
    Animal.call(this, '강아지', name, sound); //첫번째 인자로 this , 다음 인자는 animal객체 생성자 함수에 필요한 파라미터
}
Dog.prototype = Animal.prototype // prototype 공유해야하기 때문에 prototype 값을 aniaml.prototype으로 설정

function Cat(name, sound) {
    Animal.call(this, '고양이', name, sound)
}

Cat.prototype = Animal.prototype

const dog = new Dog('멍멍이', '왈왈!');
const cat = new Cat('냐옹이', '야옹야옹');

dog.say();
cat.say();
