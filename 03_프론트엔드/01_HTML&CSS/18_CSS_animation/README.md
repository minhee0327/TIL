# Animation & Multi Columns(다단)
### 1. Animation(애니메이션) 개요 - 단축
- 요소의 애니메이션을 설정/제어
    - [animation-name](#@12-animation-name): [@keyframes 규칙](#11-keyframes-rules) 의 이름 설정 (기본값: none)
    - [animation-duration](#@13-animation-duration): 애니메이션 지속 시간 설정(기본값: 0s )
    - [animation-timing-function](#@14-animation-timing-function): 타이밍 함수 지정 (기본값: ease)
    - [animation-delay](#@15-animation-delay): 애니메이션 대기시간 설정 (기본값: 0s)
    - [animation-iteration-count](#@16-animation-iteration-count): 애니메이션 반복횟수 설정 (기본값: 1)
    - [animation-direction](#@17-animation-direction): 애니메이션 반복방향 설정(기본값: normal)
    - [animation-fill-mode](#@18-animation-fill-mode): 애니메이션 전후 상태(위치)설정(기본값: none)
    - [animation-play-state](#@19-animation-play-state): 애니메이션 재생과 정지 설정(기본값: running)
    ```css
    .box{
        aniation: 애니메이션이름 지속시간 [타이밍함수 대기시간 반복횟수 전후상태 재생/정지];
        animation: hello 2s linear infinite both;
    }
    @keyframes hello{
        0%{width: 200px;}
        100%{width: 50px;}
    }
    ```

#### 1.1 @keyframes-rules
- 2개 이상의 애니메이션 중간 상태 (프레임) 지정  
```css
@keyframes 애니메이션 이름{
    0%{속성: 값;}
    50%{속성: 값;}
    100%{속성: 값;}
}
```
#### 1.2 animation-name
- @keyframes 규칙(애니메이션 프레임)의 이름을 지정
    - none: 애니메이션을 지정하지 않음
    - @keyframes 이름 : 이름이 일치하는 @keyframes 규칙의 에니매 적용

#### 1.3 animation-duration
- 시간: 지속시간을 설정 (기본값: 0s)

#### 1.4 animation-timing-function
- 타이밍 함수(애니메이션 효과를 계산하는 방법) 지정
    - ease: 빠르게-느리게
    - linear: 일정하게
    - ease-in: 느리게-빠르게
    - ease-out : 빠르게-느리게
    - ease-in-out: 느리게-빠르게-느리게
    - cubic-bezier(n,n,n,n)
    - steps(n): n 번 분할된 애니메이션

#### 1.5 animation-delay
> 음수 허용.   
> 그 값 만큼 애니메이션이 앞서 시작(애니메 주기 도중에 시작)

#### 1.6 animation-iteration-count
- 애니메이션의 반복 횟수를 설정
    - 숫자: 반복횟수 설정 (기본값: 1)
    - infinite : 무한반복

#### 1.7 animation-direction
- 애니메이션의 반복 방향을 설정
    - normal : 정방향만 반복 (기본값)
    - reverse: 역방향만 반복
    - alternate : 정방향에서 역방향으로 반복(왕복)
    - alternate-reverse: 역방향에서 정방향으로(왕복)

#### 1.8 animation-fill-mode
- 애니메이션의 전후 상태(위치)를 설정
    - none: 기존위치에서 시작 => 애니메이션 시작위치로 이동 => 동작 => 기존위치에서 끝
    - forwards: 기존위치에서 시작 => 애니메이션 시작위치로 이동=> 동작=> 애니메이션 끝 위치에서 끝
    - backwards: 애니메이션 시작 위치에서 시작 => 동작=> 기존 위치에서 끝
    - both: 애니메이션 시작 위치에서 시작=> 동작=> 애니메이션 끝 위치에서 끝

#### 1.9-animation-play-state
- 애니메이션의 재생과 정지를 설정
    - runnging: 기본값
    - paused : 애니메이션 정지  




### 2. 다단(Multi Comlumns)
- 일반 블록 레이아웃을 확장하여 여러 텍스트 다단으로 쉽게 정리하며 가독성 확보
    - columms: auto(기본값)
        - column-count
            - auto
            - 숫자(단의 갯수 결정)
        - column-width
            - auto
            - px, em, cm등 단위
            > 각 단이 줄어들 수 있는 최적너비(최소 너비)를 설정하며,  
            > 요소의 너비가 가변하여 하나의 단이 최적 너비보다 줄어들 경우 단의 갯수가 조정된다.
    - column-rule(다단 선)
        - column-rule-width
            - 기본값: medium
        - column-rule-style
            - 기본값: none
        - column-rule-color
            - 기본값: 요소의 글자색과 동일
    - column-gap
        - 단과 단 사이의 간격 설정
        - normal: 브라우저가 단과 단 사이의 간격을 설정(1em)
        - 단위 px, em, cm등 단위로 지정
