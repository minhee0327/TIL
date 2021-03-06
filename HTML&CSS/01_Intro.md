
* HTML/CSS/JavaScript

    * HTML - 시멘틱 요소 위주로, 웹의구조, 뼈대, 골조 전문
	* CSS - 웹의 시각적 요소, 모양, 미장전문
	* JavaScript - 동적으로 활성화, 생동감, 인테리어 전

* 웹표준과 웹접근성
	* 웹브라우저: 크롬, IE, 사파리 등
	* 웹브라우저를 만드는 업체: 구글, MS, 애플 등
	* 웹표준: 웹에서 사용되는 표준 기술, 규칙 등
	* 크로스 브라우징:  
    내가 만든 홈페이지나 사이트를 다른 브라우저에서 사용하더라도,  
    사용자 입장에서는 같은(유사한) 경험이라고 생각되게끔 제작하는 기술  
    [IE에서 문제 없으면 대부분 문제 없다고 판단됨]
	* 웹접근성: 신체적, 환경적 제한이 있는 사용자를 포함하여 모든 사람들이 동등하게 접근하는 웹 콘텐츠 제작.  
(정보 통신 보조기기, img 태그내부에 alt text 등등)

* Editor (VScode로)

	* 확장팩(설치 후 껐다가 켜기)
		* Korean Language Pack for VS code: VS code 한글판
		* Live Server: html 코드를 브라우저에서 확인할 수 있게 하는 기능  
        (우측하단 go live버튼 혹은 우측 마우스로 open with live server)  
        go live 끄고 싶다면, Port 부분 click

		* Beutify/Prettier: [참고](https://ux.stories.pe.kr/150) (뷰티파이: Ctrl +Alt + K)
			- auto-fix 기능true일때 저장시 설정한 사항적용됨
			- [파일] - [기본설정] - [설정] - [확장] - [나의경우prettier탭] - 우측 [설정열기] - settings.json파일에 아래 내용추가 
			```json
			"editor.formatOnSave": true
			```
		* Highlight Matching Tag
		* Night Owl
    * 사용하진 않았지만 유용한 확장팩
        * Live Sass Compiler
        * Turbo Console log
        * Terminal
        * Better Comments
        * GitLens
        * REST Client
	* 단축키 => 몇 가지 customizing 했음

	* 추가 사항
		* Ctrl+P (preferences) => 바로가기키 들어갈 수 있음
		*" Ctrl + alt + p 이런식으로 단축키 검색 가능
		* 약어로 랲핑(wrapping)
		* 래핑할 코드 선택 (Ctrl + Shift + P )(Window)
		* 참고: 가끔 vscode상에 주석처리가 뜻대로 안될 때가 있다.  
        ( 커서가 여러개 생길 때 있는데, 오른쪽 하단에 한컴 입력기로 설정된 것을  
         Microsoft 입력기로 설정하면 된다.)

	* 웹에서 사용하는 이미지

		* 비트맵: 각 픽셀이 모여 만들어진 정보의 집합, 레스터 이미지, PX(픽셀단위), 그림판, 포토샵 툴을 이용
		    * JPG(JPEG): 손실압축/ 고해상도/이미지 품질 용량 조절 쉬움/높은 압축률(적은용량)/24bit
			* PNG:비손실압축/투명도 지원(Alpha Channel지원)/GIF 대체 포맷/8bit, 24bit
			* GIF: 비손실압축/여러장의 이미지를 하나의 파일/움짤, 애니, 동영상같은 이미지/8bit
			* WEBP: JPG, PNG, GIF 모두 대체/ 완벽한 포맷 단! 지원브라우저가 한정적(IE에서 안됨)
			* 어떤 이미지를 써야할지 고민된다면?
				* 용량이 클 경우, 용량을 줄이고 싶다 => jpg
				* 이미지 투명도가 필요하다 => png
				* 움짤을 써야한다 => git(채도, 질 떨어질 수 있지만 움짤 장점)
		* 벡터: 수학적 정보 형태(SHAPE) 결과물, 이미지의 점,선,면,위치 정보 온전히 가짐, 해상도 자유로움, 일러스트 툴이용

			* SVG: 해상도 영향에서 자유로움/css로 styling가능/javaScript event handling/코드 혹은 파일 이용

	* [오픈 소스 라이선스](OpenSource.org)
		* 오픈소스: 어떤 제품을 개발하는 과정에 필요한 소스코드나 설계도를 누구나 접근해서 열람할수 있도록 공개  
        상업적으로 사용했다간 문제 생길 수 있으니 조심해서 사용. (무조건 무료는 아녀~!주의!!)  
        항상 License 부터 찾는 습관을 들이자.

		* 몇가지 라이선스
			* Apache License: 개인/상업적 이용, 배포, 수정, 특허 신청 가능
			* MIT License: 개인 소스에 이 라이선스를 사용하고 있다는 표시만 지켜주면 된다.
			* BSD License: 라이선스를 사용하고 있다는 표시만 지켜주면 된다.  
            (소스 코드 복사해 오면 보통 같이 따라옴. 지우지만 말자)
			* Beerware: 오픈 소스 개발자에게 맥주를 사줘야하는 라이선스(만나게 되면(?)ㅎㅎ)


