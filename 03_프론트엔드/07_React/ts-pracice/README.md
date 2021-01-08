# TypeScript연습

1. 타입스크립트 사용이유

   - 자동완성 및 타입확인 (js의 weeked typed 언어 보완)
   - 함수 사용시 어떤 파라미터 필요한지, 반환은 어떤값을 하는지 코드 열지 않고 확인 가능
   - 리엑트에서는 컴포넌트를 사용할 때, props로 무엇을 전달해야하는지 JSX과정에서 바로 알 수 있음.
   - 컴포넌트 내부에서도 자신의 props에 어떤 값이 있는지 state에 어떤값이 있는지 알 수 있음
   - 리덕스 사용시에도, 스토어 안에 어떤 상태가 들어있는지 바로 조회가능!

2. 실수방지

   - 타입 추론이 되니까 사소한 오타가 발생하더라도 IDE에서 바로 알 수 있다.
   - null이나 undefined일 수도 있는 값의 내부 값 혹은 함수를 호출할 때 사전에 null 체킹 하지 않으면 오류 띄우니까  
     null 체킹도 확실히 할 수 있음.

3. 실습 요약
   - package.json 설정 초기 파일 생성: yarn init -y :
   - 타입스크립트 설정파일: tsconfig.json
     - 직접 작성해도 괜찮고
     - yarn global add typescript로 typescript를 글로벌 설치후, tsc --init 명령으로 생성할 수도 있음
     - yarn으로 설치 안될시(npm install -g typescript) 후 tsc --init
     - tsconfig.json 내부에 기본 설정 review
       - target: 컴파일된 코드가 어떤 환경에서 실행될지 정의 (es5, es5...)
       - modules: 컴파일된 코드가 어던 모듈 시스템사용할지? (commonJS, es2015....)
       - strict: 모든 타입 체킹 옵션 활성화
       - esModuleInterop: commonjs모듈형태 파일을 es2015모듈 형태로 불러옴
       - outDir: 컴파일된 파일 저장 경로 설정 가능.
   - TypeScipt를 사용하면, 특정변수 또는 상수 타입을 지정할 수 있고, 사전에 지정한 타입이 아닌 값이 설정되면 바로 에러발생 시킨다.
   - 에러가 나타나면 컴파일 되지 않는다.
   -
