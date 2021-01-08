# 10\_Flex

## 1. flex 개요

* 요소의 크기가 불분명하거나 동적인 경우에도, 각 요소를 정렬할 수 있는 효율적인 방법을 제공.
* 2개의 개념으로 나뉨
  * [Container](10_flex.md#11-container-속성): 
    * items를 감싸는 부모요소, 각 item을 정렬하기위해 필수!
    * 속성
      * [display](10_flex.md#111-display): flex container 정의
      * [flex-flow](10_flex.md#113-flex-flow) \(단축\)
        * flex-direction:flex items의 주축\(main-axis\)설정
        * flex-wrap: flex items 여러 줄묶음\(줄바꿈\)설정
      * [justify-content](10_flex.md#114-justify-content): 주축\(main-axis\) 정렬방법 설정
      * [align-content](10_flex.md#115-align-content): 교차축\(cross-axis\) 정렬 방법 설정\(2줄 이상\)
      * [align-items](10_flex.md#116-align-items): 교차축\(corss-axis\)에서 items의 정렬방법 설정\(1줄\)
  * [items](10_flex.md#1.2-flex-items-속성): 
    * 속성
      * [order](10_flex.md#121-order)
      * [flex](10_flex.md#122-flex)
        * [flex-grow](10_flex.md#123-flex-grow)
        * [flex-shrink](10_flex.md#124-flex-shrink)
        * [flex-basis](10_flex.md#125-flex-basis)
      * [align-self](10_flex.md#126-align-self)

### 1.1 Container 속성

#### 1.1.1 display

* 속성
  * flex: flex container가 수직으로 쌓임
  * inline-flex: flex의 item은 동일하게 움직이지만, container가 수평으로 쌓임

#### 1.1.2 용어 정리

* 주축\(main-axis\)
* 교차축\(cross-axis\)
* main-start,flex-start: 주축의 시작
* main-end,flex-end: 주축의 끝
* cross-start, flex-start: 교차축의 시작
* cross-end, flex-end: 교차축의 끝
* flex-start, flex-end는 방향에 맞는 시작점과 끝점을 의미

#### 1.1.3 flex-flow

* flex items의 주축\(main-axis\)을 설정하고 itesm의 여러 줄 묶음\(줄바꿈\)도 설정
* 속성
  * flex-direction: 주축
    * row: 수평축 \(왼=&gt;오\)으로 표시 \(main-axis: 수평, cross-axis:수직\)
    * row-reverse: 수평축\(오=&gt;왼\)으로 표시 \(main-axis: 수평, cross-axis:수직\)
    * column: 수직축 \(위 =&gt; 아래\) 으로 표시 \(main-axis: 수직, cross-axis:수평\)
    * column-reverse: column의 반대축\(아래=&gt;위\)으로 표시 \(main-axis: 수직, cross-axis:수평\)
  * flex-wrap: items의 여러줄 묶음\(줄 바꿈 설정\)
    * no-wrap: 모든 items를 여러 줄로 묶지 않음\(한줄에 표시\) - 기본값
    * wrap: items를 여러 줄로 묶음
    * wrap-reverse: itmes를 wrap의 역방향으로 여러줄로 묶음

#### 1.1.4 justify-content

* 주축\(main-axis\) 정렬방법 설정
  * flex-start: items를 시작점\(flex-start\)점으로 정렬 \(기본값\)
  * flex-end: items를 끝점\(flex-end\)으로 정렬
  * center: items를 가운데 정렬
  * space-between: 시작 item은 시작점에, 마지막 item은 끝점에 정렬되고 나머지 items들은 사이에 고르게 정렬됨
  * space-around: items를 균등한 여백을 포함하여 정렬

#### 1.1.5 align-content

* 교차축의 정렬방법을 설정\(2줄 이상\)
* 주의점: flex-wrap 속성을 통해 items가 여러줄이고 여백이 있을 경우만 사용가능

  > items가 한 줄일 경우, align-items 속성 사용하기!

* 속성
  * stretch: container의 교차축을 늘리기 위해, items를 늘림.
  * flex-start
  * flex-end
  * center
  * space-between
  * space-around

#### 1.1.6 align-items

* 교차축\(corss-axis\)에서 items의 정렬방법 설정\(1줄\)
* 주의점은 flex-wrap을 통해 여러줄일 경우에는 align-content 속성이 우선합니다. 따라서, align-itmes를 align-content 속성값을 기본값\(strech\) 으로 설정해야 합니다.
* 속성
  * stretch
  * flex-start
  * felx-end
  * center
  * baseline: items를 문자 기준 선에 정렬

### 1.2 flex items 속성

* 속성
  * order: flex-item의 순서 설정
    * flex
      * flex-grow: 증가 너비 비율 설정
      * flex-shrink: 감소 너비 비율 설정
      * flex-basis: 공간 배분 전 기본 너비 설정
    * align-self:교차축\(cross-axis\)에서 item의 정렬 방법 설정

#### 1.2.1 order

* item의 순서 설정
* item에 숫자 지정하고 숫자 클수록 순서 밀림
* 음수 허용
* HTML 구조와 상관 없이 순서 변경할 수 있기 때문에 유용
* 속성 값
  * 숫자\(기본값: 0\)

#### 1.2.2 flex

* 아래 flex-grow, flex-shrink, flex-basis의 단축속성
* item의 너비\(증가, 감소, 기본\)을 설정하는 단축속성.
* flex: 증가너비 감소너비 기본너비;

#### 1.2.3 flex-grow

* item의 증가 너비 비율을 설정합니다.
* 숫자가 크면 더 많은 너비를 가집니다.
* item 이 가변 너비가 아니거나, 값이 0일 경우 효과 없음
* 속성값
  * 숫자\(**기본값: 0**\)로 너비 비율 설정
  * basis도 auto라고 명시하지 않으면 기본값은 0 입니다!!!

    ```css
    .item{
    flex: 1 1 20px; /* 증가너비 감소너비 기본너비*/
    flex: 1 1; /* 증가너비 감소너비*/
    flex: 1 20px; /* 증가너비 기본너비 (단위를 사용하면 flex-basis가 적용됨*/
    }
    ```

#### 1.2.4 flex-shrink

* item의 감소하는 너비의 비율을 설정합니다.
* 숫자가 크면 더 많은 너비가 감소합니다.
* item 이 가변 너비가 아니거나, 값이 0일 경우 효과 없음
* 속성값
  * 숫자\(기본값: 1\)로 감소 너비 비율 설정

#### 1.2.5 flex-basis

* item의 공간 배분 전 기본 너비 설정
* 값이 auto일 경우, width, height등의 속성으로 item의 너비를 설정할 수 있다.
* 하지만 단위 값이 주어질 경우 설정할 수 없다.
* 속성값
  * auto: 가변item과 같은 너비\(기본값\) 
  * 단위: cm, px, em 등 단위 지정

#### 1.2.6 align-self

* 교차축\(cross-axis\)에서 개별 item의 정렬 방법을 설정
* align-items는 container 내 모든 items의 정렬 방법을 설정합니다.
* 필요에 의해 일부 item만 정렬 방법을 변경하려고 할 경우, align-self를 사용할 수 있습니다.
* 이 속성은 align-items속성보다 우선합니다.
* 속성값
  * auto: container의 align-items속성을 상속받음\(기본값\)
  * stretch: container의 교차축을 채우기 위해 item을 늘림
  * flex-start: item을 각 줄의 시작점\(flex-start\)으로 정렬
  * flex-end: item을 각 줄의 끝점\(flex-end\)으로 정렬
  * center: item을 가운데 정렬
  * baseline: item을 문자 기준선에 정렬

```text
##### [맨 위로 돌아가기](#flex)
```

