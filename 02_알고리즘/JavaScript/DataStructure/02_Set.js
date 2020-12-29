// set: 중복죄는 값을 가지지 않는 값들의 리스트
// ES6부터 Set 객체가 있기는 하지만, 일반적으로 모든 기능을 포함하고 있지는 않다.
// add, clear, delete, has, values 이외 추가구현.

function mySet() {
  //set을 담을 배열
  let collection = [];

  // collection에 data가 index로 없으면 -1을 반환하는데
  // -1이 아니라면 값이 있다는 소리이므로 true반환
  this.has = function (data) {
    return collection.indexOf(data) !== -1;
  };

  //중복 제거 후 남은 배열 반환
  this.values = function () {
    return collection;
  };

  //중복 되지 않는 요소인지 확인한 뒤, 넣어주기
  this.add = function (data) {
    if (!this.has(data)) {
      collection.push(data);
      return true;
    }
    return false;
  };

  //size는 property로 가지고있음
  this.size = function () {
    return collection.length;
  };

  //ES6의 Delete기능과 유사
  this.remove = function (data) {
    if (has(data)) {
      let index = collection.indexOf(data);
      collection.splice(index, 1);
      return true;
    }
    return false;
  };
  //합집합
  this.union = function (otherSet) {
    let UnionSet = new Set();
    let firstSet = this.values();
    let secondSet = otherSet.values();

    firstSet.forEach((x) => UnionSet.add(x));
    secondSet.forEach((x) => UnionSet.add(x));

    return UnionSet;
  };
  //교집합
  this.intersection = function (otherSet) {
    let intersecitionSet = new mySet();
    var firstSet = this.values();

    firstSet.forEach(function (e) {
      if (otherSet.has(e)) {
        intersecitionSet.add(e);
      }
    });
    return intersecitionSet;
  };

  //차집합
  this.difference = function (otherSet) {
    let differenceSet = new mySet();
    var firstSet = this.values();

    firstSet.forEach(function (e) {
      if (!otherSet.has(e)) {
        differenceSet.add(e);
      }
    });
    return differenceSet;
  };

  //부분집합
  //every함수를 사용해, firstSet의 모든 요소가 otherSet에포함되는지 체크한 후, 맞다면 true반환
  this.subSet = function (otherSet) {
    let firstSet = this.values();
    return firstSet.every(function (value) {
      return otherSet.has(value);
    });
  };
}

console.log("==== using mySet====");
let setA = new mySet();
let setB = new mySet();

setA.add("A");
setB.add("B");
setB.add("C");
setB.add("A");
setB.add("D");

console.log(setA.values());
console.log(setB.values());

console.log(setA.subSet(setB)); //setA는 setB에 포함이됨.(true)
console.log(setB.subSet(setA)); //setB가 setA 포함되지 X (false)

console.log(setA.intersection(setB).values()); // 교집합(A)

console.log(setA.difference(setB).values()); //A-B
console.log(setB.difference(setA).values()); //B-A

console.log(setA.union(setB));
console.log([...setA.union(setB)]);

console.log("------using Set()------");
let setC = new Set();
let setD = new Set();

setC.add("A");
setD.add("B");
setD.add("C");
setD.add("A");
setD.add("D");

console.log(setD.values());
setD.delete("A");
console.log(setD.has("A"));
console.log(setD.add("D"));
console.log(setD.values());
