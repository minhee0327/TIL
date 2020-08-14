import { createStandardAction, createReducer } from "typesafe-actions";

/* 액션생성함수 */
export const increase = createStandardAction("counter/INCREASE")();
export const decrease = createStandardAction("counter/DECREASE")();
export const increaseBy = createStandardAction("counter/INCREASE_BY")<number>();

type CounterState = {
  count: number;
};

/* 초기상태 선언 */
const initialState: CounterState = {
  count: 0,
};

/* 리듀서 */
const counter = createReducer(initialState)
  .handleAction(increase, (state) => ({ count: state.count + 1 }))
  .handleAction(decrease, (state) => ({ count: state.count - 1 }))
  .handleAction(increaseBy, (state, action) => ({
    count: state.count + action.payload,
  }));
export default counter;
