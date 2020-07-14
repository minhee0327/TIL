//ES8
//Promise를 조금 더 쉽게 써보자.
//async는 함수 선언할 때 앞부분에
//awati는 Promise앞부분에 넣으면, 프로미스가 끝날때까지 기다렸다가 다음작업 수행.

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function makeError() {
  await sleep(1000);
  const error = new Error();
  throw error;
}

async function process() {
  try {
    await makeError();
  } catch (e) {
    console.error(e);
  }
}

process();
