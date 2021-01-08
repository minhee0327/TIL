import React from "react";
import { useSelector, useDispatch, shallowEqual } from "react-redux";
import Counter from "../components/Counter";
import { increase, decrease, setDiff } from "../modules/counter";

function CounterContainer() {
  // const { number, diff } = useSelector((state) => ({
  //   number: state.counter.number,
  //   diff: state.counter.diff,
  // }));

  //최적화 방법1: useSelector를 여러번 사용하기.
  // const number = useSelector((state) => state.counter.number);
  // const diff = useSelector((state) => state.counter.diff);

  //최적화 방법2: react-redux 의 shallowEqual함수를 useSelector의 두번째 인자로 보내줌
  const { number, diff } = useSelector(
    (state) => ({
      number: state.counter.number,
      diff: state.counter.diff,
    }),
    shallowEqual
  );

  const dispatch = useDispatch();

  const onIncrease = () => dispatch(increase());
  const onDecrease = () => dispatch(decrease());
  const onSetDiff = (diff) => dispatch(setDiff(diff));

  return (
    <Counter
      number={number}
      diff={diff}
      onDecrease={onDecrease}
      onIncrease={onIncrease}
      onSetDiff={onSetDiff}
    />
  );
}

export default CounterContainer;
