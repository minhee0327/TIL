
class Animal {
    constructor(type, name, sound) {
        this.type = type
        this.name = name
        this.sound = sound
    }
    // class 내부에 선언된 함수를 method라고 한다.
    // 이렇게 class내부에 method를 만들면 자동으로 prototype으로 등록이 된다.
    say() {
        console.log(this.sound)
    }
}

const dog = Animal('강아지', '멍멍이', '왈왈');
const cat = Animal('고양이', '냐옹이', '야옹야옹');

dog.say();
cat.say();