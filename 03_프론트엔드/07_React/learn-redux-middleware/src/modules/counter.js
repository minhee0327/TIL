//액션 타입
const INCREASE = "INCREASE";
const DECREASE = "DECREASE";

export const increase = () => ({ type: INCREASE });
export const decrease = () => ({ type: DECREASE });

//thunk함수: 리덕스에서 비동기 작업 처리에서 가장 많이 사용. (액션객체가 아닌 함수 dispatch할 수 있음.)
//비동기 작업 처리 예시
// 파라미터로는 dispatch와 getState를 받는데, dispatch만 사용할때는 굳이 파라미터 넣을 필요 없음.
export const increaseAsync = () => (dispatch) => {
  setTimeout(() => dispatch(increase()), 1000);
};
export const decreaseAsync = () => (dispatch) => {
  setTimeout(() => dispatch(decrease()), 1000);
};

const initialState = 0;

export default function counter(state = initialState, action) {
  switch (action.type) {
    case INCREASE:
      return state + 1;
    case DECREASE:
      return state - 1;
    default:
      return state;
  }
}
