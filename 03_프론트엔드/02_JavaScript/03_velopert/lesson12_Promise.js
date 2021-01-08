//javaScritpt 비동기 처리 방식 1: Promise (ES6)
//callback 지옥 탈출하기

const myPromiseSuccess = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve(1);
  }, 1000);
});

myPromiseSuccess.then((n) => console.log(n));

//실패할경우 수행할 작업, catch로 잡아주기.
const myPromiseFail = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject(new Error());
  }, 1000);
});

myPromiseFail
  .then((n) => {
    console.log(n);
  })
  .catch((error) => {
    console.log(error);
  });
