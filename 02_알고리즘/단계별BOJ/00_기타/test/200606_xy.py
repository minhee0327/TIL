n = int(input())
k = int(input())

count = 0

for i in range(n, 0, -1):
    for j in range(n, i, -1):
        count += 1
        #print(j, " ", count)
        if count == k:
            print(j)
