# 이터레이터와 제너레이터

1. 이터레이션 프로토콜
   - 이터레이터 그 자체로 크게 쓸모있다기보단, 더 쓸모있는 동작이 가능해지도록 하는데 의미가 있다.
   - 이터레이터 프로토콜은 모든 객체를 이터러블 객체로 바꿀 수 있다.
2. 제너레이터
   - 이터레이터를 사용해 자신의 실행을 제어
     - 함수의 실행을 개별적 단계로 나눔으로써, 함수의 실행을 제어함
     - 실행중인 함수와 통신
   - function 키워드 위에 (\*) 붙이는 것을 제외하면 문법은 일반 함수와 같음
   - return 이외에 yield키워드 사용
   ```js
   function* rainbow() {
     yield "red";
     yield "orange";
     yield "yellow";
     yield "green";
     yield "blue";
     yield "indigo";
     yield "violet";
   }
   ```
   - 위 제네레이터를 호출하면, 이터레이터를 얻습니다.
   ```js
   const it = rainbow();
   it.next(); // {value: 'red', done: false}
   it.next(); // {value: 'orange', done: false}
   ```
   - rainbow 제너레이터는 이터레이터를 반환하므로, for...of루프에서 쓸 수 있다.
   - 제너레이터와 호출자 사이에 양방향통신이 가능(yield 표현식과 양방향 통신 ex4)
   - 제너레이터와 return
     - 제너레이터에서 return 문을 사용하면 위치와 관계없이 done은 true가 되고, value는 반환하는 값이 된다.
     - 단, done이 true일 경우 value프로퍼티에 주의를 기울이지 않기때문에, 출력이 안될 수 있음.
     - 따라서 제너레이터로 중요한 값을 return 으로 반환하면 안됨. 제너레이터가 반환하는 값을 사용할 때에는 yield를 써야하고, return 은 제너레이터를 중간에 종료하는 목적으로만 사용할것!!!
