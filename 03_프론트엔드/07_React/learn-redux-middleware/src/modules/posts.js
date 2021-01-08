import * as postsAPI from "../api/posts";
import {
  createPromiseSaga,
  createPromiseSagaById,
  reducerUtils,
  handleAsyncActions,
  handleAsyncActionsById,
} from "../lib/asyncUtils";
import { takeEvery, getContext } from "redux-saga/effects";

/* 액션타입 */
const GET_POSTS = "GET_POSTS";
const GET_POSTS_SUCCESS = "GET_POSTS_SUCCESS";
const GET_POSTS_ERROR = "GET_POSTS_ERROR";

const GET_POST = "GET_POST";
const GET_POST_SUCCESS = "GET_POST_SUCCESS";
const GET_POST_ERROR = "GET_POST_ERROR";

// const CLEAR_POST = "CLEAR_POST";
const GO_TO_HOME = "GO_TO_HOME";

//get thunk함수 구현
export const getPosts = () => ({ type: "GET_POSTS" });
export const getPost = (id) => ({ type: "GET_POST", payload: id, meta: id });
export const goToHome = () => ({ type: "GO_TO_HOME" });

export const getPostsSaga = createPromiseSaga(GET_POSTS, postsAPI.getPosts);
export const getPostSaga = createPromiseSagaById(
  GET_POST,
  postsAPI.getPostById
);
function* gotToHomeSaga() {
  const history = yield getContext("history");
  history.push("/");
}

export function* postsSaga() {
  yield takeEvery(GET_POSTS, getPostsSaga);
  yield takeEvery(GET_POST, getPostSaga);
  yield takeEvery(GO_TO_HOME, gotToHomeSaga);
}

const initialState = {
  posts: reducerUtils.initial(),
  post: reducerUtils.initial(),
};

export default function posts(state = initialState, action) {
  switch (action.type) {
    case GET_POSTS:
    case GET_POSTS_SUCCESS:
    case GET_POSTS_ERROR:
      return handleAsyncActions(GET_POSTS, "posts", true)(state, action);
    case GET_POST:
    case GET_POST_SUCCESS:
    case GET_POST_ERROR:
      return handleAsyncActionsById(GET_POST, "post")(state, action);
    default:
      return state;
  }
}
