N = int(input())
A = list(map(int, input().split()))
DP = [1] * N
DP_lst = []

for i in range(1, N):
    temp = []
    for j in range(i):
        if A[j] < A[i] and A[j] not in temp:
            DP[i] += 1
            temp.append(A[j])
    temp.append(A[i])
    DP_lst.append(temp)

print(max(DP))
max_idx = DP.index(max(DP))
for i in DP_lst[max_idx-1]:
    print(i, end=" ")

'''
[Code Review]
- 주어진 testcase는 잘 돌아가는데,
- 뭔가 부족한 코드인거같다. 틀렸다고 뜬다.
- 차일 수정예정
'''
