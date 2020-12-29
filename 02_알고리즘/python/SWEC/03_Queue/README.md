# Queue

-   ### Queue개요
    -   삽입삭제의 위치가 제한적인 자료구조
    -   FIFO(First in Firts Out 선입선출)
    -   기본 연산
        -   enqueue(item): queue의 뒤쪽(rear:꼬리)에 원소 삽입
        -   dequeue(): queue의 앞쪽(front)에 원소 삭제하고 반환
        -   createQueue(): 공백상태 queue 생성
        -   isEmpty(): queue가 비어있는지 유무
        -   isFull(): queue가 꽉찼는지 유무
        -   peek(): queue 앞쪽 원소 삭제 없이 반환
-   ### Queue 종류

    -   선형큐
        -   삽입삭제 처리속도 빠름
        -   메모리 낭비 심함
        -   대안
            -   파이썬특징상, 리스트 특성 사용해서 메모리 절약 가능(단, 연산 시간 증가)
            -   단순 연결리스트 구현한 큐 사용해서 메모리 동적 확보가능
            -   큐 라이브러리 사용
    -   원형큐
        -   리스트의 처음과 끝이 연결되어 원형형태의 큐를 이룬다고 가정
        -   위치 재조정 위해, list크기 벗어났을 경우 리스트의 크기로 나머지 연산을 해준다.
    -   연결큐
        -   linked list 이용한 큐
    -   우선순위큐
        -   우선순위를 가진 항목들을 저장하는 큐
        -   우선순위 높은 순대로 나감
            -   사용
                -   시뮬레이션시스템
                -   네트워크 트래픽제어
                -   운영체제 task 스케쥴링
                -   입출력(버퍼)

-   ### Queue 모듈에 정의된 클래스

    -   `queue.Queue(maxsize)`클래스: 선입선출 queue객체 생성
    -   `queue.Liof(maxsize)`클래스: stack개념
    -   `queue.Priority(maxsize)`클래스: 우선순위 큐 객체
        -   입력되는 아이템 형식(순위, 아이템)
        -   우선순위는 작을수록 높은 순위
    -   동일하게 제공되는 메서드
        -   `qsize()`: queue의 크기(얼마나 item 들어있는지)
        -   `put(item[,block[,timeout]])`: 큐객체에 item 입력
        -   `get([block[,timeout]])`: queue특성에 맞게 아이템 1개 반환
        -   `empty()`: 비어있으면True
        -   `full()`: 차있으면 True

-   ### BFS

    -   큐활용
    -   인접한 정점들을 모두 차례로 방문한 후, 방문했던 정점을 시작점으로 해서 다시 인접 정점 차례로 방문

        ```py
        def BFS(v):
            visited, need_visit = [], []
            need_visit.append(v)

            while need_visit:
                node = need_visit.pop(0)
                if node not in visited:
                    visited.append(node)
                    need_visit.extend(graph[node])

            return visited
        #BFS로 순회한 결과(visited)를 볼수 있음
        ```

-   #### 참고(알고리즘 구현하면서 자주 사용했던 라이브러리)
    -   `collections 의 deque`
        -   양방향 큐
        -   그냥 pop(0)을 하는 것 보다 속도가 빨라서 작성
        -   특히 deque에 있는 popleft()를 자주 사용함.
    -   우선순위 큐할 때
        -   `from queue import priorityQueue` 자주 사용
