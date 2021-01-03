from itertools import combinations

while True:
    temp = list(map(int, input().split()))
    k, S = temp[0], temp[1:]
    if k == 0:
        break

    possibility_num = list(combinations(S, 6))
    for p in possibility_num:
        print(' '.join(map(str, p)))

    print()
'''
[문제 요약]
1~49 까지의 수들 중, k개의 수를 골라서 집합 S를 만든다.
이 때, 수를 고르는 모든 방법?

[입력]
여러개의 TC
각 TC는 한줄로 이뤄져있고, 첫번째수는 k, 다음 k개의 수는 집합 S에 포함될 수들(오름차)
입력 마지막에는 0 주어짐

[출력]
각 TC마다 수를 고르는 모든 방법 출력, 사전순 출력
각 테케 사이에는 빈줄 하나 출력

[접근, 생각 요약]
- 부분집합, itertools, combinations로 접근
- 출력시 사전순 정렬(라이브러리 사용하면서 자동 정렬 될 것으로 예상)
- 0 이 입력될때까지 반복
'''
