import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

print(A[K-1])

# 병합정렬없이도 통과
# 파이선 내장 sort(), sorted() 시간복잡도가 O(NlogN)라는 점이 인상적이다.
