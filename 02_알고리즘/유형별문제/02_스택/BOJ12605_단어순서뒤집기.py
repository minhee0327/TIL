N = int(input())

for t in range(N):
    arr = list(map(str, input().split()))
    print("Case #{}:".format(t+1), end=" ")
    for i in range(len(arr)-1, -1, -1):
        print(arr[i], end=" ")
    print()
