n = int(input())
tri = [list(map(int, input().split()))for i in range(n)]

for i in range(n-1, -1, -1):
    for j in range(len(tri[i])-1):
        if tri[i][j] > tri[i][j+1]:
            tri[i-1][j] = tri[i-1][j] + tri[i][j]
        else:
            tri[i-1][j] = tri[i-1][j] + tri[i][j+1]

print(tri[0][0])

'''
[Code Review]
- 이 문제는 3번째 푸는데(5달전, 2달전, 오늘) 세번 다 다르게 풀었다는게 너무 신기하다.
- 처음 풀때는 위=>아래로 움직이면서 양끝은 그냥 위의 값과 더하고, 가운데는 윗층의 두값중 최대값을 더해서 update해나갔고
- 두번째 풀때는 DP배열을 따로 두고 계산했고
- 마지막은 max로 풀지 않고 좌우값만 비교하면 되니까 조건문으로 계산했다.
- 마지막에 푼 방법(조건을 줘서 풀기)이 가장 속도나 공간을 덜 차지한걸로 봐서는 max를 쓰는 것이 좀 더 속도가 걸리는게 아닐까싶다.
'''
