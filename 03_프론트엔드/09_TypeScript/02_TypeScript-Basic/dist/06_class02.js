class Korean {
    constructor(name) {
        this.name = name;
    }
    say(msg) {
        console.log(msg);
    }
}
class KoreanProgrammer extends Korean {
    constructor(name, juminNum) {
        super(name);
        this.name = name;
        this.juminNum = juminNum;
    }
    loveKimchi() {
        throw new Error('Method not implemented.');
    }
    say(msg) {
        console.log(msg);
    }
    writeCode(requirement) {
        console.log(requirement);
        return requirement + '....';
    }
    studyinghard() {
        console.log('Korean programmers study hard.');
    }
}
const mini = new KoreanProgrammer('mini', 920314556);
console.log(mini.name);
mini.say('hahahah');
console.log(mini.writeCode('code code code'));
mini.studyinghard();
//# sourceMappingURL=06_class02.js.map