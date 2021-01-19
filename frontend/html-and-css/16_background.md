# 16 Background

1. background: 색상 이미지경로 반복 위치 스크롤특성
   * 속성
     * background-color: 배경 색상 \(기본값: transparent\)
     * background-image: 하나 이상 배경 이미지\(기본값: none\)
     * background-repeat: 배경이미지의 반복 \(기본값: repeat\)
     * background-position: 배경 이미지의 위치\(기본값: 0 0\)
     * background-attachment: 배경이미지 스크롤 여부\(특성\)
2. background-color: 요소의 배경 색상
   * 속성값
     * 색상
     * transparent\(기본값, 투명\)
3. background-image: 요소의 배경에 하나 이상 배경 이미지를 삽입
   * 속성값
     * none: 이미지 없음 \(기본값: none\)
     * url\("경로"\) : 이미지 경로\(url\)

       > 배경이미지 삽입 시, _**요소의 크기**_가 설정되어 있어야 배경이미지가 보일 수 있다.  
       > 하나 이상의 배경이미지를 삽입할 경우, `,`으로 구분.  
       > 먼저 작성된 이미지가 더 위에 쌓임.  
       > 이런 '다중 배경 이미지' 는 IE8 이하 버전에 사용 불가
       >
       > ```css
       > .box1{
       > background-image: 
       > url('../img/i1.jpg'),
       > url('../img/i2.jpg'),
       > url('../img/i3.jpg')
       > }
       > .box2{
       > backgounrd:
       > url('../img/i1.jpg') no-repeat,
       > url('../img/i2.jpg') no-repeat 100px 50px,
       > url('../img/i3.jpg') repeat-x;
       > }
       > ```
4. background-repeat: 반복되는 이미지 제어
   * repeat: 배경이미지를 수직, 수평으로 반복 \(기본값\)
   * repeat-x: 배경이미지를 수평으로 반복
   * repeat-y: 배경이미지를 수직으로 반복
   * no-repeat: 반복없음
5. background-position: 이미지 위치 지정
   * 속성값
     * %: 왼쪽 상단 모서리는 0% 0%, 오른쪽하단 100% 100% \(기본값 0% 0%\)
     * 방향: 방향을 입력하여 위치 설정: top, bottom, left, right, center
     * 단위: px, em, cm 등 단위로 지정
   * 사용법
     * 값이 방향일 경우

       ```css
       background-position: 방향1 방향2;
       ```

     * 값이 단위\(%, px\)인 경우

       ```css
       background-position: x축 y축;
       ```
6. background-attachment: 요소가 스크롤 될 때 배경 이미지의 스크롤 여부\(특성\) 지정
   * 속성값
     * scroll: 배경 이미지가 요소를 따라서 같이 스크롤 됨 \(기본값\)
     * fixed: 배경 이미지가 뷰포트에 고정되어, 요소와 같이 스크롤 되지 않음
       * parallax scrolling 기능 구현가능\(참고: starbucks\)
     * local: 요소 내 스크롤 시 배경이미지가 같이 스크롤 됨.
7. background-size: 배경이미지의 크기 지정
   * 속성값
     * auto: 배경이미지가 원래의 크기로 표시됨\(기본값\)
     * 단위
       * px, em, % 등 단위로 지정
       * width height 형태로 입력\(120px 370px\)
       * width만 입력하면 비율에 맞게 지정됨\(ex. 120px\)
     * cover
       * 배경 이미지의 크기 비율을 유지하며, 요소의 더 넓은 너비에 맞춰짐
       * 이미지가 잘릴 수 있음.
     * contain
       * 배경 이미지의 크기 비율을 유지하며, 요소의 더 짧은 너비에 맞춰짐
       * 이미지가 잘리지 않음.

