/* 원시값을 불변이기 때문에, 함수 내부에서 변경할 수 없음 */
function f(x) {
  console.log(`f 내부 x = ${x}`);
  x = 5;
  console.log(`f 내부 x = ${x} (할당후)`);
}

let x = 3;
console.log(`f를 호출하기 전 x = ${x}`);
f(x);
console.log(`f를 호출한 후 x = ${x}`);

/* 함수안에서, 객체 자체를 변경했을 때 함수 밖에서도 바뀐 점이 반영됨 */

function p(x) {
  o.msg = `p 함수 내부에서 수정함. (이전값: ${x})`;
}

let o = { msg: "초기값" };
console.log(`p를 호출하기 전: ${o.msg}`);
p(o);
console.log(`p를 호출한 뒤: ${o.msg}`);

/* 함수내부의 매개변수obj와 , 함수바깥에 있는 변수obj는 다르다.  */
function func(obj) {
  obj.msg = "func에서 수정함";
  obj = {
    msg: "새로운 객체!",
  };
  console.log(`func 내부: obj.msg = ${obj.msg} (할당후)`);
}

let obj = { msg: "초기값" };
console.log(`func를 호출하기전: obj.msg = ${obj.msg}`);
func(obj);
console.log(`func를 호출한 후: obj.msg = ${obj.msg}`);
