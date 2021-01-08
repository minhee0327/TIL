import React, { Component } from 'react';


class Counter extends Component {
    constructor(props) {
        super(props);
        console.log("constructor");
    }
    static getDerivedStateFromProps(nextProps, prevState) {
        console.log("getDerivedStateFromProps");
        if (nextProps.color !== prevState.color) {
            return { color: nextProps.color };
        }
        return null;
    }
    // componentDidMount : 외부 라이브러리 연동을 하거나, 해당 컴포넌트에서 필요로하는 데이터 요청
    // axios, fetch, 등을 통해 ajax요청을 하거나, DOM의 속성을 읽거나 직접 변경하는 작업 진행에 필요.

    state = {
        counter: 0,
        fixed: 1
    }

    //함수형으로 업데이트 하기
    // setState를 여러번 걸쳐서 해야되는 경우에 유용하다.
    // Increase는 2씩 증, Decrease는 1씩 감 하는걸 볼수 있다.
    handleIncrease = () => {
        this.setState(state => ({
            counter: state.counter + 1
        }))
        this.setState(state => ({
            counter: state.counter + 1
        }))
    }
    // state로 상태 업데이트 하기
    // 상태가 바로 바뀌는 것이 아니기 때문에 연속된 경우에 두번 처리되지 않음.
    // 성능적인 이유 때문에, 상태가 바로 업데이트 되지 않고 비동기적으로 업데이트 된다.
    // 업데이트 후에 어떤 작업을 하고 싶다면, 두번째 파라미터에 callback함수를 넣는 방법도 있다.
    handleDecrease = () => {
        this.setState({
            counter: this.state.counter - 1
        })
        this.setState({
            counter: this.state.counter - 1
        })
    }

    render() {
        return (
            <div>
                <h1>{this.state.counter}</h1>
                <button onClick={this.handleDecrease}>-1</button>
                <button onClick={this.handleIncrease}>+1</button>
                <p>고정된 값: {this.state.fixed}</p>
            </div>
        )
    }
}

export default Counter;