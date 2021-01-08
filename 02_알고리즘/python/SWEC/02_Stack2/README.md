# Stack 활용

-   ## 계산기문제

    -   ### 개요

        -   중위표기 => _후위표기법_ (stack 활용 계산)
            -   중위표기: 일반적으로 아는방법, 문자열 계산식 계산 일반적 방법
            -   후위표기: 연산자를 피연산자 뒤에 표기
            -   변환알고리즘1
                -   토큰읽기
                -   토큰이 피연산자이면 토큰 출력
                -   토큰이 연산자(괄호포함)일 경우
                    -   우선순위가 높으면 스택에 push
                    -   우선순위가 안높으면, 연산자의 우선순위가 토큰의 우선순위보다 작을때까지 pop한 뒤(pop한건 출력), 토큰의 연산자를 push
                    -   만약 top에 연산자 없을경우에는 push
                -   토큰이 오른쪽 괄호이면
                    -   스택의 top에 왼쪽괄호가 올때까지 pop연산
                    -   pop한 연산자 출력
                    -   왼쪽 괄호 만나면 pop만하고 출력은 X
                -   중위표기식에 더 읽을 것이 없다면 중지하고 더읽을 것이 있다면 처음부터 반복
                -   스택에 남아있는 연산자를 모두 pop하여 출력
                    -   스택 밖의 왼쪽 괄호는 우선순위 가장 높음
                    -   스택 안의 왼쪽괄호는 우선순위 가장 낮음
        -   정리

            -   피연산자는 후위표기법 수식에 바로 출력
            -   연산자는 stack을 거쳐서, ')'가 올때 '('를 만날때까지 pop하고 다시 반복
            -   stack에 담을때에는 우선순위에 따라 담긴다.
                -   연산자 우선순위 참조
                    |토큰|ISP(안)|ICP(밖)|
                    |----|---|---|
                    |)|-|-|
                    |\*, /|2|2|
                    |+, -|1|1|
                    |(|0|3|
                -   숫자가 클수록 우선순위가 높다.

        -   후위표기법으로 표현된 수식을 계산하기
            -   피연산자 만나면 스택에 push
            -   연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고 연산결과를 다시 스택에 push함
                -   먼저 들어갔던 값이 앞에 와야함
            -   수식이 끝나면 마지막으로 스택을 pop하여 출력

-   ## 백트래킹

    -   해를 찾는 도중에 막히면 (즉, 해가 아니면), 되돌아가서 다시 해를 찾는 기법
    -   최적화문제 & 결정문제를 동시에 해결할 수 있다.
    -   문제의 조건을 만족하는 해가 존재하는지 yes or no로 대답하는 문제에 많이 활용된다.
    -   기법
        -   어떤 노드의 유망성을 점검한 후, 유망하지 않을경우 해당노드의 부모로 돌아가 (back track)다음 자식 노드로 간다.
            -   어떤 노드를 방문하였을때 그 노드를 포함한 경로가 해답이 될 수 없으면 해당 노드는 유망하지 않다고 한다.
            -   반대로 해답의 가능성이 있으면 유망하다고 함
            -   pruning: 유망하지 않은 노드가 포함된 경로는 더이상 고려X
    -   알고리즘 절차
        -   상태공간 Tree의 DFS 실시
        -   각 노드가 유망한지 점검
        -   만일 노드가 유망하지 않으면, 그 노드의 부모노드로 돌아가서 계속해서 검색
        ```py
        # 백트래킹 큰 구조
        def checknode(v):
            if promising(v):
                if there is a solution at v:
                    write the solution
                else:
                    for j in each child of v:
                        checknode(j)
        ```
    -   대표 유형
        -   미로찾기
        -   N-Queen
        -   Map coloring
        -   부분집합의 합(Subset Sum)문제 등
    -   백트래킹과 DFS의 차이
        |백트래킹|DFS|
        |----|---|
        |어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면, 더이상 그 경로를 따라가지 않고 시도 횟수를 줄임 |모든 경로 추적|
        |모든 후보 검사하지 X|모든 후보 검사|
        |가지치기(prunning)||
        |불필요한 경로의 조기 차단||

    -   ### Power Set (부분집합)

        -   n개의 원소가 들어있는 집합의 모든 부분집합 (2ⁿ)

        ```py
        def process_solution(a,k):
            print("(", end =""))
            for i in range(k+1):
                if a[i]:
                    print(i,end=" ")
            print(")")

        def construct_candidate(a,k,input,c):
            c[0] = True
            c[1] = False
            return 2

        def backtrack(a,k, input):
            global MAXCANDIDATES
            c = [0] * MAXCANDIDATES

            if k == input:
                process_solutioin(a,k) # 답일 경우 원하는 작업
            else:
                k+=1
                ncandidates = construct_candidates(a,k, input, c)
                for i in range(ncandidates):
                    a[k] = c[i]
                    backtrack(a,k, input)

        MAXCANDIDATES = 100
        NMAX = 100
        a = [0] * NMAX
        backtrack(a, 0, 3)
        ```

-   ## 분할정복
    -   ### 거듭제곱(문제)
        -   보통 떠올리는방법(`O(N)`)
        ```py
        def Power(base, exponent):
            # 0의 제곱을 편의상 1로 정의.
            if base == 0 or exponent == 0:
                return 1
            result = 1
            for i in range(exponent):
                result *=base
            return result
        ```
        -   분할 정복 기반 알고리즘(`O(logN)`)
        ```py
        def Power(base, exponent):
            if base == 0 or exponent == 0:
                return 1
            if exponent %2 == 0:
                newBase = Power(base, exponent//2)
                return newBase * newBase
            else:
                newBase = Power(base, (exponent-1)//2)
                return newBase * newBase * base
        ```
