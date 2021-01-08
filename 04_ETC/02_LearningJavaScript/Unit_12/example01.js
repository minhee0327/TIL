//책갈피 역할하는 이터레이터
const books = [
  "Learning JS",
  "JAVA",
  "nodeJS",
  "express",
  "HTML",
  "CSS",
  "Ajax",
];

//이터레이터 만들기
const it = books.values();

/*
//next 메서드를 통해 읽음
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());

//출력결과
{ value: 'Learning JS', done: false }
{ value: 'JAVA', done: false }
{ value: 'nodeJS', done: false }
{ value: 'express', done: false }
{ value: 'HTML', done: false }
{ value: 'CSS', done: false }
{ value: 'Ajax', done: false }
{ value: undefined, done: true }
*/

/* while로 for of 구현해보기 */
let current = it.next();
while (!current.done) {
  console.log(current.value);
  current = it.next();
}

//이터레이터는 모두 독립적.
const it2 = books.values();
const it3 = books.values();

it2.next(); //{ value: 'Learning JS', done: false }
it2.next(); //{ value: 'JAVA', done: false }

it3.next(); //{ value: 'Learning JS', done: false }
it2.next(); //{ value: 'nodeJS', done: false }
