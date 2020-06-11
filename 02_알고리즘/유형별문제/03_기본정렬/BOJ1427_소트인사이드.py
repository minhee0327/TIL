N = int(input())

arr = []

while N != 0:
    arr.append(N % 10)
    N //= 10

arr = sorted(arr, reverse=True)
arr = list(map(str, arr))
print(''.join(arr))
