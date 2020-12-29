T = int(input())

for test_case in range(1, T+1):
    lst = list(map(int, input().split()))
    avg = round(sum(lst)/len(lst))
    print("#{} {}".format(test_case, avg))
