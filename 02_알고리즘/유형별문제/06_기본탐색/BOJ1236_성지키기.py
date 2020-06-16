N, M = map(int, input().split())
sung = [input() for _ in range(N)]

r = [i for i in range(N)]
c = [i for i in range(M)]

row = set()
columns = set()

for i in range(N):
    for j in range(M):
        if sung[i][j] == 'X':
            row.add(i)
            columns.add(j)

new_r, new_c = [], []
for i in range(N):
    if r[i] not in row:
        new_r.append(r[i])
for i in range(M):
    if c[i] not in columns:
        new_c.append(c[i])

print(max(len(new_r), len(new_c)))

'''
(내가 생각한 풀이)
1. r,c 가 가능한 index 값들을 각각 배열로 저장 (예: [1,2,3,4])
2. X가 있는 곳의 에 index값을 row, columns에 담되, 겹치는것은 제거 => set() 선택.
    - 그렇게 하면 각 row와 column에 X가 있는 좌표를 안겹치게 모두 알수있음.
3. N, M만큼 돌면서 row에 X가 없는 위치를 new_r, new_c에 담았음
4. 어찌되었든 경비병이 다 세워져 있어야 하니까 r, c중에 최대값을 고르면 다 세우면서, 최소한으로 세울 수 있음..!
'''
