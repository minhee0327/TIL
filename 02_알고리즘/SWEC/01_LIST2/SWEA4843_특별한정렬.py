for t in range(1, 1 + int(input())):
    n = int(input())
    arr = sorted(map(int, input().split()))
    ans = []

    for i in range(5):
        ans.append(arr[n-1-i])
        ans.append(arr[i])

    print("#{} {}".format(t, ' '.join(map(str, ans))))
