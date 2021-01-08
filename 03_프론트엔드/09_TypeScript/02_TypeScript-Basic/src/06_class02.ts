/*
- class의 상속과 interface와의 관계
- abstract class (완성되지 않은 class): 
    - 다른 클래스가 파생될 수 있는 기본 클래스
    - 직접 인스턴스화는 불가능하지만 
    - interface와 달리 구현 세부 정보를 포함 할 수 있다.
*/
interface Person {
    name: string;
    say(msg: string): void;
}
interface Programmer {
    writeCode(requirement: string): string;
}

//Korean은 Person이라는 interface를 받아서, 해당 interface의 data(변수)와 기능(method)을 사용할 수 있다.
//즉 아래 예제의미는 곧 Koeran은 사람이 가진 이름과 말하기 기능을 가질 수 있다.
/*
class Korean implements Person {
    constructor(public name: string) {}
    say(msg: string): void {
        console.log(msg);
    }
}
*/

//추상클래스(abstract class)
//여기서 바로 정의하지 않고, 하위타입에서 정의.
//상속받은 class에서 abstract로 명시한 부분을 반드시 구현해야한다.
abstract class Korean implements Person {
    public abstract juminNum: number;
    constructor(public name: string) {}
    say(msg: string) {
        console.log(msg);
    }
    abstract loveKimchi(): void;
}

//interface를 다중으로 상속받을 경우에는 구분자','를 이용한다.
class KoreanProgrammer extends Korean implements Programmer {
    loveKimchi(): void {
        throw new Error('Method not implemented.');
    }
    constructor(public name: string, public juminNum: number) {
        //부모 클래스의 생성자 호출
        super(name);
    }
    say(msg: string): void {
        console.log(msg);
    }
    writeCode(requirement: string): string {
        console.log(requirement);
        return requirement + '....';
    }
    // Korean Programmer만의 특징을 가질 수도 있다~~
    studyinghard() {
        console.log('Korean programmers study hard.');
    }
}

const mini = new KoreanProgrammer('mini', 920314556);
console.log(mini.name);
mini.say('hahahah');
console.log(mini.writeCode('code code code'));
mini.studyinghard();

// const sample= new Korean('min') //error: abstract class는 instance생성 불가.
