# Sample폴더 설명
- 모듈의 종류
    - Built-in Core Module (내장된 모듈, Node.js module)
        - 'path': 파일의 경로를 자유롭게 다룰 수 있도록함
        - 'readline': 사용자로부터 입력을 받는다. (공식문서 참조해서, 필요한 메서드 사용)
        - 많은 종류가 있다... 이건 공식문서를 참조해서, 필요에 맞게 적절히 사용.
    - Community-based Module (예: npm, ESM)
        - npm CLI를 사용해야함
    - Local Module (MathUtil, readline..)
        - 특정 프로젝트에 적용된 모듈
        - 로컬 환경에서 만든 모듈
        
- 각 기능별로 모듈을 관리하고 적용
- 입력받은 도형의 종류, 값에 따라 해당 넓이를 구해보자.
- 부가 설명
    ```js
    const readline = require('readline');
    ```
    - 사용자로부터 입력을 받을 수 있도록 
    - nodeJS 모듈이기 때문에, 실행환경이 nodeJS면 바로 사용할 수 있음
    - 내장되어 있는 readline