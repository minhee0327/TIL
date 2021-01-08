import {
  createStandardAction,
  ActionType,
  createReducer,
} from "typesafe-actions";
/*액션타입 선언 */
const INCREASE = "counter/INCREASE";
const DECREASE = "counter/DECREASE";
const INCREASE_BY = "counter/INCREASE_BY";

/* 액션생성함수 */
export const increase = createStandardAction(INCREASE)();
export const decrease = createStandardAction(DECREASE)();
export const increaseBy = createStandardAction(INCREASE_BY)<number>();

/* 액션객체 타입 준비 */
const actions = { increase, decrease, increaseBy };
type CounterAction = ActionType<typeof actions>;

type CounterState = {
  count: number;
};

/* 초기상태 선언 */
const initialState: CounterState = {
  count: 0,
};

/* 리듀서 */
const counter = createReducer<CounterState, CounterAction>(initialState, {
  [INCREASE]: (state) => ({ count: state.count + 1 }),
  [DECREASE]: (state) => ({ count: state.count - 1 }),
  [INCREASE_BY]: (state, action) => ({ count: state.count + action.payload }),
});
export default counter;
