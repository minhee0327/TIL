N = int(input())

count, K = 0, 1

while N != 0:
    if K > N:
        K = 1
    N -= K
    count += 1
    K += 1

print(count)
