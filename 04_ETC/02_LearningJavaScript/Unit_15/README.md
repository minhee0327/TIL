# 날짜와 시간

-   날짜, 타임존, 타임스탬프, 유닉스 시간

    -   그레고리안 달력
        -   시간을 나누는 기준이 모호하고, 윤년까지 있음..복잡..
        -   날짜와 시간 <=> 초
        -   사람들끼리 초로 시간을 알려주진않음(지금시각은 1493608660초네요 라고 하진 않지)
        -   _0초는? 1970년1월1일 0시 0분 0초(UTC, 국제표준시)_
    -   타임존
        -   오전 7시는 아침, 오후 7시는 저녁
        -   summer time...
        -   UTC을 기준으로 한 시차
            ```console
            new Date()
            <!--output: Tue Sep 01 2020 17:21:07 GMT+0900 (대한민국 표준시) -->
            ```
            -   console창에 new Date()입력하면 위와같이 UTC로부터 시차기준으로도 나오고(GMT+900), 타임존이름으로도 나오는걸 볼수 있다.(대한민국표준시)
    -   자바스크림트에서 Date 인스턴스는 모두 UTC(국제표준시, 유닉스 시간 원점)로 부터 몇 밀리초가 지났는지 나타내는 숫자.
    -   자바스크립트는 보통 이 숫자를 사람이 읽기 편한 그레고리력 날짜로 변환
    -   대한민국표준시: KST (UTC+9시간)

-   Date 객체 만드는 방법(4가지)

    -   매개변수 없이 호출: 현재 날짜 Date 객체 반환
    -   매개변수에 문자열제공: 문자열을 해석하고 맞는 날짜 반환
    -   매개변수에 숫자 제공: 유닉스 타임스템프로 해석
    -   new Date(year, month[, day, hour, minute, second, millisecond])

-   JS Date 객체의 가장 큰 문제
    -   타임존을 명시할 방법이 없음
    -   내부적으로는 항상 UTC 기준으로 저장하고, 출력할 때 운영체제에서 정의한 표준시에 맞게 변환
-   Moment.js 라이브러리
    -   타임존 지원버전
        -   세계의 타임존 정보를 모두 담고 있음
        -   이 버전으로 js Date 객체 다룰것
        -   node 환경에서는 아래 명령으로 설치
            ```console
            npm init --y
            npm install --save moment-timezone
            ```
            -   불러올때
            ```js
            const moment = require('moment-timezone');
            ```
-   날짜 데이터 만들기

    -   서버에서 날짜 생성하기(UTC 사용 혹은 타임존 명시)
    -   UTC 날짜를 사용할 수 있는 환경이라면 Date 객체의 UTC메서드 사용
        ```js
        const d = new Date(Date.UTC(2016, 4, 27)); // May 27, 2016 UTC
        const s = moment.tx([1991, 2, 27, 9, 19], 'Asia/Seoul').toDate();
        ```

-   날짜 데이터 전송하기

    -   서버에서 브라우저로 날짜 전송하거나, 반대로 브라우저에서 서버로 날짜 전송할 때 조금 복잡
    -   서버와 브라우저가 서로 다른 타임존에 있을때, 사용자는 사용자의 타임존을 기준으로 날짜를 보고싶어함
    -   JS는 UTC 기준으로 유닉스 타임스탬프 저장하므로 Date 객체를 그냥 전송해도 일반적으로 안전
    -   가장 안전한 방법 JSON 사용

        ```js
        const before = { d: new Date() };
        before.d instanceof Date; //true

        const json = JSON.stringfy(before);
        const after = JSON.parse(json);

        after.d instanceof Date;
        typeof after.d; //string
        ```

    -   어느 날짜존에 있었던간에 JSON으로 인코드 된 날짜는 UTC

-   날짜 형식(ex2)

    -   JS에서 Date 객체에서 제공하는 날짜 형식 다양하지 않아서, 원하는 형식이 없다면 직접 구현해야함
    -   Moment.js를 통해서 원하는 형식을 쉽게 만들고, 날짜 표시에 관심이 있다면, Moment.js를 권함
        -   format 메서드 써서 날짜를 원하는 형식으로 바꿈

-   날짜 구성요소(ex3)

-   날짜비교
    -   날짜 A와 날짜 B중 어느쪽이 더 앞인가 하는 단순 날짜 비교는 비교연산자를 통해 할 수 있다.
