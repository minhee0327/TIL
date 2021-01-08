/*
- enum
- 상수들의 집합 정의하여 이름을 부여한다.
- enum도 타입이기 때문에 매개변수의 타입 annotaition사용가능
- enum에 상수들을 열거하게 되면 자동으로 숫자가 부여가 된다. 
- 다만 중간에 값을 추가하게 되면서 순서가 변경되는 경우에는 사용했던 모든 코드를 수정해야하니까
- default 값으 지정해서 사용하는 편이 안전하다. (예: WELCOME = 0)
- 숫자 말고도, 문자열로만 enum의 멤버로 정의할 수도 있다.
*/

enum StarbucksGrade {
    WELCOME = 0,
    // WELCOME = 'WELCOME',
    GREEN,
    GOLD,
}

function getDiscound(v: StarbucksGrade): number {
    switch (v) {
        case StarbucksGrade.WELCOME:
            return 0;
        case StarbucksGrade.GREEN:
            return 5;
        case StarbucksGrade.GOLD:
            return 10;
    }
}

console.log(getDiscound(StarbucksGrade.GREEN)); //5
console.log(StarbucksGrade.GREEN); //1
console.log(StarbucksGrade['GOLD']); //2
console.log(StarbucksGrade[0]); //welcome
console.log(StarbucksGrade);
/*
{
  '0': 'WELCOME',
  '1': 'GREEN',
  '2': 'GOLD',
  WELCOME: 0,
  GREEN: 1,
  GOLD: 2
}
*/
