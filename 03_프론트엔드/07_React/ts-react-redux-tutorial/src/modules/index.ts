import { combineReducers } from "redux";
import counter from "./counter";
import todos from "./todos/";
import github from "./github/";
import { githubSaga } from "./github/";
import { all } from "redux-saga/effects";

/* 루트 리듀서 */
const rootReducer = combineReducers({
  counter,
  todos,
  github,
});

export default rootReducer;

//루트리듀서의 반환값을 컨테이너 컴포넌트에서 유추해서 사용하도록 export함
export type RootState = ReturnType<typeof rootReducer>;

//루트 사가 만들어서 내보내기
export function* rootSaga() {
  yield all([githubSaga()]);
}
