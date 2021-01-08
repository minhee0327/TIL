interface Soundable {
    sound(): void;
}

class Duck implements Soundable {
    sound() {
        console.log('꽥!');
    }
}

class Cat {
    sound() {
        console.log('야오옹');
    }
}

function makeSound(some: Soundable): void {
    some.sound();
}

makeSound(new Duck());
makeSound(new Cat());
//Cat에서는 Soundable 인터페이스를구현할것이라고 implement를 명시적으로 안했음.
//그저 sound메소드만 구현되어있었음. 그렇기 때문에 Soundable 객체로 봄
//strict하게 타이핑을 하고 싶을 때에는 implements를 명시적으로 사용하면 된다.
