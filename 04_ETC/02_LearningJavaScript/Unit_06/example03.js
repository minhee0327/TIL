const minhee = { name: "Minhee" };
const jonhyun = { name: "Jonghyun" };

function greet() {
  console.log(`Hello I'm ${this.name}`);
}

greet(); //Hello ~~~ undefined
greet.call(minhee); // Hello ~~~ Minhee
greet.call(jonhyun); // Hello ~~~ Jonghyun

function update(birthYear, occupation) {
  this.birthYear = birthYear;
  this.occupation = occupation;
}

//첫번째 매개변수: this로 사용할 값(객체)
// 나머지 매개변수: 호출하는 함수의 매개변수로 전달됨
update.call(minhee, 1991, "frontend");
console.log(minhee);
update.call(jonhyun, 1988, "great engineer");
console.log(jonhyun);

//apply함수
console.log("---------apply적용시--------");
update.apply(minhee, [1993, "kind"]);
console.log(minhee);
update.apply(jonhyun, [1991, "handsome"]);
console.log(jonhyun);

//bind적용시
console.log("--------bind적용시---------");
const updateMinhee = update.bind(minhee);
updateMinhee(1111, "fron");
console.log(minhee);
updateMinhee.call("Blala", 2000, "engineer");
console.log(minhee);

console.log("-----------bind 함수 구현해보기 ------");
Function.prototype.myBind = function (obj, ...args) {
  return (...__args) => this.apply(obj, ...args.concat(__args));
};
