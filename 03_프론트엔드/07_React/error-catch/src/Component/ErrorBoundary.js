import React, { Component } from 'react';
import * as Sentry from '@sentry/browser';

class ErrorBoundary extends Component {
    state = {
        error: false
    };
    componentDidCatch(error, info) {
        // error: error 내용
        // info: 에러 발생 위치
        console.log('에러발생');
        console.log({
            error,
            info
        });
        this.setState({
            error: true
        })
        // 실제로는 error가 호출되는 일을 서비스에서 '없어야 하는게' 맞다.
        // error, info값을 네트워크를 통해 다른 곳으로 전달하면 된다.
        // 이를 위해 따로 서버를 만드는 건 굉장히 번거로운 일 => solution => Sentry라는 상용서비스가 있음.

        // Sentry쪽으로 전달한 후, 실제 배포를 하게 되었을 경우, componentDidCatch를 하게 되면 Sentry에 자동 전달 안됨.
        if (process.env.NODE_ENV === 'production') {
            //production 모드에서 captureException 으로 자동전달 하도록함.
            Sentry.captureException(error, { extra: info });
        }

    }


    render() {
        if (this.state.error) {
            return <h1>에러 발생</h1>
        }
        return this.props.children
    }
}

export default ErrorBoundary;