### 글꼴, 문자
1. font
    - 글자 관련 속성들을 지정(단축)
    ```css
    font: 기울기 두께 크기/ 줄높이 글꼴;
    ```
    > 단축 속성을 사용하려면 font-size와 font-family를 필수로 입력해야한다.  

    - 속성
        - font-style: 글자 스타일(기울기) 지정
            - 속성 값
                - normal: 기본값
                - italic : 이탤릭체
                - oblique: 기울기
        - font-weight: 글자 두께(가중치) 지정
            - 속성 값
                - normal: 기본글짜 두께 , 400과 동일
                - bold: 글자 두껍게, 700과 동일
                - bolder : 부모(상위) 요소보다 더 두껍게 (bold보다 더 두껍게 아님!)
                - lighter: 부모(상위) 요소보다 더 얇게
                - 숫자 : 100~900까지 100단위 숫자 9개
        - font-size: 글자 크기 지정(medium, 16px)
            - 속성 값
                - 단위 : px, em, cm 등 단위로 지정
                - % : 부모(상위) 요소의 비율로 지정
                - xx-small, x-small, small, medium, large, x-large, xx-large
                - smaller, larger: 부모(상위) 요소대비 크기
        - line-height: 줄 높이 (normal, Recet.css적용시 1)
            - 속성값
                - normal: 브라우저의 기본 정의사용(1~1.4)
                - **숫자**: 요소 자체 글꼴 크기의 배수로 지정(1.4~1.7 추천)
                - 단위: px, em, cm등 잔위로 지정
                - %: 요소 자체 글꼴 크기의 비율로 지정
        - font-family: 글꼴 서체 지정(운영체제(브라우저)따라 다름)
            - 속성값
                - 글꼴이름 글꼴 (서체) 후보 목록을 지정
                - 글꼴 계열
                    - serif : 바탕체 
                    - sans-serif: 고딕체
                    - monospace: 고정너비(가로폭이 동등한) 글꼴계열
                    - cursive: 필기체 계열
                    - fantasy: 장식 글꼴(재미있는 문자 표현 포함)
            ```
            font-family: Arial, "Open Sans", "돋음", sans-serif;
            ```
            > 글꼴 계열은 필수 입력

2. 문자(Text) 관련속성
    - color: 문자의 색상을 지정
        - 속성값
            - 색상: 문자의 색상 지정
            - 색상표현
                - 색상이름: 브라우저에서 제공하는 색상이름(red, blue,..)
                - hex 색상코드: 16진수 색상( #000000 )
                - RGB : 빛의 삼원색 ( rgb(255,255,255))
                - RGBA : 빛의 삼원색, 투명도 ( rgba(255,255,255,.5))
                - HSL : 색상,채도, 명도(hsl(120, 100%, 50%))
                - HSLA: 색상, 채도, 명도, 투명도(hsl(120, 100%, 50%,.5))
            > 위 색상표현은 색을 이용하는 모든 속성(property)의 값으로 사용가능  
            > RGBA: RED, GREEN, BLUE, Alpha Channel  
            > HSLA: HUE, Saturation, Lightness, Alpha Channel  
    - text-align: 문자 정렬 방식 지정
        - 속성값
            - left: 기본값
            - right
            - center
            - justify : 양쪽 맞춤 ( 두줄 이상 )
            > direction(텍스트 방향 및 쓰기 방향지정/ltr, rtl) 속성의 값에 의해  
            > text-align 속성의 '기본값'이 변경될 수 있음.  
            > 일반적으로 left가 기본값으로 사용된다.
    
    - text-decoration: 문자의 장식(line)을 설정
        - 속성값
            - none
            - underline: 밑줄
            - overline: 윗줄
            - line-through: 중앙(가로지르는)선

    - text-indent: (첫번째 출의) 들여쓰기 지정
        > 음수값 사용가능  
        > 음수값을 사용하면 첫째 줄은 왼쪽으로 들여쓰기 됩니다.
    - letter-spacing: 문자의 자간(글자 사이 간격)지정
        - normal: 단어 사이의 일반 간격(기본)
        - 단위 : px, em, cm 등 단위로 지정
    - word-spacing: 단어 사이의(띄어쓰기)의 간격 지정
        - normal: 단어 사이의 일반 간격(기본)
        - 단위 : px, em, cm 등 단위로 지정