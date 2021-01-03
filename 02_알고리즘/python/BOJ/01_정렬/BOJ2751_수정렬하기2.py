import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for i in arr:
    print(i)

# ? 통과했다...?
# 강의 상에 고급정렬로 구분되있어서, 퀵이나 병합으로 구현해야하나 했는데
# 파이선 기본 정렬함수의 시간복잡도가 O(Nlog(N)) 이였나보다.
# 역시 시간, 메모리 관련해서는 sys.stdin, sys.stdout을 생각해보는게 좋겠다.
# 단, 연습하는 것도 중요하니 병합정렬을 한번 구현해볼것!
