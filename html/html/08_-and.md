# 08\_테이블&폼

1. 표콘텐츠
   * tr - row
   * th \[속성: abbr, headers, colspan, rowspan, scope\] - header
   * td \[속성: headers, colspan, rowspan\] - data
   * caption: 표의 제목
   * col, colgroup : 표의 열들을 공통적으로 정의하는 컬럼, 그의 집합
     * span 속성으로 연속해서 속성 정의할 수 있음
   * thead, tbody, tfoot: 머리글, 본문, 바닥글 지정
     * 기본적으로 테이블 레이아웃의 영향을 주지는 않음.

```css
/* 기본적으로 block 요소처럼 쓰임 */
table {
    display: table;
}
tr {
    display: table-row;
}
th,
td {
    display: table-cell;
}
```

1. form\(양식\)
   * 웹 서버에 정보를 제출하기 위한 양식의 범위를 정의
   * form이 다른 form을 자식요소로 포함 할 수 없다.
   * 속성\(기본값 이탤릭체로 표기\)
     * action : 전송 정보를 처리할 웹페이지의 url
     * methond: 서버로 전송할 HTTP 방식\(_GET_, POST\)
     * autocomplete: 사용자가 이전에 입력한 값으로 자동완성 기능 사용할지 여부\(_on_,off\)
     * name: 고유한 양식의 이름
     * novalidate: 서버로 데이터를 전송시, 양식 데이터의 유효성을 검사하지 않도록 설정.
     * target: 서버로 전송 후 응답받을 방식 지정\(_\_self_, \_blank\)
2. input: 사용자에게 입력받을 데이터 양식
   * 속성
     * autocomplete\(on, off\)
     * autofocus\(boolean\)
     * checked \(boolean\) - type속성이 radio, checkbox일때만
     * name: 양식의 이름
     * placeholder
     * readonly
     * form
     * type: 입력받을 데이터의 종류.\(button, email, password, checkbox, submit, text....\)
3. label
   * 라벨가능 요소의 제목
   * for 속성으로 라벨 가능 요소를 참조하거나, 콘텐츠로 포함
   * 라벨 가능 요소: button, input, progress, select, textarea
4. button
   * 속성
     * autofocus
     * disabled
     * form
     * name
     * type
5. textarea
6. fieldset, legend
7. select, datalist, optgroup, option
   * select: size, multiple,disabled
   * optiongroup: label, disabled
   * option: selected, label, value, disabled
   * datalist: input에 미리 정의된 옵션을 지정하여, 자동완성\(autocomplete\)기능을 제공하는데 사용
8. progress: 작업의 완료 진행률\(max:총량, value:진행률\)
   * 보통 javaScript로 value값을 control해서 현재 진행률을 나타낼 수 있다.

