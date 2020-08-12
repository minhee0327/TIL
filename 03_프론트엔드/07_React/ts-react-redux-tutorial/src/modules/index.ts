import { combineReducers } from "redux";
import counter from "./counter";
import todos from "./todos";

/* 루트 리듀서 */
const rootReducer = combineReducers({
  counter,
  todos,
});

export default rootReducer;

//루트리듀서의 반환값을 컨테이너 컴포넌트에서 유추해서 사용하도록 export함
export type RootState = ReturnType<typeof rootReducer>;
