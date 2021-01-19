# 04 Block and Inline Elements

1. 블록요소
   * 사용가능한 최대 넓이를 사용한다.
   * 크기를 지정할 수 있다.
   * witdth: 100%; height: 0; 로 시작\(정확하게는 auto 의 상태\)
   * 수직으로 쌓임
   * margin, padding 위, 아래, 좌, 우 온전히 사용가능하다.
   * 레이아웃을 잡는 용도로 사용
   * display: block; \(기본\)
   * 종류
     * div
     * h1
     * p
     * 콘텐츠 구분  

       \(header, footer, main, article, section, aside, nav,  

       address, ol, ul, dl, dt, dd, hr, pre, blockquote\)
2. 인라인요소
   * 필요한 만큼의 너비만 사용\(자신에 포함된 내용만큼만\) 
   * 크기를 지정할 수 없다.
   * width: 0; height: 0; 로 시작
   * 수평으로 쌓임
   * magin, padding 위, 아래 사용 할 수 없다.
   * 텍스트를 다루는 요소
   * display: inline; \(기본\)
   * 종류
     * span
     * img
     * a
     * b, mark, em, strong, i, dfn, cite, q, u, code, kdb,  

       sup, sub, time br

추가: 1. 마진과 패딩은 여백을 지정하는 속성이고 여백은 요소와 요소 사이의 거리를 만드는데 사용될 텐데 패딩은 시각적으로는 확인이 가능하지만, 실질적인 거리를 만들어내지 못하기 때문에, **인라인 요소에서는 패딩을 쓸 수 없다.**

1. 인라인, 블럭 속성을 바꾸고싶다면?
   * display: block, inline...

