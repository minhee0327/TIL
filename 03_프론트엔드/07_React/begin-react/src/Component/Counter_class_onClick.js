import React, { Component } from 'react';


class Counter extends Component {
    handleIncrease = () => {
        console.log('INCREASE');
        //this가 button의 이벤트로 등록하는 과정에서 메서드와 컴포넌트 인스턴스 관계가 끊김.
        console.log(this);
    }
    handleDecrease = () => {
        console.log('DECREASE');
    }

    render() {
        return (
            //sol3. onClick에 새로운 함수를 만들어 전달.(비추): 렌더링할때마다, 새로 함수가 만들어짐.(최적화 까다로움)
            <div>
                <h1>0</h1>
                <button onClick={() => this.handleDecrease}>-1</button>
                <button onClick={() => this.handleIncrease}>+1</button>
            </div>
        )
    }
}

export default Counter;