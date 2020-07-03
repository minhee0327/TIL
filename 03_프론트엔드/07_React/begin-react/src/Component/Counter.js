import React, { useReducer } from 'react';

function reducer(state, action) {
    switch (action.type) {
        case 'INCREASE':
            return state + 1;
        case 'DECREASE':
            return state - 1;
        default:
            return state;
    }
}

function Counter() {

    const [number, dispatch] = useReducer(reducer, 0)

    const onDecrease = () => {
        dispatch({ type: 'DECREASE' })
    }
    const onIncrease = () => {
        dispatch({ type: 'INCREASE' })
    }

    return (
        <div>
            <h1>{number}</h1>
            <button onClick={onDecrease}>-1</button>
            <button onClick={onIncrease}>+1</button>
        </div>
    )
}

export default Counter;