# 01\_GIT기본사용

1. **Intro**
   * 왜 Git 과 Git Hub?
   * Git: local 저장소 만들고 파일, 코드 등 관리
   * git Hub: 
     * 내가 local에서 관리하는 자료\(git으로 버전 관리한 코드\)를 다른 사람과 공유하거나 백 업 할수 있는 클라우드 서버.
     * 반대로 다른 사람이 github에 올린 자료를 복제해오거나, 어떤 커밋, 어떤 소스 코드 사용했는지 확인 및 반영 가능
     * 내가 git으로 관리하는 파일을 백업할 수 있음.
     * 공동 플젝 협업 가능
   * Curriculum
     * Git 과 버전 관리
     * Git & GitHub - CLI
     * Git & GitHub - GUI
2. 환경 설정하기
   1. 버전 관리란?
      * 원하는 시점마다 버전을 만들고, 이들 간에 자유롭게 돌아다닌다.
      * 내가 만든 버전 뿐만 아니라, 동료가 만든 버전으로 이동할 수 있고
      * 동료와 내 버전을 비교해서 최신본으로 코드를 업데이트 할 수 있다.
        1. github에 코드를 올리는 과정 \(flow\)
      * 내 컴퓨터 프로젝트 폴더에 git 쓸 거라고 명령 `git init`
      * 코딩
      * 변경 파일 중 올리기 원하는 것만 선택 `git add`
      * 선택한 파일들 한 덩어리로 만들고 설명 적기 `git commit -m message`
      * github사이트에 프로젝트 저장소 만들기\(블로그 만드는 것처럼\) 
      * 내 컴퓨터 프로젝트 폴더에 github 저장소 주소 알려주기 `git remote add`
      * 내 컴퓨터에 만들었던 덩어리 github에 올리기 `git push`
3. CLI 로 GIT 익히기 
   1.  깃 초기화와 로컬저장소 \(`git init`\)
      * 원하는 폴더\(boxiting-cat\)에서 git 초기화 \(`git init`\) 
      * .git 숨겨진 폴더 == 로컬 저장소
      * 로컬 저장소에 내가만든 버전정보, 원격저장소 주소 등이 저장됨
      * 원격 저장소에서 내 컴퓨터로 코드를 받아오면 로컬 저장소가 자동으로 생김
      * 주의점: 한 폴더에 하나의 로컬 저장소만 유지할 것!
        1. 첫번째 버전만들기 \(`git add`, `git commit`, `git log`\)
      * 커밋\(commit\) == 하나의 버전
      * 실습
        1. 깃 초기화 한 폴더 내부\(boxiting-cat\)에 README.md, index.html 파일생성
        2. 원하는 파일만 선택하기 /전체 파일 선택하기  

           `git add README.md` /  `git add .`

        3. 메세지를 달아 커밋으로 만들기   

           `git commit -m "프로젝트 설명 파일 추가"`

        4. 생성한 커밋 보기  

           `git log`
      * 커밋 시 주의
        * 의미 있는 변동사항을 묶어서 만들것.
        * 동료 개발자 혹은 미래의 내가 어떤 파일을 수정했는지 손쉽게 찾을 수 있다.
        * 커밋 메세지는 귀찮더라도 시간 들여 작성\(나중에 찾기 좋게\)

        1. 만든 버전 GitHub에 올리기 \(`git remote add`, `git push`\)
      * 로컬 저장소: 내 컴퓨터에 버전관리하는 공간
      * 원격 저장소: 로컬 저장소에 버전관리한 코드를 공유하는 클라우드 서버
      * 실습 1. GitHub에 로그인 & repository\(저장소\) 생성 2. 내 컴퓨터 git 초기화한 폴더에 GitHub 저장소 주소 알려주기 `git remote add [원하는이름] https://github.com/아이디/repository이름.git` `git remote add origin https://github.com/아이디/repository이름.git` 3. 만든 커밋 푸시하기 `git push origin master`
        * origin\(remote\) 에 master\(local \(브랜치\)에 저장된commit들이 올라가짐\)
          1. GitHub 사이트에 올라간 커밋 확인

        1. 다른 사람 저장소 받아오기 \(`git pull`\)
      * 원격 저장소를 내 컴퓨터에 받아오기: 클론 \(`git clone`\)
      * 원격 저장소의 데이터 가져오기: 풀 \(`git pull`\)
      * 다른 사람의 원격 저장소로 push할 때는 원격 저장소에 권한이 있어야 한다.
      * 실습
        * 새로운 폴더 생성\(boxiting-oct\)
        * 이전에 만든 저장소 받아오기  

            `git clone https://github.com/아이디/repo이름.git .`

          * 마지막에 . 붙히면 해당 디렉토리에 저장소 받음
          * . 생략시 repo이름으로 새 폴더 생성후 하위에 들어가짐
          * clone해오면 자동으로 .git 생성
          * zip 파일로 받을 경우 .git이 없기 때문에 초기화, 원격저장소 지정 별도로 해야함.
          * open in desktop: GitHub desktop GUI
          * 참고: 본 강의에서는 source tree 로 GUI 컨트롤

        * 업데이트 된 데이터는 풀\(pull\) 명령어로 받아올 수 있다.  

            `git pull origin master`

