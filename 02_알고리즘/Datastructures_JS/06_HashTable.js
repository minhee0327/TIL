const hash = (string, max) => {
  let hash = 0;
  for (let i = 0; i < string.length; i++) {
    hash += string.charCodeAt(i);
  }
  return hash % max;
};

const HashTable = function () {
  let storage = [];
  const storageLimit = 14;

  this.print = function () {
    console.log(storage);
  };

  //hashTable에 insert하기
  // k: key, v: value
  this.add = function (k, v) {
    let index = hash(k, storageLimit);
    //storage가 비워져있으면(undefined), 새로 배열 만들어서 [k,v]를 담아준다.
    if (storage[index] === undefined) {
      storage[index] = [[k, v]];
    }
    //비워져있지 않을경우
    else {
      let inserted = false;
      //해당 index안의 배열을 모두 확인하면서 key가 일치하는 경우에는 해당 배열의 value만 업뎃
      for (let i = 0; i < storage[index].length; i++) {
        if (storage[i][0] === k) {
          storage[i][1] = v;
          inserted = true;
        }
      }
      // 다 돌아봤는데, 일치하는 k가 없으면 해당 [k,v]를 push해주기
      if (!inserted) {
        storage[index].push([k, v]);
      }
    }
  };

  //Delete구현하기, 지우고자하는 key값을 넣어줄것
  this.remove = function (key) {
    let index = hash(key, storageLimit);
    //해당 인덱스 길이가 1이면 하나만 가지고 있는 것. && 첫번째 요소의 key값과 일치한다면 그냥 지우면됨
    if (storage[index].length === 1 && storage[index][0][0] === key) {
      delete storage[index];
    } else {
      //그게아니면 해시테이블의 index와 일치하는 배열내부를 탐색하면서 key가 같은 것을 찾고, 있으면 삭제
      for (let i = 0; i < storage[index].length; i++) {
        if (storage[index][i][0] === key) {
          delete storage[index][i];
        }
      }
    }
  };

  //Search 구현하기 (있을경우 해당 value return 해줄것)
  this.lookup = function (key) {
    let index = hash(key, storageLimit);
    if (storage[index] === undefined) {
      return undefined;
    } else {
      for (let i = 0; i < storage[index].length; i++) {
        if (storage[index][i][0] === key) {
          return storage[index][i][1];
        }
      }
    }
  };
};

console.log(hash("baeu", 14));
console.log(hash("fido", 14));
console.log(hash("rex", 14));
console.log(hash("tux", 14));

let ht = new HashTable();
ht.add("beau", "person");
ht.add("fido", "dog");
ht.add("rex", "dinosour");
ht.add("tux", "penguin");
console.log(ht.lookup("tux"));

ht.print();
