//Promise를 만드는 함수
function increaseAndPoint(n) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const value = n + 1;
      if (value === 5) {
        const error = new Error();
        error.name = "ValueIsFiveError";
        reject(error);
        return;
      }
      console.log(value);
      resolve(value);
    }, 1000);
  });
}

increaseAndPoint(0)
  .then(increaseAndPoint)
  .then(increaseAndPoint)
  .then(increaseAndPoint)
  .then(increaseAndPoint)
  .then(increaseAndPoint)
  .catch((error) => {
    console.error(error);
  });
