/*액션타입 선언 */
//as const를 씀으로써, 액션객체 만들때, action.type값 추론시, string이 아니라 'counter/INCREASE'와같이 그 자체를 추론
const INCREASE = "counter/INCREASE" as const;
const DECREASE = "counter/DECREASE" as const;
const INCREASE_BY = "counter/INCREASE_BY" as const;

/* 액션생성함수 */
export const increase = () => ({
  type: INCREASE,
});

export const decrease = () => ({
  type: DECREASE,
});
//액션에 부가적으로 필요한 값의 경우, payload이름으로 통일하는데, FSA라는 규칙에 따름
// 액션이 비슷한 구조로 이루어지게 되어, 추후 다루거나 읽거나 구조를 일반화하여 액션과 관련된 라이브러리를 사용가능토록함.
export const increaseBy = (diff: number) => ({
  type: INCREASE_BY,
  payload: diff,
});

/* 액션객체 타입 준비 */
// ReturnType<type of ___>: 특정함수의 반환값 추론
// 액션타입 선언시 as const를 하지 않으면 작동하지 않음.
type CounterAction =
  | ReturnType<typeof increase>
  | ReturnType<typeof decrease>
  | ReturnType<typeof increaseBy>;
//리덕스 모듈에서 관리할 상태 타입(number)선언
type CounterState = {
  count: number;
};

/* 초기상태 선언 */
const initialState: CounterState = {
  count: 0,
};

/* 리듀서 */
//리듀서에서는 state와 함수의 반환값이 일치해야함(CounterState)
//액션의 타입은 CounterAction(위에서 만든)
function counter(
  state: CounterState = initialState,
  action: CounterAction
): CounterState {
  switch (action.type) {
    case INCREASE:
      return { count: state.count + 1 };
    case DECREASE:
      return { count: state.count - 1 };
    case INCREASE_BY:
      return { count: state.count + action.payload };
    default:
      return state;
  }
}

export default counter;
