N = int(input())

ans, flag = -1, 0
for i in range(N//3 + 1):
    for j in range(N//5+1):
        if i * 3 + j * 5 == N:
            ans = i+j
            flag = 1
            break
    if flag:
        break
print(ans)
