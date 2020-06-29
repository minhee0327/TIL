import React from 'react';
import Hello from './Hello.js';
import './App.css'

function App() {
  const name = "react";
  //1. 인라인 스타일 작성방법
  // naming할때 Camel 표기법으로 naming한다.
  const style = {
    backgroundColor: 'black',
    color: 'aqua',
    fontSize: 24,
    padding: '1rem'
  }

  return (
    <>
      <Hello />
      {/* 1. inline 선언방식 */}
      <div style={style}>{name}</div>
      {/* 2. class 선언방식 : className으로 설정*/}
      <div className="gray-box"></div>
    </>
  );
}

export default App;
