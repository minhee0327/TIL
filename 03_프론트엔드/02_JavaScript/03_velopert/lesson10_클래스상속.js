class Animal {
    constructor(type, name, sound) {
        this.type = type
        this.name = name
        this.sound = sound
    }
    say() {
        console.log(this.sound)
    }
}

//상속 키워드 extends
// super()함수를 통해 부모 클래스의 생성자를 가리키게 됨.
class Dog extends Animal {
    constructor(name, sound) {
        super('개', name, sound);
    }
}

class Cat extends Animal {
    constructor(name, sound) {
        super('고양이', name, sound);
    }
}

const dog = new Dog('멍뭉이', '왈왈');
const dog2 = new Dog('왕자', '왕!');
const cat = new Cat('냐옹이', '야옹~');
const cat2 = new Cat('공주', '냐아');

dog.say();
dog2.say();
cat.say();
cat2.say();