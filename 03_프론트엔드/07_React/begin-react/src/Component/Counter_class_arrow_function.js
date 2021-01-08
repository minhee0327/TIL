import React, { Component } from 'react';


class Counter extends Component {
    //sol2. 커스텀 메서드 선언시, 화살표 함수 사용하기.
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
            <div>
                <h1>0</h1>
                <button onClick={this.handleDecrease}>-1</button>
                <button onClick={this.handleIncrease}>+1</button>
            </div>
        )
    }
}

export default Counter;