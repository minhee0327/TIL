# 1번 풀이
unit = int(input())
length_arr = []

for i in range(6):
    dir, l = map(int, input().split())
    length_arr.append(l)

max_w, max_h = 0, 0
rem_w, rem_h = 0, 0

for i in range(6):
    # 가로 최대
    if i % 2 == 0:
        if max_w < length_arr[i]:
            max_w = length_arr[i]
    # 세로 최대
    else:
        if max_h < length_arr[i]:
            max_h = length_arr[i]

for i in range(6):
    if i % 2 == 0:
        if length_arr[(i+5) % 6] + length_arr[(i+1) % 6] == max_h:
            rem_w = length_arr[i]
    else:
        if length_arr[(i+5) % 6] + length_arr[(i+1) % 6] == max_w:
            rem_h = length_arr[i]

print((max_w * max_h - rem_w * rem_h) * unit)
'''
[CODE REVIEW]
- 구현한 코드는
- 제거해야하는 너비의 양쪽 길이(높이)들의 합이 최대 높이와 같을 경우, 그때가 제거할 너비라는 점에 착안함

- 혹은, 구현하지는 않았지만, 가장 긴 두 변의 길이와(밖의 큰 사각형 변), 
- 위에 구한 각 변의 위치로부터 3번째 떨어진(반시계방향) 위치에 있는 길이들은 제거해야할 사각형의 길이이다.

- 이런 규칙을 찾는게 어려웠다..
- 처음에 좌표를 하나하나 다 구해서 생각을 했는데, 점으로만 생각하지 말고, 변으로 생각할 수 있었다면 좋았을것같다.
'''
