N = int(input())
switch = list(map(int, input().split()))

# 학생수만큼 반복해서, 성별과 스위치의 번호를 받음.
for _ in range(int(input())):
    S, num = map(int, input().split())
    # 성별 남
    if S == 1:
        for i in range(num-1, N, num):
            if switch[i] == 1:
                switch[i] = 0
            elif switch[i] == 0:
                switch[i] = 1

    # 성별 여
    elif S == 2:
        start, end = num-2, num
        while start > -1 and end <= N:
            print(start, end)
            if switch[start] != switch[end]:
                break

            elif switch[start] == switch[end] == 0:
                switch[start] = 1
                switch[end] = 1
            elif switch[start] == switch[end] == 1:
                switch[start] = 0
                switch[end] = 0
            start -= 1
            end += 1
    print(switch)

print(' '.join(map(str, switch)))
