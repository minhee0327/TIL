# 노드

## 노드 API 간단히 훑어보기

-   코어모듈, 파일모듈, npm 모듈

    -   `require`함수를 사용하면, 노드는 함수의 매개변수를 보고 어떤 타입인지 파악한다.
        -   코어모듈: 노드자체에서 제공하는 모듈 (예약어)
            -   일부 코어모듈은 전역(예: `process`, `buffer`), 명시적인 require문 없이 사용가능
            -   ` require(```fs```) `, ` require(```os```) `,...
        -   파일모듈:
            -   `require('./src/debug.js')`
        -   npm 모듈:
            -   node_modules에 저장되어있는 모듈파일.
            -   `require(express)`
            -   모듈을 읽는 과정
                -   모듈을 가져올때 코어 모듈 이름이 아니라면
                -   현재 디렉터리에 node_modules 서브 디렉터리가 있는지 확인하고 거기서 찾는 모듈이 있는지 확인.
                -   모듈을 찾거나, 루트 디렉터리에 도달할 때까지 과정반복.
                -   찾고자하는 모듈이 x라고 할 때
                ```
                home/minhee/test_project/node_modules/x //없으면 해당 경로 바루 위에 node_modules폴더를 찾음
                home/minhee/node_modules/x //반복해서 위로 가서 node_modules 폴더 찾음..
                home/node_modules/x
                /node_modules/x
                ```

-   파일시스템접근

    -   파일 write

        -   `path.join`으로 운영체제에 따라 디렉터리 구분자를 알맞게 사용.
            -   현재 directory뜻하는 `__dir`과 함께 사용해서 현 디렉토리 아래, fs 폴더 아래 파일 생성했다.

        ```js
        const fs = require('fs');
        const path = require('path');

        fs.writeFile(path.join(__dirname, '/fs/', 'hello.txt'), 'hello from Node~', function (err) {
            console.log(__dirname);
            if (err) console.log(`Error writing to file.`);
        });
        ```

    -   파일 read

        ```js
        const fs = require('fs');
        const path = require('path');

        fs.readFile(path.join(__dirname, '/fs/', 'hello.txt'), function (err, data) {
            if (err) return console.error(`Error reading File. ㅠ^ㅠ`);
            console.log(`Read file contents: `, data);
        });
        ```

        -   위 내용을 실행하면, 아까 write했던 폴더 내부에 있는 hello from node~ 가 나올줄 알았는데
        -   Read file contents: <Buffer 68 65 6c 6c 6f 20 66 72 6f 6d 20 4e 6f 64 65 7e>
        -   이렇게 출력됨...
        -   fs.readFile은 인코딩 정보를 제공하지 않으면, 가공 안된 바이너리 데이터인 버퍼를 반환함.
        -   따라서 인코딩 정보를 같이 넘겨주어야한다.

    -   파일 리스트 확인: `fs.readdir`
    -   파일 지울 경우: `fs.unlink`
    -   파일 옮기거나 이름 변경: `fs.rename`
    -   파일과 dir 정보 얻을 때: `fs.stat`

-   process
    -   실행중인 노드 프로그램은 process변수에 모두 접근가능
    -   해당 프로그램에 대한 정보 실행자체를 컨트롤 할 수도 있음.
    -   fatal error(치명적인 error, 실행의미 없는, 계속 실행하지 않는것이 나은 상황) => `process.exit`호출하여 즉시 실행 멈춤
    -   보통은 에러 없이 프로그램을 끝냈을 때 => 종료 코드 0
    -   프로그램에 전달된 명령줄 매개 변수 배열에 접근할 수도 있다.
