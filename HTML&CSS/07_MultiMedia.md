1. img
    - 대표속성
        - **src**: 이미지 경로
        - **alt**: 대체 텍스트
        - **srcset**: 브라우저에 제시할 이미지 **url 경로 , 원본 크기 목록** 정의/단위: w,x (반응형)
        - **sizes**: 미디어 조건, 이미지 최적화 크기 목록 정의(반응형)
        ```html
        <img srcset="images/small.png 400w, 
                    images/medium.png 700w, 
                    images/large.png 1000w" 
             sizes ="(max-width:500px) 444px, 
                     (max-width:800px) 777px,
                     1222px"
             src ="images/~~.png" alt="~~~">
        ```

2. audio
    - autoplay: 자동재생
    - controls: 제어 메뉴 표시
    - loop: 반복
    - preload: 페이지 로드 시, 파일 로드 할지 지정
        - none: 로드하지 않음
        - metadata:메타데이터만 로드
        - auto: 전체 파일 로드
    -src: 콘텐츠 url
    -muted:음소거

3. video
    - autoplay: 자동재생
    - controls: 제어메뉴
    - crossorigin: 가져오기 수행여부(anonymous, use-credentials)
    - preload: 페이지 로드시, 파일 로드 여부 지정(none/metadata/auto)
    - loop
    - muted
    - poster: 동영상 썸네일 이미지 url
    - src
    - width, height


4. figure:이미지나 삽화, 도표 등의 영역 설정
5. figcaption: figure에 포함되어 이미지나, 삽화등의 설명.
6. iframe: 다른 HTML 페이지를 현재 페이지에 삽입
    - name
    - src
    - allowfullscreen
    - frameborder
    - sandbox: 보안을 위한 읽기 전용으로 삽입(allow-form, allow-scripts, allow-same-origin)
7. canvas: 그래픽이나, 애니메이션 렌더링
8. script: 스크립트 코드를 문서에 포함하거나,참조(외부 스크립트)
    - **async**: 스크립트의 비동기적(Asynchronously) 실행여부 (src필수)
    - **defer**: 문서파싱(구문 분석) 후 작동여부 (src필수)
    - src: 포함된 스크립트 코드는 무시됨
9. noscript:스크립트가 지원하지 않는 경우에 삽입할 HTML 을 정의.