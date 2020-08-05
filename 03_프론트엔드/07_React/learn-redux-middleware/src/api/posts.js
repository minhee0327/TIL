const sleep = (n) =>new Promise((resolve) => setTimeout(resolve, n));

//임의로 만든 post api
const posts = [
  {
    id: 1,
    title: "redux 미들웨어 만들기",
    body: "리덕스 미들웨어 직접 만들어보니까 할만한데...?",
  },

  {
    id: 2,
    title: "redux - thunk",
    body: "리덕스 thunk 사용해서 비동기 작업 진행해보기!!",
  },
  {
    id: 3,
    title: "redux- saga",
    body: "redux-saga 사용하는방법까지 오늘 끝내고싶다!",
  }
];

export const getPosts = async () => {
  await sleep(500);
  return posts;
};

export const getPostById = async (id) => {
  await sleep(500);
  return posts.find((x) => x.id === id);
};
