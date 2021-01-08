import React, { useState } from 'react';

function Counter_useState() {
    const [number, setNumber] = useState(0);

    const onIncrease = () => {
        setNumber(prevnumber => prevnumber + 1);
    }
    const onDecrease = () => {
        setNumber(prevnumber => prevnumber - 1);
    }


    return (
        <div>
            <h1>{number}</h1>
            <button onClick={onDecrease}>-1</button>
            <button onClick={onIncrease}>+1</button>
        </div>
    )
}

export default Counter_useState;