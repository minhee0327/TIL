function* interrogate() {
  const name = yield "What is your name";
  const color = yield "What is your favorite color?";
  return `${name}'s favorite color is ${color}`;
}

//위 제너레이터를 호출하면 이터레이터를 얻는다
//그리고 제너레이터의 어떤부분도 실행하지 않은상태이며, next()를 호출하면 첫번째 행을 실행
//하지만, yield 표현식이 들어있기 때문에 제너레이터는 반드시 제어권을 호출자에게 넘겨야한다.
//제너레이터의 첫 행이 완료되려면, next()로 전달한 값을 받아야한다.

const it = interrogate();
it.next();
it.next("Minhee");
it.next("red");
