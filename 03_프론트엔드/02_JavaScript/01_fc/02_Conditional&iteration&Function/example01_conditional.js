console.log('-------------- example01: 기본 조건문 ------------');
/*
if(expression){
    expression(표현식)이 참일 때, 실행되는 문장(statement)모음
}
*/
if (true) {
    console.log('항상 실행');
}
if (false) {
    console.log('항상 실행되지 않음')
}

//블록에 코드 한줄이면 중괄호{}생략가능
if (true) console.log('항상 실행');
if (false) console.log('항상 실행 X');



console.log('--------------example02: falsy & truthy ---------------');
// 표현식이 거짓으로 평가될때 Falsy: false, 0, '', null, undefined, NaN
if (false) console.log(false);
if (0) console.log(0);
if ('') console.log('');
if (null) console.log(null);
if (undefined) console.log(undefined);
if (NaN) console.log(NaN);
// 표현식이 참으로 평가될때 Truethy: true, 37(0 이외 숫자), 'Mark', {}, []
if (true) console.log(true);
if (37) console.log(37);
if (-37) console.log(-37);
if ('Minhee') console.log('Minhee');
if ({}) console.log({});
if ([]) console.log([])



console.log('---------------- example03: else -----------------');
const n = 37;
if (n > 0) {
    console.log('n 이 0 보다 클 경우');
} else {
    console.log('n이 0보다 크지 않은 경우');
}

console.log('--------------- example04: else if{} -------------');
const k = 15;
if (k % 3 === 0) {
    console.log('k는 3의 배수입니다.');
} else if (k % 5 === 0) {
    console.log('k는 5의 배수입니다.');
} else {
    console.log('k는 3의 배수도 아니고, 5의 배수도 아닙니다.')
}
// 만약 3의 배수이면서, 5의 배수일 경우 어떻게 출력될까? => 3의 배수라고 출력
// 좁은 경우를 보통 위에 쓰자
if (k % 3 === 0 && k % 5 === 0) {
    console.log('k는 15의 배수입니다.')
} else if (k % 3 === 0) {
    console.log('k는 3의 배수')
} else if (k % 5 === 0) {
    console.log('k는 5의 배수')
} else {
    console.log('k는 3의 배수도 아니고, 5의 배수도 아닙니다.')
}

// 반복코드는 변수에 담아주자
const mulipleOfThree = k % 3 === 0;
const mulipleOfFive = k % 5 === 0;

if (mulipleOfThree && mulipleOfFive) {
    console.log('k는 15의 배수입니다.')
} else if (mulipleOfThree) {
    console.log('k는 3의 배수')
} else if (mulipleOfFive) {
    console.log('k는 5의 배수')
} else {
    console.log('k는 3의 배수도 아니고, 5의 배수도 아닙니다.')
}

//중첩이용가능
if (mulipleOfThree && mulipleOfFive) {
    console.log('k는 15의 배수입니다.')
} else {
    if (mulipleOfThree) {
        console.log('k는 3의 배수')
    } else if (mulipleOfFive) {
        console.log('k는 5의 배수')
    } else {
        console.log('k는 3의 배수도 아니고, 5의 배수도 아닙니다.')
    }
}


console.log('--------------- example05: 논리연산자(&&, ||, ! ) -------------');
if (true && true) console.log('두개 모두 참이면 참');
if (true && false) console.log('하나만 참이어도 거짓');
if (false && true) console.log('하나만 참이어도 거짓');
if (false && false) console.log('하나만 참이어도 거짓');

if (true || true) console.log('둘중 하나만 참이어도 참');
if (true || false) console.log('둘중 하나만 참이어도 참');
if (false || true) console.log('둘중 하나만 참이어도 참');
if (false || false) console.log('둘다 거짓이면 거짓');

if (!true) console.log('참이면 거짓');
if (!false) console.log('거짓이면 참');

console.log('--------------- example06: 논리연산자 이용한 조건부 실행 -------------');
// 표현식 && 표현식
// 둘다 참일때만 참
// 표현식은 앞에 먼저 평가하고 뒤에를 평가
// 앞 표현식을 평가해서 참일때만, 뒤 표현식을 평가할 필요가 생기기 때문에 뒤의 표현식이 실행된다.

let a = 5;
a % 5 === 0 && console.log('5로 나누어 떨어질때만 실행')

//앞의 표현식의 경과가 거짓일 때는 뒤 표현식을 평가할 필요 없어서 실행 X
a = 6;
a % 5 === 0 && console.log('5로 나누어 떨어질때만 실행')

//표현식 ||표현식
//둘중 하나만 참이면 참
// 앞 표현식을 평가해서 참이면 뒤 표현식 평가할 필요 X
b = 5;
b % 5 === 0 || console.log('5로 나누어 떨어질때 실행 안됨')

//앞 표현식을 평가해서 거짓일때만, 뒤 표현식을 평가할 필요가 생기므로, 뒤 표현식이 실행됨.
c = 6;
c % 5 === 0 || console.log('5로 나누어 떨어지지 않을 때만 실행')



console.log('--------------- example07: 삼항연산자 이용한 조건부 실행 -------------');
let d = 5;
console.log(d % 5 == 0 ? '5의 배수 입니다.' : '5의 배수가 아닙니다.');

const message = d % 5 == 0 ? '5의 배수 입니다.' : '5의 배수가 아닙니다.'
console.log(message)


console.log('--------------- example08: switch를 이용한 조건문 -------------');
//default: 뒤 문장은 항상 참이어서 실행되는 블럭
let e = 5;
switch (e) {
    default:
        console.log(e);
}

//case에 맞게 실행된뒤, default도 실행됨
switch (e % 5) {
    case 0:
        console.log('5의 배수입니다.')
    default:
        console.log(e);
}

//case에 맞게 실행된뒤 탈출하고 싶다면, case문 안에서 break실행
switch (e % 5) {
    case 0:
        console.log('5의 배수입니다.');
        break;
    default:
        console.log(e);
}

let f = 4;

switch (f % 5) {
    case 0:
        console.log('5의 배수입니다.');
        break;
    case 1:
    case 2:
    case 3:
    case 4:
        console.log('5의 배수가 아닙니다.');
        break
    default:
        console.log(e);
}
