1. Intro
    - 왜 Git 과 Git Hub?
    - Git: local 저장소 만들고 파일, 코드 등 관리
    - gitHub: 
        - 내가 local에서 관리하는 자료(git으로 버전 관리한 코드)를 다른 사람과 공유하거나 백업할수 있는 클라우드 서버.
        - 반대로 다른 사람이 github에 올린 자료를 복제해오거나, 어떤 커밋, 어떤 소스코드 사용했는지 확인 및 반영가능
        - 내가 git으로 관리하는 파일을 백업할 수 있음.
        - 공동 플젝 협업 가능
    - Curriculum
        - Git 과 버전 관리
        - Git & GitHub - CLI
        - Git & GitHub - GUI
---
2. 환경설정하기
    1. 버전관리가 뭔가요?
        - 원하는 시점마다 버전을 만들고, 이들간에 자유롭게 돌아다닌다.
        - 내가 만든 버전 뿐만 아니라, 동료가 만든 버전으로 이동할 수 있고
        - 동료와 내 버전을 비교해서 최신본으로 코드를 업데이트 할 수 있다.

    2. github에 코드를 올리는 과정 (flow)
        1. 내 컴퓨터 프로젝트 폴더에 git 쓸거라고 명령 `git init`
        2. 코딩
        3. 변경파일중 올리기 원하는 것만 선택 `git add`
        4. 선택한 파일들 한 덩어리로 만들고 설명 적기 `git commit -m message`
        5. github사이트에 프로젝트 저장소만들기(블로그 만드는 것처럼) 
        6. 내 컴퓨터 프로젝트 폴더에 github 저장소 주소 알려주기 `git remote add`
        7. 내 컴퓨터에 만들었던 덩어리 github에 올리기 `git push`

---

3. CLI 로 GIT 익히기
    1. 깃 초기화와 로컬저장소 (`git init`)
        - 원하는 폴더(boxiting-cat)에서 git 초기화 (`git init`) 
        - .git 숨겨진 폴더 == 로컬 저장소
        - 로컬 저장소에 내가만든 버전정보, 원격저장소 주소 등이 저장됨
        - 원격 저장소에서 내 컴퓨터로 코드를 받아오면 로컬 저장소가 자동으로 생김
        - 주의점: 한 폴더에 하나의 로컬 저장소만 유지할 것!
        
    2. 첫번째 버전만들기 (`git add`, `git commit`, `git log`)
        - 커밋(commit) == 하나의 버전
        - 실습
            1. 깃 초기화 한 폴더 내부(boxiting-cat)에 README.md, index.html 파일생성
            2. 원하는 파일만 선택하기 /전체 파일 선택하기  
            `git add README.md` /  `git add .`
            3. 메세지를 달아 커밋으로 만들기   
            `git commit -m "프로젝트 설명 파일 추가"`
            4. 생성한 커밋 보기  
            `git log`
        - 커밋 시 주의
            - 의미 있는 변동사항을 묶어서 만들것.
            - 동료 개발자 혹은 미래의 내가 어떤 파일을 수정했는지 손쉽게 찾을 수 있다.
            - 커밋 메세지는 귀찮더라도 시간 들여 작성(나중에 찾기 좋게)

    3. 만든 버전 GitHub에 올리기 (`git remote add`, `git push`)
        - 로컬 저장소: 내 컴퓨터에 버전관리하는 공간
        - 원격 저장소: 로컬 저장소에 버전관리한 코드를 공유하는 클라우드 서버
        - 실습
            1. GitHub에 로그인 & repository(저장소) 생성
            2. 내 컴퓨터 git 초기화한 폴더에 GitHub 저장소 주소 알려주기  
            `git remote add [원하는이름] https://github.com/아이디/repository이름.git`  
            `git remote add origin https://github.com/아이디/repository이름.git`  
            3. 만든 커밋 푸시하기
            ```git push origin master```
                - origin(remote) 에 master(local (브랜치)에 저장된commit들이 올라가짐)
            4. GitHub 사이트에 올라간 커밋 확인

    4. 다른 사람 저장소 받아오기 (`git pull`)
        - 원격 저장소를 내 컴퓨터에 받아오기: 클론 (`git clone`)
        - 원격 저장소의 데이터 가져오기: 풀 (`git pull`)
        - 다른 사람의 원격 저장소로 push할 때는 원격 저장소에 권한이 있어야 한다.
        - 실습
            - 새로운 폴더 생성(boxiting-oct)
            - 이전에 만든 저장소 받아오기  
                ```git clone https://github.com/아이디/repo이름.git .```
                - 마지막에 . 붙히면 해당 디렉토리에 저장소 받음
                - . 생략시 repo이름으로 새 폴더 생성후 하위에 들어가짐
                - clone해오면 자동으로 .git 생성
                - zip 파일로 받을 경우 .git이 없기 때문에 초기화, 원격저장소 지정 별도로 해야함.
                - open in desktop: GitHub desktop GUI
                - 참고: 본 강의에서는 source tree 로 GUI 컨트롤
            - 업데이트 된 데이터는 풀(pull) 명령어로 받아올 수 있다.  
                ```git pull origin master```

---
- 궁금점
    - 커밋 객체에 무엇이 저장될까?
    - 두 사람이 병렬로 커밋을 만들고 싶을때 어떡하지?
    - 두 사람이 만든 버전을 합칠수 있을까?
    - 남이 만든 오픈 소스에는 어떻게 기여할 수 있지?

4. GUI로 GIT 다지기
    1. 배울 내용
        - 소스트리로 로컬 저장소 추가하기
        - 애드(add) 와 커밋(commit) 이 무엇인지 스테이지 개념과 함께 이해하기.
        - 브랜치로(branch) 평행세계 나누기
        - 머지(merge)로 두 브랜치 합치기
        - 두 브랜치 충돌(conflict) 해결하기
        - 예의바른 병합요청(pull request) 보내기
        - 다른 사람 저장소 통으로 복제하기: 포크(fork)
    2. add 와 commit
        
