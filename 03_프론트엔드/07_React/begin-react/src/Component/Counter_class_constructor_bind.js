import React, { Component } from 'react';


class Counter extends Component {
    //sol1. 클래스의 생성자 메서드 constructor에서 bind작업을 해주는 것.
    constructor(props) {
        super(props);
        this.handleIncrease = this.handleIncrease.bind(this);
        this.handleDecrease = this.handleDecrease.bind(this);
    }

    handleIncrease() {
        console.log('INCREASE');
        //this가 button의 이벤트로 등록하는 과정에서 메서드와 컴포넌트 인스턴스 관계가 끊김.
        console.log(this);
    }
    handleDecrease() {
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