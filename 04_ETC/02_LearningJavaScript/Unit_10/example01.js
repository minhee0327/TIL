const u1 = { name: "Minhee" };
const u2 = { name: "Jonghyun" };
const u3 = { name: "Jamie" };
const u4 = { name: "Mark" };

const userRoles = new Map();

/* 값할당 (3가지) */
//1-1. set으로 값 할당하기
userRoles.set(u1, "User");
userRoles.set(u2, "User");
userRoles.set(u3, "Admin");
console.log(userRoles);

//1-2. chain으로 할당하기
//단, 기존에 할당되어있었다면, 새로 값이 업데이트 됨.
userRoles.set(u1, "User").set(u2, "Admin").set(u3, "User");
// console.log(userRoles);

//1-3. 배열을 넘기는 형태로 할당하기
/*
const userRoles2 = new Map([
  [u1, "User"],
  [u2, "User"],
  [u3, "Admin"],
]);
console.log(userRoles2);
*/

/* 원하는 값 가져오기: get */
console.log(userRoles.get(u1)); //USer
console.log(userRoles.get(u2)); //Admin
console.log(userRoles.get(u4)); //undefined(u4는 등록하지 않음)

/* 키가 존재하는지 확인: has */
console.log(userRoles.has(u1)); //true
console.log(userRoles.has(u4)); //false

/* map의 요소 갯수: size */
console.log(userRoles.size); //3

/* keys(), values(), entries() */
for (let u of userRoles.keys()) {
  console.log(u.name);
}

for (let r of userRoles.values()) {
  console.log(r);
}

for (let ur of userRoles.entries()) {
  console.log(`${ur[0].name}: ${ur[1]}`);
}

for (let [u, r] of userRoles.entries()) {
  console.log(`${u.name} : ${r}`);
}

for (let [u, r] of userRoles) {
  console.log(`${u.name}: ${r}`);
}

/* 이터러블 객체 아닌, 배열로 각 값을 담고싶을때 spread연산자 */
console.log([...userRoles.keys()]);
console.log([...userRoles.values()]);
console.log([...userRoles.entries()]);

/* 요소지울때 delete */
userRoles.delete(u2);
console.log(userRoles.size); //2

/*요소 모두 지울때 clear*/
userRoles.clear();
userRoles.size;
console.log(userRoles.size); //0
