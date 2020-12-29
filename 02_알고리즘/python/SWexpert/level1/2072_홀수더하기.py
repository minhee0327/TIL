T = int(input())

for test_case in range(1, T+1):
    lst = list(map(int, input().split()))
    total = 0
    for i in lst:
        if i % 2 != 0:
            total += i
    print("#{} {}".format(test_case, total))