* 궁금점
  * 커밋 객체에 무엇이 저장될까?
  * 두 사람이 병렬로 커밋을 만들고 싶을때 어떡하지?
  * 두 사람이 만든 버전을 합칠수 있을까?
  * 남이 만든 오픈 소스에는 어떻게 기여할 수 있지?
* GUI로 GIT 다지기 1. 배울 내용
  * 소스트리로 로컬 저장소 추가하기
  * 애드\(add\) 와 커밋\(commit\) 이 무엇인지 스테이지 개념과 함께 이해하기.
  * 브랜치로\(branch\) 평행세계 나누기
  * 머지\(merge\)로 두 브랜치 합치기
  * 두 브랜치 충돌\(conflict\) 해결하기
  * 예의바른 병합요청\(pull request\) 보내기
  * 다른 사람 저장소 통으로 복제하기: 포크\(fork\)
    1. add 와 commit
  * 깃에서 커밋이란? 1. 변경사항의 모음이 아님! =&gt; 하나의 최종코드 모음!! 2. 다만 기존 커밋과 비교해서 변경된 파일이 아니면 '변경되지 않았다' 고 저장해서 용량이 무겁지 않다.
    * SVN은 바로 이전 커밋과의 변경사항만 저장
    * 그래서 커밋당 용량은 더 가볍지만, 한 버전을 보려면 처음부터 계산해야 하기 때문에 느리다.
    * Git은 바로 이전 커밋만 보면 된다. \(속도 빠르다.\)

    1. 브랜치
  * 왜 같이 작업하려면 여러줄로 커밋을 쌓아야할까?
    * 한 줄에서 작업하면 충돌이 날 수 있기 때문!
    * 동시에 똑같은 코드를 고칠 가능성이 있으니까
  * n 줄로 쌓고 나중에 합칠수있을까?
    * ok. 충돌이 나더라도, 합치는 시점에 명시적으로 충돌 해결 가능.
  * source tree
    1. **master**: 내 컴퓨터에만 있는 내용
    2. **origin/master**: 원격/내컴퓨터에 있는 내용
    3. **HEAD**: 내가 지금 작업하는 로컬 브랜치
       * 많은 브랜치들 중에서도 내가 어떤 브랜치에 있는지 확인가능
    4. 브랜치 카테고리에 내가 작성한 브랜치만 보입니다.
       * 원격저장소 카테고리를 클릭해보자
       * 여기에서 내가만든 브랜치 뿐만 아니라 동료 브랜치도 확인가능.
       * 동료 브랜치 더블클릭 시 checkout할 수 있는 창 뜸.
       * checkout하면, 브랜치 카테고리에 동료 브랜치도 확인 가능.
  * 브랜치 만들기  
    * cat 브랜치를 현재 시점에 만들어라. \(HEAD가 있는 위치에\)  

      `git branch cat`

    * cat 브랜치로 이동해라.\(HEAD가 cat으로 이동\)   

      `git checkout cat`

    * commit을 진행하면, cat 브랜치는 새 커밋을 가리키고,

      기존 master브랜치는 그대로 있다. \(HEAD가 cat에 있기 때문\)
  * 실습
    * boxiting-cat저장소: master에서 feat/main-page 브랜치생성
      * feat/기능이름
        * 이렇게 쓰면 feat가 폴더처럼 되어있어서 많은 브랜치 관리에 유용하다.
        * 한 사람이 개발하는 기능 브랜치
        * 혹은 fix/버그이름, hotfix/급한버그
        * 작업이 끝나면, dev\(혹은 master\)브랜치로 PR 보내기
        * dev 브랜치에 큼지막한 작업 모두 머지되면 release, latest로 머지시키고 이를 실서버에 배포
        * 직접 커밋은 feat\(혹은 fix, hotix\)브랜치에만 합니다.
        * dev나 master, release 브랜치에는 직접 커밋하지 말고 머지만합니다.
      * source tree에서 현재 브랜치 확인하고 싶다면, bold\(두껍게\)처리된 부분을 읽으면 된다.
    * 커밋추가
    * boxiting-oct저장소: pull받기
    * master에서 feat/commit 브랜치 생성
    * 커밋 추가

    1. merge\(합치기\)
  * flow
    * master 브랜치의 최신 커밋\(base\)에 
    * oct 브랜치의 최신 커밋\(compare,head\)을 합치려고 한다.
    * 기능 개발이 마무리 되면, 기능 개발한 것을 master 브랜치에 합친다.
  * rule
    * base가 될 master 브랜치로 이동\(head를 master로 이동\)
      * source tree에서는 master를 더블클릭
    * compare 브랜치\(oct\)를 나와 합치고 싶다고 명령 `git merge oct`
      * source tree에서는 해당 브랜치 우측 클릭 후 병합
  * 종류
    * fast-forward merge
    * merge-commit
    * conflict

    1. conflict\(충돌\)
  * 머지할 때 두 버전이 같은 곳을 수정했다면 이를 수동으로 고쳐줘야한다.
  * 아래와 같이 base 에서 작성한 곳과, compare에서 작성한 곳이 충돌이 나는데 수동으로 &lt;&lt;&lt;&lt;&gt;&gt;&gt;&gt; 를 지우고 고쳐주면 된다.

    ```text
      <<<<HEAD
      [base]
      ===
      [compare]
      >>>>
    ```

    1. fork: 저장소 통채로 복제하기

  * 오픈소스에 기여하기 위해 collaboratos 등록을 부탁하지 않더라도, 내 저장소에 해당 저장소를 복제\(fork\)해서 그곳에서 자유롭게 커밋, 푸쉬후 해당 저장소에 merge해달라고 요청\(pull request\)하면 된다.
    1. pull request
  * rule
    * 머지하고 싶은 두 브랜치를 선택하고
    * 어떤 변경을 했는지 제목과 내용에 쓰면 된다.
    * 단일 저장소에서 보낼수도 있고, 포크한 저장소에서 보낼수도 있다.
    * 코드 함께 작성하는 동료 있다면, 최대한 직접 머지하는건 피하고, 풀 리퀘스트를 통해 하자.
    * 동료가 내 풀 리퀘\(PR\)을 보고 **코드 리뷰** 가능!
    * 동료의 PR에 수정이 필요하다면 댓글 달아 change request를 보낼 수 있음
    * 오픈 소스에 PR 보낼때에는 기여 안내문서\(contribution guide line\)를 반드시 참고할 것!!
  * 방법
    * repository에서 new pull request 클릭
    * base와 compare 위치 검토 후, create pull request
    * pull request를 받은 사람은 pull requests 창으로 가서
    * file changed를 클릭하면 3가지 옵션이 있다.
      * comment
      * approve
      * request change 
        1. 추가 키워드
  * rebase: 묵은 커밋을 새 커밋처럼 조작
  * amend: 깜빡하고 수정 못한 파일이 있어서, 방금 만든 커밋에 살짝 추가
  * cherry-pick: 저 커밋 하나만 떼서 지금 브랜치에 붙이고 싶을 때
  * reset: 옛날 커밋으로 시간 돌리기
  * reverse: 이 커밋의 변경사항을 되돌리고 싶다.
  * stash: 변경사항을 잠시 킵.아직 커밋 안함.

