n = int(input())

# 빌딩의 위치와 높이를 담은 배열
building = []
for _ in range(n):
    w, h = map(int, input().split())
    building.append((w, h))

building = sorted(building, key=lambda x: x[0])

# building 높이정보만 담은 배열(matrix)
matrix = [0] * (building[-1][0]+1)
for b in building:
    matrix[b[0]] = b[1]

for i in range(building[0][0], matrix.index(max(matrix))):
    if matrix[i] >= matrix[i+1]:
        matrix[i+1] = matrix[i]

for i in range(building[-1][0], matrix.index(max(matrix)), -1):
    if matrix[i-1] <= matrix[i]:
        matrix[i-1] = matrix[i]
print(sum(matrix))
