C, R = map(int, input().split())
K = int(input())
matrix = [[0] * (R+1) for _ in range(C+1)]

x, y = 0, 0
dir = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

if K > C*R:
    print(0)
else:
    for i in range(1, C*R+1):
        matrix[x][y] = i
        if i == K:
            print(x+1, y+1)
            break
        nx, ny = x+dx[dir], y+dy[dir]
        if 0 <= nx < C and 0 <= ny < R and not matrix[nx][ny]:
            x, y = nx, ny
        else:
            dir = (dir+1) % 4
            x, y = x + dx[dir], y + dy[dir]

'''
[Code Review]
- 문제를 풀면서 느낀건데, 경계지점을 조금 대충 잡는 경향이 있는것 같다. 그래서 한참을 걸려서 풀어냈다....ㅠㅠ
- 처음 x, y 를 시작할 지점을 정하는것도 1,1 / 0,0으로 고민을 했었고
- 배열의 크기를 1개 증가 시킬건지도 한참 고민을 했고
- 조건문에서 and로 모든 조건이 만족할때를 찾으려고 했는데 잠시 딴생각했나..(?) or를 써서 한참을 왜 out of index인지 고민했다...

- 결국 대충 잡은 경계값 때문에 엉뚱한데서 한참을 고민을 하고있었다.. 
- 문제를 풀면서 이 점에 유의하자..
'''
