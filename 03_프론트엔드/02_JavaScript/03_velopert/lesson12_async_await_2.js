function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

const getDog = async () => {
  await sleep(1000);
  return "멍멍이";
};
const getRabbit = async () => {
  await sleep(500);
  return "토끼";
};
const getTurtle = async () => {
  await sleep(3000);
  return "거북이";
};

async function process() {
  const dog = await getDog();
  console.log(dog);
  const rabbit = await getRabbit();
  console.log(rabbit);
  const turtle = await getTurtle();
  console.log(turtle);
}

process();

//결과
//멍멍이(1초)
//토끼(1.5초)(멍멍이 후, 0.5초)
//거북이(4.5초)(토끼후 3초)
//총 4.5초

//만약 동시에 작업을 시작하고 십다면 Promise.all을 사용하면 됨.
