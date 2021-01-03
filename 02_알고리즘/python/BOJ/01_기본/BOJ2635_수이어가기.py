n = int(input())
ans_len = 1
ans_lst = []

for i in range(1, n+1):
    temp = [n, i]
    j = 0
    while True:
        if temp[j] - temp[j+1] < 0:
            break
        else:
            temp.append(temp[j] - temp[j+1])
            j += 1

    if len(temp) > ans_len:
        ans_len = len(temp)
        ans_lst = temp[:]

print(ans_len)
print(" ".join(map(str, ans_lst)))
