# Float(띄움) & Position
1. float
    - 요소를 좌우 방향으로 **띄움** (수평 정렬)
    - float 대체로 flex box가 생겼음.
    - 속성값
        - none(기본값): 요소 띄움 없음
        - left: 왼쪽으로 띄움
        - right: 오른쪽으로 띄움
        > 요소에 float 속성을 적용하면, 적용된 요소 주변으로 문자(text)가 흐르게 됩니다.  
        > 각 요소에 float 속성이 적용되면 차례로 정렬됩니다. (기준left, right 따라 다름)  
            - 단순히 정렬만 바뀌는게 아니라 순서가 바뀐다는 점 유의!  
            
        > float 해제: float 속성이 적용된 요소의 주위로 다른 요소들이 흐르게 되는데 이를 방지하기 위해 속성을 **'해제'** 해야한다.  
            1. 형제 다음 형제 요소에 clear:(left, right, both) 추가하여 해제하기  
            2. 부모요소에 overflow: (hidden, auto) 추가하여 해제하기  
            3. **부모요소에 clearfix클래스 추가하여 해제**(추천!)  
            - 단, clearfix로 감싸진 내부에는 반드시 float할 속성들만 가지고 있어야한다.
        ```html
        <div class="clearfix parent">
            <div class="child"></div>
            <div class="child"></div>
        </div>
        ```
        ```css
        .clearfix::after{
            content:"";
            clear: both;
            display: block; /* or table*/
        }
        .child{
            float:left
        }
        ```
    - display 수정
        - float 속성이 추가된 요소는 display속성의 값이 대부분 block으로 수정됨.
        - 바뀌지 않는 값: flex, inline-flex   
        (modern web에서는 float보다 flex속성으로 수평을 지정할 수 있다.)
    - clear: float 속성이 적용되지 않도록 지정(해제)
        - 속성값
            - none: 요소 띄움 허용 (기본값)
            - left: 왼쪽 띄움 해제
            - right: 오른쪽 띄움 해제
            - both: 왼쪽, 오른쪽 모두 해제
2. position
    - 요소의 위치 지정 방법의 유형(기준)을 설정
    - 속성값
        - static: 유형(기준)없음/ 배치 불가능 (기본값)
        - relative: 요소 **자신을 기준**으로 배치
            - 주변 요소에 영향을 주거나 받을 수 있기 때문에 주의해서 사용
        - absolute: **위치상 부모요소를 기준**으로 배치
            - 조상 중, position 속성이 지정된 곳 기준
            - 만약에 position값이 없다면, 가장 조상인 viewport(window)기준
            - static이 부모로 되어있으면 그 기준으로는 배치 불가.
        - fixed: 브라우저(뷰포트) 기준으로 배치
            - 쇼핑몰 배너, 광고 배너 등에 많이 사용됨!
        - sticky: 스크롤 영역 기준으로 배치
            - top, bottom, left, right 값이 한 개 이상 존재해야함.
            - IE 지원 불가

    - top: 요소의 position 기준에 맞는 '위쪽' 에서의 거리(위치)를 지정
        - auto: 브라우저가 계산 (기본값: auto)
        - 단위 : px, em, cm 등 단위로 지정 (기본값: 0)
        - % : 부모(**위치 상의 부모(조상)**) 요소의 세로너비의 비율러 지정, 음수값 허용
    - bottom, left, right(top과 유사)
    - 특징
        - 요소 쌓임 순서(Stack order)
            - 요소가 쌓여 있는 순서를 통해, 어떤 요소가 사용자와 더 가깝게 있는지  
            (더 위에 쌓이는지를) 결정(Z축)
            1. static을 제외한 position 속성의 값이 있을 경우 가장 위에 쌓임(값은 무관)
            2. position이 모두 존재한다면 z-index 속성의 숫자값이 높을 수록 위에 쌓임.
            3. position 속성의 값이 있고, z-index 속성의 숫자 값이 같다면,  
            HTML의 마지막 코드일 수록 위에 쌓임(나중에 작성한 코드(요소))
            > position > z-index > HTML 마지막 코드
        - display 수정
            - absolute, fixed 속성값이 적용된 요소는 display 속성값이 대부분block으로 수정됨. 단, flex와 inline-flex 에는 position 속성 효과가 없다.