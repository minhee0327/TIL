T = int(input())

for _ in range(T):
    count = 0
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    index = [i for i in range(N)]

    while True:
        if max(num) == num[0]:
            count += 1
            if index[0] == M:
                print(count)
                break
            else:
                num.pop(0)
                index.pop(0)
        else:
            index.append(index.pop(0))
            num.append(num.pop(0))

# 1. 우선순위 큐로 접근해서 시간을 많이 버렸음...
# 2. 일반 큐, list로 충분히 가능했다.
# 3. 분명 맞는데 계속 무한루프에 빠졌다.. 알고보니 max값을 검증하는 걸 먼저 한 후에
# 4. 그 값이 찾고자하는 위치인지 확인해야했다.
# 5. 나의 경우, or, and로 표시해서 뭔가 꼬인것같다.

# 총정: 구현할 때, 어렵게 생각하지 말자, 단순화 하자
