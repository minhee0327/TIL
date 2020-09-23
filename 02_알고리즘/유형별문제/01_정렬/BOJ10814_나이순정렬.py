N = int(input())
arr = []

for _ in range(N):
    age, name = input().split()
    arr.append((int(age), name))

arr.sort(key=lambda x: x[0])

# print(arr)
for a in arr:
    print(str(a[0])+' '+a[1])


# 예전에 eval로 형변환 시도 했는데 이게 더 속도가 나은것 같다!
