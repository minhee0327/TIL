// 객체 비구조화 할당
const ironman = {
    name: '토니스타크',
    acotr: '로버트 다우니 주니어',
    alias: '아이언맨'
}

const camptainAmerica = {
    name: '스티븐 로저스',
    actor: '크리스 에반스',
    alias: '캡틴 아메리카'
}
//객체에서 값들을 추출해서 매개변수로 넘겨받음
function print({ alias, name, acotr }) {
    const text = `${alias}(${name}) 역할을 맡은 배우는 ${acotr}입니다.`;
    console.log(text);
}

print(ironman)
print(camptainAmerica)