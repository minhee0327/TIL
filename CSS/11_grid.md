# Grid
- Grid TOC만 필기.
- [참고링크: heropy님 블로그 참조](https://heropy.blog/2019/08/17/css-grid/)

<hr>

## Grid Properties
- [Grid Container Properties](#Grid-Container-Properties)
- [Grid Item Properites](#Grid-Item-Properties)

<hr>

### Grid Container Properties
|속성	|의미|
|-------|----| 
|display|	그리드 컨테이너(Container)를 정의|
|grid-template-rows|	명시적 행(Track)의 크기를 정의|
|grid-template-columns|	명시적 열(Track)의 크기를 정의|
|grid-template-areas|	영역(Area) 이름을 참조해 템플릿 생성|
|grid-template|	grid-template-xxx의 단축 속성|
|row-gap(grid-row-gap)|	행과 행 사이의 간격(Line)을 정의|
|column-gap(grid-column-gap)|	열과 열 사이의 간격(Line)을 정의|
|gap(grid-gap)|	xxx-gap의 단축 속성|
|grid-auto-rows|	암시적인 행(Track)의 크기를 정의|
|grid-auto-columns|	암시적인 열(Track)의 크기를 정의|
|grid-auto-flow|	자동 배치 알고리즘 방식을 정의|
|grid|	grid-template-xxx과 grid-auto-xxx의 단축 속성|
|align-content|	그리드 콘텐츠(Grid Contents)를 수직(열 축) 정렬|
|justify-content|	그리드 콘텐츠를 수평(행 축) 정렬|
|place-content|	align-content와 justify-content의 단축 속성|
|align-items|	그리드 아이템(Items)들을 수직(열 축) 정렬|
|justify-items|	그리드 아이템들을 수평(행 축) 정렬|
|place-items|	align-items와 justify-items의 단축 속성|


### Grid Item Properties
|속성	|의미|
|-------|----| 
|grid-row-start|	그리드 아이템(Item)의 행 시작 위치 지정|
|grid-row-end|	그리드 아이템의 행 끝 위치 지정|
|grid-row|	grid-row-xxx의 단축 속성(행 시작/끝 위치)|
|grid-column-start|	그리드 아이템의 열 시작 위치 지정|
|grid-column-end|	그리드 아이템의 열 끝 위치 지정|
|grid-column|	grid-column-xxx의 단축 속성(열 시작/끝 위치)|
|grid-area|	영역(Area) 이름을 설정하거나, grid-row와 |grid-column의 단축 속성|
|align-self|	단일 그리드 아이템을 수직(열 축) 정렬|
|justify-self|	단일 그리드 아이템을 수평(행 축) 정렬|
|place-self|	align-self와 justify-self의 단축 속성|
|order|	그리드 아이템의 배치 순서를 지정|
|z-index|	그리드 아이템의 쌓이는 순서를 지정|