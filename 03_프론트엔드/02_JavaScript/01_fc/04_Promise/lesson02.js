/*
 * 생성자를 통해 프로미스 객체를 만들 수 있음.
 * 생성자의 인자로 excutor 라는 함수를 사용.
 */
new Promise(/* excutor */);

/*
 * excutor 함수는 resolve와 reject를 인자로 가짐
 * (resolve, reject)=>{...}
 * resolve와 reject는 함수
 */

new Promise(/* excutor */ (resolve, reject) => {});

/* 생성자를 통해 프로미스 객체를 만드는 순간 pending(대기) 상태라고함 */
new Promise((resolve, reject) => {}); //pending

/* excutor 함수 인자 중 하나인 resolve함수를 실행하면, fullfilled(이행) 상태가 됨 */
new Promise((resolve, reject) => {
  //..
  //..
  resolve(); //fullfilled
});

/* excutor 함수 인자 중 reject함수를 실행하면 rejected(거부) 상태가 됨 */
new Promise((resolve, reject) => {
  reject(); //reject
});
