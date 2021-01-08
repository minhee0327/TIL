import React from 'react';
import './App.css';
import User from './Component/User';
import ErrorBoundary from './Component/ErrorBoundary';

function App() {
  const user = {
    id: 1,
    username: 'minhee'
  }
  return (
    <ErrorBoundary>
      {/* props를 전달하지 않아서 error 발생 */}
      {/* 개발자 화면에는 error메세지가, 실제 노출되는 화면은 빈페이지가 나타남. */}
      {/* 대신 error 발생했음을 알려줄 것. */}
      <User />
    </ErrorBoundary>
  );
}

export default App;
