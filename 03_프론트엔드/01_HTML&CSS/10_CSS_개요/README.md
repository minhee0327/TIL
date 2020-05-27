## 개요, 선택자, 상속
### 1. 기본 문법
```css
선택자 {
    속성: 속성값;
    속성: 속성값;
}
```
- 선택자(selector) 의 역할
    - 속성(Property)과 값(value)을 지정할 대상을 검색
- 속성과 값의 역할
    - 검색된 대상에 지정될 CSS 명령
- 주석(Comment)
    - 문서 내 수정사항이나 설명등을 처리
    - Browser가 해석하지 않고 넘어감
```css
/* Comment */
```


### 2. CSS 선언 방식
- 인라인(in-line) 방식
    - HTML 요소(태그)의 'style' 속성에 직접 작성하는 방식
    - 이 방식은 '선택자'가 필요없음.
- 내장(embeded) 방식
    - HTML ```<style></style>``` 안에 작성하는 방식
- **링크(link)방식 (추천!)**
    - HTML ```<link>```를 이용하여 외부 문서로 CSS를 불러와 적용하는 방식
- @import 방식
    - CSS의 @import 를 이용하여 외부문서로 CSS를 불러와 적용하는 방식
    - (간단히 말하자면) CSS가 CSS를 가져오는 방식
    - link 방식은 병렬방식으로 호출이 되는 반면, import는 직렬호출이 된다.
    - 특수한 경우에 사용하는 방식.
    ```css
    /* 현재 페이지 common1.css */
    @import url('./common2.css')
    ```


### 3. 선택자(Selector)

- 기본 선택자
    - **전체 선택자**(Universal Selector): (요소 내부의) 모든 요소 선택  
    ``` * ```
    - **태그 선택자**(Type Selector): 태그이름이 E인 요소 선택  
    ``` E ```
    - **클래스 선택자**(Class Selector): HTML class 속성의 값이 E인 요소 선택  
    ``` .E ```
    - **아이디 선택자**(ID Selector):  HTML id 속성의 값이 E인 요소 선택  
    ``` #E ```
    
- 복합 선택자(Combinator)
    - **일치 선택자**(Basic Combinator): E와 F를 동시에 만족하는 요소 선택  
    ```EF```
    - **자식 선택자**(Child Combinator): E의 자식 요소 F를 선택  
    ```E > F```
    - **후손(하위) 선택자**(Descendant combinator): E의 후손(하위)요소 F를 선택  
    ```E F```
    - **인접 형제 선택자**(Adjacent Sibling Combinator): E의 *다음* 형제요소 F 하나만 선택  
    ```E + F ```
    - **일반 형제 선택자**(General Sibling Combinator): E의 *다음* 형제요소 F 모두 선택  
    ```E ~ F```

- 가상 클래스 선택자(Pseudo-Classes Selectors) - 콜론(:) 하나 붙여서 표현
    - hover 
        - E에 마우스(포인터)가 올라가 있는 동안에만 E 선택  
        ```E:hover```
    - active
        - E를 마우스로 클릭하는 동안에만 E선택  
        ```E:active```
    - focus
        - E가 포커스 된 동안에만 E 선택 (대화형 콘텐츠에서 사용가능(input,img, tabindex..))  
        ```E:focus```
    - first-child
        - E가 형제 요소 중 첫번째 요소라면 선택  
        ```E:first-child``` 
    - last-child
        - E가 형제 요소 중 마지막 요소라면 선택  
        ```E:last-child```
    - nth-child
        - E가 형제 요소 중 n번째 요소라면 선택  
        (n 키워드 사용시 0 부터 해석(Zero-base))  
        ```E:nth-child(1)```: 1번째 요소만 선택  
        ```E:nth-child(2n)```: 짝수 요소만 선택  
        ```E:nth-child(n+3)```: 3번째 요소부터 이후 요소들 선택
        - nth-child 사용시, 뒤에서부터 해석하자. (강의 참조)
    - nth-of-type
        - E의 타입(**태그이름**)과 동일한 타입인 형제요소 중 E가 n번째 요소라면 선택  
        (n 키워드 사용시 0 부터 해석(Zero-base))  
        ```E:nth-of-type(n)```
    - not(부정선택자)
        - S가 아닌 E 선택  
        ```E:not(S)```

- 가상 요소 선택자(Psedo Element Selectors)
    - 가상의 요소를 제공해서 사용할 수 있는 선택자.
    - **before**
        - E 요소 내부의 앞에, 내용 **(content)** 삽입  
        ```E::before```
            ```css
            ul li::before{
                content:"숫자"
            }
            ```
    - **after**
        - E 요소 내부의 뒤에, 내용 **(content)** 삽입  
        ```E::after```
            ```css
            ul li::after{
                content:".0"
            }
            ```
        - content에 url()을 통해, 이미지 파일을 넣을 수도 있다.
    - 옛날에는 하나 입력해서 사용했었기 때문에 종종 :before, :after를 볼 수 있음.
    - IE8 이후부터는 콜론을 2개 (::)입력하는 것이 표준.

- 속성선택자(Attribute Selectors)
    - 참고
        - html의 속성: attribute
        - css의 속성: property
    - [attr]
        - 속성 attr을 포함한 요소 선택   
        ```[disabled]{}```
    - [attr=value]
        - 속성 attr을 포함하며, 속성값이 value인 요소 선택  
        ```[type=password]{}```  
        ```[type="password"]{}```
    - [attr^=value]
        - 속성 attr을 포함하며, 속성값이 value로 *시작하는* 요소 선택  
        ```[class^="btn-"]{}```
    - [attr$=value]
        - 속성 attr을 포함하며, 속성값이 value로 *끝나는* 요소 선택  
        ```[class$="success"]{}```

- 상속
    - 대부분 글자와 관련된 속성이 적용됨.(font, color, text-align....)
    - 강제 상속
        ```css
            .parent{
                position: absolute;
            }
            .child{
                postion: inherit;
            }
        ```
        - 단, 바로 아래 자식요소만 가능, 모든 속성이 가능한 것은 아님

- 우선순위
    - 같은 요소가 여러 선언의 대상이 될 경우, 
    - 어떤 선언의 CSS 속성(property)을 우선 적용할지 결정하는 방법
    > 우선순위에는 ' 명시도, 선언 순서, 중요도' 의 개념이 있다. 
    >1. 명시도 점수가 높은 선언이 우선(명시도)
    >2. 점수가 같은 경우, 가장 마지막에 해석(늦게 작성한)되는 선언이 우선(선언 순서)
    >3. 명시도는 '상속'규칙보다 우선(중요도)
    >4. !important 가 적용된 선언 방식이 다른 모든 방식보다 우선(중요도)

    - 점수 환산
        1. 가장중요(!important) : 모든 선언을 무시하고 가장 우선!
            - score : ∞ pt
        2. 인라인 선언방식(Style Attribute):  점수 높기 때문에, 덮어쓰기가 어려움.
            - 점수: 1000pt
        3. 아이디 선택자(ID selector)
            - 점수: 100 pt
        4. class 선택자(class selector)
            - 점수 : 10pt
        5. 태그 선택자
            - 점수 : 1 pt
        6. 전체 선택자(*)
            - 점수: 0pt
        7. 상속: 상속받은 속성은 항상 우선하지 않음
            - (계산하지 않는다.)
        > :hover 처럼 '가상 클래스' 는 '클래스' 선택자의 점수(10pt)를 가지며,  
        > :before 처럼 '가상 요소' 는 '태그' 선택자의 점수 (1pt)를 가집니다.  
        > :not() 처럼 '부전선택자' 는 점수를 가지지 않습니다.