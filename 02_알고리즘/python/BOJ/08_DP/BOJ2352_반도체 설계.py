n = int(input())  # 포트 갯수
arr = list(map(int, input().split()))  # 도착해야할 포트

max = 0

for i in range(len(arr)):
    count = 0
    print(max)
    for j in range(i+1, len(arr)):
        if arr[j] > arr[i]:
            count += 1
    if count >= max:
        max = count

print(max)

# LIS 사용하는방법은 다시 생각해봐야할것같다.
