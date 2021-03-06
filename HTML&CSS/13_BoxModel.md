# 박스 모델
1. width, height
    - 기본값 : auto (브라우저가 너비 계산)
        - width: 
            - 100% (block요소)
            - 0(px) (inline 요소)
        - height: 
            - 0(px)로 인식(block요소)
            - 0(px)로 인식(inline요소)
    - 단위: px, em, cm 등 단위 지정
    - 인라인 요소는 기본적으로 가로,세로 너비 가질수 없다.  
     대신, 텍스트 다루는데 특화

2. 최대 최소
    - max-width, max-height: 요소의 최대 가로너비, 세로너비
        - 단위: px, em, %등으로 단위 지정(기본값 : none)
        - auto : 브라우저가 너비 계산
    - min-width, min-height: 요소의 최소 가로너비, 최소 세로너비
        - 단위: px, em, %등으로 단위 지정(기본값 : 0)
        - auto : 브라우저가 너비 계산

3. margin
    - 요소의 '외부(바깥) 여백'을 지정(단축속성)
        > 음수값 사용 가능
    - 단위: px, em, cm 등으로 단위 지정(기본값 : 0)
    - auto : 브라우저가 너비 계산
    - % : 부모요소의 가로 너비에 대한 비율로 지정
    - 사용법
        - magin: 상, 우, 하, 좌 ```margin: 10px 20px 30px 40px;```
        - margin: 상, [우,좌], 하 ```margin: 10px 20px 30px;```
        - margin: [상,하],[우,좌] ```margin: 10px 20px;```
        - margin: [상,우,하,좌] ```margin: 10px;```
    - 개별속성
        - margin-top
        - margin-right
        - margin-bottom
        - margin-left
    - 마진중복(병합, collapse)
        - 마진의 특정 값들이 '중복'되어 합쳐지는 현상
            - 형제 요소들의 margin-top과 margin-bottom이 만났을 때
            - 부모 요소의 margin-top과 자식요소의 margin-top이 만났을 때
            - 부모 요소의 margin-bottom과 자식요소의 margin-bottom이 만났을 때
        > 마진 중복은 버그(오류)가 아님! 현상을 우회하거나 응용가능
        - 마진 중복 계산법
            - 마진 중복 발생시, 중복 값 계산방법  

            |조건|요소A마진|요소B마진|계산법|중복값|
            |------|---|---|---|---|
            |둘다 양수|30px|10px|더 큰값으로 중복|30px|
            |둘다 음수|-30px|-10px|더 작은값으로 중복|-30px|
            |각각 양수,음수|-30px|10px|-30+10=-20|-20px|

4. padding
    - 요소의 '내부(안)' 여백 지정(단축)
    - 단위: px, em, cm 등으로 단위 지정(기본값 : 0)
    - % : 부모요소의 가로 너비에 대한 비율로 지정
    - 사용법
        - padding: 상, 우, 하, 좌 ```margin: 10px 20px 30px 40px;```
        - padding: 상, [우,좌], 하 ```margin: 10px 20px 30px;```
        - padding: [상,하],[우,좌] ```margin: 10px 20px;```
        - padding: [상,우,하,좌] ```margin: 10px;```
    - 크기증가: 추가된 padding값 만큼 요소의 크기가 커지는 현상
    - 크기가 커지지 않도록 **직접** 계산
    ```css
        .box{
            width: 60px; /* +40px */
            height: 80px; /* +20px */
            background: red;
            padding: 10px 20px;
        }
    ```
    - 크기가 커지지 않도록 **자동** 계산
    ```css
        .box{
            width: 100px;
            height: 100px;
            background: red;
            padding: 10px 20px;
            box-sizing: border-box;
        }
    ```
    > 직접 작성하지 않고, box-sizing: border-box;를 추가.

5. border: 
    - 요소의'테두리 선'을 지정(단축)
    - 속성값
        - border-width: 선의 두께, 기본값(medium) 
            - 상, 하, 좌, 우 개별 설정 가능(단축,개별 모두 가능)
            - 속성값
                - medium: 중간두께(기본값)
                - thin: 얇은 두께
                - thick: 두꺼운 두께
                - 단위: px, em, cm 등 단위 지정
        - border-style: 선의 종류, 기본값(none) 
            - 상, 하, 좌, 우 개별 설정 가능 (단축,개별 모두 가능)
            - 속성값
                - none: 선없음(기본값)
                - solid: 실선(일반선)
                - dotted: 점선
                - dashed: 파선
                - double: 두줄선
                - 그밖: groove, ridge, inset, outset
        - border-color: 선의 색상, 기본값(black) 
            - 상, 하, 좌, 우 개별 설정 가능 (단축,개별 모두 가능)
            - 속성값
                - 색상: 선의 색상을 지정 (기본: black)
                - transparent : 투명한 선(요소의 배경색)
    - border-top-width, border-bottom-style, border-bottom-color
    - border-right-width, border-right-style, border-right-color
    - 등등..
    - border 사용할 때, 너비와 높이 계산 padding처럼 해야됨.

6. box-sizing
    - 요소의 크기 계산 기준을 지정
    - 속성값
        - content-box: 너비(w,h)만으로 요소의 크기를 계산(기본값)
        - border-box: 너비(w,h)에 안쪽여백(padding)과 테두리선(border)을 포함하여 요소크기 계산

7. display: 
    - 요소의 박스 타입(유형)을 설정
    - 속성
        - block : 블록요소(div등)
        - inline : 인라인 요소(span 등)
        - inline-block: 인라인-블록요소(input 등)
        - 기타: table, table-cell, flex 등
        - none: 요소의 박스타입이 없음(요소가 사라짐)

8. overflow(단축)
    - 요소의 크기 이상으로 내용(자식요소)이 넘쳤을 때, 내용의 보여짐을 제어.
    - 속성값
        - visible(기본값): 넘친부분 자르지 않고 그대로 보여줌
        - hidden: 넘친 부분을 잘라내고 보이지 않게함.
        - scroll: 넘친 부분 잘라내고 스크롤 바 이용해서 보여줌
        - auto: 넘친 부분 있는 경우는 잘라내고, **넘친 방향만** 스크롤바를 이용하여 볼수있게함.
9. opacity
    - 투명도 지정
    - 속성값
        - 숫자: 0~1 사이의 소숫점 숫자 (기본값: 1)
    > display: none; 은 요소가 완전 사라지는 개념
    > opacity:는 단순히 투명도 지정, 요소는 있음!!!